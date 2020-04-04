"""
@author FF

"""
from PySide2 import QtGui, QtWidgets, QtCore

from PySide2.QtWidgets import QMainWindow, QDialog, QFileDialog
from PySide2.QtWidgets import QWidget, QGridLayout, QVBoxLayout
from PySide2.QtCore import Signal, QTimer, QObject, SIGNAL

import os

from gui.gui_main import Ui_MainWindow


class MainWin(QObject, Ui_MainWindow):
    # this main class is the main window and contain all button specification

    def __init__(self):
        self.mainwindow = QMainWindow()
        Ui_MainWindow.__init__(self)
        self.setupUi(self.mainwindow)
        QObject.__init__(self)

        combo_data = ['', 'song', 'playlist', 'album', 'artist']
        self.comboBox.addItems(combo_data)
        self.pushButtonFolder.clicked.connect(self.folder_opener)

    # os.system('explorer.exe "C:\users\%username%\Desktop"')

    def folder_opener(self):
        self.mymusicfolder = 'C:\\Users\\%username%\\'
        mydir = QFileDialog.getExistingDirectory(None, 'Select a folder:', self.mymusicfolder, QFileDialog.ShowDirsOnly)

        self.plainTextEdit_2.setPlainText(mydir)
        # self.plainTextEdit_2.plainTextDirectory(mydir)
        # plainTextDirectory
        # os.system(r'explorer.exe /select "C:\users\%username%\Music"')

    def user_checker(self):
        mac_address = bytes(get_mac_address(), 'utf8')
        dk = pbkdf2_hmac('sha256', mac_address, b'salt', 100000)
        key_bin = binascii.hexlify(dk)

        return key_bin

    def time_dep_program(self, time_system):
        print('Time system is:')