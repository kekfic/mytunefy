from spotdl.spotify_tools import fetch_playlist
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, String, MetaData, Table, Binary, Integer, Float
from sqlalchemy.exc import IntegrityError, OperationalError
from spotdl.internals import sanitize_title
from resources.downloader import get_song_data
from logzero import logger as log
from resources import resources as rs

# Global Variables

# -----------------------------
rs.set_current_directory()


#
def get_user_database(dbtype='sqlite', dbname='users_mtf'):
    "This function search inside pre-created database to check if user has permission"

    SQLITE = 'sqlite'
    # user database
    USERFILE = rs.MY_WORKING_DIR + '\\db_data\\users_mtf'
    USERNAME = 'users'

    DB_ENGINE = {
        SQLITE: 'sqlite:///' + USERFILE
    }
    user_list = []
    engine_url = DB_ENGINE[dbtype].format(DB=dbname)
    db_engine = create_engine(engine_url)
    query = "SELECT * FROM {TBL_USR};".format(TBL_USR=USERNAME)
    with db_engine.connect() as connection:
        try:
            result = connection.execute(query)
            res = result.fetchall()
        except Exception as e:
            print(e)
            result = False
    if res:
        for row in res:
            user_list.append(row[0])

    return res, user_list


# def get_put_db_thread_parser(data):
#
#     id = data[0]
#
#     if id == 'mylist':
#         first_junk, category, url = data
#         result = [category, url]
#
#     elif id == 'song':
#         first_junk, songpath, url_song = data
#         result = [songpath, url_song]
#
#     elif id == 'end':
#         pass


"""
 -----------------------------------------------
            Function of the downloader 
 ----------------------------------------------
 """


def db_music_inserter(mydatabase):
    # Todo: Complete all the cases - Update, delete, rename. As well the function is quite large
    """This function is within a thread and write/read from music user database
        Logic:
            This function is running inside a thread. Communication between main thread and
            other thread is made through globla Queue() variable.
            In a infinitive while, this function wait for instructions.
            There are different "put". For the type of data (playlist/album/song), from
            singular song and from other mechanism for communication.
            The function insert/update database whenever an isntruction to do so is done.
            "end" key control the writing od database.

            category variable could be 'track', 'playlist', 'album', 'artist'
    """

    song_path_list = []
    song_url_list = []
    url = ''
    running = True
    "Pre-variable before infinite loop"
    while running:
        'get a list of value from queue of other thread'
        dbparser = rs.songPusher.get()

        if dbparser[0] == 'song':
            'parsing inside downloader'
            first_junk, song_path, song_url = dbparser

            song_name, album_name, artist_name, \
            album_url, artist_url, duration = get_song_data(song_url)
            artist_id = mydatabase.check_artist(artist_name, artist_url)
            album_id = mydatabase.check_album(album_name, artist_id, album_url)
            # todo put choice for format
            filename = sanitize_title(artist_name + ' - ' + song_name) + '.mp3'
            mydatabase.insert_song(song_name, album_id, artist_id, filename, song_path, song_url, duration)
            log.info("Inserting in song db. As: {0}, {1}, {2}".format(song_name, album_name, artist_name))

        elif dbparser[0] == 'list' or 'artist':
            # todo solve this parser
            'parsing, my list is the put inside start download function'
            junk, folder, song_url_list, category, name_file, args = dbparser

            playlist_url = args.playlist
            if playlist_url:
                playlist = fetch_playlist(playlist_url)['name']
            else:
                playlist = ''

            print(playlist)

            for i in range(len(song_url_list)):
                "I ll do a trick assign playlist and check if it is equal to the other names"

                song_name, album_name, artist_name, \
                album_url, artist_url, duration = get_song_data(song_url_list[i])

                # todo put choice for format
                filename = sanitize_title(artist_name + ' - ' + song_name) + args.output_ext

                mydatabase.insert_song_list_into_db(song_name, playlist, album_name, artist_name,
                                                    filename, folder, [album_url,
                                                                       artist_url,
                                                                       song_url_list[i],
                                                                       playlist_url], duration)

                log.info('Inserting song in database. As: {0}, {1}, {2}, {3} '.format(song_name, playlist, album_name,
                                                                                      artist_name))

            'clear list variable'
            song_path_list.clear()
            song_url_list.clear()
        elif dbparser[0] == 'exit_thread':
            running = False


