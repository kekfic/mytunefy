# Importing Required Modules & libraries
import operator
from tkinter import *
import pygame
import os


from PySide2.QtCore import QObject, Signal, QAbstractTableModel, SIGNAL, Qt, QModelIndex
from PySide2.QtGui import QStandardItemModel, QStandardItem, QFont, QBrush
from PySide2.QtWidgets import QMainWindow, QMessageBox, QApplication, \
    QHeaderView
from music_player import mydelegate
from gui.gui_main_player import Ui_PlayerMainWindow
from music_player import table_model

class MyReimplementedWindow(QMainWindow):
    """Reimplementing main window for closeEvent option"""

    def closeEvent(self, event):
        result = QMessageBox.question(self,
                                      "Confirm Uscita MyTuneFy...",
                                      "Confermi di voler uscire ?",
                                      QMessageBox.Yes | QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()


class MainWinPlayer(QObject, Ui_PlayerMainWindow):
    """ this main class is the main window and contain all button specification """

    # threadSignal = Signal(object)

    def __init__(self):
        self.main_window_player = MyReimplementedWindow()
        Ui_PlayerMainWindow.__init__(self)
        self.setupUi(self.main_window_player)

        QObject.__init__(self)

        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()

        os.chdir("D:\\Musica\\")
        # Fetching Songs
        raw_song_tracks = os.listdir()
        self.raw_songs = raw_song_tracks.copy()

        songtracks= []
        header = ['', 'Title', 'Artist', ' ']
        i = 0
        for item in raw_song_tracks:
            if '.mp3' in item:
                try:
                    labels = self.parsing_song(item)
                  #  labels.insert(0, QPushButton(''))
                    songtracks.append(labels)
                except Exception as e:
                    print('Song: {} - not consider cause {}'.format(item, e))
                    self.raw_songs.pop(i)
            else:
                self.raw_songs.pop(i)
            i += 1


        print(len(songtracks))
        print(len(self.raw_songs))


        self.table_model = table_model.MyTableModel (self.main_window_player, songtracks, header)
        self.tableView.setModel(self.table_model)
        #self.tableView.resizeColumnsToContents()
        self.tableView.setColumnWidth(0, 250)
        self.tableView.setColumnWidth(1, 200)

        self.tableView.setShowGrid(FALSE)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().hide()
       # self.tableView.mouseDoubleClickEvent()
        #self.connect(self.PlayPauseButton, Signal('triggered()'), self.parsing_song)
        #self.PlayPauseButton.con

        self.tableView.setItemDelegateForColumn(2, mydelegate.ButtonDelegate())

        # hh = QHeaderView(Qt.Horizontal, self.tableView)
        # hh.setStyleSheet("QHeaderView::section { background-color:black};")
       #  font = QFont('Arial', 18)
        #hh.setBackgroundRole(Q)
       #  hh.(font)

        #hh.setForegroundRole(QPalette.ColorRole)


        # Inserting Songs into Playlist
        # for track in songtracks:
        #     self.playlist.insert(END, track)
    def printer(self):
        print('hello')

    def parsing_song(self, song):
        listsplit = re.split(r'[-.]', song)
        listsong = [x.strip() for x in listsplit]
        art = listsong[1].split('(')[0]
        artist = art.strip()

        return [listsong[0], artist, listsong[2]]


    def playsong(self, songname):
        # Displaying Selected Song title
        #self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load()
        # Playing Selected Song
        pygame.mixer.music.play()

    def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

    def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()

    def unpausesong(self):
        # Displaying Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWinPlayer()
    gui.main_window_player.show()
    # gui.show()

    sys.exit(app.exec_())
