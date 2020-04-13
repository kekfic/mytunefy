from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
import os

#Global Variables
#Song database
SQLITE = 'sqlite'
USER = 'new_user'
SONGTot ='total_song'
MY_SONG_DB = os.getcwd() + '\\database\\song_db'
#-----------------------------

#user database
USERFILE = os.getcwd() + '\\database\\users_mtf'
USERNAME = 'users'
#
def get_user_database(dbtype = 'sqlite', dbname ='users_mtf'):
    "This class look inside precreated database to check if user has permission"
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



class MySongDatabase:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///'+MY_SONG_DB
    }

    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, user_name='', password='', dbname=''):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        metadata = MetaData()
        users = Table(USER, metadata,
                      Column('playlist', String, primary_key=True),
                      Column('album', String),
                      Column('artist', String, primary_key=True),
                      )
        songdata = Table(SONGTot, metadata,
                         Column('song', String, primary_key=True),
                         Column('playlist', String, ForeignKey('{}.playlist'.format(USER))),
                         Column('album', String),
                         Column('artist', String, ForeignKey('{}.artist'.format(USER))),
                         Column('folder', String)
                         )
        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    def execute_query(self, query=''):
        if query == '': return
        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

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

    def sample_query_user(self):
        # Sample Query
        query = "SELECT * FROM {TBL_USR};".format(TBL_USR=USERS)
        self.print_all_data(query=query)
        # Sample Query Joining
        # query = "SELECT u.last_name as last_name, " \
        #         "a.email as email, a.address as address " \
        #         "FROM {TBL_USR} AS u " \
        #         "LEFT JOIN {TBL_ADDR} as a " \
        #         "WHERE u.id=a.user_id AND u.last_name LIKE 'M%';" \
        #     .format(TBL_USR=USERS, TBL_ADDR=ADDRESSES)
        self.print_all_data(query=query)

    def sample_delete(self):
        # Delete Data by Id
        query = "DELETE FROM {} WHERE id=3".format(USERS)
        self.execute_query(query)
        self.print_all_data(USER)
        # Delete All Data
        '''
        query = "DELETE FROM {}".format(USER)
        self.execute_query(query)
        self.print_all_data(USER)
        '''

    def sample_insert(self):
        # Insert Data
        query = "INSERT INTO {}(id, first_name, last_name) " \
                "VALUES (3, 'Terrence','Jordan');".format(USER)
        self.execute_query(query)
        self.print_all_data(USER)

    def sample_update(self):
        # Update Data
        query = "UPDATE {} set first_name='XXXX' WHERE id={id}" \
            .format(USER, id=3)
        self.execute_query(query)
        self.print_all_data(USER)


