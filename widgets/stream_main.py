"""
@author FF

"""
import os
import sys
from queue import Queue

from PySide2.QtCore import QObject, Signal, Qt
from PySide2.QtWidgets import QFileDialog, QApplication, QWidget


from gui.stream_list import Ui_StreamListAdd

from spotdl import const, internals
from lib_mytune.spotdl_inherited import *
import threading

from resources import resources as rs
from lib_mytune import spotdl_inherited as spt_dl_in
from resources.db_streaming import db_music_stream_inserter
from resources.login import db_song_stream_conn


class MainStream(QObject, Ui_StreamListAdd):
    urlDataSignal = Signal()

    """ this main class is the main window and contain all button specification """
    # threadSignal = Signal(object)
    # dialogSignal = Signal(object)
    def __init__(self, parent=None):
        self.stream_window = QWidget()
        super(MainStream, self).__init__(parent)
        Ui_StreamListAdd().__init__()
        self.setupUi(self.stream_window)
       # self.stream_window.setWindowModality(Qt.WindowModality)

        self.quecreat = Queue()
        self.all_urls = []
        self.all_categories = []
        self.name_categories = []
        self.count = 0

        'hiding progress bar'
        self.progressBar.hide()
        'Two signal for folder and download button launch'
        self.pushButtonFolder.clicked.connect(self.folder_opener)
        

        'setting the args global variable with default values'
        const.args = rs.get_arguments()
        const.args.folder = internals.get_music_dir()
        os.makedirs('cache', exist_ok=True)
        const.args.folder = os.getcwd() + '/cache/'

        'Plain text, setting folder text and configuring signal'
        self.plainTextEditUrl.textChanged.connect(self.text_from_plain_text)

        'listWidget beahaviour'
        self.listWidgetUrls.hide()
        self.listWidgetUrls.itemDoubleClicked.connect(self.remove_item)
        self.pushButtonStream.clicked.connect(self.stream_button_handler)
        self.database_streaming = db_song_stream_conn()
    
    def stream_button_handler(self):
        """When start button is pushed, check for correcteness nad start a thread for downloading"""
        # Todo: trying implement a better way of threading.
        self.count = self.listWidgetUrls.count()
        if self.count:
            self.retrieve_data([self.count, self.all_categories.copy(), self.all_urls.copy(), self.name_categories.copy()])
            "Clearing the QWidgetList and other objects"
            self.listWidgetUrls.clear()
            self.listWidgetUrls.hide()
            self.all_categories.clear()
            self.all_urls.clear()
            self.name_categories.clear()
            "Dehabilitate folder button"
            #self.pushButtonFolder.setEnabled(False)
            # self.progressBarHandler(self.count)

    def retrieve_data(self, data):

        all_tracks = []

        count, all_categories, all_urls, name_categories = data

        for i in range(count):
            category_list = all_categories[i]

            if category_list == 'playlist':
                all_tracks = get_tracks_playlist(all_urls[i])
            elif category_list == 'album':
                all_tracks = get_tracks_album(all_urls[i])
            elif category_list == 'artist':
                #all_tracks, num_tracks = get_tracks_artist(all_urls[i])
                pass
            elif category_list == 'track':
                pass
            "assign the current const.args.group"

            db_music_stream_inserter([all_categories[i], all_urls[i], name_categories[i], all_tracks], self.database_streaming)

            #todo: check if aI need this part
            rs.assign_parser_url(category_list, all_urls[i])
            "Starting the main according url parsing"
            #spt_dl_in.main_func_caller()
            "Resetting the parser because it is unique"
            rs.reset_parser_url()


    def folder_opener(self):
        """Selecting the download folder"""
        self.mydir = QFileDialog.getExistingDirectory(self.stream_window, 'Select a directory', const.args.folder,
                                                      QFileDialog.ShowDirsOnly)
        if not self.mydir:
            self.mydir = internals.get_music_dir()
        #self.plainTextDirectory.setPlainText(self.mydir)
        self.mydir.replace("/", "\\")
        const.args.folder = self.mydir

    def remove_item(self):
        """Remove item from QWidgetList if double clicked"""

        item = self.listWidgetUrls.currentRow()
        self.listWidgetUrls.takeItem(item)
        self.name_categories.pop(item)
        self.all_urls.pop(item)
        self.all_categories.pop(item)
    
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

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     gui = MainStream()
#     gui.stream_window.show()
#     sys.exit(app.exec_())