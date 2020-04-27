from spotdl.spotify_tools import fetch_album, fetch_playlist, fetch_albums_from_artist
from spotdl import const, spotify_tools, internals, youtube_tools, downloader, convert,internals
# todo resolve the import
import re
import sys
import logzero
from slugify import slugify
import os
from resources import resources as rs
from logzero import logger as log
import pafy



def match_args():
    # Todo major changing here, I shall probably change everything,
    # I add operation variable, for now it is a patch
    operation = ''
    text_file = ''
    tracks_url = []

    if const.args.song:
        for track in const.args.song:
            track_dl = downloader.Downloader(raw_song=track)
            track_dl.download_single()
            # pushing the songame and path for streaming/downloadin/database
            rs.songPusher.put(['song', const.args.folder, track])
            # when only one track is downloaded, there is no need for listing
        operation = 'list'

    elif const.args.playlist:
        tracks_url = spotify_tools.write_playlist(
            playlist_url=const.args.playlist, text_file=const.args.write_to
        )

        playlist = fetch_playlist(const.args.playlist)
        text_file = u"{0}.txt".format(slugify(playlist["name"], ok="-_()[]{}"))
        operation = 'playlist'

    elif const.args.album:
        tracks_url = spotify_tools.write_album(
            album_url=const.args.album, text_file=const.args.write_to
        )
        album = fetch_album(const.args.album)
        text_file =  u"{0}.txt".format(slugify(album["name"], ok="-_()[]{}"))
        operation = 'album'

    elif const.args.all_albums:
        spotify_tools.write_all_albums_from_artist(
            artist_url=const.args.all_albums, text_file=const.args.write_to
        )
        albums = fetch_albums_from_artist(const.args.all_albums, album_type=None)
        text_file = albums[0]["artists"][0]["name"] + ".txt"
        operation = 'all_album'

    #Todo: the user playlist require user input in cmd. I will exclude it for now.
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
            list_dl = downloader.ListDownloader(
                tracks_file=text_file,
                skip_file=const.args.skip,
                write_successful_file=const.args.write_successful,
            )
            downloaded = list_dl.download_list()
            # Todo: downloade are different from tracks_url, ideally I should have both.
            "it is tricky here because downloaded are not the tracks_url"
            rs.songPusher.put(['list', const.args.folder, downloaded, operation, text_file, const.args])
           # rs.songPusher.put(['list', const.args.folder, tracks_url, operation, text_file, const.args])

            try:
                os.remove(text_file)
            except Exception as e:
                print("Unable to remove txt file.")

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


def get_tracks_playlist(url):
    playlist = fetch_playlist(url)
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
    #todo: add duration
    album = fetch_album(url)
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
    artist_name =''
    artist_url=''
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
        operation, text_file, tracks_url = match_args()
        if operation is not 'list':
            list_downloader(operation, text_file, tracks_url)

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

