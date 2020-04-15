from sqlalchemy import create_engine
from sqlalchemy import Column, String, MetaData, Table, Binary
import os
import time
from utilities.creating_exe import key_creator

# Global Variables
SQLITE = 'sqlite'
USERS = 'users'
PASSWORD = '762d8ee40c9ece0a38736b8236a522a9f132d572133b07c22ad3625e6584cb7e'

MYDIR = "D:\\Programmi\\Python\\MyTuneFy\\" + '\\database\\users_mtf'
engine_url = 'sqlite:///' + MYDIR
db_engine = create_engine(engine_url)
my_key = b'6f97f66b280c5451958a6733caf0f9c80c2ca4ce8e682ddb114c7877f8bf5d67'

def execute_query(query='', variable=()):
    if query == '': return

    with db_engine.connect() as connection:
        try:
            result=connection.execute(query, variable)
            res = result.fetchall()
        except Exception as e:
            print('ERROR', e)

    return  res

def execute_select_query( query=''):
    if query == '': return
    with db_engine.connect() as connection:

        try:
            resul=connection.execute(query)
            res = resul.fetchall()
        except Exception as e:
            print(e)
            res = False
    return res

def query_user_table(category, name):
    # Sample Query
    query = "SELECT * FROM {TAB_USER} WHERE {CAT} = ? ;".format(TAB_USER=USERS, CAT=category)
    variable = (name,)
    res= execute_query(query, variable)
    return res


print(os.getcwd())
res = query_user_table('the_key', my_key)
if res:
    print('Hello World')

