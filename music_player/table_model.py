import operator

from PySide2.QtCore import QAbstractTableModel, QModelIndex, Qt, SIGNAL
from PySide2.QtGui import QColor, QFont, QBrush
from PySide2 import QtGui

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
        # self.headerData(self.header, Qt.Horizontal, role=Qt.BackgroundRole)

    def rowCount(self, index=QModelIndex()):
        return len(self.mylist)

    def columnCount(self, index=QModelIndex()):
        return 4

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        # elif role != Qt.DisplayRole:
        #     return None
        column = index.column()
        if role == Qt.DisplayRole:
            if column == 0:
                return
            elif column == 1:
                return self.mylist[index.row()][1]
            elif column == 2:
                return self.mylist[index.row()][0]
            elif column == 3:
                return self.mylist[index.row()][2]
        # elif role == Qt.BackgroundColorRole:
        #     return QColor(Qt.Red)
        elif role == Qt.FontRole:
            font = QFont()
            font.setFamily('Comic Sans MS')
            font.setPointSize(9)
            #font.setBold(True)
            return font
        else:
            return None



    def headerData(self, col, orientation, role = Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        if role == Qt.BackgroundRole and Qt.BackgroundColorRole:
            return QColor(Qt.black)
        elif role == Qt.ForegroundRole:
            return QBrush(Qt.black)
        elif role == Qt.FontRole:
            font = QFont()
            font.setPointSize(13)
            font.setFamily('MS Shell Dig 2')

            return font

        return None

        # if role == Qt.FontRole:
        #     if orientation == Qt.Vertical:
        #         font = QFont()
        #         font.setBold(True)
        #         return font
        # if role == Qt.BackgroundColorRole:
        #     return QColor('blue')
        # if role == Qt.ForegroundRole:
        #     return QBrush('Black')


    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
                             key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))