#!/usr/bin/env python3
import os
import sys
import time

from resources.resources import set_current_directory
from PySide2.QtWidgets import QApplication, QMessageBox, QDialog
from PySide2.QtGui import QMovie
from main_classes.window_handler import MainWin
from main_classes.widget_class import LoadingGif
from resources.login import valid_user


if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        CurrentPath = sys._MEIPASS
        # If it's not use the path we're on now
    else:
        CurrentPath = os.path.dirname(__file__)

    "Setting the directory, I could do it as well with CurrentPath"
    set_current_directory()

    app = QApplication(sys.argv)

    movie = QMovie("resources/gif/music1.gif")
    splash = LoadingGif(movie)
    splash.show()
    # splash.showMessage("<h1><font color='white'>Welcome to MyTuneFy!</font></h1>")
    start = time.time()

    while movie.state() == QMovie.Running and time.time() < start + 5:
        app.processEvents()

    if valid_user():

        "downloader"
        #  -------------------working on player
        guiDown = MainWin()
        guiDown.mainwindow.show()
        splash.close()
        # gui.mainwindow.showMaximized()
        sys.exit(app.exec_())

    else:
        # Todo: add type of error (Db not found, no user, time licence, other).
        # Todo: add some system to have logs when executable crash (a log file)
        splash.close()
        mydialog = QDialog()
        result = QMessageBox.information(mydialog, "Invalid USER", 'Invalid User - Please contact administrator.')
        print('User not allowed')
        sys.exit(3)
