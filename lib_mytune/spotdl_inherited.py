import time
import urllib
import os
import sys
import logzero
from spotdl import downloader, spotify_tools, const, convert, metadata, internals, youtube_tools
from logzero import logger as log
import youtube_dl
import pafy
from resources import resources as rs
from slugify import slugify


class EnhancedDownloader(downloader.Downloader):
    """Inherited class"""
    def __init__(self, raw_song, number=None):
        super().__init__(raw_song, number=None)

    def download_single(self):
        """ Logic behind downloading a song. """

        if self._to_skip():
            return

        # "[number]. [artist] - [song]" if downloading from list
        # otherwise "[artist] - [song]"
        youtube_title = youtube_tools.get_youtube_title(self.content, self.number)
        log.info("{} ({})".format(youtube_title, self.content.watchv_url))

        # generate file name of the song to download
        songname = self.refine_songname(self.content.title)

        if const.args.dry_run:
            return

        song_existence = downloader.CheckExists(songname, self.meta_tags)
        if not song_existence.already_exists(self.raw_song):
            down_song = self._download_single(songname)
            if down_song:
                rs.songPusher.put(['track', songname+const.args.output_ext,
                                   self.raw_song, self.meta_tags, const.args])
            return down_song
        else:
            rs.songPusher.put(['track', songname + const.args.output_ext,
                               self.raw_song, self.meta_tags, const.args])


class ListDownloaderInherited(downloader.ListDownloader):
    """Inherited class"""
    def __init__(self, tracks_file, skip_file, write_successful_file):
        super().__init__(tracks_file, skip_file=None, write_successful_file=None)


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


# spotify_tools.write_all_albums_from_artist()

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


def match_args():
    # Todo major changing here, I shall probably change everything,
    # I add operation variable, for now it is a patch
    operation = ''
    text_file = ''
    tracks_url = []

    if const.args.song:
        for track in const.args.song:
            track_dl = EnhancedDownloader(raw_song=track)
            track_dl.download_single()
        operation = 'list'

    elif const.args.playlist:
        tracks_url = spotify_tools.write_playlist(
            playlist_url=const.args.playlist, text_file=const.args.write_to
        )

        playlist = spotify_tools.fetch_playlist(const.args.playlist)
        text_file = u"{0}.txt".format(slugify(playlist["name"], ok="-_()[]{}"))
        operation = 'playlist'

    elif const.args.album:
        tracks_url = spotify_tools.write_album(
            album_url=const.args.album, text_file=const.args.write_to
        )
        album = spotify_tools.fetch_album(const.args.album)
        text_file = u"{0}.txt".format(slugify(album["name"], ok="-_()[]{}"))
        operation = 'album'

    elif const.args.all_albums:
        spotify_tools.write_all_albums_from_artist(
            artist_url=const.args.all_albums, text_file=const.args.write_to
        )
        albums = spotify_tools.fetch_albums_from_artist(const.args.all_albums, album_type=None)
        text_file = albums[0]["artists"][0]["name"] + ".txt"
        operation = 'all_album'

    # Todo: the user playlist require user input in cmd. I will exclude it for now.
    """     
    elif const.args.username:
        spotify_tools.write_user_playlist(
            username=const.args.username, text_file=const.args.write_to
        )
        playlist = fetch_playlist(const.args.playlist)
        text_file = u"{0}.txt".format(slugify(playlist["name"], ok="-_()[]{}"))
        operation = 'username'
    """

    return operation, text_file, tracks_url


def list_downloader(operation, text_file, tracks_url):
    if operation is not 'list':
        if const.args.write_m3u:
            youtube_tools.generate_m3u(
                track_file=text_file
            )
        else:
            # list_name = str(self.category_list) + '.txt'
            list_dl = ListDownloaderInherited(
                tracks_file=text_file,
                skip_file=const.args.skip,
                write_successful_file=const.args.write_successful,
            )
            downloaded = list_dl.download_list()

            try:
                os.remove(text_file)
            except Exception as e:
                print("Unable to remove txt file.")


def get_tracks_playlist(url):
    playlist = spotify_tools.fetch_playlist(url)
    tracks_very_raw = playlist["tracks"]
    songs_in_playlist = len(tracks_very_raw)
    i = 0
    track = []
    for item in tracks_very_raw['items']:
        data = item['track']
        song_name = data['name']
        artist_name = data['artists'][0]['name']
        album = data['album']['name']
        duration_ms = data['duration_ms']
        track.append([song_name, artist_name, album, duration_ms])
        i = i + 1

    return track, i


def get_tracks_album(url):
    album = spotify_tools.fetch_album(url)
    album_name = album['name']
    artist = album['artists'][0]['name']
    num_song = len(album['tracks']['items'])
    song_name = []
    duration = []
    for item in album['tracks']['items']:
        song_name.append(item['name'])
        duration.append(item['duration_ms'])

    return ([song_name, artist, album_name, duration], num_song)


def get_song_data(url):
    """Retrieve song, artist, album, playlist name from url"""

    song_name = ''
    album_name = ''
    album_url = ''
    artist_name = ''
    artist_url = ''
    duration = None

    try:
        track = spotify_tools.generate_metadata(url)
        song_name = track['name']
        artist_name = track['album']['artists'][0]['name']
        album_name = track['album']['name']
        album_url = track['album']['external_urls']['spotify']
        artist_url = track['album']['artists'][0]['external_urls']['spotify']
        duration = track['duration']

    except Exception as e:
        print('Error as :', e)

    return [song_name, album_name, artist_name, album_url, artist_url, duration]


def get_name_for_list_widget(category_list, url):
    "This function get the album/song/playlist/artist name from url"
    try:
        if category_list == 'playlist':
            playlist = spotify_tools.fetch_playlist(url)
            name = playlist['name']
            text_file = "Playlist:  " + name
        elif category_list == 'track':
            track = spotify_tools.generate_metadata(url)
            name = track['name']
            artist_name = track['album']['artists'][0]['name']
            text_file = 'Song:  ' + name + ' - ' + artist_name
        elif category_list == 'artist':
            artist = spotify_tools.fetch_albums_from_artist(url)
            name = artist[0]['artists'][0]['name']
            text_file = u"Complete albums of " + artist[0]['artists'][0]['name']
        elif category_list == 'album':
            album = spotify_tools.fetch_album(url)
            name = u"{0}".format(slugify(album["name"], ok="-_()[]{}"))
            text_file = 'Album:  ' + name + ' - ' + album['artists'][0]['name']
        else:
            text_file = 'Not Found name'
            name = ''
    except Exception as e:
        print("{} name not found! Setting standard name.".format(category_list))
        text_file = str(category_list) + url[31:-1]
        name = ' '

    return text_file, name


def main_func_caller():
    # Todo try new implementation
    internals.filter_path(const.args.folder)
    youtube_tools.set_api_key()
    logzero.setup_default_logger(formatter=const._formatter, level=const.args.log_level)

    try:
        operation, text_file, tracks_url = match_args()
        if operation is not 'list':
            list_downloader(operation, text_file, tracks_url)

    # I don't need this type of exception, I'll remove another time
    except Exception as e:
        print(e)
        operation = False
        log.exception(e)
        sys.exit(3)
