from hashlib import pbkdf2_hmac
from binascii import hexlify

from sqlalchemy import create_engine
from sqlalchemy import Column, String, MetaData, Table, Binary
from sqlalchemy.exc import IntegrityError, OperationalError

from main_classes.handle import get_name_for_list_widget, get_song_data
from logzero import logger as log
from resources import resources as rs

from random import choice
import string

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
def song_id_creator(variable):
    """This function create the hash-like mac to check with db and for song id purpose"""
    variable_b = bytes(variable, 'utf8')
    dk = pbkdf2_hmac('sha256', variable_b, b'salt', 100000)
    key_bin = hexlify(dk)

    return key_bin


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


""" Function of the downloader """


def database_handler(mydatabase):
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
    category = ''
    url = ''
    existing_cat = False
    running = True
    "Pre-variable before infinite loop"
    while running:
        'get a list of value from queue of other thread'

        dbparser = rs.songPusher.get()

        if dbparser[0] == 'mylist':
            'parsing, my list is the put inside start download function'
            first_junk, category, url = dbparser

        elif dbparser[0] == 'song':
            'parsing inside downloader'
            first_junk, songpath, url_song = dbparser
            song_path_list.append(songpath)
            song_url_list.append(url_song)

        elif dbparser[0] == 'end':
            'the string end indicate that download cicle has ended'
            if category == 'track':
                try:
                    song_name, artist, album = get_song_data(song_url_list[0])
                    mydatabase.insert_song_table(songname=song_name, playlist=None, album=album,
                                                 artist=artist, folder=song_path_list[0],
                                                 url=song_url_list[0])
                    log.info("Inserting in song db. As: {0}, {1}, {2}".format(song_name, album, artist))
                except Exception as e:
                    print("Unable to retrieve song data.", e)

            else:
                junk, name = get_name_for_list_widget(category, url)
                'obtain name of the category'
                res_db_category = mydatabase.query_user_table(category, name)
                if not res_db_category:
                    'check if playlist/album is already present, if not add it in db'
                    mydatabase.insert_user_table(category, url, name)

                for i in range(len(song_url_list)):
                    "I ll do a trick assign playlist and check if it is equal to the other names"
                    try:
                        song_name, artist, album = get_song_data(song_url_list[i])
                        name = refine_string(name)
                        artist = refine_string(artist)
                        album = refine_string(album)


                        if name == album or name == artist:
                            " the empty string is creating problem, generating a random index,"
                            playlist = ''
                        else:
                            playlist = name
                        mydatabase.insert_song_table(songname=song_name,
                                                     playlist=playlist, album=album,
                                                     artist=artist, folder=song_path_list[i],
                                                     url=song_url_list[i])

                        if playlist:
                            log.info('Inserting in song db. As: {0}, {1}, {2}, {3} '.format(song_name, playlist, album,
                                                                                            artist))
                        else:
                            log.info("Inserting in song db. As: {0}, {1}, {2}".format(song_name, album, artist))

                    except Exception as e:
                        print("Unable to retrieve song data.", e)

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
        result = mydbObj.query_user_general()
        return result
    else:
        return None

def parsing_user_db_data(fetchall_result):
    playlist = []
    album = []
    artist = []
    if fetchall_result:
        for row in fetchall_result:
            if row[0]:
                playlist.append([row[0], row[3]])
            elif row[1]:
                album.append([row[1], row[3]])
            elif row[2]:
                artist.append([row[2], row[3]])

    return playlist, album, artist

def player_get_all_songs():
    pass



def get_songs_for_type(category):
    pass


class MySongDatabase:
    """ This class handle the songs database, connection and query are here defined.
        The idea of the structure is for having a portable daabase, with minimum changes
        between different type of database. The one here is based on sqlite.

    """
    "Class global variables"
    # Song database
    SQLITE = 'sqlite'
    USER = 'db_user'
    SONGTot = 'total_song'

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
        users = Table(self.USER, metadata,
                      Column('playlist', String),
                      Column('album', String),
                      Column('artist', String),
                      Column('url', String)
                      )
        songdata = Table(self.SONGTot, metadata,
                         Column('id', Binary, primary_key=True),
                         Column('song', String),
                         Column('playlist', String),
                         Column('album', String),
                         Column('artist', String),
                         Column('folder', String),
                         Column('url', String)
                         )
        try:
            metadata.create_all(self.db_engine)
            # print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

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


    def query_user_general(self):
        query = "SELECT * FROM {TBL_USR};".format(TBL_USR=self.USER)
        res = self.execute_general_query(query)
        return res

    def query_user_table(self, category, name):
        # Sample Query
        # query = "SELECT * FROM {TAB_USER} WHERE {CAT} = ? ;".format(TAB_USER=USERS, CAT=category)
        query = "SELECT * FROM {TBL_USR} WHERE {CAT}=?;".format(TBL_USR=self.USER, CAT=category)
        variable = (name,)
        res = self.execute_select_query(query, name)
        return res

    def query_song_table(self, song='', playlist='', album='', category=''):
        query = "SELECT * FROM {TBL_USR} WHERE {CAT} = ?;".format(TBL_USR=self.SONGTot, CAT=category)
        # print(query)

        return query

    def insert_user_table(self, category, url, name):
        playlist = ''
        album = ''
        artist = ''
        query = "INSERT INTO {TABL_USR}(playlist, album, artist, url) " \
                "VALUES (?, ?, ? , ? );".format(TABL_USR=self.USER)
        if category == 'playlist':
            playlist = name
        elif category == 'album':
            album = name
        elif category == 'artist':
            artist = name
        variable = (playlist, album, artist, url)
        self.execute_query(query, variable)

    def insert_song_table(self, songname='', playlist='', album='', artist='', folder='', url=''):
        query = "INSERT INTO {TABL_USR} (id, song, playlist, album, artist, folder, url) " \
                "VALUES (?, ?, ?, ? , ?, ?, ? );".format(TABL_USR=self.SONGTot)

        myid = song_id_creator(songname + artist)
        variable = (myid, songname, playlist, album, artist, folder, url)
        self.execute_query(query, variable)

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
