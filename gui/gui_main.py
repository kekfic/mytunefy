# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui_main.ui',
# licensing of '.\gui_main.ui' applies.
#
# Created: Tue Apr 21 20:42:57 2020
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 775)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 154, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 2, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 154, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 2, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 2, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 2, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/cuffie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_Folder = QtWidgets.QFrame(self.centralwidget)
        self.frame_Folder.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_Folder.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_Folder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Folder.setLineWidth(5)
        self.frame_Folder.setObjectName("frame_Folder")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_Folder)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButtonFolder = QtWidgets.QPushButton(self.frame_Folder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonFolder.sizePolicy().hasHeightForWidth())
        self.pushButtonFolder.setSizePolicy(sizePolicy)
        self.pushButtonFolder.setMinimumSize(QtCore.QSize(204, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonFolder.setFont(font)
        self.pushButtonFolder.setStyleSheet("QPushButton {\n"
"  \n"
"    border: 2px solid #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #535353);\n"
"    color: rgba(200, 200, 200, 200);\n"
"    image-position:left;\n"
"    \n"
"    \n"
"    image: url(:/mytunefy/resources/icons/folder.png);\n"
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
"    image-position: left;\n"
"    \n"
"    \n"
"    }\n"
"")
        self.pushButtonFolder.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonFolder.setFlat(True)
        self.pushButtonFolder.setObjectName("pushButtonFolder")
        self.verticalLayout_2.addWidget(self.pushButtonFolder)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.plainTextDirectory = QtWidgets.QPlainTextEdit(self.frame_Folder)
        self.plainTextDirectory.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextDirectory.sizePolicy().hasHeightForWidth())
        self.plainTextDirectory.setSizePolicy(sizePolicy)
        self.plainTextDirectory.setMinimumSize(QtCore.QSize(200, 40))
        self.plainTextDirectory.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextDirectory.setFont(font)
        self.plainTextDirectory.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextDirectory.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextDirectory.setReadOnly(True)
        self.plainTextDirectory.setObjectName("plainTextDirectory")
        self.verticalLayout_2.addWidget(self.plainTextDirectory)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_Folder)
        self.pushButton_2.setMinimumSize(QtCore.QSize(202, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"  \n"
"    color: rgba(200, 200, 200, 200);\n"
"    image-position:left;\n"
"    \n"
"    \n"
"    image: url(:/mytunefy/resources/icons/playlist-dark-green.png);\n"
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
"    image-position: left;\n"
"    \n"
"    \n"
"    image: url(:/mytunefy/resources/icons/playlist-light-green.png);\n"
"    }\n"
"")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_Folder)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QtCore.QSize(202, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"  \n"
"    color: rgba(200, 200, 200, 200);\n"
"    image-position:left;\n"
"    \n"
"    \n"
"    image: url(:/mytunefy/resources/icons/playlist-azul-green.png);\n"
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
"    image-position: left;\n"
"    \n"
"    \n"
"    }\n"
"")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.frame_Folder)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_URL = QtWidgets.QLabel(self.centralwidget)
        self.label_URL.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label_URL.setFont(font)
        self.label_URL.setAlignment(QtCore.Qt.AlignCenter)
        self.label_URL.setObjectName("label_URL")
        self.verticalLayout_3.addWidget(self.label_URL)
        self.plainTextEditUrl = QtWidgets.QPlainTextEdit(self.centralwidget)
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
        self.verticalLayout_3.addWidget(self.plainTextEditUrl)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.listWidgetUrls = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetUrls.sizePolicy().hasHeightForWidth())
        self.listWidgetUrls.setSizePolicy(sizePolicy)
        self.listWidgetUrls.setMinimumSize(QtCore.QSize(350, 0))
        self.listWidgetUrls.setMaximumSize(QtCore.QSize(16777215, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 149, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 149, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.listWidgetUrls.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(13)
        font.setItalic(True)
        self.listWidgetUrls.setFont(font)
        self.listWidgetUrls.setStyleSheet("QListWidget{\n"
"    background-color: rgb(217, 217, 217);\n"
"    font-family: \"Gill Sans MT\";\n"
"}\n"
"")
        self.listWidgetUrls.setAlternatingRowColors(True)
        self.listWidgetUrls.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidgetUrls.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidgetUrls.setObjectName("listWidgetUrls")
        self.verticalLayout_3.addWidget(self.listWidgetUrls)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StartPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartPushButton.setMinimumSize(QtCore.QSize(200, 100))
        self.StartPushButton.setMaximumSize(QtCore.QSize(1500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.StartPushButton.setFont(font)
        self.StartPushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StartPushButton.setStyleSheet("QPushButton {\n"
"  \n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #535353);\n"
"    color: rgba(200, 200, 200, 200);\n"
"    \n"
"    \n"
"    image: url(:/mytunefy/resources/icons/down_music_dark_grey.png);\n"
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
"    image: url(:/mytunefy/resources/icons/down_music_light_grey.png);\n"
"    }\n"
"")
        self.StartPushButton.setText("")
        self.StartPushButton.setIconSize(QtCore.QSize(80, 80))
        self.StartPushButton.setAutoRepeat(True)
        self.StartPushButton.setFlat(True)
        self.StartPushButton.setObjectName("StartPushButton")
        self.horizontalLayout_3.addWidget(self.StartPushButton)
        self.pushButtonStream = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStream.setEnabled(False)
        self.pushButtonStream.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButtonStream.setStyleSheet("QPushButton {\n"
"  \n"
"    border-radius: 20px;\n"
"    color: rgba(200, 200, 200, 200);\n"
"    \n"
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
"    \n"
"    image: url(:/mytunefy/resources/icons/stream_light-grey.png);\n"
"    }\n"
"")
        self.pushButtonStream.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/stream_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStream.setIcon(icon1)
        self.pushButtonStream.setIconSize(QtCore.QSize(80, 80))
        self.pushButtonStream.setCheckable(True)
        self.pushButtonStream.setFlat(True)
        self.pushButtonStream.setObjectName("pushButtonStream")
        self.horizontalLayout_3.addWidget(self.pushButtonStream)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(" border-radius: 5px;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_bottomPhrase = QtWidgets.QLabel(self.centralwidget)
        self.label_bottomPhrase.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(12)
        self.label_bottomPhrase.setFont(font)
        self.label_bottomPhrase.setObjectName("label_bottomPhrase")
        self.horizontalLayout.addWidget(self.label_bottomPhrase)
        self.label_IconPlay = QtWidgets.QLabel(self.centralwidget)
        self.label_IconPlay.setMaximumSize(QtCore.QSize(30, 30))
        self.label_IconPlay.setText("")
        self.label_IconPlay.setPixmap(QtGui.QPixmap(":/spotify/resources/icons/play1.png"))
        self.label_IconPlay.setScaledContents(True)
        self.label_IconPlay.setObjectName("label_IconPlay")
        self.horizontalLayout.addWidget(self.label_IconPlay)
        self.label_IconHead = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_IconHead.sizePolicy().hasHeightForWidth())
        self.label_IconHead.setSizePolicy(sizePolicy)
        self.label_IconHead.setMaximumSize(QtCore.QSize(30, 30))
        self.label_IconHead.setText("")
        self.label_IconHead.setPixmap(QtGui.QPixmap(":/spotify/resources/icons/music4.png"))
        self.label_IconHead.setScaledContents(True)
        self.label_IconHead.setObjectName("label_IconHead")
        self.horizontalLayout.addWidget(self.label_IconHead)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuMenu.setIcon(icon2)
        self.menuMenu.setObjectName("menuMenu")
        self.menuFormat = QtWidgets.QMenu(self.menuMenu)
        self.menuFormat.setObjectName("menuFormat")
        self.menuOverride_Policy = QtWidgets.QMenu(self.menuMenu)
        self.menuOverride_Policy.setObjectName("menuOverride_Policy")
        self.menuAdvanced = QtWidgets.QMenu(self.menuMenu)
        self.menuAdvanced.setObjectName("menuAdvanced")
        self.menuIn_Format = QtWidgets.QMenu(self.menuMenu)
        self.menuIn_Format.setEnabled(False)
        self.menuIn_Format.setObjectName("menuIn_Format")
        self.menuEncoding = QtWidgets.QMenu(self.menuMenu)
        self.menuEncoding.setObjectName("menuEncoding")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLanguage = QtWidgets.QMenu(self.menubar)
        self.menuLanguage.setMinimumSize(QtCore.QSize(170, 0))
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuAppearence = QtWidgets.QMenu(self.menubar)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/theme2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAppearence.setIcon(icon3)
        self.menuAppearence.setObjectName("menuAppearence")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionhelp = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/manual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionhelp.setIcon(icon4)
        self.actionhelp.setObjectName("actionhelp")
        self.actionReadMe = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReadMe.setIcon(icon5)
        self.actionReadMe.setObjectName("actionReadMe")
        self.actionL = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/ita.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionL.setIcon(icon6)
        self.actionL.setObjectName("actionL")
        self.actionEng = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/eng.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEng.setIcon(icon7)
        self.actionEng.setObjectName("actionEng")
        self.action_mp3 = QtWidgets.QAction(MainWindow)
        self.action_mp3.setCheckable(True)
        self.action_mp3.setChecked(True)
        self.action_mp3.setObjectName("action_mp3")
        self.action_m4a = QtWidgets.QAction(MainWindow)
        self.action_m4a.setCheckable(True)
        self.action_m4a.setObjectName("action_m4a")
        self.action_flac = QtWidgets.QAction(MainWindow)
        self.action_flac.setCheckable(True)
        self.action_flac.setObjectName("action_flac")
        self.actionSkip = QtWidgets.QAction(MainWindow)
        self.actionSkip.setCheckable(True)
        self.actionSkip.setChecked(True)
        self.actionSkip.setObjectName("actionSkip")
        self.actionPrompt = QtWidgets.QAction(MainWindow)
        self.actionPrompt.setCheckable(True)
        self.actionPrompt.setObjectName("actionPrompt")
        self.actionForce = QtWidgets.QAction(MainWindow)
        self.actionForce.setCheckable(True)
        self.actionForce.setObjectName("actionForce")
        self.actionFile_Format = QtWidgets.QAction(MainWindow)
        self.actionFile_Format.setEnabled(False)
        self.actionFile_Format.setObjectName("actionFile_Format")
        self.actionSearch_Format = QtWidgets.QAction(MainWindow)
        self.actionSearch_Format.setEnabled(False)
        self.actionSearch_Format.setObjectName("actionSearch_Format")
        self.actionTrim_Silence = QtWidgets.QAction(MainWindow)
        self.actionTrim_Silence.setCheckable(True)
        self.actionTrim_Silence.setEnabled(True)
        self.actionTrim_Silence.setObjectName("actionTrim_Silence")
        self.actionDry_Run = QtWidgets.QAction(MainWindow)
        self.actionDry_Run.setCheckable(True)
        self.actionDry_Run.setObjectName("actionDry_Run")
        self.actionNo_Spaces = QtWidgets.QAction(MainWindow)
        self.actionNo_Spaces.setCheckable(True)
        self.actionNo_Spaces.setObjectName("actionNo_Spaces")
        self.actionMusic_Video_Only = QtWidgets.QAction(MainWindow)
        self.actionMusic_Video_Only.setCheckable(True)
        self.actionMusic_Video_Only.setObjectName("actionMusic_Video_Only")
        self.actionSkip_2 = QtWidgets.QAction(MainWindow)
        self.actionSkip_2.setEnabled(False)
        self.actionSkip_2.setObjectName("actionSkip_2")
        self.action_mp4 = QtWidgets.QAction(MainWindow)
        self.action_mp4.setCheckable(True)
        self.action_mp4.setChecked(True)
        self.action_mp4.setEnabled(True)
        self.action_mp4.setObjectName("action_mp4")
        self.action_wbm = QtWidgets.QAction(MainWindow)
        self.action_wbm.setObjectName("action_wbm")
        self.actionDark_Theme = QtWidgets.QAction(MainWindow)
        self.actionDark_Theme.setCheckable(True)
        self.actionDark_Theme.setChecked(True)
        self.actionDark_Theme.setObjectName("actionDark_Theme")
        self.actionLight_Theme = QtWidgets.QAction(MainWindow)
        self.actionLight_Theme.setCheckable(True)
        self.actionLight_Theme.setObjectName("actionLight_Theme")
        self.actionffmpeg = QtWidgets.QAction(MainWindow)
        self.actionffmpeg.setCheckable(True)
        self.actionffmpeg.setChecked(True)
        self.actionffmpeg.setObjectName("actionffmpeg")
        self.actionavconv = QtWidgets.QAction(MainWindow)
        self.actionavconv.setCheckable(True)
        self.actionavconv.setObjectName("actionavconv")
        self.actionyml_Config = QtWidgets.QAction(MainWindow)
        self.actionyml_Config.setEnabled(False)
        self.actionyml_Config.setObjectName("actionyml_Config")
        self.menuFormat.addAction(self.action_mp3)
        self.menuFormat.addAction(self.action_m4a)
        self.menuFormat.addAction(self.action_flac)
        self.menuOverride_Policy.addAction(self.actionSkip)
        self.menuOverride_Policy.addAction(self.actionPrompt)
        self.menuOverride_Policy.addAction(self.actionForce)
        self.menuAdvanced.addAction(self.actionTrim_Silence)
        self.menuAdvanced.addAction(self.actionDry_Run)
        self.menuAdvanced.addAction(self.actionNo_Spaces)
        self.menuAdvanced.addAction(self.actionMusic_Video_Only)
        self.menuAdvanced.addAction(self.actionSkip_2)
        self.menuAdvanced.addAction(self.actionyml_Config)
        self.menuIn_Format.addAction(self.action_mp4)
        self.menuIn_Format.addAction(self.action_wbm)
        self.menuEncoding.addAction(self.actionffmpeg)
        self.menuEncoding.addAction(self.actionavconv)
        self.menuMenu.addAction(self.menuAdvanced.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menuFormat.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menuOverride_Policy.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menuEncoding.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menuIn_Format.menuAction())
        self.menuMenu.addAction(self.actionFile_Format)
        self.menuMenu.addAction(self.actionSearch_Format)
        self.menuHelp.addAction(self.actionhelp)
        self.menuHelp.addAction(self.actionReadMe)
        self.menuLanguage.addAction(self.actionL)
        self.menuLanguage.addAction(self.actionEng)
        self.menuAppearence.addAction(self.actionDark_Theme)
        self.menuAppearence.addAction(self.actionLight_Theme)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAppearence.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuLanguage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MyTuneFy", None, -1))
        self.pushButtonFolder.setText(QtWidgets.QApplication.translate("MainWindow", "Cartella Download", None, -1))
        self.plainTextDirectory.setWhatsThis(QtWidgets.QApplication.translate("MainWindow", "Download folder", None, -1))
        self.plainTextDirectory.setPlainText(QtWidgets.QApplication.translate("MainWindow", "C:\\Music", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Lista Playlist scaricate", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Lista Playlist Streaming", None, -1))
        self.label_URL.setText(QtWidgets.QApplication.translate("MainWindow", "URL", None, -1))
        self.plainTextEditUrl.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Copiare link  Spotify qui", None, -1))
        self.listWidgetUrls.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Doppio click sulla voce selezionata per rimuoverla dalla lista", None, -1))
        self.StartPushButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "download", None, -1))
        self.StartPushButton.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Press for download", None, -1))
        self.pushButtonStream.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Premere per accedere al Player", None, -1))
        self.label_bottomPhrase.setText(QtWidgets.QApplication.translate("MainWindow", "Where words fail, music speaks.", None, -1))
        self.menuMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Menu", None, -1))
        self.menuFormat.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Songs output format", None, -1))
        self.menuFormat.setTitle(QtWidgets.QApplication.translate("MainWindow", "Out Format", None, -1))
        self.menuOverride_Policy.setTitle(QtWidgets.QApplication.translate("MainWindow", "Override Policy", None, -1))
        self.menuAdvanced.setTitle(QtWidgets.QApplication.translate("MainWindow", "Advanced", None, -1))
        self.menuIn_Format.setTitle(QtWidgets.QApplication.translate("MainWindow", "In Format", None, -1))
        self.menuEncoding.setTitle(QtWidgets.QApplication.translate("MainWindow", "Encoding", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.menuLanguage.setTitle(QtWidgets.QApplication.translate("MainWindow", "Language", None, -1))
        self.menuAppearence.setTitle(QtWidgets.QApplication.translate("MainWindow", "Appearence", None, -1))
        self.actionhelp.setText(QtWidgets.QApplication.translate("MainWindow", "Manual", None, -1))
        self.actionReadMe.setText(QtWidgets.QApplication.translate("MainWindow", "ReadMe", None, -1))
        self.actionL.setText(QtWidgets.QApplication.translate("MainWindow", "Ita", None, -1))
        self.actionEng.setText(QtWidgets.QApplication.translate("MainWindow", "Eng", None, -1))
        self.action_mp3.setText(QtWidgets.QApplication.translate("MainWindow", ".mp3", None, -1))
        self.action_m4a.setText(QtWidgets.QApplication.translate("MainWindow", ".m4a", None, -1))
        self.action_flac.setText(QtWidgets.QApplication.translate("MainWindow", ".flac", None, -1))
        self.actionSkip.setText(QtWidgets.QApplication.translate("MainWindow", "Skip", None, -1))
        self.actionPrompt.setText(QtWidgets.QApplication.translate("MainWindow", "Prompt", None, -1))
        self.actionForce.setText(QtWidgets.QApplication.translate("MainWindow", "Force", None, -1))
        self.actionFile_Format.setText(QtWidgets.QApplication.translate("MainWindow", "File Format", None, -1))
        self.actionSearch_Format.setText(QtWidgets.QApplication.translate("MainWindow", "Search Format", None, -1))
        self.actionTrim_Silence.setText(QtWidgets.QApplication.translate("MainWindow", "Trim Silence", None, -1))
        self.actionTrim_Silence.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "remove silence from the start of the audio", None, -1))
        self.actionDry_Run.setText(QtWidgets.QApplication.translate("MainWindow", "Dry Run", None, -1))
        self.actionNo_Spaces.setText(QtWidgets.QApplication.translate("MainWindow", "No Spaces", None, -1))
        self.actionMusic_Video_Only.setText(QtWidgets.QApplication.translate("MainWindow", "Music Video Only", None, -1))
        self.actionSkip_2.setText(QtWidgets.QApplication.translate("MainWindow", "Skip", None, -1))
        self.action_mp4.setText(QtWidgets.QApplication.translate("MainWindow", ".m4a", None, -1))
        self.action_wbm.setText(QtWidgets.QApplication.translate("MainWindow", ".wbm", None, -1))
        self.actionDark_Theme.setText(QtWidgets.QApplication.translate("MainWindow", "Dark Theme", None, -1))
        self.actionLight_Theme.setText(QtWidgets.QApplication.translate("MainWindow", "Light Theme", None, -1))
        self.actionffmpeg.setText(QtWidgets.QApplication.translate("MainWindow", "ffmpeg", None, -1))
        self.actionavconv.setText(QtWidgets.QApplication.translate("MainWindow", "avconv", None, -1))
        self.actionyml_Config.setText(QtWidgets.QApplication.translate("MainWindow", "yml Config", None, -1))

from .import icons_rc
