# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui_main_player.ui',
# licensing of '.\gui_main_player.ui' applies.
#
# Created: Wed May  6 20:10:30 2020
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PlayerMainWindow(object):
    def setupUi(self, PlayerMainWindow):
        PlayerMainWindow.setObjectName("PlayerMainWindow")
        PlayerMainWindow.resize(1097, 831)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PlayerMainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/play1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PlayerMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PlayerMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameTop = QtWidgets.QFrame(self.centralwidget)
        self.frameTop.setMinimumSize(QtCore.QSize(0, 70))
        self.frameTop.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frameTop.setStyleSheet("QFrame:hover{\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #535353);\n"
"}")
        self.frameTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTop.setObjectName("frameTop")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frameTop)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.TopLayout = QtWidgets.QHBoxLayout()
        self.TopLayout.setContentsMargins(10, 0, 10, 0)
        self.TopLayout.setObjectName("TopLayout")
        self.frame = QtWidgets.QFrame(self.frameTop)
        self.frame.setMinimumSize(QtCore.QSize(80, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 40)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toolButtonGeneral = QtWidgets.QToolButton(self.frame)
        self.toolButtonGeneral.setMinimumSize(QtCore.QSize(60, 30))
        self.toolButtonGeneral.setMaximumSize(QtCore.QSize(75, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.toolButtonGeneral.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolButtonGeneral.setFont(font)
        self.toolButtonGeneral.setStyleSheet("\n"
"border-radius: 5px;")
        self.toolButtonGeneral.setIconSize(QtCore.QSize(20, 20))
        self.toolButtonGeneral.setObjectName("toolButtonGeneral")
        self.verticalLayout_4.addWidget(self.toolButtonGeneral)
        self.TopLayout.addWidget(self.frame)
        self.FolderButton = QtWidgets.QPushButton(self.frameTop)
        self.FolderButton.setMinimumSize(QtCore.QSize(124, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.FolderButton.setFont(font)
        self.FolderButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #2566ff, stop: 1 #3a93ff);\n"
"    color: white;\n"
"    min-width: 120px;\n"
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
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.FolderButton.setObjectName("FolderButton")
        self.TopLayout.addWidget(self.FolderButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TopLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.frameTop)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton.setStyleSheet("QPushButton {\n"
"  \n"
"    border-radius: 20px;\n"
"    color: rgba(200, 200, 200, 200);\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/setting1.png);\n"
"   \n"
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
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.TopLayout.addWidget(self.pushButton)
        self.label_User = QtWidgets.QLabel(self.frameTop)
        self.label_User.setMinimumSize(QtCore.QSize(185, 0))
        self.label_User.setMaximumSize(QtCore.QSize(180, 70))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        self.label_User.setFont(font)
        self.label_User.setStyleSheet("QLabel{\n"
"\n"
"    color: rgb(41, 111, 255);\n"
"}")
        self.label_User.setAlignment(QtCore.Qt.AlignCenter)
        self.label_User.setObjectName("label_User")
        self.TopLayout.addWidget(self.label_User)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TopLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TopLayout.addItem(spacerItem2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frameTop)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
"color: white;\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.TopLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_7.addLayout(self.TopLayout)
        self.verticalLayout_2.addWidget(self.frameTop)
        self.centralhorizontalLayout = QtWidgets.QHBoxLayout()
        self.centralhorizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.centralhorizontalLayout.setObjectName("centralhorizontalLayout")
        self.verticalLayout_Library = QtWidgets.QVBoxLayout()
        self.verticalLayout_Library.setContentsMargins(0, 10, 10, 10)
        self.verticalLayout_Library.setObjectName("verticalLayout_Library")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setContentsMargins(35, 0, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.StreamModeButton = QtWidgets.QPushButton(self.centralwidget)
        self.StreamModeButton.setMinimumSize(QtCore.QSize(200, 40))
        self.StreamModeButton.setMaximumSize(QtCore.QSize(200, 45))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(83, 83, 83))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(83, 83, 83))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(83, 83, 83))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(83, 83, 83))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(83, 83, 83))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(83, 83, 83))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(83, 83, 83))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(83, 83, 83))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(83, 83, 83))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.StreamModeButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.StreamModeButton.setFont(font)
        self.StreamModeButton.setStyleSheet("QPushButton {\n"
"  \n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #535353);\n"
"    color: rgba(200, 200, 200, 200);\n"
"    image-position:left;\n"
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
"    image-position: left;\n"
"    image: url(:/mytunefy/resources/icons/stream_light-grey.png);\n"
"    }\n"
"\n"
"QPushButton:hover:checked{\n"
"    color: white;\n"
"      background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    image-position: left;\n"
"    image: url(:/mytunefy/resources/icons/stream_light-grey.png);\n"
"    }\n"
"QPushButton:checked{\n"
"    color: red;\n"
"      background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    image-position: left;\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/stream_icon.png);\n"
"    }")
        self.StreamModeButton.setCheckable(True)
        self.StreamModeButton.setChecked(False)
        self.StreamModeButton.setDefault(False)
        self.StreamModeButton.setObjectName("StreamModeButton")
        self.verticalLayout_7.addWidget(self.StreamModeButton)
        self.pushButtonDownloader = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDownloader.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButtonDownloader.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonDownloader.setFont(font)
        self.pushButtonDownloader.setStyleSheet("QPushButton {\n"
"  \n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #535353);\n"
"    color: rgba(200, 200, 200, 200);\n"
"    image-position:left;\n"
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
"    image-position: left;\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/down_music_light_grey.png);\n"
"    }\n"
"")
        self.pushButtonDownloader.setObjectName("pushButtonDownloader")
        self.verticalLayout_7.addWidget(self.pushButtonDownloader)
        self.comboBoxCategory = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCategory.setMinimumSize(QtCore.QSize(220, 30))
        self.comboBoxCategory.setMaximumSize(QtCore.QSize(220, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 96, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 96, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 96, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 96, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 96, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 96, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 96, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 96, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 96, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.comboBoxCategory.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.comboBoxCategory.setFont(font)
        self.comboBoxCategory.setStyleSheet("QComboBox{\n"
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
        self.comboBoxCategory.setObjectName("comboBoxCategory")
        self.comboBoxCategory.addItem("")
        self.comboBoxCategory.addItem("")
        self.comboBoxCategory.addItem("")
        self.comboBoxCategory.addItem("")
        self.comboBoxCategory.addItem("")
        self.verticalLayout_7.addWidget(self.comboBoxCategory)
        self.verticalLayout_Library.addLayout(self.verticalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_Library.addItem(spacerItem3)
        self.label_library = QtWidgets.QLabel(self.centralwidget)
        self.label_library.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_library.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_library.setFont(font)
        self.label_library.setAlignment(QtCore.Qt.AlignCenter)
        self.label_library.setObjectName("label_library")
        self.verticalLayout_Library.addWidget(self.label_library)
        self.horizontalLayout_library = QtWidgets.QHBoxLayout()
        self.horizontalLayout_library.setContentsMargins(0, 5, -1, -1)
        self.horizontalLayout_library.setObjectName("horizontalLayout_library")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(245, 320))
        self.listWidget.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("QListView {\n"
"    background-color: rgb(15, 15, 15);\n"
"    color:  rgb(210, 210, 210);\n"
"    font-weight: bold;\n"
"\n"
"}")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_library.addWidget(self.listWidget)
        self.verticalLayout_Library.addLayout(self.horizontalLayout_library)
        self.newPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        self.newPlaylistButton.setEnabled(False)
        self.newPlaylistButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.newPlaylistButton.setFont(font)
        self.newPlaylistButton.setObjectName("newPlaylistButton")
        self.verticalLayout_Library.addWidget(self.newPlaylistButton)
        self.centralhorizontalLayout.addLayout(self.verticalLayout_Library)
        self.frame_songs = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_songs.sizePolicy().hasHeightForWidth())
        self.frame_songs.setSizePolicy(sizePolicy)
        self.frame_songs.setMinimumSize(QtCore.QSize(0, 450))
        self.frame_songs.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.frame_songs.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_songs.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_songs.setObjectName("frame_songs")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_songs)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playlist_label = QtWidgets.QLabel(self.frame_songs)
        self.playlist_label.setMinimumSize(QtCore.QSize(50, 35))
        self.playlist_label.setMaximumSize(QtCore.QSize(650, 45))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.playlist_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.playlist_label.setFont(font)
        self.playlist_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playlist_label.setObjectName("playlist_label")
        self.horizontalLayout.addWidget(self.playlist_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonPlaylist = QtWidgets.QPushButton(self.frame_songs)
        self.pushButtonPlaylist.setMinimumSize(QtCore.QSize(134, 45))
        self.pushButtonPlaylist.setMaximumSize(QtCore.QSize(140, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(37, 102, 255))
        gradient.setColorAt(1.0, QtGui.QColor(58, 147, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(37, 102, 255))
        gradient.setColorAt(1.0, QtGui.QColor(58, 147, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(37, 102, 255))
        gradient.setColorAt(1.0, QtGui.QColor(58, 147, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(37, 102, 255))
        gradient.setColorAt(1.0, QtGui.QColor(58, 147, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(37, 102, 255))
        gradient.setColorAt(1.0, QtGui.QColor(58, 147, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(37, 102, 255))
        gradient.setColorAt(1.0, QtGui.QColor(58, 147, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(37, 102, 255))
        gradient.setColorAt(1.0, QtGui.QColor(58, 147, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(37, 102, 255))
        gradient.setColorAt(1.0, QtGui.QColor(58, 147, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(37, 102, 255))
        gradient.setColorAt(1.0, QtGui.QColor(58, 147, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonPlaylist.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.pushButtonPlaylist.setFont(font)
        self.pushButtonPlaylist.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 22px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #2566ff, stop: 1 #3a93ff);\n"
"    color: #c8c8c8;\n"
"    min-width: 130px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        color: white;\n"
"}\n"
"")
        self.pushButtonPlaylist.setObjectName("pushButtonPlaylist")
        self.horizontalLayout.addWidget(self.pushButtonPlaylist)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.toolButtonPlaylist = QtWidgets.QToolButton(self.frame_songs)
        self.toolButtonPlaylist.setMinimumSize(QtCore.QSize(45, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.toolButtonPlaylist.setFont(font)
        self.toolButtonPlaylist.setStyleSheet("QToolButton{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.toolButtonPlaylist.setObjectName("toolButtonPlaylist")
        self.horizontalLayout.addWidget(self.toolButtonPlaylist)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_QTableView = QtWidgets.QVBoxLayout()
        self.verticalLayout_QTableView.setSpacing(10)
        self.verticalLayout_QTableView.setContentsMargins(10, 5, 0, 0)
        self.verticalLayout_QTableView.setObjectName("verticalLayout_QTableView")
        self.verticalLayout.addLayout(self.verticalLayout_QTableView)
        self.centralhorizontalLayout.addWidget(self.frame_songs)
        self.verticalLayout_2.addLayout(self.centralhorizontalLayout)
        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 115))
        self.frame_bottom.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout.setContentsMargins(10, 0, 1, 0)
        self.bottomLayout.setObjectName("bottomLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_bottom)
        self.frame_3.setMinimumSize(QtCore.QSize(260, 80))
        self.frame_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.song_name_label = QtWidgets.QLabel(self.frame_3)
        self.song_name_label.setMaximumSize(QtCore.QSize(350, 350))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.song_name_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.song_name_label.setFont(font)
        self.song_name_label.setStyleSheet("QLabel{\n"
"color: rgb(53, 66, 255);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.song_name_label.setText("")
        self.song_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.song_name_label.setObjectName("song_name_label")
        self.verticalLayout_5.addWidget(self.song_name_label)
        self.song_artist_label = QtWidgets.QLabel(self.frame_3)
        self.song_artist_label.setMaximumSize(QtCore.QSize(300, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 66, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.song_artist_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.song_artist_label.setFont(font)
        self.song_artist_label.setStyleSheet("QLabel{\n"
"color: rgb(53, 66, 160);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.song_artist_label.setText("")
        self.song_artist_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.song_artist_label.setObjectName("song_artist_label")
        self.verticalLayout_5.addWidget(self.song_artist_label)
        self.bottomLayout.addWidget(self.frame_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomLayout.addItem(spacerItem6)
        self.frame_control = QtWidgets.QFrame(self.frame_bottom)
        self.frame_control.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_control.setMaximumSize(QtCore.QSize(16777215, 115))
        self.frame_control.setStyleSheet("")
        self.frame_control.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_control.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_control.setObjectName("frame_control")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(65, -1, 65, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.shuffleButton = QtWidgets.QPushButton(self.frame_control)
        self.shuffleButton.setMinimumSize(QtCore.QSize(25, 25))
        self.shuffleButton.setMaximumSize(QtCore.QSize(27, 27))
        self.shuffleButton.setStyleSheet("QPushButton {\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/shuffle-darker-grey.png);\n"
"  \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    image: url(:/mytunefy/resources/icons/shuffle-azul-grey.png);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        \n"
"    image: url(:/mytunefy/resources/icons/shuffle-light-grey.png);\n"
"}\n"
"QPushButton:checked{\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/shuffle-green-grey.png);\n"
"}")
        self.shuffleButton.setText("")
        self.shuffleButton.setIconSize(QtCore.QSize(25, 18))
        self.shuffleButton.setCheckable(True)
        self.shuffleButton.setChecked(False)
        self.shuffleButton.setFlat(True)
        self.shuffleButton.setObjectName("shuffleButton")
        self.horizontalLayout_4.addWidget(self.shuffleButton)
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.backTrackButton = QtWidgets.QPushButton(self.frame_control)
        self.backTrackButton.setMinimumSize(QtCore.QSize(35, 35))
        self.backTrackButton.setMaximumSize(QtCore.QSize(35, 35))
        self.backTrackButton.setAutoFillBackground(False)
        self.backTrackButton.setStyleSheet("QPushButton {\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/backtrack4.png);\n"
"}\n"
"QPushButton:pressed:hover {\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/backtrack4.png);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        \n"
"    image: url(:/mytunefy/resources/icons/backtrack5.png);\n"
"}\n"
"")
        self.backTrackButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/spotify/resources/icons/backtrack3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backTrackButton.setIcon(icon1)
        self.backTrackButton.setIconSize(QtCore.QSize(30, 30))
        self.backTrackButton.setCheckable(True)
        self.backTrackButton.setFlat(True)
        self.backTrackButton.setObjectName("backTrackButton")
        self.horizontalLayout_4.addWidget(self.backTrackButton)
        spacerItem8 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.PlayPauseButton = QtWidgets.QPushButton(self.frame_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayPauseButton.sizePolicy().hasHeightForWidth())
        self.PlayPauseButton.setSizePolicy(sizePolicy)
        self.PlayPauseButton.setMinimumSize(QtCore.QSize(45, 45))
        self.PlayPauseButton.setMaximumSize(QtCore.QSize(45, 45))
        self.PlayPauseButton.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(40, 40, 40);\n"
"    \n"
"    \n"
"    image: url(:/mytunefy/resources/icons/play_grey.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    image: url(:/mytunefy/resources/icons/pause-butt.png);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"QPushButton:hover{\n"
"        \n"
"    image: url(:/mytunefy/resources/icons/play_white.png);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"image: url(:/mytunefy/resources/icons/pause2.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover:checked{\n"
"image: url(:/mytunefy/resources/icons/pause-light-grey.png);\n"
"} \n"
"")
        self.PlayPauseButton.setText("")
        self.PlayPauseButton.setIconSize(QtCore.QSize(35, 35))
        self.PlayPauseButton.setCheckable(True)
        self.PlayPauseButton.setChecked(False)
        self.PlayPauseButton.setAutoExclusive(False)
        self.PlayPauseButton.setFlat(True)
        self.PlayPauseButton.setObjectName("PlayPauseButton")
        self.horizontalLayout_4.addWidget(self.PlayPauseButton)
        spacerItem9 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.nextTrackButton = QtWidgets.QPushButton(self.frame_control)
        self.nextTrackButton.setMinimumSize(QtCore.QSize(35, 35))
        self.nextTrackButton.setMaximumSize(QtCore.QSize(35, 35))
        self.nextTrackButton.setStyleSheet("QPushButton {\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/next-darker-grey.png);\n"
"}\n"
"QPushButton:pressed:hover {\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/next-darker-grey.png);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        \n"
"    image: url(:/mytunefy/resources/icons/next-light-grey.png);\n"
"}\n"
"")
        self.nextTrackButton.setText("")
        self.nextTrackButton.setIconSize(QtCore.QSize(30, 30))
        self.nextTrackButton.setCheckable(True)
        self.nextTrackButton.setFlat(True)
        self.nextTrackButton.setObjectName("nextTrackButton")
        self.horizontalLayout_4.addWidget(self.nextTrackButton)
        spacerItem10 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.repeatButton = QtWidgets.QPushButton(self.frame_control)
        self.repeatButton.setMinimumSize(QtCore.QSize(25, 25))
        self.repeatButton.setMaximumSize(QtCore.QSize(25, 25))
        self.repeatButton.setAutoFillBackground(False)
        self.repeatButton.setStyleSheet("QPushButton {\n"
"    \n"
"    image: url(:/mytunefy/resources/icons/repeat-track-dark-grey.png);\n"
"  \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        \n"
"    image: url(:/mytunefy/resources/icons/repeat-track-light-grey.png);\n"
"}\n"
"QPushButton:checked{\n"
"image: url(:/mytunefy/resources/icons/repeat-track-green.png);\n"
"}")
        self.repeatButton.setText("")
        self.repeatButton.setIconSize(QtCore.QSize(25, 20))
        self.repeatButton.setCheckable(True)
        self.repeatButton.setFlat(True)
        self.repeatButton.setObjectName("repeatButton")
        self.horizontalLayout_4.addWidget(self.repeatButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalSlider = QtWidgets.QSlider(self.frame_control)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 30))
        self.horizontalSlider.setStyleSheet("QSlider {\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 8px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.bottomLayout.addWidget(self.frame_control)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomLayout.addItem(spacerItem11)
        self.frame_2 = QtWidgets.QFrame(self.frame_bottom)
        self.frame_2.setMinimumSize(QtCore.QSize(125, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_2.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"background-color: rgb(40, 40, 40);\n"
"background-image: url(:/spotify/resources/icons/play-red.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(0, 5, 5, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.IconLogo = QtWidgets.QLabel(self.frame_2)
        self.IconLogo.setMaximumSize(QtCore.QSize(60, 60))
        self.IconLogo.setText("")
        self.IconLogo.setPixmap(QtGui.QPixmap(":/mytunefy/resources/icons/cuffie-azul.png"))
        self.IconLogo.setScaledContents(True)
        self.IconLogo.setObjectName("IconLogo")
        self.horizontalLayout_5.addWidget(self.IconLogo)
        self.verticalSlider = QtWidgets.QSlider(self.frame_2)
        self.verticalSlider.setStyleSheet("QSlider {\n"
"    min-height: 90px;\n"
"    max-height: 90px;\n"
"}\n"
"QSlider::handle:vertiical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::groove:vertical { \n"
"    background: black;\n"
"    border: 2px solid #424242; \n"
"    height: 70px; \n"
"    width: 6px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_5.addWidget(self.verticalSlider)
        self.bottomLayout.addWidget(self.frame_2)
        self.horizontalLayout_6.addLayout(self.bottomLayout)
        self.verticalLayout_2.addWidget(self.frame_bottom)
        PlayerMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlayerMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayerMainWindow)

    def retranslateUi(self, PlayerMainWindow):
        PlayerMainWindow.setWindowTitle(QtWidgets.QApplication.translate("PlayerMainWindow", "MyTuneFy Player", None, -1))
        self.toolButtonGeneral.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "...", None, -1))
        self.FolderButton.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "PushButton", None, -1))
        self.pushButton.setStatusTip(QtWidgets.QApplication.translate("PlayerMainWindow", "Impostazioni", None, -1))
        self.label_User.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "User Name", None, -1))
        self.StreamModeButton.setStatusTip(QtWidgets.QApplication.translate("PlayerMainWindow", "Play streaming quando la canzone non si trova nella cartella locale", None, -1))
        self.StreamModeButton.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "Streaming Music", None, -1))
        self.pushButtonDownloader.setStatusTip(QtWidgets.QApplication.translate("PlayerMainWindow", "Scarica Musica", None, -1))
        self.pushButtonDownloader.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "Download", None, -1))
        self.comboBoxCategory.setCurrentText(QtWidgets.QApplication.translate("PlayerMainWindow", "Playlist", None, -1))
        self.comboBoxCategory.setItemText(0, QtWidgets.QApplication.translate("PlayerMainWindow", "Playlist", None, -1))
        self.comboBoxCategory.setItemText(1, QtWidgets.QApplication.translate("PlayerMainWindow", "Album", None, -1))
        self.comboBoxCategory.setItemText(2, QtWidgets.QApplication.translate("PlayerMainWindow", "Artista", None, -1))
        self.comboBoxCategory.setItemText(3, QtWidgets.QApplication.translate("PlayerMainWindow", "Brani", None, -1))
        self.comboBoxCategory.setItemText(4, QtWidgets.QApplication.translate("PlayerMainWindow", "Cartella", None, -1))
        self.label_library.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "La Tua Libreria", None, -1))
        self.newPlaylistButton.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "Nuova playlist", None, -1))
        self.playlist_label.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "Playlist name", None, -1))
        self.pushButtonPlaylist.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "Play", None, -1))
        self.toolButtonPlaylist.setText(QtWidgets.QApplication.translate("PlayerMainWindow", "...", None, -1))

from .import icons_rc
