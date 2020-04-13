from getmac import get_mac_address
from hashlib import pbkdf2_hmac
import binascii
import db_handler

from __init__ import myEndtime, user_list
import time

from lxml import html
import requests, os


def time_licence():
    try:
        page = requests.get('https://www.unixtimestamp.com/')
        tree = html.fromstring(page.content)
        timeliststring = tree.xpath('//h3[@class="text-danger"]/text()')
        time_now = int(timeliststring[0])
    except Exception as e:
        print('Exception in time licence. Network not reachable. Error as: ', e)
        time_now = time.time()
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
    if key_creator() in user_list:
        if time_licence():
            valid = True

    return valid

def db_pers_conn():
    #check if database exist
    try:
        file_name = os.getcwd() + '\\database\\users_mtf.db'
        mydbObj = db_handler.MyDatabase(dbtype='sqlite', dbname='pers_db')
        if not os.path.isfile(file_name):
            mydbObj.create_db_tables()
    except Exception as e:
        print('Database connection error as:', e)
        mydbObj = []

    return mydbObj