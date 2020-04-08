import const
import downloader
import spotify_tools
import re
import internals
import youtube_tools
import logzero
import sys
import platform
import pprint
import logzero
from logzero import logger as log
import threading


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



def main():
    # Todo try new implementation
    internals.filter_path(const.args.folder)
    youtube_tools.set_api_key()
    logzero.setup_default_logger(formatter=const._formatter, level=const.args.log_level)

    try:
        operation, text_file = match_args()
        #mythread = threading.Thread(target=list_downloader, args=(operation, text_file))

        if operation is not 'list':
            #mythread.start()
            list_downloader(operation, text_file)
        # else:
        #     list_downloader(operation, text_file)

    # I don't need this type of exception, I'll remove another time
    except Exception as e:
        print(e)
        operation = False
        log.exception(e)
        sys.exit(3)
