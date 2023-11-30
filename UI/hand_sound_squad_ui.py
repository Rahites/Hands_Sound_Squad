# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hand_sound_squad.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, QTimer, Qt)
from PySide6.QtGui import (QFont, QFontDatabase, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QProgressBar,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox)
import icons_rc
from predict_coordinate import predict_word
from predict_josa import JOSA, tts

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Left_menu = QWidget(self.centralwidget)
        self.Left_menu.setObjectName(u"Left_menu")
        self.Left_menu.setEnabled(True)
        self.Left_menu.setMinimumSize(QSize(200, 0))
        self.Left_menu.setMaximumSize(QSize(200, 16777215))
        self.Left_menu.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.Left_menu.setHidden(True)
        self.gridLayout_22 = QGridLayout(self.Left_menu)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(-1, 30, -1, 30)
        self._3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self._3, 4, 0, 1, 1)

        self.Home_btn = QToolButton(self.Left_menu)
        self.Home_btn.setObjectName(u"Home_btn")
        self.Home_btn.setMinimumSize(QSize(0, 50))
        self.Home_btn.setMaximumSize(QSize(150, 50))
        self.Home_btn.setLayoutDirection(Qt.LeftToRight)
        self.Home_btn.setStyleSheet(u"QToolButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	border-radius: 9px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/w_home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home_btn.setIcon(icon)
        self.Home_btn.setIconSize(QSize(22, 22))

        self.gridLayout_22.addWidget(self.Home_btn, 0, 0, 1, 1)

        self.FullS_btn = QToolButton(self.Left_menu)
        self.FullS_btn.setObjectName(u"FullS_btn")
        self.FullS_btn.setMinimumSize(QSize(0, 50))
        self.FullS_btn.setMaximumSize(QSize(150, 50))
        self.FullS_btn.setStyleSheet(u"QToolButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 9px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/pp_zoomin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FullS_btn.setIcon(icon1)
        self.FullS_btn.setIconSize(QSize(22, 22))

        self.gridLayout_22.addWidget(self.FullS_btn, 1, 0, 1, 1)

        self.NormS_btn = QToolButton(self.Left_menu)
        self.NormS_btn.setObjectName(u"NormS_btn")
        self.NormS_btn.setMinimumSize(QSize(0, 50))
        self.NormS_btn.setMaximumSize(QSize(150, 50))
        self.NormS_btn.setStyleSheet(u"QToolButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 9px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/pp_zoomout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NormS_btn.setIcon(icon2)
        self.NormS_btn.setIconSize(QSize(22, 22))

        self.gridLayout_22.addWidget(self.NormS_btn, 2, 0, 1, 1)

        self.Close_btn = QToolButton(self.Left_menu)
        self.Close_btn.setObjectName(u"Close_btn")
        self.Close_btn.setMinimumSize(QSize(0, 50))
        self.Close_btn.setMaximumSize(QSize(150, 50))
        self.Close_btn.setStyleSheet(u"QToolButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 9px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/pp_exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_btn.setIcon(icon3)
        self.Close_btn.setIconSize(QSize(22, 22))

        self.gridLayout_22.addWidget(self.Close_btn, 5, 0, 1, 1)


        self.horizontalLayout.addWidget(self.Left_menu)

        self.Main_board = QWidget(self.centralwidget)
        self.Main_board.setObjectName(u"Main_board")
        self.Main_board.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.Main_board)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QWidget(self.Main_board)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 136))
        self.Header.setMaximumSize(QSize(16777215, 136))
        self.Header.setStyleSheet(u"QWidget{\n"
"	border-bottom: 6px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(249, 249, 249, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, -1, 30, 15)
        self.Menu_btn = QToolButton(self.Header)
        self.Menu_btn.setObjectName(u"Menu_btn")
        self.Menu_btn.setMinimumSize(QSize(90, 90))
        self.Menu_btn.setMaximumSize(QSize(90, 90))
        self.Menu_btn.setFocusPolicy(Qt.ClickFocus)
        self.Menu_btn.setStyleSheet(u"QToolButton{\n"
"	border: 6px solid;\n"
"	border-color: rgb(249, 249, 249);\n"
"	border-radius: 38px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/pp_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_btn.setIcon(icon4)
        self.Menu_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.Menu_btn)

        self._1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self._1)

        self.Title = QLabel(self.Header)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(760, 70))
        self.Title.setMaximumSize(QSize(760, 70))
        font_path = "./font/fizzy-soda.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.Title.setStyleSheet(u"QLabel{\n"
"	border-bottom: 0px solid;\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:550, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 36pt \"Fizzy Soda\";\n"
"}")
        self.Title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.User_btn = QToolButton(self.Header)
        self.User_btn.setObjectName(u"User_btn")
        self.User_btn.setMinimumSize(QSize(90, 90))
        self.User_btn.setMaximumSize(QSize(90, 90))
        self.User_btn.setStyleSheet(u"QToolButton{\n"
"	border: 6px solid;\n"
"	border-color: rgb(249, 249, 249);\n"
"	border-radius: 38px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/pp_user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.User_btn.setIcon(icon5)
        self.User_btn.setIconSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.User_btn)


        self.verticalLayout.addWidget(self.Header)

        self.All_pages = QStackedWidget(self.Main_board)
        self.All_pages.setObjectName(u"All_pages")
        self.All_pages.setStyleSheet(u"")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.verticalLayout_3 = QVBoxLayout(self.Page1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Middle1 = QWidget(self.Page1)
        self.Middle1.setObjectName(u"Middle1")
        self.Middle1.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.Middle1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, -1, 30, 0)
        self.Word_frm11 = QFrame(self.Middle1)
        self.Word_frm11.setObjectName(u"Word_frm11")
        self.Word_frm11.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 18px;\n"
