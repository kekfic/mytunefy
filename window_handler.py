"""
@author FF

"""
from queue import Queue

from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import QObject, Signal, SIGNAL

from gui.gui_main import Ui_MainWindow
import getpass

from spotdl_mod import const, handle, internals
import threading
import webbrowser

from spotdl_mod.spotify_tools import fetch_playlist, fetch_album, fetch_albums_from_artist, generate_metadata
from slugify import slugify

from my_main_functions import main, url_parser, assign_parser_url, reset_parser_url
from login import db_song_conn

"""
My list of variables:

        self.quecreat = Queue() - queue object for pushing data between threads
        self.all_urls = [] - list of the urls to be downloaded
        self.all_categories = [] - list of the type of argument (Playlist, Album, Song)
        self.url_text = False - Probably unused
        self.count = 0 - TO be modified
        self.mydir = 'C:\\Users\\' + getpass.getuser() + '\\Music\\' - default folder to be opened for user 

"""



class MyClassThread(QObject, threading.Thread):
    "Inheritance of thread class, unused"
    mySignal = Signal(object)

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        QObject.__init__(self)
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        pass


class MyWindow(QMainWindow):
    "Reimplementing main window for closeEvent option"

    def closeEvent(self, event):
        result = QMessageBox.question(self,
                                      "Confirm Exit...",
                                      "Are you sure you want to exit ?",
                                      QMessageBox.Yes | QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()


class MainWin(QObject, Ui_MainWindow):
    """ this main class is the main window and contain all button specification """
    threadSignal = Signal(object)

    def __init__(self):
        self.mainwindow = MyWindow()
        Ui_MainWindow.__init__(self)
        self.setupUi(self.mainwindow)

        QObject.__init__(self)
        #Todo; check all unused variables and functions
        self.quecreat = Queue()
        self.all_urls = []
        self.all_categories = []
        self.url_text = False
        self.count = 0
        self.mydir = 'C:\\Users\\' + getpass.getuser() + '\\Music\\'

        #hiding progress bar
        self.progressBar.hide()
        #Two signal for folder and download button launch
        self.pushButtonFolder.clicked.connect(self.folder_opener)
        self.StartPushButton.clicked.connect(self.threading_launcher)

        #setting the args global variable with default values
        const.args = handle.get_arguments()
        const.args.folder = internals.get_music_dir()

        # Plain text, setting folder text and configuring signal
        self.plainTextDirectory.setPlainText(const.args.folder)
        self.plainTextEditUrl.textChanged.connect(self.text_from_plain_text)

        # listWidget beahaviour
        self.listWidgetUrls.hide()
        self.listWidgetUrls.itemDoubleClicked.connect(self.remove_item)

        #Menu signals
        self.connect(self.action_m4a, SIGNAL("triggered()"), self.out_format)
        self.connect(self.action_flac, SIGNAL("triggered()"), self.out_format)
        self.connect(self.action_mp3, SIGNAL("triggered()"), self.out_format)

        self.connect(self.actionffmpeg, SIGNAL("triggered()"), self.encoding_sel)
        self.connect(self.actionavconv, SIGNAL("triggered()"), self.encoding_sel)

        self.connect(self.actionDry_Run, SIGNAL("triggered()"), self.advanced_option)
        self.connect(self.actionMusic_Video_Only, SIGNAL("triggered()"), self.advanced_option)
        self.connect(self.actionNo_Spaces, SIGNAL("triggered()"), self.advanced_option)
        self.connect(self.actionTrim_Silence, SIGNAL("triggered()"), self.advanced_option)

        self.connect(self.actionReadMe, SIGNAL("triggered()"), self.open_readme)
        self.connect(self.actionhelp, SIGNAL("triggered()"), self.open_manual)

        #Setting thread tha take care of the download, this allow a responsive main window
        self.mythread = MyClassThread(target=self.startDownload)
        self.mythread = threading.Thread(target=self.startDownload, daemon=True)
        self.mythread.start()

        self.threadSignal.connect(self.progressBarcomplete)

        #database connection configuration, in progress
        self.database = db_song_conn()
        if self.database:
            #Get playlist and album downloaded data from
            pass



    def folder_opener(self):
        "Selecting the download folder"

        self.mydir = QFileDialog.getExistingDirectory(self.mainwindow, 'Select a directory', self.mydir,
                                                      QFileDialog.ShowDirsOnly)
        self.plainTextDirectory.setPlainText(self.mydir)
        self.mydir.replace("/", "\\")
        const.args.folder = self.mydir

    def remove_item(self):
        "Remove item from QWidgetList if double clicked"
        item = self.listWidgetUrls.currentRow()
        self.listWidgetUrls.takeItem(item)

        self.all_urls.pop(item)
        self.all_categories.pop(item)

    def threading_launcher(self):
        "When start button is pushed, check for correcteness nad start a thread for downloading"
        # Todo: trying implement a better way of threading
        self.count = self.listWidgetUrls.count()
        if self.count:
            self.quecreat.put([self.count, self.all_categories.copy(), self.all_urls.copy()])
            "Clearing the QWidgetList and other objects"
            self.listWidgetUrls.clear()
            self.all_categories.clear()
            self.all_urls.clear()
            self.progressBarHandler(self.count)

    def startDownload(self):
        # Todo I don't like it very much
        "Start the function for downloading"
        index = 0
        while threading.main_thread().is_alive():
            if index:
                #if thread has ended the download, update the progressbar
                self.threadSignal.emit(index)

                index = 0
            count, all_categories, all_urls = self.quecreat.get()
            for i in range(count):
                #
                url = all_urls[i]
                category_list = all_categories[i]
                "assign the current const.args.group"
                assign_parser_url(category_list, url)
                "Starting the main according url parsing"
                main()
                "Resetting the parser because it is unique"
                reset_parser_url()
            index += 1


    def text_from_plain_text(self, url=None):
        if url is None:
            url = self.plainTextEditUrl.toPlainText()
            category_list = url_parser(url)
            if category_list:
                self.listWidgetHandler(url, category_list)
                self.plainTextEditUrl.clear()

    def listWidgetHandler(self, url, category_list):
        text_playlist = self.get_name_for_list_widget(category_list, url)
        self.listWidgetUrls.addItem(text_playlist)
        self.all_categories.append(category_list)
        self.all_urls.append(url)
        number_item = self.listWidgetUrls.count()
        self.listWidgetUrls.setMaximumHeight(number_item * self.listWidgetUrls.sizeHintForRow(0))
        if self.listWidgetUrls.isHidden():
            self.listWidgetUrls.show()
        if not self.progressBar.isHidden():
            self.progressBar.hide()

    def get_name_for_list_widget(self, category_list, url):
        "This function get the album/song/playlist/artist name from url"
        try:
            if category_list == 'playlist':
                playlist = fetch_playlist(url)
                name = u"Playlist Name: {0}".format(slugify(playlist["name"], ok="-_()[]{}"))
                text_file = 'User: ' + playlist['tracks']['items'][0]['added_by']['id'] + ' - ' + name
            elif category_list == 'track':
                track = generate_metadata(url)
                text_file = 'Song: ' + track['name'] + ' - ' + track['album']['artists'][0]['name']
            elif category_list == 'artist':
                artist = fetch_albums_from_artist(url)
                text_file = u"Complete albums of " + artist[0]['artists'][0]['name']
            elif category_list == 'album':
                album = fetch_album(url)
                name = u"{0}".format(slugify(album["name"], ok="-_()[]{}"))
                text_file = 'Album: ' + name + ' of : ' + album['artists'][0]['name']
            else:
                text_file = 'Not Found name'
        except Exception as e:
            print("{} name not found! Setting standard name.".format(category_list))
            text_file = str(category_list) + url[31:-1]

        return text_file

    def progressBarcomplete(self, index):
        self.progressBar.setValue(100)

    def progressBarHandler(self, totalitem):
        if self.progressBar.isHidden():
            self.progressBar.show()
        if totalitem == 1:
            percentage = round(1 / (totalitem + 0.5), 2) * 100
        else:
            percentage = round(1 / totalitem, 2) * 100

        self.progressBar.setValue(percentage)

    def open_readme(self):
        pass

    def open_manual(self):
        webbrowser.open('https://nextcloud-theficos.duckdns.org/s/BHwEPTxrfyFiyWp')

    def out_format(self):
        "Function"
        sender_object = self.sender().objectName()
        if sender_object == 'action_mp3':
            const.args.output_ext = '.mp3'
            self.action_m4a.setChecked(False)
            self.action_flac.setChecked(False)
        elif sender_object == 'action_m4a':
            const.args.output_ext = '.m4a'
            self.action_mp3.setChecked(False)
            self.action_flac.setChecked(False)
        elif sender_object == 'action_flac':
            const.args.output_ext = '.flac'
            self.action_mp3.setChecked(False)
            self.action_m4a.setChecked(False)


    def encoding_sel(self):

        sender_object = self.sender().objectName()
        if sender_object == 'actionffmpeg':
            const.args.avconv = False
            self.actionavconv.isChecked(False)
        else:
            const.args.avconv = True
            self.actionffmpeg.isChecked(False)

    def advanced_option(self):
        sender_object = self.sender().objectName()
        if sender_object == 'actionDry_run':
            if self.actionDry_Run.isChecked():
                self.actionDry_Run.isChecked(False)
                const.args.dry_run = False
            else:
                self.actionDry_Run.isChecked(True)
                const.args.dry_run = True
        elif sender_object == "actionNo_Soaces":
            if self.actionNo_Spaces.isChecked():
                self.actionNo_Spaces.isChecked(False)
                const.args.no_spaces = False
            else:
                self.actionNo_Spaces.isChecked(True)
                const.args.no_spaces = True
        elif sender_object == "actionMusic_Video_Only":
            if self.actionMusic_Video_Only.isChecked():
                self.actionMusic_Video_Only.isChecked(False)
                const.args.music_videos_only = False
            else:
                self.actionMusic_Video_Only.isChecked(True)
                const.args.music_videos_only = True
        elif sender_object == "actionTrim_Silence":
            if self.actionTrim_Silence.isChecked():
                self.actionTrim_Silence.isChecked(False)
                const.args.trim_silence = False
            else:
                self.actionTrim_Silence.isChecked(True)
                const.args.trim_silence = True