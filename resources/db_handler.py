
from sqlalchemy import create_engine
from sqlalchemy import Column, String, MetaData, Table, Binary
from sqlalchemy.exc import IntegrityError, OperationalError

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

            song_name, playlist, album, artist = get_song_data(song_url)
            mydatabase.insert_song_table(songname=song_name, playlist=playlist, album=album,
                                         artist=artist, folder=song_path,
                                         url=song_url)
            log.info("Inserting in song db. As: {0}, {1}, {2}".format(song_name, album, artist))

        elif dbparser[0] == 'list':
            #todo solve this parser
            'parsing, my list is the put inside start download function'
            junk, folder, song_url_list, category, name_file = dbparser
            raw_name = name_file.split('.')[0]
            name = rs.refine_string(raw_name)
            "check if this category exist in db"
            res_db_category = mydatabase.query_user_table(category, name)
            if not res_db_category:
                ' add it in db'
                mydatabase.insert_user_table(category, url, raw_name)
                playlist_checker = False
            else:
                playlist_checker = True

            for i in range(len(song_url_list)):
                "I ll do a trick assign playlist and check if it is equal to the other names"

                song_name, playlist, album, artist = get_song_data(song_url_list[i], raw_name)
                mydatabase.insert_song_table(songname=song_name,
                                             playlist=playlist, album=album,
                                             artist=artist, folder=folder,
                                             url=song_url_list[i])

                log.info('Inserting song in database. As: {0}, {1}, {2}, {3} '.format(song_name, playlist, album,
                                                                                    artist))

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
    plname = []
    alname = []
    arname = []
    if fetchall_result:
        for row in fetchall_result:
            if row[0]:
                playlist.append([row[0], row[3]])
                plname.append(row[0])
            elif row[1]:
                album.append([row[1], row[3]])
                alname.append(row[1])
            elif row[2]:
                artist.append([row[2], row[3]])
                arname.append(row[2])

    return playlist, album, artist, plname, alname, arname

def player_get_all_songs():
    pass



def get_songs_from_db(category='', option=''):
    """ Player function for geting all playlist and songs in db """
    file_name = rs.MY_WORKING_DIR + '\\db_data\\song_db'
    if file_name:
        mydbObj = MySongDatabase(dbtype='sqlite', dbname='song_db')
        result = mydbObj.query_song_table(category, option)
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
        "Called from insert into table"
        if query == '': return
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query, variable)
            except IntegrityError as e:
                log.warning("Song: {} of Artist: {} is already present."
                            .format(variable[1], variable[4]))
                self.playlist_checker()
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

    def query_song_table(self, category, option):
        if not option:
            "select all song"
            query = "SELECT * FROM {TBL_USR};".format(TBL_USR=self.SONGTot)
            res = self.execute_general_query(query)
        else:
            query = "SELECT * FROM {TBL_USR} WHERE {CAT} = ?;".format(TBL_USR=self.SONGTot, CAT=category)
            variable = (option,)
            res = self.execute_select_query(query, variable)

        return res

    def select_specified_song(self, category, songname = '', playlist = '', artist=''):
        myid = rs.song_id_creator(songname + artist)
        variable = (myid,)
        pass


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

        myid = rs.song_id_creator(songname + artist)
        variable = (myid, songname, playlist, album, artist, folder, url)
        self.playCheckVariable = (myid, playlist)
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

    def playlist_checker(self):
        """
         This function is called when we try to add to db a song that is altready present.
         This can happen in two cases: recharging data from an already used item,
         album or artist or playlist. Or from a song that is in two playlist.You should check this one

        """
        pass



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
