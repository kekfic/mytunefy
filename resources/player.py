import platform
import os
import sys
import random

import vlc
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal


class SongPlayer(QObject):
    songChanged = Signal(object)

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

        # Create an empty vlc media player
        self._mediaplayer = self.instance.media_list_player_new()
        self._mediaplayer.event_manager().event_attach(vlc.EventType.MediaListPlayerNextItemSet, self._song_finished)
        self._mediaplayer.event_manager().event_attach(vlc.EventType.MediaListEndReached, self._list_ended)
        self.is_paused = False
        self.timer = QtCore.QTimer()

    def set_list(self, filenames, current_playlist, shuffle=False):
        #Todo: shuffle strategy is wrong
        self.duration = None
        self._song_number = len(filenames)

        if self._current_playing == current_playlist:
            pass
        else:
            self.set_current_playlist(current_playlist)

        self.filenames = filenames
        current_filenames = filenames.copy()

        if self._shuffle:
            random.shuffle(current_filenames)
            print('shuffle')
        self._open_file(current_filenames)

    def _plays_song(self, current_filenames):

        self._mediaplayer.play()
        self.is_paused = False

    def pause_track(self):
        self._mediaplayer.pause()
        self.timer.stop()

    def play_track(self):
        self._mediaplayer.play_item_at_index(0)
        self._mediaplayer.play()
        self.timer.start()

    def next_track(self):
        if self._mediaplayer.is_playing():
            self._mediaplayer.next()

    def back_track(self):
        if self._mediaplayer.is_playing():
            self._mediaplayer.previous()

    def set_track(self, index):
        self._mediaplayer.play_item_at_index(index)

    def play_this_item(self, index, songlist, current_playlist):
        if self._current_playing == current_playlist:
            pass
        else:
            self.set_current_playlist(current_playlist)
        if self.filenames:
            if self.filenames == songlist:
                self._mediaplayer.play_item_at_index(index)
            else:
                self.set_list(songlist, current_playlist)
                self._mediaplayer.play()
                self._mediaplayer.play_item_at_index(index)
        else:
            self.set_list(songlist, current_playlist)
            self._mediaplayer.play()
            self._mediaplayer.play_item_at_index(index)

    def set_current_playlist(self, playlist):
        self._current_playlist = playlist
    def return_playlist_name(self):
        return self._current_playlist


    def stop(self):
        """Stop player
        """
        self._mediaplayer.stop()

    def _list_ended(self, event):
        pass

    def _song_finished(self, event):
        artist, song_name, index = self.current_playing()
        self.songChanged.emit([artist, song_name, index])


    def is_playing(self):
        return self._mediaplayer.is_playing()

    def shuffle_mode(self, mode=False):
        self._shuffle = mode

    def current_playing(self):
        filepath = self._mediaplayer.get_media_player().\
            get_media().get_mrl().title().replace('%20', ' ')

        artist, song_name, index = self.get_data_from_mrl\
                                        (filepath)

        return artist, song_name, index

    def get_data_from_mrl(self, fileplayer):
        #todo: no reference to class, move in another place
        artist_raw = ''
        raw_name = ''
        artist = ''
        song_name = ''
        index = None
        try:
            fileplayer = fileplayer.split('/')[-1].lower()
            fileplayer = fileplayer.replace('%c3%a9', 'é')
            fileplayer = fileplayer.replace('%c3%a8', 'è')
            fileplayer = fileplayer.replace('%c3%a0', 'à')
            fileplayer = fileplayer.replace('%c3%b9', 'ù')
            fileplayer = fileplayer.replace('%28', '(')
            fileplayer = fileplayer.replace('%29', ')')
            fileplayer = fileplayer.replace('%c3%ad', 'í')
            fileplayer = fileplayer.replace('%c3%a1', 'á')
            fileplayer = fileplayer.replace('%27', '\'')
            fileplayer = fileplayer.replace('%c3%ba', 'ú')
            fileplayer = fileplayer.replace('%c3%b3', 'ó')
            fileplayer = fileplayer.replace(' %c3%b1', 'ñ')

            print(fileplayer)
            songs_in_path = []
            for song in self.filenames:
                text_s=song.split('/')[-1].lower()
                songs_in_path.append(text_s)
            if fileplayer in songs_in_path:
                index = songs_in_path.index(fileplayer)
                if fileplayer.count(' - ') > 1:
                    fileplayer = fileplayer.replace(' - live', '')
                    fileplayer = fileplayer.replace(' - remastered', '')
                    fileplayer = fileplayer.replace(' - remix', '')
                    fileplayer = fileplayer.replace(' - spanish', '')
                    fileplayer = fileplayer.replace(' - 2001', '')
                    fileplayer = fileplayer.replace(' - 2012', '')

                    if fileplayer.count(' - ') > 1:
                        print('Unable to sanitaze song, song name could be wrong')
                        artist_raw, raw_name, junk = fileplayer.split(' - ')
                    else:
                        artist_raw, raw_name = fileplayer.split(' - ')

                artist = artist_raw.strip()
                song_name = raw_name.split('.mp')[0].strip()
                print('Song exist')
            else:
                print('song not found')

        except Exception as e:
            print('Player error as ', e)

        return [artist, song_name, index]

    def set_volume(self, volume):
        """Set the volume
        """
        self._mediaplayer.audio_set_volume(volume)

    def _open_file(self, filenames):

        self._media = self.instance.media_list_new(filenames)
        # Set the the file list
        self._mediaplayer.set_media_list(self._media)
        # Parse the metadata of the file
#        self._media.parse()


    def set_position(self):
        """Set the movie position according to the position slider.
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
        """Set the movie position according to the position slider.
        """

        # The vlc MediaPlayer needs a float value between 0 and 1, Qt uses
        # integer variables, so you need a factor; the higher the factor, the
        # more precise are the results (1000 should suffice).

        # todo: check positon of slider
        # Set the media position to where the slider was dragged
        self.timer.stop()
        #pos = self._slider.value()
        self._mediaplayer.get_media_player().set_position(value / 100.0)
        self.timer.start()


    def get_slider_position(self):
        pos = self._mediaplayer.get_media_player().get_position()
        return pos

    def update_ui(self):
        """Updates the user interface"""

        # Set the slider's position to its corresponding media position
        # Note that the setValue function only takes values of type int,
        # so we must first convert the corresponding media position.
        media_pos = int(self.mediaplayer.get_position() * 1000)
        self._slider.setValue(media_pos)

        # No need to call this function if nothing is played
        if not self.mediaplayer.is_playing():
            self.timer.stop()

            # After the video finished, the play button stills shows "Pause",
            # which is not the desired behavior of a media player.
            # This fixes that "bug".
            if not self.is_paused:
                self.stop()
