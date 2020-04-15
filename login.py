from getmac import get_mac_address
from hashlib import pbkdf2_hmac
import binascii
import database_mytunefy
import base64
from __init__ import myEndtime
import time

from lxml import html
import requests
import os


def time_licence():
    """Function for time licence comproval"""
    try:
        page = requests.get('https://www.unixtimestamp.com/')
        tree = html.fromstring(page.content)
        timeliststring = tree.xpath('//h3[@class="text-danger"]/text()')
        time_now = int(timeliststring[0])
        if not os.path.isfile('txt/timestart.txt'):
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
            with open('txt/timestart.txt', 'r') as file:
                newtime = file.read()
                dectime = base64.b64decode(newtime)
                time_now = dectime.decode('utf-8')

    if time_now < myEndtime:
        valid_licence = True
    else:
        valid_licence = False

    return valid_licence

def key_creator():
    mac_address = bytes(get_mac_address(), 'utf8')
    dk = pbkdf2_hmac('sha256', mac_address, b'salt', 100000)
    key_bin = binascii.hexlify(dk)

    return key_bin

def valid_user():
    valid = False
    res, user_list = database_mytunefy.get_user_database()
    if key_creator() in user_list:
        if time_licence():
            valid = True

    return valid

def db_song_conn():
    #check if database exist
    try:
        file_name = os.getcwd() + '\\database\\song_db'
        mydbObj = database_mytunefy.MySongDatabase(dbtype='sqlite', dbname='song_db')
        if not os.path.isfile(file_name):
            mydbObj.create_db_tables()
    except Exception as e:
        print('Database connection error as:', e)
        mydbObj = []

    return mydbObj