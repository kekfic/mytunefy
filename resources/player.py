

import platform
import os
import sys
import vlc


class SongPlayer:

    def __init__(self):
        # Create a basic vlc instance
        self.instance = vlc.Instance()
        self.media = None
        # Create an empty vlc media player
        self.mediaplayer = self.instance.media_player_new()
        self.is_paused = False
      #  self.timer = QtCore.QTimer(self)
        #self.timer.setInterval(100)
       # self.timer.timeout.connect(self.update_ui)

    def play_pause(self):
        """Toggle play/pause status
        """
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            #self.playbutton.setText("Play")
            self.is_paused = True
            #self.timer.stop()
        else:
            if self.mediaplayer.play() == -1:
             #   self.open_file()
                return

            self.mediaplayer.play()
            #self.playbutton.setText("Pause")
            #self.timer.start()
            self.is_paused = False

    def stop(self):
        """Stop player
        """
        self.mediaplayer.stop()
       # self.playbutton.setText("Play")

    def set_volume(self, volume):
        """Set the volume
        """
        self.mediaplayer.audio_set_volume(volume)

    def set_position(self):
        """Set the movie position according to the position slider.
        """

        # The vlc MediaPlayer needs a float value between 0 and 1, Qt uses
        # integer variables, so you need a factor; the higher the factor, the
        # more precise are the results (1000 should suffice).

        # Set the media position to where the slider was dragged
        self.timer.stop()
        pos = self.positionslider.value()
        self.mediaplayer.set_position(pos / 1000.0)
        self.timer.start()

    def time_change(self, time):
        if not self.horizontalSlider.isSliderDown():
            self.horizontalSlider.setValue(time)

    def total_time_change(self, time):
        self.horizontalSlider.setRange(0, time)

    def slider_value_change(self):
        value = self.horizontalSlider.value()
        print
        value
        self.media_obj.seek(value)

    def update_ui(self):
        """Updates the user interface"""

        # Set the slider's position to its corresponding media position
        # Note that the setValue function only takes values of type int,
        # so we must first convert the corresponding media position.
        media_pos = int(self.mediaplayer.get_position() * 1000)
        self.positionslider.setValue(media_pos)

        # No need to call this function if nothing is played
        if not self.mediaplayer.is_playing():
            self.timer.stop()

            # After the video finished, the play button stills shows "Pause",
            # which is not the desired behavior of a media player.
            # This fixes that "bug".
            if not self.is_paused:
                self.stop()
