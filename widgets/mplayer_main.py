# Importing Required Modules & libraries
import operator

import os
import threading
import time

from widgets.downld_main import MainWin
from PySide2 import QtGui
from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QMainWindow, QMessageBox
from spotdl import internals, const
from resources import resources as rs, graphics
from gui.gui_main_player import Ui_PlayerMainWindow
from list_class.tableViewClass import MyTableView
from lib_mytune.player import SongPlayer
from resources.internal_classes import SongData
from resources.db_handler import player_get_all_user_data, parsing_user_db_data,\
    get_songs_from_db
from lib_mytune import spotdl_inherited as spt_dl_in

from widgets.stream_main import MainStream


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
        "Initial variables"
        self._id_artist_list = []
        self._id_album_list = []
        self._artists_name_list = []
        self._album_name_list = []
        self._stream_mode = False
        self.shuffle = False
        self.current_playing_list = ''
        self.playing_song_data = ''
        self.playing_category = ''
        self.current_item = None
        self.current_playing_tracks_list = [['', ''], ['', '']]
        self.current_p_tracks_list_url = [['', ''], ['', '']]
        self.label_User.setText(os.getlogin())
        self.my_song_player = SongPlayer(self.horizontalSlider, self.verticalSlider)
        self.pushButtonDownloader.clicked.connect(self.down_main_window)
        self.StreamModeButton.clicked.connect(self.stream_mode_button)
        self.verticalSlider.valueChanged.connect(self.volume_hanler)

        graphics.scroll_bar_appearance(self.listWidget.verticalScrollBar())
        self.verticalSlider.setValue(100)

        self.comboBoxCategory.setCurrentIndex(4)  # setting index at cartella
        if os.path.isfile('db_data/song_db'):
            self.category = self.comboBoxCategory.currentText()
            self.category_list = self.get_list_in_db(db_name='song_db')
            if self.category != 'Cartella':
                self.fill_list_view(self.category, self.category_list)

        self.comboBoxCategory.currentIndexChanged.connect(self.combo_box_handler)
        # todo set

        self.set_local_folder()
        self.local_tracks, self.filenames_local = self.get_local_songs()

        self.header = ['', '', 'Title', 'Artist', 'Album', 'Folder', '', '']
        self.tableView = MyTableView(self.frame_songs, self.local_tracks)

        self.playlist_label.setText("Cartella Locale - ~/Musica")
        self.verticalLayout_QTableView.addWidget(self.tableView)

        self.listWidget.itemClicked.connect(self.select_list)

        "Unsetting for now the delegate, I am unable to use it well"
        # self.tableView.setItemDelegate(ButtonDelegate(self))
        # self.connect(self.tableView.mouseDoubleClickEvent, SIGNAL("triggered()"), self.double_click_table)

        self.main_window_player.closeSignal.connect(self.cleanExit)


        header = self.tableView.horizontalHeader()
        header.sectionClicked.connect(self.sort_table_view)
      #  header.sectionsClide
        self.tableView.doubleClicked.connect(self.double_click_table)
        self.listWidget.itemDoubleClicked.connect(self.play_list)
        self.pushButtonPlaylist.clicked.connect(self.play_list_button)

        "song bar button behaviour"
        self.PlayPauseButton.clicked.connect(self.play_track)
        self.nextTrackButton.clicked.connect(self.next_track)
        self.backTrackButton.clicked.connect(self.back_track)
        self.shuffleButton.clicked.connect(self.shuffle_mode)
        self.repeatButton.clicked.connect(self.repeat_mode)
        # ----------------------------------------------------

        self.my_song_player.songChanged.connect(self._song_changed)

        self.streaming_thread = threading.Thread(target=self.downloader_stream, args=(), daemon=True)
        self.streaming_thread.start()


    def _song_changed(self, data):
        # Todo: something strange with index
        artist, song_name, index = data
        self.playing_song_data = [artist, song_name, index]
        if index:
            if self.category == 'Cartella':
                self.label_song_text_setter(self.local_tracks[index][0],
                                            self.local_tracks[index][1])
                self.tableView.playing_behavior(index)

            else:
                item = self.listWidget.currentItem()
                if item.text() == self.current_playing_list:
                    self.label_song_text_setter(self.songs_category.tracks()[index][1],
                                                 self.songs_category.tracks()[index][0])
                    self.tableView.playing_behavior(index)
                else:
                    self.label_song_text_setter(self.current_playing_tracks_list[index][1],
                                                self.current_playing_tracks_list[index][0])
                    

    def sort_table_view(self):
        order = self.tableView.horizontalHeader().sortIndicatorOrder().name.decode()
        position = self.my_song_player.get_slider_position()
        artist, song_name, index = self.playing_song_data
        if not song_name:
            song_name = self.songs_category.song_names()[index]

        if index == 2:
            self.songs_category.sort_data('song_names', order)
        elif index == 3:
            self.songs_category.sort_data(order=order)

        index = self.songs_category.song_names().index(song_name)

        self.my_song_player.stop()
        self.my_song_player.play_this_item(index, self.songs_category.filenames(), self.current_playing_list)
        self.tableView.playing_behavior(index)
        self.my_song_player.play_track()
        self.my_song_player.set_song_position(position*100)


    def select_list(self):
        #Todo: meditate if is safer and more efficient use local variable(not self)
        # ------ Important------
        self.item = self.listWidget.currentItem()
        if self.item is None:
            list_widget = self.current_item
        else:
            list_widget = self.item.text()

        if self._stream_mode:
            songtracks = self.get_songs(list_widget, self.category, self.category_list, dbname='song_stream_db')
        else:
            songtracks = self.get_songs(list_widget, self.category, self.category_list)

        self.playlist_label.setText(self.item.text())

        self.tableView.set_new_model(self.frame_songs, songtracks, self.header)
        if self.item.text() == self.current_playing_list:
            self.pushButtonPlaylist.setText('Pause')
        else:
            self.pushButtonPlaylist.setText('Play')

        if self.playing_song_data and self.item.text() == self.current_playing_list:
            artist, song_name, index = self.playing_song_data
            if index:
                self.tableView.playing_behavior(index)

        return self.item, songtracks

    def play_list_button(self):
        #Todo: reorganize this function
        item = self.listWidget.currentItem()
        if self.pushButtonPlaylist.text() == 'Pause':
            self.my_song_player.pause_track()
            self.pushButtonPlaylist.setText('Play')
            self.PlayPauseButton.setChecked(False)
        else:
            self.pushButtonPlaylist.setText('Pause')
            if self.category == 'Cartella':
                self.my_song_player.stop()
                self.current_playing_list = 'Local'
                self.filenames = self.filenames_local.copy()
                self.my_song_player.set_list(self.filenames, self.current_playing_list)
                self.play_track()
                self.label_song_text_setter(self.local_tracks[0][0],
                                            self.local_tracks[0][1])
                self.PlayPauseButton.setChecked(True)
                self.tableView.playing_behavior(0)

            else:
                self.current_playing_list = item.text()


                self.reset_list_widget_color()
                item.setForeground(QtGui.QBrush(QtGui.QColor(40, 40, 180)))
                self.my_song_player.stop()
                self.label_song_text_setter(self.songs_category.tracks()[0][0],
                                            self.songs_category.tracks()[0][1])
                self.playing_song_data = [self.songs_category.tracks()[0][0],
                                          self.songs_category.tracks()[0][1], 0]
                "Setting current playing list because when select list I change this values"
                self.current_playing_tracks_list = self.songs_category.tracks().copy()
                self.current_p_tracks_list_url = self.songs_category.url().copy()
                self.PlayPauseButton.setChecked(True)
                self.tableView.playing_behavior(0)

                "streaming data are downloaded"
                if self._stream_mode:
                    self.download_streaming_songs(self.songs_category.url()[0:5])
                    time.sleep(5)
                self.my_song_player.set_list(self.songs_category.filenames(), self.current_playing_list)
                self.play_track()


    def play_list(self):
        # todo:wrong logic, should take into account which list

        sender_object = self.sender().objectName()
        self.my_song_player.stop()
        self.pushButtonPlaylist.setText('Pause')

        item, self.songtracks = self.select_list()
        self.current_playing_list = item.text()

            
        self.reset_list_widget_color()
        item.setForeground(QtGui.QBrush(QtGui.QColor(40, 40, 180)))
        self.label_song_text_setter(self.songs_category.tracks()[0][0],
                                    self.songs_category.tracks()[0][1])
        self.playing_song_data = [self.songs_category.tracks()[0][0],
                                  self.songs_category.tracks()[0][1], 0]
        self.PlayPauseButton.setChecked(True)

        if self._stream_mode:
            if not os.path.isfile(self.songs_category.filenames()[0]):
                self.download_streaming_songs(self.songs_category.url()[0:5])
                time.sleep(5)

        self.my_song_player.set_list(self.songs_category.filenames(), self.current_playing_list)
        self.play_track()

        self.current_playing_tracks_list = self.songs_category.tracks().copy()
        self.current_p_tracks_list_url = self.songs_category.url().copy()

    def double_click_table(self, index):
        row = index.row()
        #        self.tableView.rowAt()
        if self.category == 'Cartella':
            self.current_playing_list = 'Local'
            self.filenames = self.filenames_local.copy()
            pass
        else:

            self.label_song_text_setter(self.songs_category.tracks()[row][1],
                                        self.songs_category.tracks()[row][0])

            self.playing_song_data = [self.songs_category.tracks()[row][0],
                                      self.songs_category.tracks()[row][1], row]

            self.filenames = self.songs_category.filenames()

            self.current_playing_list = self.item.text()
            self.reset_list_widget_color()
            self.item.setForeground(QtGui.QBrush(QtGui.QColor(40, 60, 200)))
            self.current_playing_tracks_list = self.songs_category.tracks().copy()
            self.current_p_tracks_list_url = self.songs_category.url().copy()

        self.tableView.playing_behavior(row)
        self.PlayPauseButton.setChecked(True)
        self.pushButtonPlaylist.setText('Pause')
        "test streaming mode"
        if self._stream_mode:
            if not os.path.isfile(self.songs_category.filenames()[row]):
                self.download_streaming_songs([self.songs_category.url()[row]])
                time.sleep(6)

        self.my_song_player.play_this_item(row, self.filenames, self.current_playing_list)



    # self.playsong(self.playlist[row], self.folder_song[row])

    def download_streaming_songs(self, url_cache_list, url_category='', shuffle_mode=False, folder=''):
        "I plan to precharge 5 songs"
        if shuffle_mode:
            print('get next song in list')
        if url_category:
            "here I could do a pre-charging"
            pass

        const.args = rs.get_arguments()
        "To speed up download I do not require metadata or conversion "
        const.args.output_ext = ".m4a"
        if folder:
            pass
        else:
            const.args.folder = os.getcwd() + '/cache/'

        for url_song in url_cache_list:
            rs.streamData.put(['track', url_song])


    def downloader_stream(self):
        data = True
        while data:
            category, url = rs.streamData.get()
            rs.assign_parser_url(category, url)
            "Starting the main according url parsing"
            spt_dl_in.main_func_caller()
            "Resetting the parser because it is unique"
            rs.reset_parser_url()

    def reset_list_widget_color(self):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        pass

    def label_song_text_setter(self, songname='', artist=''):
        self.song_name_label.setText(songname)
        self.song_artist_label.setText(artist)


    # ---------------------------------------------------------------------------------
    def play_track(self):
        if self.my_song_player.is_playing():
            self.my_song_player.pause_track()
            # self.PlayPauseButton.setStyleSheet('image: url(:/mytunefy/resources/icons/play_grey.png);')
        else:
            self.my_song_player.play_track()
            # self.PlayPauseButton.setStyleSheet('image: url(:/mytunefy/resources/icons/pause-butt.png)')

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

    def get_list_in_db(self, db_name):
        res = player_get_all_user_data(db_name)
        if res:
            try:
                self.playlist, self.album, self.artist, \
                plname, alname, arname = parsing_user_db_data(res)

                plname, self.playlist = [list(x) for x in zip(*sorted(zip(plname,
                                         self.playlist), key=operator.itemgetter(0)))]

                alname, self.album = [list(x) for x in zip(*sorted(zip(alname,
                                                                           self.album), key=operator.itemgetter(0)))]

                arname, self.artist = [list(x) for x in zip(*sorted(zip(arname,
                                                                        self.artist), key=operator.itemgetter(0)))]
            except Exception as e:
                print('Error when getting values from db, as:', e)
                return [None, None, None]
        else:
            return [None, None, None]

        return [plname, alname, arname]

    def combo_box_handler(self):
        self.listWidget.clear()
        self.category = self.comboBoxCategory.currentText()
        if self.category == 'Cartella':
            self.local_tracks, self.filenames_local = self.get_local_songs()
            self.tableView.set_new_model(self.frame_songs, self.local_tracks, self.header)
        elif self.category == 'Brani':
            pass
        else:
            self.fill_list_view(self.category, self.category_list)



    def fill_list_view(self, category, category_list):
        # Todo: aggiungere selezione da cartella locale
        item = self.dictListView[category]
        self.listWidget.addItems(category_list[item])

    def get_songs(self, option, category, category_list, dbname='song_db'):
        """Option indicate a single category, if not all song will be returned
            song structure:
            artist, song_name, album, folder

        """
        # Todo: add functionality
        fullDictSongs = {
            0 : self.playlist,
            1 : self.album,
            2 : self.artist ,
            "Brani": 3,
            "Cartella": 4
        }

        if category == 'Cartella':
            raw_songs = self.get_local_songs()
        elif category == 'Brani':
            raw_songs = get_songs_from_db(id, category)
            pass
        else:
            "if id is for brani, nothing happens"
            index_cat = category_list[self.dictListView[category]]
            index_in_list = index_cat.index(option)

            index_list = fullDictSongs[self.dictListView[category]][index_in_list][0]
            raw_songs = get_songs_from_db(index_list, category, dbname)
            tracks = []
            id_data = [self._id_artist_list, self._id_album_list, self._artists_name_list, self._album_name_list]

            self.songs_category = SongData(raw_songs, category_list, self.artist, self.album)
            data_list_id = self.songs_category.run_parser(id_data, dbname)

            self._id_artist_list, self._id_album_list, self._artists_name_list, self._album_name_list = data_list_id
            #if category == 'Playlist':
            self.songs_category.sort_data()

            return self.songs_category.tracks()

    def set_local_folder(self, folder=''):
        if folder:
            self.music_folder = folder
        else:
            self.music_folder = internals.get_music_dir()

    def get_local_songs(self):
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
                    labels = rs.parsing_song(item)
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


    def volume_hanler(self):
        value = self.verticalSlider.value()
        self.my_song_player.set_volume(value)

    def cleanExit(self):
        # Todo: I have a warning/error for mmdevice when closing the program.
        print('Use this function for saving data and cleaning')
        self.my_song_player.stop()
        # vlc.libvlc_media_player_stop(self.my_song_player._mediaplayer.get_media_player())
        # vlc.libvlc_release(self.my_song_player.instance)
        # vlc.AudioFlushCb()
        # vlc.AudioCleanupCb()
        # vlc.libvlc_vlm_del_media(self.my_song_player.instance, self.my_song_player._media)

        # vlc.libvlc_wait(self.my_song_player.instance)



    def reset_combobox_downloader(self):
        if os.path.isfile('db_data/song_db'):
            self.category = self.comboBoxCategory.currentText()
            self.category_list = self.get_list_in_db(db_name='song_db')
            if self.category != 'Cartella':
                self.fill_list_view(self.category, self.category_list)


    def down_main_window(self):
        #todo: check if this window works when db is not created
        if self._stream_mode:
            ListStream = MainStream(self.main_window_player)
            ListStream.stream_window.show()
        else:
            guiDown = MainWin()
            guiDown.mainwindow.show()



    def stream_mode_button(self):
        #Todo: check thread logic, start and join...
        if self._stream_mode:
            self._stream_mode = False
            #self.pushButtonDownloader.setEnabled(True)
            self.reset_combobox_downloader()
            self.pushButtonDownloader.setText("Download")

        else:
            #self.pushButtonDownloader.setEnabled(False)
            self.pushButtonDownloader.setText("Aggiungi Playlist")
            self._stream_mode = True
            self.StreamModeButton.isChecked()
            self.stream_db = None

            self._artists_name_list.clear()
            self._artists_name_list.clear()
            self._id_album_list.clear()
            self._id_artist_list.clear()
            self.listWidget.clear()

            if os.path.isfile('db_data/song_stream_db'):
                self.category = self.comboBoxCategory.currentText()
                self.category_list = self.get_list_in_db(db_name='song_stream_db')
        #        self.comboBoxCategory.setCurrentIndex(0)
        #         if self.category != 'Cartella':
        #             self.fill_list_view(self.category, self.category_list)