def player_get_all_user_data():
    """ Player function for geting all playlist and songs in db """
    file_name = rs.MY_WORKING_DIR + '\\db_data\\song_db'
    if file_name:
        mydbObj = MySongDatabase(dbtype='sqlite', dbname='song_db')
        artist_row = mydbObj.query_select_all('artists')
        album_row = mydbObj.query_select_all('albums')
        playlist_row = mydbObj.query_select_all('playlists')
        return [artist_row, album_row, playlist_row]
    else:
        return None


def parsing_user_db_data(fetchall_result):
    if fetchall_result:
        artist, album, playlist = fetchall_result
    else:
        return

    pldata = []
    aldata = []
    ardata = []

    for row in artist:
        ardata.append(row[1])
    for row in album:
        aldata.append(row[2])
    for row in playlist:
        pldata.append(row[1])

    return playlist, album, artist, pldata, aldata, ardata


def player_get_all_songs():
    pass


def get_songs_from_db(id_type, option):
    """ Player function for geting all playlist and songs in db """
    file_name = rs.MY_WORKING_DIR + '\\db_data\\song_db'
    if not option:
        return None
    if file_name:
        mydbObj = MySongDatabase(dbtype='sqlite', dbname='song_db')
        if option == 'Brani':
            result = mydbObj.query_select_all('songs')
        else:
            result = mydbObj.query_all_song_for_specified_type(id_type=id_type, option=option)

        return result
    else:
        return None


