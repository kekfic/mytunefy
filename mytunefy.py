#!/usr/bin/env python3
import os
import sys
import time

from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QMovie
from window_handler import MainWin
from widget_class import LoadingGif
from login import valid_user


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
        time.sleep(5)