# Importing Required Modules & libraries
import operator
import time
from getpass import getpass
from tkinter import *
import os

from PySide2 import QtGui, QtCore
from PySide2.QtCore import QObject, Signal, QAbstractTableModel, SIGNAL, Qt, QModelIndex, QEvent
from PySide2.QtWidgets import QMainWindow, QMessageBox, QApplication, \
    QHeaderView, QTableView
from spotdl import internals
from spotdl.internals import sanitize_title

from list_class.mydelegate import ButtonDelegate
from gui.gui_main_player import Ui_PlayerMainWindow
from list_class.tableViewClass import MyTableView
from resources.player import SongPlayer
from resources.db_handler import player_get_all_songs, player_get_all_user_data, parsing_user_db_data, get_songs_from_db
from resources.downloader import get_tracks_playlist, get_tracks_album


class MyReimplementedWindow(QMainWindow):
    """Reimplementing main window for closeEvent option"""
    closeSignal = Signal()

    def closeEvent(self, event):
        result = QMessageBox.question(self,
                                      "Confirm Uscita MyTuneFy...",
                                      "Confermi di voler uscire ?",
                                      QMessageBox.Yes | QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            self.closeSignal.emit()
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

        self.my_song_player = SongPlayer(self.horizontalSlider, self.verticalSlider)
        self.horizontalSlider.sliderReleased.connect(self.h_slider_hanlder)
        self.horizontalSlider.sliderMoved.connect(self.h_slider_hanlder)
        #self.horizontalSlider.valueChanged.connect(self.h_slider_hanlder)

        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(2000)  # .5 seconds
        self.checkThreadTimer.start()

        self.checkThreadTimer.timeout.connect(self.slider_update)

        self.shuffle = False
        self.current_list = ''
        self.comboBoxCategory.setCurrentIndex(4)# setting index at cartella
        if os.path.isfile('db_data/song_db'):
            self.category = self.comboBoxCategory.currentText()
            self.category_list = self.get_list_in_db()
            if self.category != 'Cartella':

                self.fill_list_view(self.category, self.category_list)

        self.comboBoxCategory.currentIndexChanged.connect(self.combo_box_handler)
        # todo set
        self.local_tracks, self.filenames_local = self.get_local_songs()

        self.header = ['', '', 'Title', 'Artist', 'Album', 'Date', '', '']
        self.tableView = MyTableView(self.frame_songs, self.local_tracks)

        self.playlist_label.setText("Cartella Locale - ~/Musica")
        self.verticalLayout_QTableView.addWidget(self.tableView)


        self.listWidget.itemClicked.connect(self.select_list)

        "Unsetting for now the delegate, I am unable to use it well"
        # self.tableView.setItemDelegate(ButtonDelegate(self))
        # self.connect(self.tableView.mouseDoubleClickEvent, SIGNAL("triggered()"), self.double_click_table)

        self.main_window_player.closeSignal.connect(self.clearExit)

        #this three signal do almost the same thing, condensate
        self.listWidget.itemDoubleClicked.connect(self.play_list)
        self.tableView.doubleClicked.connect(self.double_click_table)
        self.pushButtonPlaylist.clicked.connect(self.play_list)

        "song bar button behaviour"
        self.PlayPauseButton.clicked.connect(self.play_track)
        self.nextTrackButton.clicked.connect(self.next_track)
        self.backTrackButton.clicked.connect(self.back_track)
        self.shuffleButton.clicked.connect(self.shuffle_mode)
        self.repeatButton.clicked.connect(self.repeat_mode)
        self.my_song_player.songChanged.connect(self._song_changed)



    def clearExit(self):
        print('Use thi function for saving data and cleaning')


    def h_slider_hanlder(self):

        value = self.horizontalSlider.value()
        self.my_song_player.set_song_position(value)

    def slider_update(self):
        if self.my_song_player.is_playing():
            value = self.my_song_player.get_slider_position()*100
            self.horizontalSlider.setValue(value)

    def _song_changed(self, data):
        # Todo: something strange with index
        artist, song_name, index = data
        if index:

            if self.category == 'Cartella':
                self.label_song_text_setter(self.local_tracks[index][0],
                                            self.local_tracks[index][1])
                self.tableView.playing_behavior(index)

            else:
                self.label_song_text_setter(self.songtracks[index][1],
                                        self.songtracks[index][0])
                self.tableView.playing_behavior(index)


    def play_item(self):
        pass

    def select_list(self):
        self.list_selected = True
        item = self.listWidget.currentItem()
        if item is None:
            list_widget= self.current_list
        else:
            list_widget = item.text()
        songtracks = self.get_songs(list_widget, self.category, self.category_list)

        self.playlist_label.setText(item.text())

        # songtracks = sorted(songtracks, key=operator.itemgetter(3))
        # songtracks.reverse()

        self.tableView.set_new_model(self.frame_songs, songtracks, self.header)
        if item.text() == self.current_list:
            self.pushButtonPlaylist.setText('Pause')
        else:
            self.pushButtonPlaylist.setText('Play')

        return item.text(), songtracks

    def play_list(self):
        #todo:wrong logic, shoul take into account which list

        sender_object = self.sender().objectName()
        item = self.listWidget.currentItem().text()
        if sender_object == 'pushButtonPlaylist':
            print (item)

        if self.current_list == item:
            self.pause_track()
            self.pushButtonPlaylist.setText('Play')
        else:
            self.pause_track()
            self.pushButtonPlaylist.setText('Pause')
            self.current_list, self.songtracks = self.select_list()
            # self.songtracks.sorted(self.songtracks,
            #                      key=operator.itemgetter(3))
            # self.songtracks.reverse()
            self.play = True
            self.my_song_player.set_list(self.filenames, self.current_list)
            self.play_track()

    def double_click_table(self, index):
        row = index.row()
#        self.tableView.rowAt()
        if self.category == 'Cartella':
            self.current_list = 'Local'
            self.filenames= self.filenames_local
            pass
        else:
            self.current_list, self.songtracks = self.select_list()
            self.label_song_text_setter(self.songtracks[row][1],
                                    self.songtracks[row][0])
        self.tableView.playing_behavior(row)
        self.my_song_player.play_this_item(row, self.filenames, self.current_list)
        self.PlayPauseButton.setChecked(True)
        self.pushButtonPlaylist.setText('Pause')
       # self.playsong(self.playlist[row], self.folder_song[row])

    def label_song_text_setter(self, songname='', artist='' ):
        self.song_name_label.setText(songname)
        self.song_artist_label.setText(artist)

    def parsing_song(self, song):
        # todo call with another name and move from here
        # poping format
        listsplit = re.split(r'[-.]', song)
        listsong = [x.strip() for x in listsplit]
        art = listsong[1].split('(')[0]
        artist = art.strip()

        return [listsong[0], artist, 'Album', 'Current Folder']

    # ---------------------------------------------------------------------------------
    def play_track(self):
        if self.my_song_player.is_playing():
            self.my_song_player.pause_track()
            #self.PlayPauseButton.setStyleSheet('image: url(:/mytunefy/resources/icons/play_grey.png);')
        else:
            self.my_song_player.play_track()
            #self.PlayPauseButton.setStyleSheet('image: url(:/mytunefy/resources/icons/pause-butt.png)')

    def pause_track(self):
        self.my_song_player.pause_track()

    def next_track(self):
        self.my_song_player.next_track()

    def back_track(self):
        self.my_song_player.back_track()

    def shuffle_mode(self):
        if self.shuffle == True:
            self.my_song_player.shuffle_mode(False)
            self.shuffle = False
        else:
            self.shuffle = True
            self.my_song_player.shuffle_mode(True)

    def repeat_mode(self):
        self.repeat = True
    # -----------------------------------------------------------------------

    def get_list_in_db(self):
        res = player_get_all_user_data()
        if res:
            self.playlist, self.album, self.artist, \
            plname, alname, arname = parsing_user_db_data(res)
        else:
            return [None, None, None]

        return [plname, alname, arname]

    def get_local_songs(self):
        self.music_folder = internals.get_music_dir()

        # Fetching Songs
        raw_song_tracks = os.listdir(self.music_folder)
        self.raw_songs = raw_song_tracks.copy()
        songtracks = []
        filenames_local = []
        i = 0
        for item in raw_song_tracks:
            if '.mp3' in item:
                try:
                    filenames_local.append(self.music_folder + '/' + item)
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

        return songtracks, filenames_local

    def combo_box_handler(self):
        self.listWidget.clear()
        self.category = self.comboBoxCategory.currentText()
        if self.category == 'Cartella':
           self.local_tracks, self.filenames_local= self.get_local_songs()
           self.tableView.set_new_model(self.frame_songs, self.local_tracks, self.header)
        else:
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
            raw_songs = self.get_local_songs()
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
            self.filenames = []
            self.duration = []
            raw_songs = sorted(raw_songs, key=operator.itemgetter(5))

            for item in raw_songs:
                artist_id = item[4]
                album_id = item[3]
                tracks.append([category_list[2][artist_id - 1], item[2],
                               category_list[1][album_id - 1], item[5]])

                time.sleep(0.5)

                self.filenames.append(item[5])
#                self.filenames.append(item[6] + '/' + title_raw + ext)
                self.duration.append(item[7])



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
