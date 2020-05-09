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
            if column == 0:
                pass
            elif column == 1:
                pass
            elif column == 2:
                return self.mylist[index.row()][1]
            elif column == 3:
                return self.mylist[index.row()][0]
            elif column == 4:
                return self.mylist[index.row()][2]
            elif column == 5:
                try:
                    song_path = self.mylist[index.row()][3].rsplit('/', 1)[0]
                except Exception as e:
                    song_path = self.mylist[index.row()][3]
                return song_path

        elif role == Qt.FontRole:
            font = QFont()
            font.setFamily('Comic Sans MS')
            font.setPointSize(10)
            return font
        #
        # elif role == Qt.ForegroundRole:
        #     if
        else:
            return None

    def headerData(self, col, orientation, role=Qt.DisplayRole):

        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        if role == Qt.BackgroundRole and Qt.BackgroundColorRole:
            return QColor(Qt.white)
        elif role == Qt.ForegroundRole:
            return QBrush(Qt.white)
        elif role == Qt.FontRole:
            font = QFont()
            font.setPointSize(13)
            font.setFamily('MS Shell Dig 2')
            return font
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignLeft



    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        #todo : something wrong when sorting by song name
        if col == 2:
            col = 1

        if col == 1 or col == 3:
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
                                     "    selection-background-color: rgb(40, 80, 230, 50);\n"
                                     "    selection-color: white\n"
                                     "}\n"
                                     "QHeaderView::section { background-color:black}\n"
                                     "QHeaderView::section { background-color:rgb(30, 30, 30) }")
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setShowGrid(False)
        self.setGridStyle(QtCore.Qt.NoPen)
        header = ['', '', 'Title', 'Artist', 'Album', 'Date', 'Folder', '']

        table_model = MyTableModel(parent, tracks, header)
        self.setModel(table_model)
        #self.resizeColumnsToContents()
        self.setColumnWidth(0, 10)
        self.setColumnWidth(1, 10)
        self.setColumnWidth(2, 390)
        self.setColumnWidth(3, 260)
        self.setColumnWidth(4, 260)
        self.setColumnWidth(5, 500)
        self.resizeRowsToContents()
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setShowGrid(False)
        self.verticalHeader().hide()
        self.horizontalHeader().show()
        self.horizontalScrollBar().hide()
        self.set_scroll_bar_style()
        self.setSortingEnabled(True)
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
        row = self.rootIndex()


    def set_scroll_bar_style(self):
        self.verticalScrollBar().setStyleSheet("QScrollBar:vertical\n"
                                               " {\n"
                                               "     background-color: #2A2929;\n"
                                               "     width: 15px;\n"
                                               "     margin: 15px 3px 15px 3px;\n"
                                               "     border: 1px transparent #2A2929;\n"
                                               "     border-radius: 4px;\n"
                                               " }\n"
                                               "\n"
                                               " QScrollBar::handle:vertical\n"
                                               " {\n"
                                               "     background-color: red;         /* #605F5F; */\n"
                                               "     min-height: 5px;\n"
                                               "     border-radius: 4px;\n"
                                               " }\n"
                                               "\n"
                                               " QScrollBar::sub-line:vertical\n"
                                               " {\n"
                                               "     margin: 3px 0px 3px 0px;\n"
                                               "     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
                                               "     height: 10px;\n"
                                               "     width: 10px;\n"
                                               "     subcontrol-position: top;\n"
                                               "     subcontrol-origin: margin;\n"
                                               " }\n"
                                               "\n"
                                               " QScrollBar::add-line:vertical\n"
                                               " {\n"
                                               "     margin: 3px 0px 3px 0px;\n"
                                               "     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
                                               "     height: 10px;\n"
                                               "     width: 10px;\n"
                                               "     subcontrol-position: bottom;\n"
                                               "     subcontrol-origin: margin;\n"
                                               " }\n"
                                               "\n"
                                               " QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
                                               " {\n"
                                               "\n"
                                               "     border-image: url(:/qss_icons/rc/up_arrow.png);\n"
                                               "     height: 10px;\n"
                                               "     width: 10px;\n"
                                               "     subcontrol-position: top;\n"
                                               "     subcontrol-origin: margin;\n"
                                               " }\n"
                                               "\n"
                                               "\n"
                                               " QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
                                               " {\n"
                                               "     border-image: url(:/qss_icons/rc/down_arrow.png);\n"
                                               "     height: 10px;\n"
                                               "     width: 10px;\n"
                                               "     subcontrol-position: bottom;\n"
                                               "     subcontrol-origin: margin;\n"
                                               " }\n"
                                               "\n"
                                               " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
                                               " {\n"
                                               "     background: none;\n"
                                               " }\n"
                                               "\n"
                                               "\n"
                                               " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                               " {\n"
                                               "     background: none;\n"
                                               " }\n"
                                               "")
