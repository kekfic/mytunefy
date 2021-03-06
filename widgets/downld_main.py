"""
@author FF

"""
from queue import Queue

from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from PySide2.QtCore import QObject, Signal, SIGNAL

from gui.gui_main import Ui_MainWindow

from spotdl import const, internals
import threading
import webbrowser

from resources.db_handler import db_music_inserter
from resources.login import db_song_conn
from widgets.widget_class import YoutubeDialog
from resources import resources as rs
from lib_mytune import spotdl_inherited as spt_dl_in

"""
My list of variables:

    self.quecreat = Queue() - queue object for pushing data between threads
    self.all_urls = [] - list of the urls to be downloaded
    self.all_categories:  list of the type of argument (Playlist, Album, Song)
 
    self.count: TO be modified
    self.mydir: default folder to be opened for user 

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
    """Reimplementing main window for closeEvent option"""

    def closeEvent(self, event):
        result = QMessageBox.question(self,
                                      "Confirm Uscita MyTuneFy...",
                                      "Confermi di voler uscire ?",
                                      QMessageBox.Yes | QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()


class MainWin(QObject, Ui_MainWindow):
    """ this main class is the main window and contain all button specification """
    threadSignal = Signal(object)
    dialogSignal = Signal(object)

    def __init__(self):
        self.mainwindow = MyWindow()
        Ui_MainWindow.__init__(self)
        self.setupUi(self.mainwindow)

        QObject.__init__(self)
        # Todo; check all unused variables and functions
        self.quecreat = Queue()
        self.all_urls = []
        self.all_categories = []
        self.name_categories = []
        self.count = 0

        'hiding progress bar'
        self.progressBar.hide()
        'Two signal for folder and download button launch'
        self.pushButtonFolder.clicked.connect(self.folder_opener)
        self.StartPushButton.clicked.connect(self.download_button_handler)

        'setting the args global variable with default values'
        const.args = rs.get_arguments()
        const.args.folder = internals.get_music_dir()

        'Plain text, setting folder text and configuring signal'
        self.plainTextDirectory.setPlainText(const.args.folder)
        self.plainTextEditUrl.textChanged.connect(self.text_from_plain_text)

        'listWidget beahaviour'
        self.listWidgetUrls.hide()
        self.listWidgetUrls.itemDoubleClicked.connect(self.remove_item)

        self.menu_connection()

        self.pushButtonYoutube.clicked.connect(self.youtube_button)

        'Setting thread tha take care of the download, this allow a responsive main window'
        # self.mythread = MyClassThread(target=self.startDownload)
        self.mythread = threading.Thread(target=self.threaded_downloader, daemon=True)
        self.mythread.start()

        self.threadSignal.connect(self.thread_down_status_completed)

        'database connection configuration, in progress'
        self.database = db_song_conn()
        if self.database:
            self.db_thread = threading.Thread(target=db_music_inserter, daemon=True, args=(self.database,))
            self.db_thread.start()



    def folder_opener(self):
        """Selecting the download folder"""
        self.mydir = QFileDialog.getExistingDirectory(self.mainwindow, 'Select a directory', const.args.folder,
                                                      QFileDialog.ShowDirsOnly)
        if not self.mydir:
            self.mydir = internals.get_music_dir()
        self.plainTextDirectory.setPlainText(self.mydir)
        self.mydir.replace("/", "\\")
        const.args.folder = self.mydir

    def remove_item(self):
        """Remove item from QWidgetList if double clicked"""

        item = self.listWidgetUrls.currentRow()
        self.listWidgetUrls.takeItem(item)
        self.name_categories.pop(item)
        self.all_urls.pop(item)
        self.all_categories.pop(item)

    def download_button_handler(self):
        """When start button is pushed, check for correcteness nad start a thread for downloading"""
        # Todo: trying implement a better way of threading.
        self.count = self.listWidgetUrls.count()
        if self.count:
            self.quecreat.put([self.count, self.all_categories.copy(), self.all_urls.copy(), self.name_categories.copy()])
            "Clearing the QWidgetList and other objects"
            self.listWidgetUrls.clear()
            self.listWidgetUrls.hide()
            self.all_categories.clear()
            self.all_urls.clear()
            self.name_categories.clear()
            "Dehabilitate folder button"
            self.pushButtonFolder.setEnabled(False)
            self.progressBarHandler(self.count)

    def threaded_downloader(self):
        "Start the function for downloading"
        index = 0
        while threading.main_thread().is_alive():
            if index:
                # todo : change this criteria
                # if thread has ended the download, update the progressbar
                self.threadSignal.emit(index)
                #rs.songPusher.put(['end'])
                index = 0
            count, all_categories, all_urls, name_categories = self.quecreat.get()
            for i in range(count):
                url = all_urls[i]
                category_list = all_categories[i]
                "push"
                rs.songPusher.put(['category', all_categories[i], all_urls[i], name_categories[i]])
                "assign the current const.args.group"
                rs.assign_parser_url(category_list, url)
                "Starting the main according url parsing"
                spt_dl_in.main_func_caller()
                "Resetting the parser because it is unique"
                rs.reset_parser_url()

            index += 1

    def text_from_plain_text(self, url=None):
        if url is None:
            url = self.plainTextEditUrl.toPlainText()
            category_list = rs.url_parser(url)
            if category_list:
                self.listWidgetHandler(url, category_list)
                self.plainTextEditUrl.clear()

    def listWidgetHandler(self, url, category_list):
        "Get from urls and adding to list widget"

        text_playlist, name = spt_dl_in.get_name_for_list_widget(category_list, url)
        self.listWidgetUrls.addItem(text_playlist)
        self.name_categories.append(name)
        self.all_categories.append(category_list)
        self.all_urls.append(url)
        number_item = self.listWidgetUrls.count()
        self.listWidgetUrls.setMaximumHeight(number_item * self.listWidgetUrls.sizeHintForRow(0))
        if self.listWidgetUrls.isHidden():
            self.listWidgetUrls.show()
        if not self.progressBar.isHidden():
            self.progressBar.hide()

    def thread_down_status_completed(self, index):
        self.pushButtonFolder.setEnabled(True)
        self.progressBar.setValue(100)

    def progressBarHandler(self, totalitem):
        if self.progressBar.isHidden():
            self.progressBar.show()
        if totalitem == 1:
            percentage = round(1 / (totalitem + 0.5), 2) * 100
        else:
            percentage = round(1 / totalitem, 2) * 100

        self.progressBar.setValue(percentage)

    """
        ------------------------------------------------------------
                    Youtube Dialog - blocking
        ------------------------------------------------------------
    """

    def youtube_button(self):
        temp = YoutubeDialog(QDialog(self.mainwindow), self.dialogSignal)
        if temp.dialog.exec_():
            pass

    def playlist_button(self):
        pass
    """ 
        ------------------------------------------------------------
                                Menu
        ------------------------------------------------------------
    """
    def menu_connection(self):
        'Menu signals'
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

    def open_readme(self):
        pass

    def open_manual(self):
        pass

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
