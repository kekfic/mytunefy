"""
@author FF

"""
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtGui import QMovie, QPainter, QPixmap
from PySide2.QtWidgets import QMainWindow, QDialog, QFileDialog, QLabel, QSplashScreen
from PySide2.QtWidgets import QWidget, QGridLayout, QVBoxLayout
from PySide2.QtCore import Signal, QTimer, QObject, SIGNAL

import os

from gui.gui_main import Ui_MainWindow
import re

import sys
import platform
import pprint
import logzero
from logzero import logger as log

#import __version__
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
    if const.args.song:
        for track in const.args.song:
            print(track)
            track_dl = downloader.Downloader(raw_song=track)
            track_dl.download_single()
        operation = 'track'
    elif const.args.list:
        if const.args.write_m3u:
            youtube_tools.generate_m3u(
                track_file=const.args.list
            )
        else:
            list_dl = downloader.ListDownloader(
                tracks_file=const.args.list,
                skip_file=const.args.skip,
                write_successful_file=const.args.write_successful,
            )
            list_dl.download_list()
        operation = 'list'
    elif const.args.playlist:
        spotify_tools.write_playlist(
            playlist_url=const.args.playlist, text_file=const.args.write_to
        )
        operation = 'playlist'
    elif const.args.album:
        spotify_tools.write_album(
            album_url=const.args.album, text_file=const.args.write_to
        )
        operation = 'album'
    elif const.args.all_albums:
        spotify_tools.write_all_albums_from_artist(
            artist_url=const.args.all_albums, text_file=const.args.write_to
        )
        operation = 'all_album'
    elif const.args.username:
        spotify_tools.write_user_playlist(
            username=const.args.username, text_file=const.args.write_to
        )
        operation = 'username'

    return operation

def main(url, category_list):
    const.args = handle.get_arguments([url, category_list, ''])

    internals.filter_path(const.args.folder)
    youtube_tools.set_api_key()

    logzero.setup_default_logger(formatter=const._formatter, level=const.args.log_level)

    try:
        match_args()
        # actually we don't necessarily need this, but yeah...
        # explicit is better than implicit!
        sys.exit(0)

    except KeyboardInterrupt as e:
        log.exception(e)
        sys.exit(3)




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
    # this main class is the main window and contain all button specification

    def __init__(self):
        self.mainwindow = QMainWindow()
        Ui_MainWindow.__init__(self)
        self.setupUi(self.mainwindow)
        QObject.__init__(self)

        #combo_data = ['', 'song', 'playlist', 'album', 'artist']
        #self.comboBox.addItems(combo_data)
        self.pushButtonFolder.clicked.connect(self.folder_opener)
        self.progressBar.hide()
        self.StartPushButton.clicked.connect(self.startDownload)


    def folder_opener(self):

        self.mymusicfolder = 'C:\\Users\\%username%\\Music'
        mydir = QFileDialog.getExistingDirectory(None, 'Select a folder:', self.mymusicfolder, QFileDialog.ShowDirsOnly)
        self.plainTextDirectory.setPlainText(mydir)

    def startDownload(self):
        print("Start downloading")
        self.url = self.text_from_plain_text()
        self.category_list = self.parser_category(self.url)
        main(self.url, self.category_list)

    def text_from_plain_text(self):
        url = self.plainTextEdit.toPlainText()
        print(url)
        return url

    def parser_category(self, url):
        # Todo: if a wrong url or line is inserted, parser fails
        #  File "D:\Programmi\Python\Spotify-app\window_handler.py", line 152, in parser_category
        #     junk, data = re.split(r'.com/', url)
        # ValueError: not enough values to unpack (expected 2, got 1)

        junk, data = re.split(r'.com/', url)
        print(junk, data)
        category_list, junk = re.split(r'/', data)
        print('Category:', category_list)

        return category_list

    def time_dep_program(self, time_system):
        print('Time system is:')


