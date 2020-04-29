import platform
import os
import sys
from random import random

import vlc
from PySide2 import QtCore


class SongPlayer:

    def __init__(self, slider, audio_slider):
        # Create a basic vlc instance

        self.instance = vlc.Instance('--novideo')
        self._slider = slider
        self._audio_slider = audio_slider

        self._media = None

        # Create an empty vlc media player
        self._mediaplayer = self.instance.media_list_player_new()
        self._mediaplayer.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, self._song_finished)
        self.is_paused = False
        self.timer = QtCore.QTimer()


    def set_list(self, filenames, shuffle=False, repeat=False):
        self.duration = None
        self._song_number = len(filenames)
        self._shuffle= shuffle
        self._repeat = repeat

        self.filenames = filenames
        current_filenames = filenames.copy()

        if self._shuffle:
            random.shuffle(current_filenames)
        self._open_file(current_filenames)

    def _plays_song(self, current_filenames):

        self.open_file(current_filenames)
        self._mediaplayer.play()
        self.is_paused = False

    def pause_track(self):
        self._mediaplayer.pause()
        self.timer.stop()

    def play_track(self):
        self._mediaplayer.play()
        self.timer.start()

    def next_track(self):
        if self._mediaplayer.is_playing():
            self._mediaplayer.next()

    def back_track(self):
        if self._mediaplayer.is_playing():
            self._mediaplayer.back()

    def set_track(self, index):
        self._mediaplayer.play_item_at_index(index)

    def play_pause(self):
        """Toggle play/pause status
        """
        if self._mediaplayer.is_playing():
            self._mediaplayer.pause()

            self.is_paused = True
            self.timer.stop()
        else:
            if self._mediaplayer.play() == -1:
                #todo:----
                print('the player is closed')
                pass

                return

            self._mediaplayer.play()
            self.is_paused = False

    def stop(self):
        """Stop player
        """
        self._mediaplayer.stop()

    def _song_finished(self):
        pass

    def is_playing(self):
        return self._mediaplayer.is_playing()

    def shuffle_mode(self):
        if self._shuffle_is_active == True:
            self._shuffle_is_active = False
        else:
            self._shuffle_is_active = True


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

        # Set the media position to where the slider was dragged
        self.timer.stop()
        pos = self._slider.value()
        self.mediaplayer.set_position(pos / 1000.0)
        self.timer.start()

    def time_change(self, time):
        if not self._slider.isSliderDown():
            self._slider.setValue(time)

    def total_time_change(self, time):
        self._slider.setRange(0, time)



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
