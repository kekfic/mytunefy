from PySide2 import QtGui, QtCore
from PySide2.QtCore import Signal, QEvent
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QStyledItemDelegate, QStyle, QStyleOptionButton, QApplication, QStyleOption


class ButtonDelegate(QStyledItemDelegate):
    buttonClicked = Signal(int, int)

    def __init__(self, parent = None):
        super(ButtonDelegate, self).__init__(parent)
        self._pressed = None

    def paint(self, painter, option, index):
    # if index.column()==0:
        painter.save()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/play1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        opt = QStyleOptionButton()
        #opt.text = index.data().toString()

        brush = painter.brush().setColor(QtGui.QColor(0, 0, 0))
        opt.rect = option.rect
       # opt.flat = True
        #opt.text = 'Play'
        opt.icon = icon
        #opt.ButtonFeature = opt.Flat
        #opt.styleObject = opt.
        opt.iconSize = QtCore.QSize(20, 20)
        palette = QtGui.QPalette()
        #brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        #brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        #painter.fillRect(option.rect, brush)


       # opt.initFrom(palette)
        opt.palette = palette

        if self._pressed and self._pressed == (index.row(), index.column()):
            opt.state = QStyle.State_Enabled | QStyle.State_Sunken
        else:
            opt.state = QStyle.State_Enabled | QStyle.State_Raised
        QApplication.style().drawControl(QStyle.CE_PushButton, opt, painter)
        painter.restore()

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.MouseButtonPress:
            # store the position that is clicked
            self._pressed = (index.row(), index.column())
            return True
        elif event.type() == QEvent.MouseButtonRelease:
            if self._pressed == (index.row(), index.column()):
                # we are at the same place, so emit
                self.buttonClicked.emit(*self._pressed)
            elif self._pressed:
                # different place.
                # force a repaint on the pressed cell by emitting a dataChanged
                # Note: This is probably not the best idea
                # but I've yet to find a better solution.
                oldIndex = index.model().index(*self._pressed)
                self._pressed = None
                index.model().dataChanged.emit(oldIndex, oldIndex)
            self._pressed = None
            return True
        else:
            # for all other cases, default action will be fine
            return super(ButtonDelegate, self).editorEvent(event, model, option, index)