"}")
        self.gridLayout = QGridLayout(self.Word_frm11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Word_wgt11 = QWidget(self.Word_frm11)
        self.Word_wgt11.setObjectName(u"Word_wgt11")
        self.Word_wgt11.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.gridLayout_16 = QGridLayout(self.Word_wgt11)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(-1, -1, -1, 21)
        self.Enter_btn1 = QToolButton(self.Word_wgt11)
        self.Enter_btn1.setObjectName(u"Enter_btn1")
        self.Enter_btn1.setMinimumSize(QSize(270, 270))
        self.Enter_btn1.setMaximumSize(QSize(270, 270))
        self.Enter_btn1.setFocusPolicy(Qt.ClickFocus)
        self.Enter_btn1.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.Enter_btn1.setStyleSheet(u"QToolButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 230));\n"
"	border-radius: 121px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/w_add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Enter_btn1.setIcon(icon6)
        self.Enter_btn1.setIconSize(QSize(100, 100))
        self.Enter_btn1.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout_16.addWidget(self.Enter_btn1, 1, 0, 1, 1)

        self.Label11 = QLabel(self.Word_wgt11)
        self.Label11.setObjectName(u"Label11")
        self.Label11.setMinimumSize(QSize(270, 50))
        self.Label11.setMaximumSize(QSize(270, 50))
        font_path = "./font/fizzy-soda.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.Label11.setStyleSheet(u"QLabel{\n"
"	border: 0px solid;\n"
"	color: qlineargradient(spread:pad, x1:30, y1:0.5, x2:150, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 18pt \"Fizzy Soda\";\n"
"}")
        self.Label11.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.Label11, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.Word_wgt11, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.Word_frm11)

        self._b11 = QWidget(self.Middle1)
        self._b11.setObjectName(u"_b11")
        self._b11.setMinimumSize(QSize(40, 0))
        self._b11.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self._b11)

        self.Word_frm12 = QFrame(self.Middle1)
        self.Word_frm12.setObjectName(u"Word_frm12")
        self.Word_frm12.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 18px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Word_frm12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Word_wgt12 = QWidget(self.Word_frm12)
        self.Word_wgt12.setObjectName(u"Word_wgt12")
        self.Word_wgt12.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.gridLayout_17 = QGridLayout(self.Word_wgt12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(-1, -1, -1, 21)
        self.Label12 = QLabel(self.Word_wgt12)
        self.Label12.setObjectName(u"Label12")
        self.Label12.setMinimumSize(QSize(270, 50))
        self.Label12.setMaximumSize(QSize(270, 50))
        font_path = "./font/fizzy-soda.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.Label12.setStyleSheet(u"QLabel{\n"
"	border: 0px solid;\n"
"	color: qlineargradient(spread:pad, x1:30, y1:0.5, x2:150, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 18pt \"Fizzy Soda\";\n"
"}")
        self.Label12.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.Label12, 0, 0, 1, 1)

        self.Enter_btn2 = QToolButton(self.Word_wgt12)
        self.Enter_btn2.setObjectName(u"Enter_btn2")
        self.Enter_btn2.setEnabled(True)
        self.Enter_btn2.setMinimumSize(QSize(270, 270))
        self.Enter_btn2.setMaximumSize(QSize(270, 270))
        self.Enter_btn2.setFocusPolicy(Qt.ClickFocus)
        self.Enter_btn2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Enter_btn2.setAutoFillBackground(False)
        self.Enter_btn2.setStyleSheet(u"QToolButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 121px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/pp_add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Enter_btn2.setIcon(icon7)
        self.Enter_btn2.setIconSize(QSize(100, 100))
        self.Enter_btn2.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout_17.addWidget(self.Enter_btn2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.Word_wgt12, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.Word_frm12)

        self._b12 = QWidget(self.Middle1)
        self._b12.setObjectName(u"_b12")
        self._b12.setMinimumSize(QSize(40, 0))
        self._b12.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self._b12)

        self.Word_frm13 = QFrame(self.Middle1)
        self.Word_frm13.setObjectName(u"Word_frm13")
        self.Word_frm13.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 18px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.Word_frm13)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Word_wgt13 = QWidget(self.Word_frm13)
        self.Word_wgt13.setObjectName(u"Word_wgt13")
        self.Word_wgt13.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.gridLayout_18 = QGridLayout(self.Word_wgt13)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(-1, -1, -1, 21)
        self.Label13 = QLabel(self.Word_wgt13)
        self.Label13.setObjectName(u"Label13")
        self.Label13.setMinimumSize(QSize(270, 50))
        self.Label13.setMaximumSize(QSize(270, 50))
        font_path = "./font/fizzy-soda.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.Label13.setStyleSheet(u"QLabel{\n"
"	border: 0px solid;\n"
"	color: qlineargradient(spread:pad, x1:30, y1:0.5, x2:150, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 18pt \"Fizzy Soda\";\n"
"}")
        self.Label13.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.Label13, 0, 0, 1, 1)

        self.Enter_btn3 = QToolButton(self.Word_wgt13)
        self.Enter_btn3.setObjectName(u"Enter_btn3")
        self.Enter_btn3.setMinimumSize(QSize(270, 270))
        self.Enter_btn3.setMaximumSize(QSize(270, 270))
        self.Enter_btn3.setFocusPolicy(Qt.ClickFocus)
        self.Enter_btn3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Enter_btn3.setStyleSheet(u"QToolButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 230));\n"
"	border-radius: 121px;\n"
"}")
        self.Enter_btn3.setIcon(icon6)
        self.Enter_btn3.setIconSize(QSize(100, 100))
        self.Enter_btn3.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout_18.addWidget(self.Enter_btn3, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.Word_wgt13, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.Word_frm13)


        self.verticalLayout_3.addWidget(self.Middle1)

        self.Bottom1 = QWidget(self.Page1)
        self.Bottom1.setObjectName(u"Bottom1")
        self.Bottom1.setMinimumSize(QSize(0, 160))
        self.Bottom1.setMaximumSize(QSize(16777215, 160))
        self.Bottom1.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.Bottom1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Predict_btn = QToolButton(self.Bottom1)
        self.Predict_btn.setObjectName(u"Predict_btn")
        self.Predict_btn.setMinimumSize(QSize(90, 90))
        self.Predict_btn.setMaximumSize(QSize(90, 90))
        font = QFont()
        font.setBold(False)
        self.Predict_btn.setFont(font)
        self.Predict_btn.setStyleSheet(u"QToolButton{\n"
"	border: 0px solid;\n"
"	border-color: rgb(247, 247, 247);\n"
"	border-radius: 38px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 240));\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/w_send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Predict_btn.setIcon(icon8)
        self.Predict_btn.setIconSize(QSize(45, 45))
        self.Predict_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout_4.addWidget(self.Predict_btn, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.Bottom1)

        self.All_pages.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.verticalLayout_4 = QVBoxLayout(self.Page2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Middle2 = QWidget(self.Page2)
        self.Middle2.setObjectName(u"Middle2")
        self.gridLayout_7 = QGridLayout(self.Middle2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(30, -1, 30, 0)
        self.Word_frm21 = QFrame(self.Middle2)
        self.Word_frm21.setObjectName(u"Word_frm21")
        self.Word_frm21.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 18px;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.Word_frm21)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.Word_wgt21 = QWidget(self.Word_frm21)
        self.Word_wgt21.setObjectName(u"Word_wgt21")
        self.Word_wgt21.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.gridLayout_19 = QGridLayout(self.Word_wgt21)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.Label21 = QLabel(self.Word_wgt21)
        self.Label21.setObjectName(u"Label21")
        self.Label21.setMinimumSize(QSize(270, 50))
        self.Label21.setMaximumSize(QSize(270, 50))
        font_path = "./font/fizzy-soda.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.Label21.setStyleSheet(u"QLabel{\n"
"	border: 0px solid;\n"
"	color: qlineargradient(spread:pad, x1:30, y1:0.5, x2:150, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 18pt \"Fizzy Soda\";\n"
"}")
        self.Label21.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.Label21, 0, 0, 1, 1)

        self.PWord_lb1 = QLabel(self.Word_wgt21)
        self.PWord_lb1.setObjectName(u"PWord_lb1")
        self.PWord_lb1.setMinimumSize(QSize(270, 270))
        self.PWord_lb1.setMaximumSize(QSize(270, 270))
        font_path = "./font/esamanru Bold.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.PWord_lb1.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 230));\n"
"	border-radius: 121px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 32pt \"\uc774\uc0ac\ub9cc\ub8e8\uccb4 Bold\";\n"
"}")
        self.PWord_lb1.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.PWord_lb1, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.Word_wgt21, 0, 0, 1, 1)

        self.Word_PBar1 = QProgressBar(self.Word_frm21)
        self.Word_PBar1.setObjectName(u"Word_PBar1")
        self.Word_PBar1.setMaximumSize(QSize(380, 7))
        self.Word_PBar1.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: rgb(255, 255, 255);\n"
