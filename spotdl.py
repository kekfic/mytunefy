#!/usr/bin/env python3
import os
import sys

from getmac import get_mac_address
from hashlib import pbkdf2_hmac
import binascii

# Todo: check why __version__ in not working
# import __version__


from __init__ import personal_key
import time

# My modification
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QMovie
from window_handler import MainWin
from widget_class import LoadingGif


# --


def user_checker():
    mac_address = bytes(get_mac_address(), 'utf8')
    dk = pbkdf2_hmac('sha256', mac_address, b'salt', 100000)
    key_bin = binascii.hexlify(dk)

    return key_bin


if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        CurrentPath = sys._MEIPASS
        # If it's not use the path we're on now
    else:
        CurrentPath = os.path.dirname(__file__)

    if personal_key == user_checker():

        print('User allowed.')
        app = QApplication(sys.argv)

        movie = QMovie("resources/gif/music1.gif")
        splash = LoadingGif(movie)
        splash.show()
        start = time.time()

        while movie.state() == QMovie.Running and time.time() < start + 5:
            app.processEvents()

        gui = MainWin()
        gui.mainwindow.show()
        splash.close()
        # gui.mainwindow.showMaximized()

        sys.exit(app.exec_())
    else:
        print('User not allowed')
