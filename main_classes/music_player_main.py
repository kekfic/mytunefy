# Importing Required Modules & libraries
import operator
from getpass import getpass
from tkinter import *
import pygame
import os


from PySide2.QtCore import QObject, Signal, QAbstractTableModel, SIGNAL, Qt, QModelIndex
from PySide2.QtWidgets import QMainWindow, QMessageBox, QApplication, \
    QHeaderView, QTableView
from list_class.mydelegate import ButtonDelegate
from gui.gui_main_player import Ui_PlayerMainWindow
from list_class.tableViewClass import MyTableView
from resources.database_mytunefy import player_get_all_songs, player_get_all_user_data, parsing_user_db_data


class MyReimplementedWindow(QMainWindow):
    """Reimplementing main window for closeEvent option"""

    def closeEvent(self, event):
        result = QMessageBox.question(self,
                                      "Confirm Uscita MyTuneFy...",
                                      "Confermi di voler uscire ?",
                                      QMessageBox.Yes | QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()


class MainWinPlayer(QObject, Ui_PlayerMainWindow):
    """ this main class is the main window and contain all button specification """

    # threadSignal = Signal(object)

    def __init__(self):
        self.main_window_player = MyReimplementedWindow()
        Ui_PlayerMainWindow.__init__(self)
        self.setupUi(self.main_window_player)

        QObject.__init__(self)

        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()

        if os.path.isfile('db_data/song_db'):
            self.get_playlist_in_db()

        self.comboBoxCategory.currentIndexChanged.connect(self.combo_box_handler)
        # todo set
        songtracks = self.local_song_folder()

        self.tableView = MyTableView(self.frame_songs, tracks=songtracks)
        self.verticalLayout_QTableView.addWidget(self.tableView)

        "Unsetting for now the delegate, I am not ready for using it"
        #self.tableView.setItemDelegate(ButtonDelegate(self))
        #self.connect(self.tableView.mouseDoubleClickEvent, SIGNAL("triggered()"), self.double_click_table)
        self.tableView.doubleClicked.connect(self.double_click_table)
        #self.PlayPauseButton.con
        self.connect(self.PlayPauseButton, SIGNAL('triggered()'), self.playsong)


        # Inserting Songs into Playlist
        # for track in songtracks:
        #     self.playlist.insert(END, track)
    def printer(self):
        print('hello')

    def double_click_table(self, index):
        row = index.row()
        column = index.column()

    def parsing_song(self, song):
        #todo call with another name and move from here
        listsplit = re.split(r'[-.]', song)
        listsong = [x.strip() for x in listsplit]
        art = listsong[1].split('(')[0]
        artist = art.strip()

        return [listsong[0], artist, listsong[2]]

    #---------------------------------------------------------------------------------
    def playsong(self, songname):
        # Displaying Selected Song title
        #self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load()
        # Playing Selected Song
        pygame.mixer.music.play()

    def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

    def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()

    def unpausesong(self):
        # Displaying Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()

    #-----------------------------------------------------------------------


    def get_playlist_in_db(self):
        res = player_get_all_user_data()
        if res:
            self.playlist, self.artist, self.album = parsing_user_db_data(res)


    def local_song_folder(self, folder):
        my_working_folder = os.getcwd()
        try:
            os.chdir(folder)
        except Exception as e:
            print(e)
            self.mydir = 'C:\\Users\\' + getpass.getuser() + '\\Music\\'

        # Fetching Songs
        raw_song_tracks = os.listdir()
        self.raw_songs = raw_song_tracks.copy()
        songtracks = []

        i = 0
        for item in raw_song_tracks:
            if '.mp3' in item:
                try:
                    labels = self.parsing_song(item)
                    #  labels.insert(0, QPushButton(''))
                    songtracks.append(labels)
                except Exception as e:
                    print('Song: {} - not consider cause {}'.format(item, e))
                    self.raw_songs.pop(i)
            else:
                self.raw_songs.pop(i)
            i += 1

        os.chdir(my_working_folder)

        return songtracks

    def combo_box_handler(self):
        category = self.comboBoxCategory.currentText()
        self.fill_list_view(category)

    def fill_list_view(self, category):
        self.listWidget.addItem()