"	text-align: center;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 230));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Word_PBar1.setTextVisible(False)

        self.gridLayout_8.addWidget(self.Word_PBar1, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.Word_frm21, 0, 0, 1, 1)

        self._b21 = QWidget(self.Middle2)
        self._b21.setObjectName(u"_b21")
        self._b21.setMinimumSize(QSize(40, 0))
        self._b21.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_7.addWidget(self._b21, 0, 1, 1, 1)

        self.Word_frm22 = QFrame(self.Middle2)
        self.Word_frm22.setObjectName(u"Word_frm22")
        self.Word_frm22.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 18px;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.Word_frm22)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Word_wgt22 = QWidget(self.Word_frm22)
        self.Word_wgt22.setObjectName(u"Word_wgt22")
        self.Word_wgt22.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.gridLayout_20 = QGridLayout(self.Word_wgt22)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.Label22 = QLabel(self.Word_wgt22)
        self.Label22.setObjectName(u"Label22")
        self.Label22.setMinimumSize(QSize(270, 50))
        self.Label22.setMaximumSize(QSize(270, 50))
        font_path = "./font/fizzy-soda.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.Label22.setStyleSheet(u"QLabel{\n"
"	border: 0px solid;\n"
"	color: qlineargradient(spread:pad, x1:30, y1:0.5, x2:150, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 18pt \"Fizzy Soda\";\n"
"}")
        self.Label22.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.Label22, 0, 0, 1, 1)

        self.PWord_lb2 = QLabel(self.Word_wgt22)
        self.PWord_lb2.setObjectName(u"PWord_lb2")
        self.PWord_lb2.setMinimumSize(QSize(270, 270))
        self.PWord_lb2.setMaximumSize(QSize(270, 270))
        font_path = "./font/esamanru Bold.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.PWord_lb2.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 121px;\n"
