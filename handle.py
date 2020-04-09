from logzero import logger as log
import logging
import yaml
import os
import internals

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


def merge(default, config):
    """ Override default dict with config dict. """
    merged = default.copy()
    merged.update(config)
    return merged


def get_config(config_file):
    try:
        with open(config_file, "r") as ymlfile:
            cfg = yaml.safe_load(ymlfile)
    except FileNotFoundError:
        log.info("Writing default configuration to {0}:".format(config_file))
        with open(config_file, "w") as ymlfile:
            yaml.dump(default_conf, ymlfile, default_flow_style=False)
            cfg = default_conf

        for line in yaml.dump(
                default_conf["spotify-downloader"], default_flow_style=False
        ).split("\n"):
            if line.strip():
                log.info(line.strip())
        log.info(
            "Please note that command line arguments have higher priority "
            "than their equivalents in the configuration file"
        )

    return cfg["spotify-downloader"]


def override_config(config_file, parser, raw_args=None):
    """ Override default dict with config dict passed as comamnd line argument. """
    config_file = os.path.realpath(config_file)
    config = merge(default_conf["spotify-downloader"], get_config(config_file))
    parser.set_defaults(**config)
    return parser.parse_args(raw_args)

def override_arg(raw_args):
    print('overriding')

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
    parser.no_spaces =  False
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