class MySongDatabase:
    # Todo: reduce the number of execute and queries.
    """ This class handle the songs database, connection and query are here defined.
        The idea of the structure is for having a portable daabase, with minimum changes
        between different type of database. The one here is based on sqlite.

    """
    "Class global variables"
    SQLITE = 'sqlite'
    USER = 'db_user'  # deprecated

    SONGTot = 'total_song'
    ALBUMS = 'db_albums'
    ARTISTS = 'db_artists'
    PLAYLISTS = 'db_playlist'
    PLAYLIST_SONG = 'db_play_song'

    dictTable = {
        'songs': 'total_song',
        'albums': 'db_albums',
        'artists': 'db_artists',
        'playlists': 'db_playlist',
        'play_song': 'db_play_song'
    }

    MY_SONG_DB = rs.MY_WORKING_DIR + '\\db_data\\song_db'

    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///' + MY_SONG_DB
    }
    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, user_name='', password='', dbname=''):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        """ Database creatiion
        """
        metadata = MetaData()

        artists = Table(self.ARTISTS, metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String, unique=True),
                        Column('url', String)
                        )
        albumsT = Table(self.ALBUMS, metadata,
                        Column('id', Integer, primary_key=True),
                        Column('artist_id', Integer, ForeignKey('db_artists.id')),
                        Column('name', String),
                        Column('key', Binary, unique=True),
                        Column('url', String)
                        )
        playlistT = Table(self.PLAYLISTS, metadata,
                          Column('id', Integer, primary_key=True),
                          Column('name', String, unique=True),
                          Column('url', String)
                          )
        songdataT = Table(self.SONGTot, metadata,
                          Column('id', Integer, primary_key=True),
                          Column('key', Binary, unique=True),
                          Column('name', String),
                          Column('album_id', Integer, ForeignKey('db_albums.id')),
                          Column('artist_id', Integer, ForeignKey('db_artists.id')),
                          Column('filename', String),
                          Column('folder', String),
                          Column('url', String),
                          Column('duration', Float)
                          )

        playlistsongT = Table(self.PLAYLIST_SONG, metadata,
                              Column('id', Integer, primary_key=True),
                              Column('playlist_id', Integer, ForeignKey('db_playlist.id')),
                              Column('song_id', Integer, ForeignKey('total_song.id')),
                              Column('key', Binary, unique=True)
                              )
        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    "-----------------------------------------------------------------------------------"
    def execute_insert_query(self, query='', variable=()):
        if query == '': return
        # print(query)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query, variable)
                res = result.lastrowid

            except IntegrityError as e:
                log.warning('IntegrityError as: {}'.format(e))
            except OperationalError as e:
                log.error("Operational error as: {}".format(e))
            except Exception as e:
                print(e)
                res = False
        return res

    def execute_select_query(self, query='', variable=()):
        if query == '': return
        # print(query)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query, variable)
                res = result.fetchall()
            except Exception as e:
                print(e)
                res = False
        return res


    def execute_general_query(self, query=''):
        "Usualli called when want to retreive all data from query"
        if query == '': return

        result = ''
        # print(query)
        with self.db_engine.connect() as connection:
            try:
                res = connection.execute(query)
                result = res.fetchall()
            except Exception as e:
                print(e)
        return result

    def execute_query(self, query='', variable=()):
        "Called when no feedback is required"
        if query == '': return
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query, variable)
            except IntegrityError as e:
                log.warning("Song: {} of Artist: {} is already present."
                            .format(variable[1], variable[4]))
            except OperationalError as e:
                log.error("Operational error as: {}".format(e))
            except Exception as e:
                print('General Error as:', e)

    "------------------------------------------------------------------------------"

    def check_playlist(self, playlist, url):
        query = 'SELECT id FROM {TABL} where name = ? '.format(TABL=self.PLAYLISTS)
        playlist_id = self.execute_select_query(query, (playlist,))
        if not playlist_id:
            queryPl = "INSERT INTO {TABL} (name, url) VALUES (?, ?);".format(TABL=self.PLAYLISTS)
            playlist_id = self.execute_insert_query(queryPl, (playlist, url))
        else:
            playlist_id = playlist_id[0][0]

        return playlist_id

    def check_artist(self, artist, url):
        query = 'SELECT id FROM {TABL} where name = ? '.format(TABL=self.ARTISTS)
        artist_id = self.execute_select_query(query, (artist,))
        if not artist_id:
            queryAr = "INSERT INTO {TABL} (name, url) " \
                      "VALUES (?, ? )".format(TABL=self.ARTISTS)
            artist_id = self.execute_insert_query(queryAr, (artist, url))
        else:
            artist_id = artist_id[0][0]

        return artist_id

    def check_album(self, album, artist_id, url):
        myid = rs.key_id_creator(album + str(artist_id))
        query = 'SELECT id FROM {TABL} where key = ? '.format(TABL=self.ALBUMS)
        album_id = self.execute_select_query(query, (myid,))
        if not album_id:
            query = "INSERT INTO {TABL} (artist_id, name, key, url) " \
                    "VALUES (?, ?, ?, ? )".format(TABL=self.ALBUMS)
            album_id = self.execute_insert_query(query, (artist_id, album, myid, url))
        else:
            album_id = album_id[0][0]
        return album_id

    def insert_song(self, name, album_id, artist_id, folder, filename, url, duration):

        key = rs.key_id_creator(name + str(artist_id))
        query = 'SELECT id FROM {TABL} where key = ? '.format(TABL=self.SONGTot)
        song_id = self.execute_select_query(query, (key))
        if not song_id:
            query = "INSERT INTO {TABL} (key, name, album_id, artist_id, filename, folder, url, duration) " \
                    "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)".format(TABL=self.SONGTot)
            song_id = self.execute_insert_query(query, (key, name, album_id, artist_id,
                                                        filename, folder, url, duration))
        else:
            song_id = song_id[0][0]

        return song_id

    def insert_song_list_into_db(self, songname='', playlist='', album='',
                                 artist='', filename='', folder='', url=[], duration=''):

        url_art, url_alb, url_song, url_playlist = url
        # Todo --- complex
        if artist == '': return
        if album == '': return
        "insert should return row index of inserted data, what if artist is already there?"

        artist_id = self.check_artist(artist, url_art)
        album_id = self.check_album(album, artist_id, url_alb)

        myid = rs.key_id_creator(songname + str(artist_id))
        query = "SELECT id FROM {TABL} where key = ? ".format(TABL=self.SONGTot)
        song_id = self.execute_select_query(query, variable=myid)

        if not song_id:
            song_id = self.insert_song(songname, album_id, artist_id, folder, filename, url_song, duration)

        if playlist:
            playlist_id = self.check_playlist(playlist, url_playlist)
            query = "INSERT INTO {TABL} (playlist_id, song_id, key)" \
                    " VALUES (?, ?, ?)".format(TABL=self.PLAYLIST_SONG)
            mykey = rs.key_id_creator(songname + playlist)
            self.execute_insert_query(query, (playlist_id, song_id, mykey))

    "---------------------------------------------------------------------------------------------------"


    def query_select_specified_rows(self, table, index_table, identifier):
        "select a specified item from table"
        query = "SELECT * FROM {TABL} where {OPT} = ? ".format(TABL=self.dictTable[table], OPT=index_table)
        rows = self.execute_select_query(query, (identifier))

        return rows

    def query_select_all(self, table):
        "Select all data from a table"
        query = "SELECT * FROM {TABL}".format(TABL=self.dictTable[table])
        all_data = self.execute_general_query(query)
        return all_data

    def query_all_song_for_specified_type(self, id_type=None, option=''):

        if not option or id_type == None:
            return

        if option == 'Artista':
            rows_songs = self.query_select_specified_rows('songs', 'artist_id', id_type)
        elif option == 'Album':
            rows_songs = self.query_select_specified_rows('songs', 'album_id', id_type)

        elif option == 'Playlist':
            rows = self.query_select_specified_rows('play_song', 'playlist_id', id_type)
            rows_songs = []
            for item in rows:
                song_id = item[2]
                res = self.query_select_specified_rows('songs', 'id', song_id)
                rows_songs.append(res[0])
        else:
            rows_songs=[]

        return rows_songs

    def select_specified_song(self, category, songname='', playlist='', artist=''):
        myid = rs.key_id_creator(songname + artist)
        variable = (myid,)
        pass



    def delete_song_table(self, songname):
        query = "DELETE FROM {TABL_USR} (song) VALUES (?)".format(TABL_USR=self.SONGTot)
        variable = (songname,)

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row)  # print(row[0], row[1], row[2])
                result.close()
        print("\n")



    # def sample_delete(self):
    #     # Delete Data by Id
    #     query = "DELETE FROM {} WHERE id=3".format(USER)
    #     self.execute_query(query)
    #     self.print_all_data(USER)
    #     # Delete All Data
    #     '''
    #     query = "DELETE FROM {}".format(USER)
    #     self.execute_query(query)
    #     self.print_all_data(USER)
    #     '''
    #
    # def sample_insert(self):
    #     # Insert Data
    #     query = "INSERT INTO {}(id, first_name, last_name) " \
    #             "VALUES (3, 'Terrence','Jordan');".format(USER)
    #     self.execute_query(query)
    #     self.print_all_data(USER)
    #
    # def sample_update(self):
    #     # Update Data
    #     query = "UPDATE {} set first_name='XXXX' WHERE id={id}" \
    #         .format(USER, id=3)
    #     self.execute_query(query)
    #     self.print_all_data(USER)