"	color: qlineargradient(spread:pad, x1:30, y1:0.5, x2:150, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 700 32pt \"\uc774\uc0ac\ub9cc\ub8e8\uccb4 Bold\";\n"
"}")
        self.PWord_lb2.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.PWord_lb2, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.Word_wgt22, 0, 0, 1, 1)

        self.Word_PBar2 = QProgressBar(self.Word_frm22)
        self.Word_PBar2.setObjectName(u"Word_PBar2")
        self.Word_PBar2.setMaximumSize(QSize(380, 7))
        self.Word_PBar2.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: rgb(255, 255, 255);\n"
"	text-align: center;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 230));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Word_PBar2.setTextVisible(False)

        self.gridLayout_6.addWidget(self.Word_PBar2, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.Word_frm22, 0, 2, 1, 1)

        self._b4 = QWidget(self.Middle2)
        self._b4.setObjectName(u"_b4")
        self._b4.setMinimumSize(QSize(40, 0))
        self._b4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_7.addWidget(self._b4, 0, 3, 1, 1)

        self.Word_frm23 = QFrame(self.Middle2)
        self.Word_frm23.setObjectName(u"Word_frm23")
        self.Word_frm23.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 18px;\n"
"}")
        self.gridLayout_9 = QGridLayout(self.Word_frm23)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Word_wgt23 = QWidget(self.Word_frm23)
        self.Word_wgt23.setObjectName(u"Word_wgt23")
        self.Word_wgt23.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.gridLayout_21 = QGridLayout(self.Word_wgt23)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.Label23 = QLabel(self.Word_wgt23)
        self.Label23.setObjectName(u"Label23")
        self.Label23.setMinimumSize(QSize(270, 50))
        self.Label23.setMaximumSize(QSize(270, 50))
        font_path = "./font/fizzy-soda.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.Label23.setStyleSheet(u"QLabel{\n"
"	border: 0px solid;\n"
"	color: qlineargradient(spread:pad, x1:30, y1:0.5, x2:150, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 18pt \"Fizzy Soda\";\n"
"}")
        self.Label23.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.Label23, 0, 0, 1, 1)

        self.PWord_lb3 = QLabel(self.Word_wgt23)
        self.PWord_lb3.setObjectName(u"PWord_lb3")
        self.PWord_lb3.setMinimumSize(QSize(270, 270))
        self.PWord_lb3.setMaximumSize(QSize(270, 270))
        font_path = "./font/esamanru Bold.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.PWord_lb3.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 230));\n"
