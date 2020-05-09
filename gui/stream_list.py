# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\stream_list.ui',
# licensing of '.\stream_list.ui' applies.
#
# Created: Wed May  6 13:22:13 2020
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_StreamListAdd(object):
    def setupUi(self, StreamListAdd):
        StreamListAdd.setObjectName("StreamListAdd")
        StreamListAdd.resize(599, 489)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        StreamListAdd.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/stream_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StreamListAdd.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(StreamListAdd)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setContentsMargins(120, 10, 120, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonFolder = QtWidgets.QPushButton(StreamListAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonFolder.sizePolicy().hasHeightForWidth())
        self.pushButtonFolder.setSizePolicy(sizePolicy)
        self.pushButtonFolder.setMinimumSize(QtCore.QSize(204, 60))
        self.pushButtonFolder.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonFolder.setFont(font)
        self.pushButtonFolder.setStyleSheet("QPushButton {\n"
"  \n"
"    border: 2px solid #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #535353);\n"
"    border-radius: 20px;\n"
"    color: rgba(200, 200, 200, 200);\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: navy; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: white;\n"
"    \n"
"    }\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resources/icons/new-folder-music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonFolder.setIcon(icon1)
        self.pushButtonFolder.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonFolder.setFlat(True)
        self.pushButtonFolder.setObjectName("pushButtonFolder")
        self.verticalLayout_2.addWidget(self.pushButtonFolder)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_URL = QtWidgets.QLabel(StreamListAdd)
        self.label_URL.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label_URL.setFont(font)
        self.label_URL.setAlignment(QtCore.Qt.AlignCenter)
        self.label_URL.setObjectName("label_URL")
        self.verticalLayout.addWidget(self.label_URL)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.plainTextEditUrl = QtWidgets.QPlainTextEdit(StreamListAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditUrl.sizePolicy().hasHeightForWidth())
        self.plainTextEditUrl.setSizePolicy(sizePolicy)
        self.plainTextEditUrl.setMinimumSize(QtCore.QSize(0, 35))
        self.plainTextEditUrl.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.plainTextEditUrl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.plainTextEditUrl.setFont(font)
        self.plainTextEditUrl.setAutoFillBackground(True)
        self.plainTextEditUrl.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.plainTextEditUrl.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEditUrl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEditUrl.setLineWidth(2)
        self.plainTextEditUrl.setDocumentTitle("")
        self.plainTextEditUrl.setPlainText("")
        self.plainTextEditUrl.setOverwriteMode(False)
        self.plainTextEditUrl.setBackgroundVisible(False)
        self.plainTextEditUrl.setCenterOnScroll(False)
        self.plainTextEditUrl.setObjectName("plainTextEditUrl")
        self.verticalLayout.addWidget(self.plainTextEditUrl)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.listWidgetUrls = QtWidgets.QListWidget(StreamListAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetUrls.sizePolicy().hasHeightForWidth())
        self.listWidgetUrls.setSizePolicy(sizePolicy)
        self.listWidgetUrls.setMinimumSize(QtCore.QSize(200, 0))
        self.listWidgetUrls.setMaximumSize(QtCore.QSize(16777215, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.listWidgetUrls.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(13)
        font.setItalic(True)
        self.listWidgetUrls.setFont(font)
        self.listWidgetUrls.setStyleSheet("QListWidget{\n"
"    background-color: ;\n"
"    background-color: rgb(40, 40, 90);\n"
"    font-family: \"Gill Sans MT\";\n"
"    color: #ffffff;\n"
"}\n"
"")
        self.listWidgetUrls.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidgetUrls.setAlternatingRowColors(True)
        self.listWidgetUrls.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidgetUrls.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidgetUrls.setObjectName("listWidgetUrls")
        self.verticalLayout.addWidget(self.listWidgetUrls)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButtonStream = QtWidgets.QPushButton(StreamListAdd)
        self.pushButtonStream.setEnabled(True)
        self.pushButtonStream.setMinimumSize(QtCore.QSize(440, 100))
        self.pushButtonStream.setStyleSheet("QPushButton {\n"
"  \n"
"    border-radius: 20px;\n"
"    color: rgba(200, 200, 200, 200);\n"
"    margin-right: 120px;\n"
"    margin-left: 120px;\n"
"    image: url(:/mytunefy/resources/icons/stream_grey.png);\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: white;\n"
"    image: url(:/mytunefy/resources/icons/stream_light-grey.png);\n"
"    }\n"
"")
        self.pushButtonStream.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/stream_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStream.setIcon(icon2)
        self.pushButtonStream.setIconSize(QtCore.QSize(80, 80))
        self.pushButtonStream.setCheckable(True)
        self.pushButtonStream.setFlat(False)
        self.pushButtonStream.setObjectName("pushButtonStream")
        self.verticalLayout.addWidget(self.pushButtonStream)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.progressBar = QtWidgets.QProgressBar(StreamListAdd)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(" border-radius: 5px;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(StreamListAdd)
        QtCore.QMetaObject.connectSlotsByName(StreamListAdd)

    def retranslateUi(self, StreamListAdd):
        StreamListAdd.setWindowTitle(QtWidgets.QApplication.translate("StreamListAdd", "Streaming List", None, -1))
        self.pushButtonFolder.setText(QtWidgets.QApplication.translate("StreamListAdd", "Cartella Cache", None, -1))
        self.label_URL.setText(QtWidgets.QApplication.translate("StreamListAdd", "URL", None, -1))
        self.plainTextEditUrl.setStatusTip(QtWidgets.QApplication.translate("StreamListAdd", "Copiare link  Spotify qui", None, -1))
        self.listWidgetUrls.setStatusTip(QtWidgets.QApplication.translate("StreamListAdd", "Doppio click sulla voce selezionata per rimuoverla dalla lista", None, -1))
        self.pushButtonStream.setStatusTip(QtWidgets.QApplication.translate("StreamListAdd", "Premere per accedere al Player", None, -1))

from .import icons_rc
