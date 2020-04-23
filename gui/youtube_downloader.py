# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube_downloader.ui',
# licensing of 'youtube_downloader.ui' applies.
#
# Created: Wed Apr 22 20:16:38 2020
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DialogYoutubeDL(object):
    def setupUi(self, DialogYoutubeDL):
        DialogYoutubeDL.setObjectName("DialogYoutubeDL")
        DialogYoutubeDL.resize(604, 616)
        DialogYoutubeDL.setMinimumSize(QtCore.QSize(0, 450))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 25, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 25, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 25, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 25, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        DialogYoutubeDL.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        DialogYoutubeDL.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/youtube2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogYoutubeDL.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogYoutubeDL)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_folder = QtWidgets.QFrame(DialogYoutubeDL)
        self.frame_folder.setMinimumSize(QtCore.QSize(0, 140))
        self.frame_folder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_folder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_folder.setObjectName("frame_folder")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_folder)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonFolder = QtWidgets.QPushButton(self.frame_folder)
        self.pushButtonFolder.setMinimumSize(QtCore.QSize(220, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonFolder.setFont(font)
        self.pushButtonFolder.setStyleSheet("QPushButton {\n"
"  \n"
"    border: 2px solid #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #535353);\n"
"    color: rgba(200, 200, 200, 200);\n"
"    margin-left: 120px;\n"
"    margin-right:120px;\n"
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
"    color: white;    \n"
"    \n"
"    }\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/youtu_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonFolder.setIcon(icon1)
        self.pushButtonFolder.setIconSize(QtCore.QSize(35, 35))
        self.pushButtonFolder.setObjectName("pushButtonFolder")
        self.verticalLayout_3.addWidget(self.pushButtonFolder)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_folder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(33, 0))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.frame_folder)
        spacerItem = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setContentsMargins(10, 0, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(DialogYoutubeDL)
        self.comboBox.setMinimumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"border:                 none;\n"
"background-color:   rgb(87, 96, 134);\n"
"color:                      rgb(255, 255, 255);\n"
"font-weight:            bold;\n"
"padding:                    5px \n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border:                 none;\n"
"    background-color:   rgb(87, 96, 134);\n"
"    color:                      rgb(255, 255, 255);\n"
"    font-weight:            bold;\n"
"    padding:                    0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image:                      url(:/icons/combobox_down_arrow.png);\n"
"    padding-right:          5px;\n"
"}\n"
"\n"
"QListView{\n"
"    border:                 none;\n"
"    color:                      rgb(87, 96, 134);\n"
"    background-color:   rgb(255, 255, 255);\n"
"    font-weight:            bold;\n"
"    selection-background-color: rgb(47, 175, 178);\n"
"    show-decoration-selected: 1;\n"
"    margin-left:                -10px;\n"
"    padding-left    :           15px;\n"
"}\n"
"\n"
"QListView::item:hover{\n"
"\n"
"    background-color:   rgb(47, 175, 178);\n"
"    border:                 none;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/musicaicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, "")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.checkBox = QtWidgets.QCheckBox(DialogYoutubeDL)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("\n"
"color: rgb(0, 170, 0);")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonSetting = QtWidgets.QPushButton(DialogYoutubeDL)
        self.pushButtonSetting.setMinimumSize(QtCore.QSize(102, 50))
        self.pushButtonSetting.setStyleSheet("QPushButton {\n"
"  \n"
"    color: rgba(200, 200, 200, 200);\n"
"    image: url(:/mytunefy/resources/icons/setting1.png);\n"
"    min-width: 100px;\n"
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
"    image: url(:/mytunefy/resources/icons/setting-white.png);\n"
"    }\n"
"")
        self.pushButtonSetting.setText("")
        self.pushButtonSetting.setFlat(True)
        self.pushButtonSetting.setObjectName("pushButtonSetting")
        self.horizontalLayout.addWidget(self.pushButtonSetting)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.label_url = QtWidgets.QLabel(DialogYoutubeDL)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.label_url.setFont(font)
        self.label_url.setStyleSheet("QLabel{\n"
"    font-weight: bold;\n"
"     color:white;\n"
"}")
        self.label_url.setAlignment(QtCore.Qt.AlignCenter)
        self.label_url.setObjectName("label_url")
        self.verticalLayout.addWidget(self.label_url)
        self.plainTextEditUrl = QtWidgets.QPlainTextEdit(DialogYoutubeDL)
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
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.listWidget = QtWidgets.QListWidget(DialogYoutubeDL)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(13)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget{\n"
"    background-color: rgb(217, 217, 217);\n"
"    font-family: \"Gill Sans MT\";\n"
"    color: #009500\n"
"}\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(45, 10, 45, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonDownload = QtWidgets.QPushButton(DialogYoutubeDL)
        self.pushButtonDownload.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        self.pushButtonDownload.setFont(font)
        self.pushButtonDownload.setStyleSheet("QPushButton {\n"
"  \n"
"    border-radius: 20px;\n"
"    color:#535353;\n"
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
"    }\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDownload.setIcon(icon4)
        self.pushButtonDownload.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonDownload.setFlat(True)
        self.pushButtonDownload.setObjectName("pushButtonDownload")
        self.horizontalLayout_2.addWidget(self.pushButtonDownload)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame_download = QtWidgets.QFrame(DialogYoutubeDL)
        self.frame_download.setMinimumSize(QtCore.QSize(0, 55))
        self.frame_download.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_download.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_download.setObjectName("frame_download")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_download)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_download)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 25))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"border: 1px solid black;\n"
