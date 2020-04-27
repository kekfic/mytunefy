# Importing Required Modules & libraries
import operator
from getpass import getpass
from tkinter import *
import pygame
import os

from PySide2.QtCore import QObject, Signal, QAbstractTableModel, SIGNAL, Qt, QModelIndex
from PySide2.QtWidgets import QMainWindow, QMessageBox, QApplication, \
    QHeaderView, QTableView
from spotdl import internals

from list_class.mydelegate import ButtonDelegate
from gui.gui_main_player import Ui_PlayerMainWindow
from list_class.tableViewClass import MyTableView
from resources.db_handler import player_get_all_songs, player_get_all_user_data, parsing_user_db_data, get_songs_from_db
from resources.downloader import get_tracks_playlist, get_tracks_album


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
    dictListView = {
        "Playlist": 0,
        "Album": 1,
        "Artista": 2,
        "Brani": 3,
        "Cartella": 4
    }

    def __init__(self):
        self.main_window_player = MyReimplementedWindow()
        Ui_PlayerMainWindow.__init__(self)
        self.setupUi(self.main_window_player)

        QObject.__init__(self)

        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init(48000, -16, 2, 1024)

        if os.path.isfile('db_data/song_db'):
            self.category = self.comboBoxCategory.currentText()
            self.category_list = self.get_list_in_db()
            # songs_in_db = self.get_songs(self.category, self.category_list)
            # self.category_list.append(songs_in_db)
            self.fill_list_view(self.category, self.category_list)

        self.comboBoxCategory.currentIndexChanged.connect(self.combo_box_handler)
        # todo set
        self.local_tracks = self.local_song_folder()

        self.tableView = MyTableView(self.frame_songs, self.local_tracks)
        self.playlist_label.setText("Cartella Locale - ~/Musica")
        self.verticalLayout_QTableView.addWidget(self.tableView)

        self.listWidget.itemDoubleClicked.connect(self.play_item)
        self.listWidget.itemClicked.connect(self.select_list)
        "Unsetting for now the delegate, I am not ready for using it"
        # self.tableView.setItemDelegate(ButtonDelegate(self))
        # self.connect(self.tableView.mouseDoubleClickEvent, SIGNAL("triggered()"), self.double_click_table)

        self.tableView.doubleClicked.connect(self.double_click_table)
        # self.PlayPauseButton.con
        #self.connect(self.PlayPauseButton, SIGNAL('triggered()'), self.playsong)
        self.PlayPauseButton.clicked.connect(self.playsong)


    def printer(self):
        print('hello')

    def play_item(self):
        pass

    def select_list(self):
        item = self.listWidget.currentItem()
        self.songtracks = self.get_songs(item.text(), self.category, self.category_list)

        header = ['', '', 'Title', 'Artist', 'Album', 'Date', '', '']
        self.playlist_label.setText(item.text())
        self.tableView.set_new_model(self.frame_songs, self.songtracks, header)

    def double_click_table(self, index):
        row = index.row()
        print(row)
        print(self.songtracks[row])
        self.song_name_label.setText(self.songtracks[row][1])
        self.song_artist_label.setText(self.songtracks[row][0])
        self.playsong(self.playlist[row], self.folder_song[row])

    def parsing_song(self, song):
        # todo call with another name and move from here
        # poping format
        listsplit = re.split(r'[-.]', song)
        listsong = [x.strip() for x in listsplit]
        art = listsong[1].split('(')[0]
        artist = art.strip()

        return [listsong[0], artist, 'Album', 'Current Folder']

    # ---------------------------------------------------------------------------------
    def playsong(self, songname, folder_song):
        if self.status_play == True:
            self.stopsong()
        # Displaying Selected Song title
        # self.track.set(self.playlist.get(ACTIVE))
        # # Displaying Status
        # self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(songname+'/'+folder_song)
        # Playing Selected Song
        pygame.mixer.music.play()
        self.status_play = True

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

    # -----------------------------------------------------------------------

    def get_list_in_db(self):
        res = player_get_all_user_data()
        if res:
            self.playlist, self.album, self.artist, \
            plname, alname, arname = parsing_user_db_data(res)
        else:
            return [None, None, None]

        return [plname, alname, arname]

    def local_song_folder(self):
        self.music_folder = internals.get_music_dir()

        # Fetching Songs
        raw_song_tracks = os.listdir(self.music_folder)
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
                # eliminating wrong format or other file in folder
                self.raw_songs.pop(i)
            i += 1

        return songtracks

    def combo_box_handler(self):
        self.listWidget.clear()
        self.category = self.comboBoxCategory.currentText()
        self.fill_list_view(self.category, self.category_list)

    def fill_list_view(self, category, category_list):
        # Todo: aggiungere selezione da cartella locale
        item = self.dictListView[category]
        self.listWidget.addItems(category_list[item])

    def get_songs(self, option, category, category_list):
        """Option indicate a single category, if not all song will be returned
            song structure:
            artist, song_name, album, folder

        """

        if category == 'Cartella':
            raw_songs = self.local_song_folder()
        elif category == 'Brani':
            raw_songs = get_songs_from_db(id, category)
            pass
        else:
            "if id is for brani, nothing happens"
            index_cat = category_list[self.dictListView[category]]
            id = index_cat.index(option) + 1
            raw_songs = get_songs_from_db(id, category)
            tracks = []
            self.playlist = []
            self.folder_song = []
            for item in raw_songs:
                artist_id = item[4]
                album_id = item[3]
                tracks.append([category_list[2][artist_id - 1], item[2],
                               category_list[1][album_id - 1], item[5], item[6]])
                self.playlist.append(item[5])
                self.folder_song.append(item[6])

        return tracks

    def comboBoxParser(self, key, datalist):
        # todo: implement it
        print("Starting the data parsing.")
        switcher = {
            'Artista': self.get_songs,
            'Album': self.get_songs,
            'Playlist': self.fanc3,
            'Brani': self.func4,
            'Cartella': self.func5,
        }
        func = switcher.get(key)(datalist)
        return func


class spotyfyDataRetrievier:
    """This class save data"""

    def __init__(self, name, category, url):

        self._name = name
        self._category = category
        self._url = url
        self._tracks = []
        self._get_tracks_from_url()
        self._only_tracks = []

    def numb_songs(self):
        return self._song_numb

    def track_data(self):
        return self._tracks

    def name(self):
        return self._name

    def only_tracks(self):
        return self._only_tracks

    def _get_tracks_from_url(self):

        if self._category == 'Album':
            self.data, self._song_numb = get_tracks_playlist(self._url)

            for i in range(self._song_numb):
                self._only_tracks.append(self.data[0][i])
                self._tracks.append([self.data[0][i],
                                     self.data[1], self.data[2], self.data[3][i]])

        elif self._category == 'Playlist':
            self.data, self._song_numb = get_tracks_playlist(self._url)
            self._tracks = self.data

    # def _match_song_with_local_data(self):
    #     song_in_db = get_songs(self._category, self._name, artist=True)
    #     only_songs = []
    #     for row in song_in_db:
    #         only_songs.append(row[1])
    #
    #     if len(song_in_db) == self._song_numb:
    #         if self._only_tracks.sort() == only_songs.sort():
    #             print ("List are equal")
    #             self.matching = True
    #     else:
    #         print(" Not matching")
    #         self.matching = False
    #         self.diff = self._song_numb - len(song_in_db)
    #         for i in range(self._song_numb):
    #             print('select every song to che existance')
    #     pass
