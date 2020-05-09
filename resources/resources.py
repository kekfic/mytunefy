import operator
import string
from _hashlib import pbkdf2_hmac
from binascii import hexlify
from queue import Queue
import datetime
from os import listdir, getcwd
from random import choice
import re
from logzero import logger as log
import platform
import pprint
from spotdl import const
import logging
import sys
from spotdl import internals


_LOG_LEVELS_STR = ["INFO", "WARNING", "ERROR", "DEBUG"]
#Global queue
songPusher = Queue()
streamData = Queue()
#working_dir
MY_WORKING_DIR = None

myEndtime = datetime.datetime(2020, 12, 31, 0, 0).timestamp()


# Todo: this was from the spotfl handle, I could implement in a different way
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
        "spotify_client_id": " ",
        "spotify_client_secret": " ",
    }
}

def debug_sys_info():
    log.debug("Python version: {}".format(sys.version))
    log.debug("Platform: {}".format(platform.platform()))
    log.debug(pprint.pformat(const.args.__dict__))


def log_leveller(log_level_str):
    loggin_levels = [logging.INFO, logging.WARNING, logging.ERROR, logging.DEBUG]
    log_level_str_index = _LOG_LEVELS_STR.index(log_level_str)
    loggin_level = loggin_levels[log_level_str_index]
    return loggin_level

def refine_string(string_to_refine):
    #todo don't know if it is useful, there should be some library
    mystring = string_to_refine.lower()
    mystring = mystring.replace('-', ' ')
    mystring = mystring.replace('_', ' ')
    mystring = mystring.replace(':', ' ')
    mystring = mystring.replace('  ', ' ')
    mystring = mystring.replace('.', ' ')
    mystring = mystring.replace('á', 'a')
    mystring = mystring.replace('à', 'a')
    mystring = mystring.replace('í', 'i')
    mystring = mystring.replace('ó', 'o')
    # mystring = mystring.replace('ñ', 'n')
    mystring = mystring.replace('ú', 'u')
    mystring = mystring.replace('é', 'e')
    mystring = mystring.replace('è', 'e')

    return mystring

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(length))

def check_my_dir(dir):
    if dir in listdir():
        pass
    else:
        return None

def set_current_directory():
    global MY_WORKING_DIR

    MY_WORKING_DIR = getcwd()

    return MY_WORKING_DIR

def key_id_creator(variable):
    """This function create the hash-like mac to check with db and for song id purpose"""
    variable_b = bytes(variable, 'utf8')
    dk = pbkdf2_hmac('sha256', variable_b, b'salt', 100000)
    key_bin = hexlify(dk)

    return key_bin


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



def get_arguments(raw_args=None, to_group=True, to_merge=True):
    #todo: define a better way to set this configuration
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
    parser.spotify_client_id = "45642ced0f5a4bedaec1f86b4ed7f89e"
    parser.spotify_client_secret = "6532f359d2f14d9e9d24fd4b3d269dba"

    return parser

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

def parsing_song(song):
    # todo call with another name and move from here
    # poping format
    listsplit = re.split(r'[-.]', song)
    listsong = [x.strip() for x in listsplit]
    art = listsong[1].split('(')[0]
    artist = art.strip()

    return [listsong[0], artist, 'Album', 'Current Folder']

def characters_converter(fileplayer):
    #todo check if there is some library
    # or directly with some vlx configuration
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
    fileplayer = fileplayer.replace('%c3%b1', 'ñ')
    fileplayer = fileplayer.replace('%5b', '[')
    fileplayer = fileplayer.replace('%5d', ']')
    fileplayer = fileplayer.replace('%c3%ac', 'ì')
    fileplayer = fileplayer.replace('%c3%b2', 'ò')

    return fileplayer


def get_data_from_mrl(fileplayer, filenames):
    #todo: check if splitter '.m' works for every songs
    # ideally a would have two possible formats mp3 and m4a
    # even if flac format is possible

    artist_raw = ''
    raw_name = ''
    artist = ''
    song_name = ''
    index = None
    try:
        fileplayer = characters_converter(fileplayer)
        print("Filename trying to play ------>", fileplayer)
        songs_in_path = []
        for song in filenames:
            text_s = song.split('/')[-1].lower()
            songs_in_path.append(text_s)
        if fileplayer in songs_in_path:
            index = songs_in_path.index(fileplayer)

            if fileplayer.count(' - ') > 1:
                print('NOTE: Song name or artist name could be wrong.')
                artist_raw, raw_name, junk = fileplayer.split(' - ')
            else:
                artist_raw, raw_name = fileplayer.split(' - ')

            artist = artist_raw.strip()
            song_name = raw_name.split('.m')[0].strip()
            #song_name = song_name.split('.m4a')[0].strip()
        else:
            print('Song Not Found!!')

    except Exception as e:
        print('Player error as: -----> ', e)

    return [artist, song_name, index]



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
