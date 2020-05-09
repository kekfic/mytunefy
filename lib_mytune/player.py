import platform
import os
import sys
import random
import time

from resources import resources as rs

import vlc
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal


class SongPlayer(QObject):
    songChanged = Signal(object)
    timerEnded = Signal()

    def __init__(self, slider, audio_slider):
        super().__init__()
        # Create a basic vlc instance

        self.instance = vlc.Instance('--novideo')
        self._slider = slider
        self._audio_slider = audio_slider
        self.filenames = []
        self._current_playing = ''
        self._media = None
        self._shuffle = False
        self._repeat = False
        self._current_playlist = ''
        # Create an empty vlc media player
        self._mediaplayer = self.instance.media_list_player_new()
        self._mediaplayer.event_manager().event_attach(vlc.EventType.MediaListPlayerNextItemSet, self._song_finished)
        self._mediaplayer.event_manager().event_attach(vlc.EventType.MediaListEndReached, self._list_ended)

        # self.horizontalSlider.sliderMoved.connect(self.h_slider_hanlder)
        self._slider.sliderPressed.connect(self.h_slider_hanlder)
        self._slider.sliderReleased.connect(self.h_slider_hanlder)

        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(1000)  # .5 seconds
        self.checkThreadTimer.start()

        self.checkThreadTimer.timeout.connect(self.slider_update)

       # self._mediaplayer.event_manager().event_attach(vlc.EventType.M, self._list_ended)
        self.is_paused = False
        self.timer = QtCore.QTimer()


    def set_list(self, filenames, current_playlist):

        #Todo: shuffle strategy is wrong
        self.duration = None
        self._song_number = len(filenames)
        self.set_current_playlist(current_playlist)
        self.filenames = filenames
        if self._shuffle:
            self.temp_playlist = self.filenames.copy()
            random.shuffle(self.temp_playlist)
            self._open_file(self.temp_playlist)
        else:
            self._open_file(self.filenames)

    def _open_file(self, filenames):
        self._media = self.instance.media_list_new(filenames)
        # Set the the file list
        self._mediaplayer.set_media_list(self._media)

    "Song command-------------------------"

    def play_track(self):
        self._mediaplayer.play()
        self.timer.start()

    def pause_track(self):
        self._mediaplayer.pause()
        self.timer.stop()

    def next_track(self):
        self._mediaplayer.next()

    def back_track(self):
     self._mediaplayer.previous()

    def set_track(self, index):
        self._mediaplayer.play_item_at_index(index)

    def stop(self):
        self._mediaplayer.stop()

    "--------------------------------------------------------------------"

    def play_this_item(self, index, songlist, current_playlist):

        if self._current_playlist != current_playlist:
            self.set_current_playlist(current_playlist)
            self.set_list(songlist, current_playlist)
        if self._shuffle:
            index_temp= self.temp_playlist.index(self.filenames[index])
            self.set_track(index_temp)
        else:
            self.set_track(index)

    def play_random(self):
        index = random.randint(0, self._song_number - 1)
        self.set_track(index)

    def set_current_playlist(self, playlist):
        self._current_playlist = playlist

    def return_playlist_name(self):
        return self._current_playlist

    def _list_ended(self, event):
        pass

    def _song_finished(self, event):
        artist, song_name, index = self.current_playing(self.filenames)
        self.songChanged.emit([artist, song_name, index])

    def is_playing(self):
        return self._mediaplayer.is_playing()

    def shuffle_mode(self, mode=False):
        #todo: not working
        self._shuffle = mode
        if mode:
            self.set_list(self.filenames, self._current_playlist)
            self.play_track()

    def current_playing(self, filenames):
        filepath = self._mediaplayer.get_media_player().\
            get_media().get_mrl().title().replace('%20', ' ')

        artist, song_name, index = rs.get_data_from_mrl\
                                        (filepath, filenames)

        return artist, song_name, index


    def set_volume(self, volume):
        """Set the volume
        """
        self._mediaplayer.get_media_player().audio_set_volume(volume)




    def set_position(self):
        """Set position according to the position slider.
        """

        # The vlc MediaPlayer needs a float value between 0 and 1, Qt uses
        # integer variables, so you need a factor; the higher the factor, the
        # more precise are the results (1000 should suffice).

        # todo: check positon of slider
        # Set the media position to where the slider was dragged
        self.timer.stop()
        pos = self._slider.value()
        self._mediaplayer.get_media_player().set_position(pos / 1000.0)
        self.timer.start()

    def time_change(self, time):
        if not self._slider.isSliderDown():
            self._slider.setValue(time)

    def total_time_change(self, time):
        self._slider.setRange(0, time)

    def set_song_position(self, value):
        """Set the position according to the position slider.
        """
        # todo: check positon of slider
        # Set the media position to where the slider was dragged
        self.timer.stop()
        #pos = self._slider.value()
        self._mediaplayer.get_media_player().set_position(value / 100.0)

        self.timer.start()


    def get_slider_position(self):
        pos = self._mediaplayer.get_media_player().get_position()
        return pos

    def h_slider_hanlder(self):
        sender_object = self.sender().objectName()
        self.checkThreadTimer.stop()
        value = self._slider.value()
        self.set_song_position(value)

        self.checkThreadTimer.start()

    def h_slider_value_changed(self):
        sender_object = self.sender().objectName()

    def slider_update(self):
        sender_object = self.sender().objectName()
        # if sender_object == 'horizontalSlider':
        #     value = self._slider.value()
        #     self.set_song_position(value)

        if self.is_playing():
            value = self.get_slider_position() * 100
            self._slider.setValue(value)


