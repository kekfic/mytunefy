#!/usr/bin/env python3
import os
import sys

from getmac import get_mac_address
from hashlib import pbkdf2_hmac
import binascii


from __init__ import myEndtime, user_list
import time

from lxml import html
import requests
# My modification
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QMovie
from window_handler import MainWin
from widget_class import LoadingGif


# --
def time_licence():
    try:
        page = requests.get('https://www.unixtimestamp.com/')
        tree = html.fromstring(page.content)
        timeliststring = tree.xpath('//h3[@class="text-danger"]/text()')
        time_now = int(timeliststring[0])
    except Exception as e:
        print('Exception in time licence as: ', e)
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

# Todo gif not running in .exe file
if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        CurrentPath = sys._MEIPASS
        # If it's not use the path we're on now
    else:
        CurrentPath = os.path.dirname(__file__)

    if valid_user():

        app = QApplication(sys.argv)

        movie = QMovie("resources/gif/music1.gif")
        splash = LoadingGif(movie)
        splash.show()
        #splash.showMessage("<h1><font color='white'>Welcome to MyTuneFy!</font></h1>")
        start = time.time()

        while movie.state() == QMovie.Running and time.time() < start + 5:
            app.processEvents()

        gui = MainWin()
        gui.mainwindow.show()
        #gui.show()
        splash.close()
        # gui.mainwindow.showMaximized()

        sys.exit(app.exec_())
    else:
        print('User not allowed')
