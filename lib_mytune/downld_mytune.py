from spotdl import const, convert
import pafy

class mySimpleYoutubeDownloader:
    """ This class is an add-on to download from youtube.
        There are other library/project that do this, in the future
        this class could be """

    def __init__(self, url):
        self._myvid = pafy.new(url)
        self._video_format = 'm4a'
        self._audio_format = 'mp3'
        self._audio = False

    def is_video(self, quality='any'):
        if quality != 'any':
            self._video_format = quality
        down_item = self._myvid.getbest(preftype=quality)
        return down_item

    def is_audio(self, quality='any'):
        self._audio = True
        if quality != 'any':
            self._audio_format = quality
        down_item = self._myvid.getbestaudio(preftype=quality)
        return down_item

    def download(self, folder):
        if self._audio:
            down_item = self.is_audio()
            filename = down_item.download(folder)
            input_song = self.title() + ".webm"
            output_song = self.title() + ".mp3"
            convert.song(input_song,
                          output_song,
                          folder,
                          avconv=const.args.avconv,
                          trim_silence=const.args.trim_silence,
                          delete_original=not const.args.no_remove_original, )

        else:
            down_item = self.is_video()
            filename = down_item.download(folder)

    def title(self):
        return self._myvid.title

    def other_data(self):
        pass

