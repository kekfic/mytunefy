from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, MetaData, Table, Binary
from sqlalchemy.ext.declarative import declarative_base
import os


from creating_exe import key_creator
# Global Variables
SQLITE = 'sqlite'
USERS = 'users'
PASSWORD = '762d8ee40c9ece0a38736b8236a522a9f132d572133b07c22ad3625e6584cb7e'

MYDIR = os.getcwd() + '\\database\\users_mtf'


class MyUserDb:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///'+MYDIR
    }

    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        metadata = MetaData()
        users = Table(USERS, metadata,
                      Column('the_key', String, primary_key=True, unique=True),
                      Column('mac_address', String),
                      Column('user_name', String)
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
                print('ERROR', e)

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

    def insert_user(self, personal_key, mac_address='', user=''):
        # Insert Data
        query = "INSERT INTO users (the_key, mac_address, user_name) " \
                "VALUES (?, ?, ?);", (personal_key, mac_address, user)
        self.execute_query(query)
        self.print_all_data(USERS)

      #  self.print_all_data(USERS)


if __name__=='__main__':
    mydb = MyUserDb(dbtype='sqlite', dbname='users_mtf')
    myfile = os.getcwd() + '\\database\\users_mtf'
    if not os.path.isfile(myfile):
        mydb.create_db_tables()

    user_name = ''
    # while user_name is not 'exit':
    mac_add = input('Type Mac: ')
    user_name = input('Type user name: ')
    key, mac_add = key_creator(mac_add)

    # if user_name is not 'exit':
    mydb.insert_user(personal_key='key', mac_address='b', user='a')
