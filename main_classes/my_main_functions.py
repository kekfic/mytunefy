from spotdl_mod import const, youtube_tools, downloader, spotify_tools, internals
import re
import sys
import platform
import pprint
import logzero
from logzero import logger as log
from slugify import slugify


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
            # with open('txt/'+'SS_'+text_file, 'w') as testfile:
            #     for item in list_dl.mysonglist:
            #         testfile.write(item+'\n')

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



def get_name_for_list_widget(category_list, url ):
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


def main():
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
