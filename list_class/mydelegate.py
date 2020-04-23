import operator

import PySide2
from PySide2 import QtGui, QtCore
from PySide2.QtCore import Signal, QEvent, Qt, QModelIndex, QSize
from PySide2.QtGui import QPixmap, QPen, QBrush, QHoverEvent
from PySide2.QtWidgets import QStyledItemDelegate, QStyle, QStyleOptionButton, QApplication, QStyleOption, QWidget, \
    QStyleOptionViewItem, qApp, QPushButton


class ButtonDelegate(QStyledItemDelegate):
    buttonClicked = Signal(int, int)

    def __init__(self, parent=None):
        super(ButtonDelegate, self).__init__(parent)
        # MyPushButton.__init__(self)
        self._pressed = None
        self._hover = None

    def createEditor(self, parent, option, index):
        if index.column() == 0:
            pushButton = QPushButton(parent)
            pushButton.hide()
            #pushButton.setIcon(QtGui.QPixmap(":/spotify/resources/icons/play_lgrey.png"), QtGui.QIcon.Normal,
                             #  QtGui.QIcon.Off)
            return pushButton
        else:
            return QStyledItemDelegate.createEditor(self, parent, option, index)

    def paint(self, painter, option, index):

        if index.column() == 0:
            painter.save()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/play_lgrey.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            palette = QApplication.palette()
            opt = QStyleOptionButton()
            opt.icon = icon
            opt.iconSize = QtCore.QSize(30, 30)
            opt.rect = option.rect

            color = palette.highlight().color() \
                if option.state & QStyle.State_Selected \
                else QtGui.QColor(index.model().data(index, Qt.BackgroundColorRole))


            if self._pressed and self._pressed == (index.row(), index.column()):
                opt.state = QStyle.State_Enabled | QStyle.State_Sunken
                opt.icon = icon

            elif self._hover and self._hover == (index.row(), index.column()):
                print('oh man')
                opt.icon = icon
            else:
                opt.state = QStyle.State_Enabled | QStyle.State_Raised
            QApplication.style().drawControl(QStyle.CE_PushButtonLabel, opt, painter)
            painter.restore()
        else:
            QStyledItemDelegate.paint(self, painter, option, index)

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

    def mouseMoveEvent(event):
        pass

    def sizeHint(self, option, index):

        return QStyledItemDelegate.sizeHint(self, option, index)