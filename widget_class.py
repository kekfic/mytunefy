from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtWidgets import QSplashScreen, QWidget


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


class CustomQWidget(QWidget):
    """
    This class is for a custom widget, not used
    """
    def __init__(self, parent=None):
        super(CustomQWidget, self).__init__(parent)

        label = QLabel("I am a custom widget")

        button = QPushButton("A useless button")

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)