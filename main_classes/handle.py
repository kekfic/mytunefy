from spotdl_mod import downloader
from spotdl import const, spotify_tools, internals, youtube_tools
import re
import sys
import platform
import pprint
import logzero
from logzero import logger as log
from slugify import slugify
import logging
from spotdl import internals

_LOG_LEVELS_STR = ["INFO", "WARNING", "ERROR", "DEBUG"]

# Todo ---> changed overwrite default to skip
default_conf = {
    "spotify-downloader": {
        "no-remove-original": False,
        "manual": False,
        "no-metadata": False,
        "no-fallback-metadata": False,
        "avconv": False,
        "folder": internals.get_music_dir(),
        "overwrite": "skip",
        "input-ext": ".m4a",
        "output-ext": ".mp3",
        "write-to": None,
        "trim-silence": False,
        "download-only-metadata": False,
        "dry-run": False,
        "music-videos-only": False,
        "no-spaces": False,
        "file-format": "{artist} - {track_name}",
        "search-format": "{artist} - {track_name} lyrics",
        "youtube-api-key": None,
        "skip": None,
        "write-successful": None,
        "log-level": "INFO",
        "spotify_client_id": "4fe3fecfe5334023a1472516cc99d805",
        "spotify_client_secret": "0f02b7c483c04257984695007a4a8d5c",
    }
}


def log_leveller(log_level_str):
    loggin_levels = [logging.INFO, logging.WARNING, logging.ERROR, logging.DEBUG]
    log_level_str_index = _LOG_LEVELS_STR.index(log_level_str)
    loggin_level = loggin_levels[log_level_str_index]
    return loggin_level


def get_arguments(raw_args=None, to_group=True, to_merge=True):
    # help = 'Load tracks from playlist URL into {}'.format()
    parser = type("", (), {})()
    parser.youtube_api_key = None
    parser.log_level = "INFO"
    parser.song = ''
    parser.list = ''
    parser.playlist = ''
    parser.album = ''
    parser.artist = ''
    parser.all_albums = ''
    parser.username = ''
    parser.no_metadata = False
    parser.manual = False
    parser.input_ext = ".m4a"
    parser.output_ext = ".mp3"
    parser.overwrite = "skip"
    parser.skip = None
    parser.no_fallback_metadata = False
    parser.write_successful = None
    parser.write_to = None
    parser.write_m3u = False
    parser.search_format = "{artist} - {track_name} lyrics"
    parser.no_spaces = False
    parser.file_format = '{artist} - {track_name}'
    parser.download_only_metadata = False
    parser.trim_silence = False
    parser.dry_run = False
    parser.music_videos_only = False
    parser.avconv = False
    parser.no_remove_original = False

    parser.spotify_client_id = "4fe3fecfe5334023a1472516cc99d805"
    parser.spotify_client_secret = "0f02b7c483c04257984695007a4a8d5c"

    return parser


def debug_sys_info():
    log.debug("Python version: {}".format(sys.version))
    log.debug("Platform: {}".format(platform.platform()))
    log.debug(pprint.pformat(const.args.__dict__))


def match_args():
    # Todo major changing here, I shall probably change everything,
    # I add operation variable, for now it is a patch
    operation = ''
    text_file = ''
    if const.args.song:
        for track in const.args.song:
            track_dl = downloader.Downloader(raw_song=track)
            track_dl.download_single()
            # when only one track is downloaded, there is no need for listing
        operation = 'list'
    elif const.args.playlist:
        tracks, text_file = spotify_tools.write_playlist(
            playlist_url=const.args.playlist, text_file=const.args.write_to
        )
        operation = 'playlist'
    elif const.args.album:
        tracks, text_file = spotify_tools.write_album(
            album_url=const.args.album, text_file=const.args.write_to
        )
        operation = 'album'
    elif const.args.all_albums:
        text_file = spotify_tools.write_all_albums_from_artist(
            artist_url=const.args.all_albums, text_file=const.args.write_to
        )
        operation = 'all_album'
    elif const.args.username:
        links_playlist, text_file = spotify_tools.write_user_playlist(
            username=const.args.username, text_file=const.args.write_to
        )
        operation = 'username'

    return operation, text_file


def list_downloader(operation, text_file):
    if operation is not 'list':
        if const.args.write_m3u:
            youtube_tools.generate_m3u(
                track_file=const.args.list
            )
        else:
            # list_name = str(self.category_list) + '.txt'
            list_dl = downloader.ListDownloader(
                tracks_file=text_file,
                skip_file=const.args.skip,
                write_successful_file=const.args.write_successful,
            )
            list_dl.download_list()

            operation = 'list'


def url_parser(url):
    category_list = ''
    substring = 'https://open.spotify.com/'
    if substring in url:
        try:
            junk, data = re.split(r'.com/', url)
            category_list, junk = re.split(r'/', data)
        except ValueError as e:
            print("Url Parser Error: {}".format(e))
        except Exception as e:
            print("General error in url splitting:", e)
    else:
        category_list = False

    return category_list


def get_song_data(url):
    song_name = ''
    artist_name = ''
    album_name = ''

    try:
        track = spotify_tools.generate_metadata(url)
        song_name = track['name']
        artist_name = track['album']['artists'][0]['name']
        album_name = track['album']['name']
    except Exception as e:
        print('Error as :', e)

    return [song_name, artist_name, album_name]


def get_name_for_list_widget(category_list, url):
    "This function get the album/song/playlist/artist name from url"
    try:
        if category_list == 'playlist':
            playlist = spotify_tools.fetch_playlist(url)
            name = u"{0}".format(slugify(playlist["name"], ok="-_()[]{}"))
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


def assign_parser_url(category_list, url):
    if category_list == 'playlist':
        const.args.playlist = url
    elif category_list == 'track':
        const.args.song = [url]
    elif category_list == 'album':
        const.args.album = url
    elif category_list == 'artist':
        const.args.all_albums = url


def reset_parser_url():
    const.args.playlist = ''
    const.args.song = ''
    const.args.album = ''
    const.args.artist = ''


def main_func_caller():
    # Todo try new implementation
    internals.filter_path(const.args.folder)
    youtube_tools.set_api_key()
    logzero.setup_default_logger(formatter=const._formatter, level=const.args.log_level)

    try:
        operation, text_file = match_args()
        if operation is not 'list':
            list_downloader(operation, text_file)

    # I don't need this type of exception, I'll remove another time
    except Exception as e:
        print(e)
        operation = False
        log.exception(e)
        sys.exit(3)


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
            song_download(input_song,
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