"padding: 1px;\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #fff,\n"
"stop: 0.4999 #eee,\n"
"stop: 0.5 #ddd,\n"
"stop: 1 #eee );\n"
"width: 15px;\n"
"color: #00aa00 ;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #78d,\n"
"stop: 0.4999 #46a,\n"
"stop: 0.5 #45a,\n"
"stop: 1 #238 );\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"border: 1px solid black;\n"
"}")
        self.progressBar.setProperty("value", 50)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.label_download = QtWidgets.QLabel(self.frame_download)
        self.label_download.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.label_download.setFont(font)
        self.label_download.setStyleSheet("QLabel{\n"
"    font-weight: bold;\n"
"     color: rgb(0, 170, 0);\n"
"\n"
"    }\n"
"")
        self.label_download.setAlignment(QtCore.Qt.AlignCenter)
        self.label_download.setObjectName("label_download")
        self.verticalLayout_2.addWidget(self.label_download)
        self.verticalLayout.addWidget(self.frame_download)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)

        self.retranslateUi(DialogYoutubeDL)
        QtCore.QMetaObject.connectSlotsByName(DialogYoutubeDL)

    def retranslateUi(self, DialogYoutubeDL):
        DialogYoutubeDL.setWindowTitle(QtWidgets.QApplication.translate("DialogYoutubeDL", "Youtube Downloader", None, -1))
        self.pushButtonFolder.setText(QtWidgets.QApplication.translate("DialogYoutubeDL", "Cartella download", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("DialogYoutubeDL", "C:\\User\\Music\\", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("DialogYoutubeDL", "Video - mp4", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("DialogYoutubeDL", "Audio - mp3", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("DialogYoutubeDL", "Qualità Massima", None, -1))
        self.label_url.setText(QtWidgets.QApplication.translate("DialogYoutubeDL", "Incolla URL", None, -1))
        self.plainTextEditUrl.setStatusTip(QtWidgets.QApplication.translate("DialogYoutubeDL", "Copiare link  Spotify qui", None, -1))
        self.pushButtonDownload.setText(QtWidgets.QApplication.translate("DialogYoutubeDL", "Scarica", None, -1))
        self.label_download.setText(QtWidgets.QApplication.translate("DialogYoutubeDL", "Completato", None, -1))

from .import icons_rc
