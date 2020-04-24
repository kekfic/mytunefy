from queue import Queue

from PySide2.QtCore import  QObject
from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtWidgets import QSplashScreen, QFileDialog
from gui.youtube_downloader import Ui_DialogYoutubeDL
import threading
from main_classes.handle import mySimpleYoutubeDownloader
from random import randint
from logzero import logger as log
import os

class LoadingGif(QSplashScreen):
    """
       Starting splash class
       """

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


class YoutubeDialog(QObject, Ui_DialogYoutubeDL):
    # Todo: adapt for any other available format

    #downSignal = Signal(object)

    available_formats = {
        "Video": "any",
        "Video - mp4": "mp4",
        "Video - xx": "xx",
        "Audio": "any",
        "Audio - mp3": "mp3",
        "Audio - m4a": "m4a"
    }

    def __init__(self, dialog, mysignal):
        Ui_DialogYoutubeDL.__init__(self)
        #super().__init__(self)
        self.setupUi(dialog)
        self.dialog = dialog
        self.mydownload = None

        self.downSignal = mysignal

        self.all_item = []
        self.queYoutube = Queue()
        self.listWidget.hide()
        self.frame_download.hide()
        self.folder = os.getcwd()

        self.lineEdit.setText(self.folder)
        self.pushButtonDownload.clicked.connect(self.threading_launcher)
        self.comboBox.currentIndexChanged.connect(self.get_combobox)
        self.pushButtonFolder.clicked.connect(self.folder_changer)
        self.plainTextEditUrl.textChanged.connect(self.text_from_plain_text)

        self.downSignal.connect(self.progressBar100)

        self.mythread = threading.Thread(target=self.download, daemon=True)
        self.mythread.start()


    def threading_launcher(self):

        if self.mydownload is None:
            return

        self.count = self.listWidget.count()
        if self.count:
            extension, item = self.get_combobox()
            if 'Video' in item:
                self.mydownload.is_video(extension)
            elif 'Audio' in item:
                self.mydownload.is_audio(extension)
            self.queYoutube.put('download')

            self.listWidget.clear()
            self.listWidget.hide()
            self.label_download.hide()
            #
            self.frame_download.show()

            "Fake progress bar"
            val_progbar = randint(20, 55)
            self.progressBar.setValue(val_progbar)


    def download(self):
        #Todo this way of handling signal is not good. change it
        index = 0
        while threading.main_thread().is_alive():
            if index:
                self.downSignal.emit(index)
                index = 0
            down = self.queYoutube.get()
            if down == 'download':
                self.mydownload.download(self.folder)

            index += 1

    def progressBar100(self):
        self.progressBar.setValue(100)
        self.label_download.show()


    def get_combobox(self):
        item = self.comboBox.currentText()
        extension = self.available_formats[item]
        return extension, item

    def folder_changer(self):
        self.folder = QFileDialog.getExistingDirectory(self.dialog, 'Select a directory', self.folder,
                                                  QFileDialog.ShowDirsOnly)
        if not self.folder:
            self.folder = os.getcwd()
        self.lineEdit.setText(self.folder)
        self.folder.replace("/", "\\")

        return self.folder

    def text_from_plain_text(self, url=None):
        if url is None:
            url = self.plainTextEditUrl.toPlainText()
            my_url = self.valid_url(url)
            if my_url:
                try:
                    self.mydownload = mySimpleYoutubeDownloader(url)
                    title = self.mydownload.title()
                    self.listWidgetHandler(title)
                    self.plainTextEditUrl.clear()
                except Exception as e:
                    log.error(e)

    def valid_url(self, url):
        valid = False
        substring = 'https://youtu.be/'
        #substring2 = 'https://www.youtube.com/'
        if substring in url:
            valid = True

        return valid

    def listWidgetHandler(self, title):
        "Get from urls and adding to list widget"

        # text_playlist, junk = get_name_for_list_widget(category_list, url)
        self.listWidget.addItem(title)
        self.all_item.append(title)
        number_item = self.listWidget.count()
        self.listWidget.setMaximumHeight(number_item * self.listWidget.sizeHintForRow(0))
        if self.listWidget.isHidden():
            self.listWidget.show()
        if not self.frame_download.isHidden():
            self.frame_download.hide()
