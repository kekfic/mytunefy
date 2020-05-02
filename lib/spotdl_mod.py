import time
import urllib
import os
from spotdl import downloader, spotify_tools, const, convert, metadata, internals
from logzero import logger as log
import youtube_dl
import pafy
from resources import resources as rs


class EnhancedDownloader(downloader.Downloader):
    def __init__(self, raw_song, number=None ):
        super().__init__(raw_song, number=None)

    def _download_single(self, songname):
        # deal with file formats containing slashes to non-existent directories
        songpath = os.path.join(const.args.folder, os.path.dirname(songname))
        os.makedirs(songpath, exist_ok=True)
        input_song = songname + const.args.input_ext
        output_song = songname + const.args.output_ext
        if download_song(input_song, self.content):
            print("")
            try:
                convert.song(
                    input_song,
                    output_song,
                    const.args.folder,
                    avconv=const.args.avconv,
                    trim_silence=const.args.trim_silence,
                    delete_original=not const.args.no_remove_original,
                )
            except FileNotFoundError:
                encoder = "avconv" if const.args.avconv else "ffmpeg"
                log.warning("Could not find {0}, skip encoding".format(encoder))
                output_song = self.unconverted_filename(songname)

            if not const.args.no_metadata and self.meta_tags is not None:
                metadata.embed(
                    os.path.join(const.args.folder, output_song), self.meta_tags
                )
            " Push to thread db handler, type, filename, url, metadata, glob variable"
            rs.songPusher.put(['song', songname, self.raw_song, self.meta_tags, const.args])
            return True


class ListDownloaderInherited(downloader.ListDownloader):
    def __init__(self, tracks_file, skip_file, write_successful_file):
        super(ListDownloaderInherited, self).__init__(tracks_file, skip_file=None,write_successful_file=None)


    def _download_list(self):
        downloaded_songs = []

        for number, raw_song in enumerate(self.tracks, 1):
            print("")
            try:
                track_dl = EnhancedDownloader(raw_song, number=number)
                track_dl.download_single()
            except (urllib.request.URLError, TypeError, IOError) as e:
                # detect network problems
                self._cleanup(raw_song, e)
                # TODO: remove this sleep once #397 is fixed
                # wait 0.5 sec to avoid infinite looping
                time.sleep(0.5)
                continue

            downloaded_songs.append(raw_song)
            # Add track to file of successful downloads
            if self.write_successful_file is not None:
                self._write_successful(raw_song)

            log.debug("Removing downloaded song from tracks file")
            internals.trim_song(self.tracks_file)

        return downloaded_songs


#spotify_tools.write_all_albums_from_artist()

def download_song(file_name, content):
    """ Download the audio file from YouTube. """
    _, extension = os.path.splitext(file_name)
    if extension in (".webm", ".m4a"):
        link = content.getbestaudio(preftype=extension[1:])
    else:
        log.debug("No audio streams available for {} type".format(extension))
        return False

    if link:
        try:
            log.debug("Downloading from URL: " + link.url)
            filepath = os.path.join(const.args.folder, file_name)
            log.debug("Saving to: " + filepath)
            link.download(filepath=filepath)
        except Exception as e:
            log.debug("Youtube cache error")
            with youtube_dl.YoutubeDL(pafy.g.def_ydl_opts) as ydl:
                ydl.cache.remove()

            log.debug("Downloading from URL: " + link.url)
            filepath = os.path.join(const.args.folder, file_name)
            log.debug("Saving to: " + filepath)
            link.download(filepath=filepath)

        return True
    else:
        log.debug("No audio streams available")
        return False