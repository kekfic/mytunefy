"""
@author FF

"""
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QMainWindow, QDialog
from PySide2.QtWidgets import QWidget,QGridLayout,QVBoxLayout
from PySide2.QtCore import Signal,QTimer,QObject,SIGNAL


from gui.gui_main import Ui_MainWindow

class MainWin(QObject,Ui_MainWindow):
#this main class is the main window and contain all button specification   
        
    def __init__(self):
        self.mainwindow = QMainWindow()
        Ui_MainWindow.__init__(self)
        self.setupUi(self.mainwindow)
        QObject.__init__(self)     