import string
from _hashlib import pbkdf2_hmac
from binascii import hexlify
from queue import Queue
import datetime
from os import listdir, getcwd
from random import choice

from logzero import logger as log
import platform
import pprint
from spotdl import const
import logging
import sys
from spotdl import internals

_LOG_LEVELS_STR = ["INFO", "WARNING", "ERROR", "DEBUG"]
songPusher = Queue()
MY_WORKING_DIR = None

myEndtime = datetime.datetime(2020, 7, 20, 0, 0).timestamp()


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

def song_id_creator(variable):
    """This function create the hash-like mac to check with db and for song id purpose"""
    variable_b = bytes(variable, 'utf8')
    dk = pbkdf2_hmac('sha256', variable_b, b'salt', 100000)
    key_bin = hexlify(dk)

    return key_bin

def parser_db(res):
    pass
# def return_directory():
#     global MY_WORKING_DIR
#
#     return MY_WORKING_DIR





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