"	border-radius: 121px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 32pt \"\uc774\uc0ac\ub9cc\ub8e8\uccb4 Bold\";\n"
"}")
        self.PWord_lb3.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.PWord_lb3, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.Word_wgt23, 0, 0, 1, 1)

        self.Word_PBar3 = QProgressBar(self.Word_frm23)
        self.Word_PBar3.setObjectName(u"Word_PBar3")
        self.Word_PBar3.setMaximumSize(QSize(380, 7))
        self.Word_PBar3.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: rgb(255, 255, 255);\n"
"	text-align: center;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 230));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Word_PBar3.setTextVisible(False)

        self.gridLayout_9.addWidget(self.Word_PBar3, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.Word_frm23, 0, 4, 1, 1)


        self.verticalLayout_4.addWidget(self.Middle2)

        self.Bottom2 = QWidget(self.Page2)
        self.Bottom2.setObjectName(u"Bottom2")
        self.Bottom2.setMinimumSize(QSize(0, 160))
        self.Bottom2.setMaximumSize(QSize(16777215, 160))
        self.gridLayout_10 = QGridLayout(self.Bottom2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.WtoS_btn = QToolButton(self.Bottom2)
        self.WtoS_btn.setObjectName(u"WtoS_btn")
        self.WtoS_btn.setMinimumSize(QSize(90, 90))
        self.WtoS_btn.setMaximumSize(QSize(90, 90))
        self.WtoS_btn.setStyleSheet(u"QToolButton{\n"
"	border: 0px solid;\n"
"	border-color: rgb(247, 247, 247);\n"
"	border-radius: 38px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 240));\n"
"}")
        self.WtoS_btn.setIcon(icon8)
        self.WtoS_btn.setIconSize(QSize(45, 45))

        self.gridLayout_10.addWidget(self.WtoS_btn, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.Bottom2)

        self.All_pages.addWidget(self.Page2)
        self.Page3 = QWidget()
        self.Page3.setObjectName(u"Page3")
        self.verticalLayout_2 = QVBoxLayout(self.Page3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Middle3 = QWidget(self.Page3)
        self.Middle3.setObjectName(u"Middle3")
        self.Middle3.setMinimumSize(QSize(0, 551))
        self.Middle3.setMaximumSize(QSize(16777215, 551))
        self.gridLayout_11 = QGridLayout(self.Middle3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(30, 4, 30, 0)
        self.Sentence_frm = QFrame(self.Middle3)
        self.Sentence_frm.setObjectName(u"Sentence_frm")
        self.Sentence_frm.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 17px;\n"
"}")
        self.Sentence_frm.setFrameShape(QFrame.StyledPanel)
        self.Sentence_frm.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.Sentence_frm)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.Sentence_wgt = QWidget(self.Sentence_frm)
        self.Sentence_wgt.setObjectName(u"Sentence_wgt")
        self.Sentence_wgt.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.gridLayout_14 = QGridLayout(self.Sentence_wgt)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.Sentence_lb = QLabel(self.Sentence_wgt)
        self.Sentence_lb.setObjectName(u"Sentence_lb")
        self.Sentence_lb.setMinimumSize(QSize(1100, 180))
        self.Sentence_lb.setMaximumSize(QSize(1300, 180))
        font_path = "./font/esamanru Bold.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.Sentence_lb.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 52px;\n"
"	color: qlineargradient(spread:pad, x1:200, y1:0.5, x2:1000, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 700 48pt \"\uc774\uc0ac\ub9cc\ub8e8\uccb4 Bold\";\n"
"}")
        self.Sentence_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.Sentence_lb, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.Sentence_wgt, 0, 0, 1, 1)

        self.Sentence_PBar = QProgressBar(self.Sentence_frm)
        self.Sentence_PBar.setObjectName(u"Sentence_PBar")
        self.Sentence_PBar.setMinimumSize(QSize(0, 7))
        self.Sentence_PBar.setMaximumSize(QSize(16777215, 7))
        self.Sentence_PBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: rgb(255, 255, 255);\n"
