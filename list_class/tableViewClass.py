import operator

from PySide2.QtCore import QAbstractTableModel, QModelIndex, Qt, SIGNAL
from PySide2.QtGui import QColor, QFont, QBrush
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import QTableView


class MyTableModel(QAbstractTableModel):
    """This class is the model that the QTable view use"""

    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
        # self.headerData(self.header, Qt.Horizontal, role=Qt.BackgroundRole)

    def rowCount(self, index=QModelIndex()):
        return len(self.mylist)

    def columnCount(self, index=QModelIndex()):
        return 8

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        column = index.column()
        if role == Qt.DisplayRole:
            if column == 2:
                return self.mylist[index.row()][1]
            elif column == 3:
                return self.mylist[index.row()][0]
            elif column == 4:
                return self.mylist[index.row()][2]
            elif column == 5:
                return self.mylist[index.row()][3]
            elif column == 0:
                return QtWidgets.QPushButton

        # elif role == Qt.BackgroundRole:
        #      return QBrush(Qt.black)

        elif role == Qt.FontRole:
            font = QFont()
            font.setFamily('Comic Sans MS')
            font.setPointSize(10)

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
        if order == Qt.AscendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))


class MyTableView(QTableView):
    """ Reimplementation of the table View so that I can control all the feature"""

    def __init__(self, parent=None, tracks=[]):
        super().__init__(parent)
        self.setParent(parent)

        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(11)
        self.setFont(font)
        self.setStyleSheet("QTableView{\n"
                                     "    background-color: rgb(30, 30, 30);\n"
                                     "    color: white;\n"
                                     "    selection-background-color: rgb(230, 230, 230, 50);\n"
                                     "}\n"
                                     "QHeaderView::section { background-color:black}")
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setShowGrid(False)
        self.setGridStyle(QtCore.Qt.NoPen)
        header = ['', '', 'Title', 'Artist', 'Album', 'Date', '', '']

        table_model = MyTableModel(parent, tracks, header)
        self.setModel(table_model)
        #self.resizeColumnsToContents()
        self.setColumnWidth(0, 10)
        self.setColumnWidth(1, 10)
        self.setColumnWidth(2, 390)
        self.setColumnWidth(3, 280)
        self.setColumnWidth(4, 240)
        self.setColumnWidth(5, 350)
        self.resizeRowsToContents()
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setShowGrid(False)
        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        self.horizontalScrollBar().hide()
        #self.sortByColumn(2)

    def set_new_model(self, parent, tracks, header):
        header = ['', '', 'Title', 'Artist', 'Album', 'Folder', '', '']
        table_model = MyTableModel(parent, tracks, header)
        self.setModel(table_model)
        self.resizeRowsToContents()

    def mouseMoveEvent(self, event):

       """Reimplementing the movse move event"""
       self.setMouseTracking(True)
    #   self.setSelectionBehavior()#SelectRows to be set
       # mHoverRow = index.row()
       # mHoverColumn = index.column()
       # print (index.row())

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            pass

        #QTableView.indexAt(QTableView.currentIndex(event.pos()))
        #print(QTableView.indexAt(QTableView.currentIndex(QModelIndex.row())))
        return None

    def playing_behavior(self, index):
        # todo: find method to keep selected even when plylist is changed
        self.selectRow(index)
       # self.setBackgroundRole(QtGui.QColor('rgb(45, 200, 0)'))

       # if (self.selectionBehavior() == SelectRows and oldHoverRow != mHoverRow):
       #     for (int i in range columnCount()):
       #
       #         update(model()->index(mHoverRow, i))
       #
       #  if (selectionBehavior() == SelectColumns & & oldHoverColumn != mHoverColumn) {
       #  for (int i = 0; i < model()->rowCount(); ++i) {
       #  update(model()->index(i, mHoverColumn));
       #  update(model()->index(i, oldHoverColumn))

# def tableViewConf(parent, tableView, tracks=[]):
#
#     header = ['', '', 'Title', 'Artist', 'Album', 'Date', '', '']
#
#     table_model = MyTableModel(parent, tracks, header)
#     tableView.setModel(table_model)
#     tableView.resizeColumnsToContents()
#     tableView.setColumnWidth(2, 280)
#     tableView.setColumnWidth(3, 230)
#     tableView.setSelectionBehavior(QTableView.SelectRows)
#     tableView.setShowGrid(False)
#     tableView.verticalHeader().hide()
#     tableView.horizontalHeader().hide()
#     #tableView.setAlternatingRowColors(True)
#
