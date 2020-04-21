from getmac import get_mac_address
from hashlib import pbkdf2_hmac
from binascii import hexlify
import time
from lxml import html
import requests
from os import listdir, makedirs, path
import base64
from resources.resources import myEndtime, MY_WORKING_DIR
from resources.database_mytunefy import MySongDatabase, get_user_database



def time_licence():
    """Function for time licence comproval"""
    try:
        page = requests.get('https://www.unixtimestamp.com/')
        tree = html.fromstring(page.content)
        timeliststring = tree.xpath('//h3[@class="text-danger"]/text()')
        time_now = int(timeliststring[0])
        if 'txt' not in listdir():
            makedirs('txt', exist_ok=True)

        if not path.isfile('txt/timestart'):
            with open('txt/timestart', 'wb') as file:
                encodedtime = base64.b64encode(bytes(str(time.time()), 'utf-8'))
                file.write(encodedtime)
    except Exception as e:
        print('Exception in time licence. Network not reachable. Error as: ', e)
        time.sleep(4)
        try:
            print('New attempt to time licence.')
            page = requests.get('https://www.epochconverter.com/')
            tree = html.fromstring(page.content)
            timeliststring = tree.xpath('.//div[@id="ecclock"]/text()')
            time_now = int(timeliststring[0])
        except Exception as e:
            print('ERROR - Second attempt to time licence failed. Error as:', e)
            time.sleep(2)
            with open('txt/timestart', 'r') as file:
                newtime = file.read()
                dectime = base64.b64decode(newtime)
                time_str = (dectime.decode('utf-8'))
                time_now = int(time_str.split('.')[0])

    if time_now < myEndtime:
        valid_licence = True
    else:
        valid_licence = False

    return valid_licence

def key_creator():
    """This function create the hash-like mac to check with db"""

    mac_address = bytes(get_mac_address(), 'utf8')
    dk = pbkdf2_hmac('sha256', mac_address, b'salt', 100000)
    key_bin = hexlify(dk)

    return key_bin

def valid_user():
    valid = False
    try:
        res, user_list = get_user_database()
        if key_creator() in user_list:
            if time_licence():
                valid = True

    except Exception as e:
        print('Database error as:', e)

    return valid

def db_song_conn():
    #check if database exist
    try:
        file_name = MY_WORKING_DIR + '\\db_data\\song_db'
        mydbObj = MySongDatabase(dbtype='sqlite', dbname='song_db')
        if not path.isfile(file_name):
            mydbObj.create_db_tables()
    except Exception as e:
        print('Database connection error as:', e)
        mydbObj = []

    return mydbObj