"	text-align: center;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 230));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Sentence_PBar.setValue(0)
        self.Sentence_PBar.setTextVisible(False)

        self.gridLayout_12.addWidget(self.Sentence_PBar, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.Sentence_frm, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.Middle3)

        self.Bottom3 = QWidget(self.Page3)
        self.Bottom3.setObjectName(u"Bottom3")
        self.Bottom3.setMinimumSize(QSize(0, 148))
        self.Bottom3.setMaximumSize(QSize(16777215, 148))
        self.horizontalLayout_3 = QHBoxLayout(self.Bottom3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, 0, 30, 0)
        self.BGroup1 = QWidget(self.Bottom3)
        self.BGroup1.setObjectName(u"BGroup1")
        self.BGroup1.setMaximumSize(QSize(16777215, 130))
        self.gridLayout_13 = QGridLayout(self.BGroup1)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(30, 30, 30, 30)

        self.horizontalLayout_3.addWidget(self.BGroup1)

        self.BGroup2 = QWidget(self.Bottom3)
        self.BGroup2.setObjectName(u"BGroup2")
        self.BGroup2.setMaximumSize(QSize(16777215, 130))
        self.gridLayout_15 = QGridLayout(self.BGroup2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(30, -1, 30, -1)
        self.Basic_Sound_btn = QToolButton(self.BGroup2)
        self.Basic_Sound_btn.setObjectName(u"Basic_Sound_btn")
        self.Basic_Sound_btn.setMinimumSize(QSize(90, 90))
        self.Basic_Sound_btn.setMaximumSize(QSize(90, 90))
        self.Basic_Sound_btn.setStyleSheet(u"QToolButton{\n"
"	border: 0px solid;\n"
"	border-color: rgb(250, 250, 250);\n"
"	border-radius: 38px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 5, 255, 240), stop:1 rgba(118, 44, 255, 240));\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/w_audio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Basic_Sound_btn.setIcon(icon9)
        self.Basic_Sound_btn.setIconSize(QSize(45, 45))

        self.gridLayout_15.addWidget(self.Basic_Sound_btn, 0, 1, 1, 1)

        self.Basic_Sound_lb = QLabel(self.BGroup2)
        self.Basic_Sound_lb.setObjectName(u"Basic_Sound_lb")
        font_path = "./font/esamanru Bold.ttf"
        QFontDatabase.addApplicationFont(font_path)
        self.Basic_Sound_lb.setStyleSheet(u"QLabel{\n"
"	color: qlineargradient(spread:pad, x1:30, y1:0.5, x2:150, y2:0.5, stop:0 rgba(63, 5, 255, 255), stop:1 rgba(118, 44, 255, 255));\n"
"	font: 700 26pt \"\uc774\uc0ac\ub9cc\ub8e8\uccb4 Bold\";\n"
"}")
        self.Basic_Sound_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.Basic_Sound_lb, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.BGroup2)

        self.BGroup3 = QWidget(self.Bottom3)
        self.BGroup3.setObjectName(u"BGroup3")
        self.BGroup3.setMaximumSize(QSize(16777215, 130))
        self.gridLayout_5 = QGridLayout(self.BGroup3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.horizontalLayout_3.addWidget(self.BGroup3)


        self.verticalLayout_2.addWidget(self.Bottom3)

        self.All_pages.addWidget(self.Page3)

        self.verticalLayout.addWidget(self.All_pages)


        self.horizontalLayout.addWidget(self.Main_board)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.FullS_btn.clicked.connect(MainWindow.showFullScreen)
        self.NormS_btn.clicked.connect(MainWindow.showNormal)
        self.Close_btn.clicked.connect(MainWindow.close)

        # 기능 추가
        # 메뉴
        self.Menu_btn.clicked.connect(self.show_menu)
        self.Home_btn.clicked.connect(self.to_firstpage)

        self.All_pages.setCurrentIndex(0)

        # 관절좌표 업로드
        self.word1 = None
        self.word2 = None
        self.word3 = None
        
        # 예측한 문장
        self.sentence = 'None'
        self.tts_path = None

        self.Enter_btn1.clicked.connect(self.upload_word1)
        self.Enter_btn2.clicked.connect(self.upload_word2)
        self.Enter_btn3.clicked.connect(self.upload_word3)

        # 단어 예측 버튼
        self.Predict_btn.clicked.connect(self.word_predict)

        # 문장화 버튼
        self.WtoS_btn.clicked.connect(self.josa_predict)

        QMetaObject.connectSlotsByName(MainWindow)
        
        # TTS 버튼
        self.Basic_Sound_btn.clicked.connect(self.playsound)

    # 메뉴
    def show_menu(self):
        if self.Left_menu.isHidden():
            return self.Left_menu.setVisible(True)
        else:
            return self.Left_menu.setHidden(True)

    # 처음으로 리셋
    def to_firstpage(self):
        W_add = QIcon()
        W_add.addFile(u":/icons/w_add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Enter_btn1.setIcon(W_add)
        self.Enter_btn1.setIconSize(QSize(100, 100))
        self.Enter_btn1.setToolButtonStyle(Qt.ToolButtonIconOnly)

        P_add = QIcon()
        P_add.addFile(u":/icons/pp_add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Enter_btn2.setIcon(P_add)
        self.Enter_btn2.setIconSize(QSize(100, 100))
        self.Enter_btn2.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.Enter_btn3.setIcon(W_add)
        self.Enter_btn3.setIconSize(QSize(100, 100))
        self.Enter_btn3.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.word1 = None
        self.word2 = None
        self.word3 = None

        self.Word_PBar1.setValue(0)
        self.Word_PBar2.setValue(0)
        self.Word_PBar3.setValue(0)

        self.PWord_lb1.setText("")
        self.PWord_lb2.setText("")
        self.PWord_lb3.setText("")

        self.Sentence_lb.setText("")

        return self.All_pages.setCurrentIndex(0)

    # 전처리 된 npy파일 업로드
    def upload_word1(self):
        self.word1 = QFileDialog.getOpenFileName()[0] # 업로드한 이미지 경로가 저장
        print('Word 1 Uploaded!!')
        print(self.word1)

        icon_Wchecked = QIcon()
        icon_Wchecked.addFile(u":/icons/w_checked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Enter_btn1.setIcon(icon_Wchecked)
        self.Enter_btn1.setIconSize(QSize(102, 102))
        self.Enter_btn1.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Enter_btn1.setAutoRaise(False)
        
    def upload_word2(self):
        self.word2 = QFileDialog.getOpenFileName()[0] # 업로드한 이미지 경로가 저장
        print('Word 2 Uploaded!!')
        print(self.word2)

        icon_Pchecked = QIcon()
        icon_Pchecked.addFile(u":/icons/pp_checked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Enter_btn2.setIcon(icon_Pchecked)
        self.Enter_btn2.setIconSize(QSize(100, 100))
        self.Enter_btn2.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Enter_btn2.setAutoRaise(False)
        
    def upload_word3(self):
        self.word3 = QFileDialog.getOpenFileName()[0] # 업로드한 이미지 경로가 저장
        print('Word 3 Uploaded!!')
        print(self.word3)

        icon_Wchecked = QIcon()
        icon_Wchecked.addFile(u":/icons/w_checked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Enter_btn3.setIcon(icon_Wchecked)
        self.Enter_btn3.setIconSize(QSize(102, 102))
        self.Enter_btn3.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Enter_btn3.setAutoRaise(False)

    def word_predict(self):
        print('Click Predict Button!!')
        
        if self.word1 is None and self.word2 is None and self.word3 is None:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("알림")
            msg_box.setText("NPY 파일을 먼저 넣어주세요!")
            msg_box.exec_()
            return    
                           
        elif self.word3 is None:
            self.All_pages.setCurrentIndex(1)

            self.predicted_word1 = predict_word('weight/LSTM_Attention_final_model.pth', self.word1, self.update_progress1)
            self.predicted_word2 = predict_word('weight/LSTM_Attention_final_model.pth', self.word2, self.update_progress2)
            self.predicted_word3 = None

            self.PWord_lb1.setText(f"{self.predicted_word1}")
            self.PWord_lb2.setText(f"{self.predicted_word2}")
            self.PWord_lb3.setText("")

            self.Word_PBar1.setValue(0)
            self.Word_PBar2.setValue(0)
            self.Word_PBar3.setValue(0)
            return
        
        elif self.word3 is not None:
            self.All_pages.setCurrentIndex(1)

            self.predicted_word1 = predict_word('weight/LSTM_Attention_final_model.pth', self.word1, self.update_progress1)
            self.predicted_word2 = predict_word('weight/LSTM_Attention_final_model.pth', self.word2, self.update_progress2)
            self.predicted_word3 = predict_word('weight/LSTM_Attention_final_model.pth', self.word3, self.update_progress3)
            
            self.PWord_lb1.setText(f"{self.predicted_word1}")
            self.PWord_lb2.setText(f"{self.predicted_word2}")
            self.PWord_lb3.setText(f"{self.predicted_word3}")

            self.Word_PBar1.setValue(0)
            self.Word_PBar2.setValue(0)
            self.Word_PBar3.setValue(0)
            return

    
    def update_progress1(self, value):
        self.Word_PBar1.setValue(int(value))

    def update_progress2(self, value):
        self.Word_PBar2.setValue(int(value))

    def update_progress3(self, value):
        self.Word_PBar3.setValue(int(value))

    def update_progress4(self, value):
        self.Sentence_PBar.setValue(int(value))

    def josa_predict(self):
        self.All_pages.setCurrentIndex(2)
        
        if self.predicted_word3 is None:
            self.sentence = JOSA([self.predicted_word1, self.predicted_word2], self.update_progress4)
        else:
            self.sentence = JOSA([self.predicted_word1, self.predicted_word2, self.predicted_word3], self.update_progress4)
        
        self.Sentence_lb.setText(self.sentence)
        self.Sentence_PBar.setValue(0)
        QTimer.singleShot(100, self.playsound)

    def playsound(self):
        # tts(f'./tts/{self.sentence}.mp3')
        tts(f'./tts/result.mp3')
    
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Home_btn.setText("")
        self.FullS_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.NormS_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Close_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Menu_btn.setText("")
        self.Title.setText(QCoreApplication.translate("MainWindow", u"HAND SOUND SQUAD", None))
        self.User_btn.setText("")
        self.Enter_btn1.setText("")
        self.Label11.setText(QCoreApplication.translate("MainWindow", u"1ST WORD", None))
        self.Label12.setText(QCoreApplication.translate("MainWindow", u"2ND WORD", None))
        self.Enter_btn2.setText("")
        self.Label13.setText(QCoreApplication.translate("MainWindow", u"3RD WORD", None))
        self.Enter_btn3.setText("")
        self.Predict_btn.setText("")
        self.Label21.setText(QCoreApplication.translate("MainWindow", u"1ST WORD", None))
        self.PWord_lb1.setText("")
        self.Label22.setText(QCoreApplication.translate("MainWindow", u"2ND WORD", None))
        self.PWord_lb2.setText("")
        self.Label23.setText(QCoreApplication.translate("MainWindow", u"3RD WORD", None))
        self.WtoS_btn.setText("")
        self.Sentence_lb.setText("")
        self.Basic_Sound_btn.setText("")
        self.Basic_Sound_lb.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
    # retranslateUi

