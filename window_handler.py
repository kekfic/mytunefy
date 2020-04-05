"""
@author FF

"""

from PySide2.QtGui import QPainter, QPixmap, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QMainWindow, QFileDialog, QSplashScreen, QWidget, QLabel, QPushButton, QHBoxLayout, \
    QListWidgetItem

from PySide2.QtCore import QObject

from gui.gui_main import Ui_MainWindow
import re

import sys
import platform
import pprint
import logzero
from logzero import logger as log

import const
import handle
import internals
import spotify_tools
import youtube_tools
import downloader


def debug_sys_info():
    log.debug("Python version: {}".format(sys.version))
    log.debug("Platform: {}".format(platform.platform()))
    log.debug(pprint.pformat(const.args.__dict__))


def match_args():
    # Todo major changing here, I shall probably change everything,
    # I add operation variable, for now it is a patch
    operation = ''
    text_file = ''
    if const.args.song:
        for track in const.args.song:
            track_dl = downloader.Downloader(raw_song=track)
            track_dl.download_single()
            # when only one track is downloaded, there is no need for listing
        operation = 'list'
    elif const.args.playlist:
        tracks, text_file = spotify_tools.write_playlist(
            playlist_url=const.args.playlist, text_file=const.args.write_to
        )
        operation = 'playlist'
    elif const.args.album:
        tracks, text_file = spotify_tools.write_album(
            album_url=const.args.album, text_file=const.args.write_to
        )
        operation = 'album'
    elif const.args.all_albums:
        text_file = spotify_tools.write_all_albums_from_artist(
            artist_url=const.args.all_albums, text_file=const.args.write_to
        )
        operation = 'all_album'
    elif const.args.username:
        links_playlist, text_file = spotify_tools.write_user_playlist(
            username=const.args.username, text_file=const.args.write_to
        )
        operation = 'username'

    return operation, text_file


class CustomQWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomQWidget, self).__init__(parent)

        label = QLabel("I am a custom widget")

        button = QPushButton("A useless button")

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

class LoadingGif(QSplashScreen):
    def __init__(self, movie, parent=None):
        movie.jumpToFrame(0)
        pixmap = QPixmap(movie.frameRect().size())

        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self, event):
        self.movie.stop()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)

    def sizeHint(self):
        return self.movie.scaledSize()


class MainWin(QObject, Ui_MainWindow):
    """ this main class is the main window and contain all button specification """

    def __init__(self):
        self.mainwindow = QMainWindow()
        Ui_MainWindow.__init__(self)
        self.setupUi(self.mainwindow)
        QObject.__init__(self)

        self.text_file = ''
        self.operation = ''

        self.pushButtonFolder.clicked.connect(self.folder_opener)
        self.progressBar.hide()
        self.StartPushButton.clicked.connect(self.startDownload)

        const.args = handle.get_arguments()
        const.args.folder = internals.get_music_dir()

        self.plainTextDirectory.setPlainText(const.args.folder)
        self.plainTextEditUrl.textChanged.connect(self.text_from_plain_text)

        item = QListWidgetItem(self.listWidgetUrls)
        item_widget = CustomQWidget()
        item.setSizeHint(item_widget.sizeHint())
        self.listWidgetUrls.addItem(item)
        self.listWidgetUrls.setItemWidget(item, item_widget)


    def folder_opener(self):
        mydefaultfolder = 'C:\\Users\\%username%\\Music'
        self.mydir = QFileDialog.getExistingDirectory(None, 'Select a folder:', mydefaultfolder,
                                                      QFileDialog.ShowDirsOnly)
        self.plainTextDirectory.setPlainText(self.mydir)
        self.mydir.replace("/", "\\")
        const.args.folder = self.mydir

    def startDownload(self):
        self.main()


    def text_from_plain_text(self):
        self.url = self.plainTextEditUrl.toPlainText()
        self.category_list = self.url_parser(self.url)
        if self.category_list:
            self.listWidgetUrls.addItem(self.url)


    def url_parser(self, url):
        # Todo: if a wrong url or line is inserted, parser fails
        #  File "D:\Programmi\Python\Spotify-app\window_handler.py", line 152, in parser_category
        #     junk, data = re.split(r'.com/', url)
        # ValueError: not enough values to unpack (expected 2, got 1)
        category_list = ''

        try:
            junk, data = re.split(r'.com/', url)
            if self.check_url(junk):
                category_list, junk = re.split(r'/', data)
        except ValueError as e:
            print("Parser url as {}:".format(e))
        except Exception as e:
            print("General error in url splitting:", e)

        if category_list == 'playlist':
            const.args.playlist = url
        elif category_list == 'track':
            const.args.song = [url]
        elif category_list == 'album':
            const.args.album = url
        elif category_list == 'artist':
            const.args.artist = url
        else:
            category_list = False
            
        return category_list

    def check_url(self, junk):
        if junk == 'https://open.spotify':
            valid_url = True
        else:
            valid_url = False

        return valid_url

    def time_dep_program(self, time_system):
        print('Time system is:')

    def list_downloader(self):
        if self.operation is not 'list':
            if const.args.write_m3u:
                youtube_tools.generate_m3u(
                    track_file=const.args.list
                )
            else:
                # list_name = str(self.category_list) + '.txt'
                list_dl = downloader.ListDownloader(
                    tracks_file=self.text_file,
                    skip_file=const.args.skip,
                    write_successful_file=const.args.write_successful,
                )
                list_dl.download_list()
                self.operation = 'list'

    def main(self):
        # Todo try new implementation
        internals.filter_path(const.args.folder)
        youtube_tools.set_api_key()
        logzero.setup_default_logger(formatter=const._formatter, level=const.args.log_level)

        try:
            self.operation, self.text_file = match_args()

            # actually we don't necessarily need this, but yeah...
            # explicit is better than implicit!
            if self.operation is not 'list':
                self.list_downloader()

        # I don't need this type of exception, I'll remove another time
        except Exception as e:
            print(e)
            self.operation = False
            log.exception(e)
            sys.exit(3)
