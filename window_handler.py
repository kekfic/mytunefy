"""
@author FF

"""
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtGui import QMovie, QPainter, QPixmap
from PySide2.QtWidgets import QMainWindow, QDialog, QFileDialog, QLabel, QSplashScreen
from PySide2.QtWidgets import QWidget, QGridLayout, QVBoxLayout
from PySide2.QtCore import Signal, QTimer, QObject, SIGNAL

import os

from gui.gui_main import Ui_MainWindow
import re


class LoadingGif(QSplashScreen):
    def __init__(self, movie, parent=None):
        movie.jumpToFrame(0)
        pixmap = QPixmap(movie.frameRect().size())

        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self, event):
        self.movie.stop()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)

    def sizeHint(self):
        return self.movie.scaledSize()



class MainWin(QObject, Ui_MainWindow):
    # this main class is the main window and contain all button specification

    def __init__(self):
        self.mainwindow = QMainWindow()
        Ui_MainWindow.__init__(self)
        self.setupUi(self.mainwindow)
        QObject.__init__(self)

        #combo_data = ['', 'song', 'playlist', 'album', 'artist']
        #self.comboBox.addItems(combo_data)
        self.pushButtonFolder.clicked.connect(self.folder_opener)
        self.progressBar.hide()

    # os.system('explorer.exe "C:\users\%username%\Desktop"')

    def folder_opener(self):
        self.mymusicfolder = 'C:\\Users\\%username%\\'
        mydir = QFileDialog.getExistingDirectory(None, 'Select a folder:', self.mymusicfolder, QFileDialog.ShowDirsOnly)

        self.plainTextEdit_2.plainTextDirectory(mydir)

    def user_checker(self):
        mac_address = bytes(get_mac_address(), 'utf8')
        dk = pbkdf2_hmac('sha256', mac_address, b'salt', 100000)
        key_bin = binascii.hexlify(dk)

        return key_bin

    def text_from_plain_text(self):
        self.url = print(self.plainTextEdit.toText())

    def parser(self, url):
        junk, data = re.split(r'.com/', url)
        category = re.split(r'/*', data)

        return category

    def time_dep_program(self, time_system):
        print('Time system is:')
