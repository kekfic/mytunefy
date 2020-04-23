import os, sys
<<<<<<< HEAD
from hashlib import pbkdf2_hmac
from binascii import hexlify

from sqlalchemy import create_engine
from sqlalchemy import Column, String, MetaData, Table, Binary
from sqlalchemy.exc import IntegrityError
=======
>>>>>>> master

def testpath():
    if getattr(sys, 'frozen', False):
        CurrentPath = sys._MEIPASS
        print('firstif', CurrentPath)
        # If it's not use the path we're on now
    else:
        CurrentPath = os.path.dirname(__file__)
<<<<<<< HEAD
        print('second if', CurrentPath)


def database_song_test(dbtype='sqlite', dbname='song_db'):
    SQLITE = 'sqlite'
    USER = 'db_user'
    SONGTot = 'total_song'

    MY_SONG_DB = os.getcwd() + '\\db_data\\song_db'
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///' + MY_SONG_DB
    }
    engine_url = DB_ENGINE[dbtype].format(DB=dbname)
    db_engine = create_engine(engine_url)

    return db_engine



def select_from_database(category, name, db_engine):
    SQLITE = 'sqlite'
    USER = 'db_user'
    SONGTot = 'total_song'

    query = "SELECT * FROM {TBL_USR} WHERE {CAT}=?;".format(TBL_USR=SONGTot, CAT=category)
    variable = (name,)
    res = execute_query(query, name, db_engine)
    return res

def select_from_song_database(category, name, db_engine):
    SQLITE = 'sqlite'
    USER = 'db_user'
    SONGTot = 'total_song'

    query = "SELECT * FROM {TBL_USR} WHERE {CAT}=?;".format(TBL_USR=SONGTot, CAT=category)
    variable = (name,)
    res = execute_query(query, name, db_engine)
    return res

def select_all_from_user_database(db_engine):
    SQLITE = 'sqlite'
    USER = 'db_user'
    query = "SELECT * FROM {TBL_USR};".format(TBL_USR=USER)
    res = execute_query(db_engine, query)
    return res

def execute_query(db_engine, query):

    with db_engine.connect() as connection:
        result = connection.execute(query)
        res = result.fetchall()

    return res

def execute_query_with_varibale(db_engine, query, variable):
    with db_engine.connect() as connection:
        result = connection.execute(query, variable)
        res = result.fetchall()

    return res


def test_song_db():
    db_engine = database_song_test()
    res = select_from_database()
    return res

def test_user_db_select_all():
    db_engine = database_song_test()
    res = select_all_from_user_database(db_engine)

    return res
=======
        print('second if', CurrentPath)
>>>>>>> master
