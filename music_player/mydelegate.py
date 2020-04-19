import operator

import PySide2
from PySide2 import QtGui, QtCore
from PySide2.QtCore import Signal, QEvent, Qt, QModelIndex
from PySide2.QtGui import QPixmap, QPen, QBrush
from PySide2.QtWidgets import QStyledItemDelegate, QStyle, QStyleOptionButton, QApplication, QStyleOption, QWidget, \
    QStyleOptionViewItem, qApp


from gui.push_button import MyPushButton

class ButtonDelegate(QStyledItemDelegate):
    buttonClicked = Signal(int, int)

    def __init__(self, parent = None):
        super(ButtonDelegate, self).__init__(parent)
        #MyPushButton.__init__(self)
        self._pressed = None

    # def createEditor(self, parent, option, index):
    #     combo = QtGui.QPushButton(parent)
    #
    #     # self.connect(combo, QtCore.SIGNAL("currentIndexChanged(int)"), self, QtCore.SLOT("currentIndexChanged()"))
    #     #combo.clicked.connect(self.currentIndexChanged)
    #     return combo
    #    pass

    def paint(self, painter, option, index):

        painter.save()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/play_lgrey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/backtrack3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #opt = QStyleOptionButton()
        opt = QStyleOptionButton()
        #setBackgroundRole()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)#
        opt.icon = icon

        #opt.palette.setBrush(QtGui.QPalette.Button, QBrush(QtGui.QColor(Qt.green)))
        opt.iconSize = QtCore.QSize(30, 30)
        opt.rect = option.rect


        if self._pressed and self._pressed == (index.row(), index.column()):
            opt.state = QStyle.State_Enabled | QStyle.State_Sunken
            opt.icon = icon2
        else:
            opt.state = QStyle.State_Enabled | QStyle.State_Raised
        QApplication.style().drawControl(QStyle.CE_PushButtonLabel, opt, painter)
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