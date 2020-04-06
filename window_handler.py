"""
@author FF

"""
import time

from PySide2 import QtWidgets

from PySide2.QtWidgets import QMainWindow, QFileDialog, QSplashScreen, QWidget, QLabel, QPushButton, QHBoxLayout, \
    QListWidgetItem, QDialog, qApp

from PySide2.QtCore import QObject
from pyside2uic.properties import QtCore

from gui.gui_main import Ui_MainWindow
import re
import getpass

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
from spotify_tools import fetch_playlist, fetch_album, fetch_albums_from_artist
from slugify import slugify

from my_main_functions import main, url_parser, assign_parser_url, reset_parser_url


class MainWin(QObject, Ui_MainWindow):
    """ this main class is the main window and contain all button specification """

    def __init__(self):
        self.mainwindow = QMainWindow()
        Ui_MainWindow.__init__(self)
        self.setupUi(self.mainwindow)
        QObject.__init__(self)

        self.all_urls = []
        self.all_categories = []
        self.text_file = ''
        self.operation = ''
        self.url_text = False
        self.pushButtonFolder.clicked.connect(self.folder_opener)
        self.progressBar.hide()
        self.StartPushButton.clicked.connect(self.startDownload)

        const.args = handle.get_arguments()
        const.args.folder = internals.get_music_dir()

        self.plainTextDirectory.setPlainText(const.args.folder)
        self.plainTextEditUrl.textChanged.connect(self.text_from_plain_text)

        self.listWidgetUrls.hide()
        self.listWidgetUrls.itemDoubleClicked.connect(self.remove_item)

        # Todo self action Paste has not been implemented
        """
        self.actionPaste = QtWidgets.QAction(self.plainTextEditUrl)
        self.actionPaste.setObjectName("actionPaste")
        #self.actionPaste.setShortcut(_translate("ModifiedTableView", "Ctrl+V"))
        self.actionPaste.triggered.connect(self.text_from_plain_text)
        self.plainTextEditUrl.addAction(self.actionPaste)
        self.copiedtext = qApp.clipboard().text()
        """
        """
        self.rcMenu = QtWidgets.QMenu(self.mainwindow)
        self.action_delete_row = self.rcMenu.addAction('Delete Row', self.delete_row)
        #self.action_insert_row = self.rcMenu.addAction('Insert Row', self.insert_row)
        self.mainwindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.mainwindow.customContextMenuRequested.connect(self.onRightClick)
        #

    def onRightClick(self, QPos=None):
        parent = self.sender()
        pPos = parent.mapToGlobal(QtCore.QPoint(5, 20))
        mPos = pPos + QPos

        self.rcMenu.move(mPos)
        self.rcMenu.show()

    def delete_row(self):
        self.listWidgetUrls.removeItemWidget(self,)
        """

    def folder_opener(self):
        "Selecting the download folder"
        mydefaultfolder = 'C:\\Users\\' + getpass.getuser() + '\\Music\\'
        self.mydir = QFileDialog.getExistingDirectory(self.mainwindow, 'Select a directory', mydefaultfolder,
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


    def startDownload(self):
        #Todo I don't like it very much
        "Start the function for downloading"
        count = self.listWidgetUrls.count()
        if count:
            for i in range(count):

                self.progressBarHandler(i, count)
                url = self.all_urls[i]
                category_list = self.all_categories[i]
                "assign the current const.args.group"
                assign_parser_url(category_list, url)
                "Starting the main according url parsing"
                main()
                "Resetting the parser because it is unique"
                reset_parser_url()
        "Clearing the QWidgetList and other objects"
        self.listWidgetUrls.clear()
        self.progressBar.setValue(100)
        self.all_categories.clear()
        self.all_urls.clear()

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
        try:
            if category_list == 'playlist':
                playlist = fetch_playlist(url)
                text_file = u"Playlist: {0}".format(slugify(playlist["name"], ok="-_()[]{}"))
                text_file = text_file.upper() + ' of user: ' + playlist['tracks']['items'][0]['added_by']['id']
            elif category_list == 'track':
                track = spotify_tools.generate_metadata(url)
                text_file = track['name'] + ' - ' + track['album']['artists'][0]['name']
            elif category_list == 'artist':
                artist = fetch_albums_from_artist(url)
                text_file = u"Complete albums of " + artist[0]['artists'][0]['name']
            elif category_list == 'album':
                album = fetch_album(url)
                text_file = u"{0}".format(slugify(album["name"], ok="-_()[]{}"))
                text_file = text_file + ' of artist: ' + album['artists'][0]['name']
            else:
                text_file = 'Not Found name'
        except Exception as e:
            print("Name not found")
            text_file = str(category_list) + url[31:-1]

        return text_file

    def progressBarHandler(self, numbitem, totalitem):
        if self.progressBar.isHidden():
            self.progressBar.show()
        percentage = round(numbitem/totalitem, 2)*100
        self.progressBar.setValue(percentage)



    def check_url(self, junk):
        if junk == 'https://open.spotify':
            valid_url = True
        else:
            valid_url = False

        return valid_url

    def time_dep_program(self, time_system):
        print('Time system is:')
