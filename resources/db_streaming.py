from lib_mytune.spotdl_inherited import EnhancedDownloader
from logzero import logger as log
from resources import resources as rs

rs.set_current_directory()

def db_music_stream_inserter(dbparser, mydatabase):
    # Todo: Complete all the cases - Update, delete, rename. As well the function is quite large
    """This function is within a
        Logic:


            category variable could b
    """



    "Pre-variable before infinite loop"
    category, url_category, name_category, all_tracks = dbparser

    if category == 'playlist':
        playlist = name_category
        playlist_url = url_category

        for track in all_tracks:
            song_name, artist_name, album_name, \
                duration, track_url, album_url, artist_url = track
            try:
                song_data_retreiver = EnhancedDownloader(track_url)
                filename, metadata = song_data_retreiver.return_song_name()
                filename = 'cache/' + filename + '.m4a'
                mydatabase.insert_song_list_into_db(song_name, playlist, album_name, artist_name,
                                                    filename, [album_url,
                                                               artist_url,
                                                               track_url,
                                                               playlist_url], duration)
                print("Inserting song in database. As: {0}, {1}, "
                      "{2}, {3} ".format(song_name, playlist, album_name, artist_name))
            except Exception as e:
                print(e)

    else:
        playlist = ''
        playlist_url = ''
        album_url = url_category
        album_name = name_category

        for track in all_tracks:
            song_name, artist_name, album_name, duration, track_url, artist_url = track

            song_data_retreiver = EnhancedDownloader(track_url)
            filename, metadata = song_data_retreiver.return_song_name()
            mydatabase.insert_song_list_into_db(song_name, playlist, album_name, artist_name,
                                                filename, [album_url,
                                                                   artist_url,
                                                                   track_url,
                                                                   playlist_url], duration)

            log.info('Inserting song in database. As: {0}, {1}, '
                     '      {2}, {3} '.format(song_name, playlist, album_name,artist_name))

