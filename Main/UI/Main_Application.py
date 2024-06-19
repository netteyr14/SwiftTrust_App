# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Application.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import all_images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(759, 773)
        icon = QIcon()
        icon.addFile(u":/Main/window_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #040f13;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/Bg/title.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.side_menu = QFrame(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(200, 0))
        self.side_menu.setStyleSheet(u"#side_menu{\n"
"	background-color: #071e26;\n"
"	border-radius: 20px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.pbtn_widthdraw = QPushButton(self.frame_4)
        self.pbtn_widthdraw.setObjectName(u"pbtn_widthdraw")
        font = QFont()
        font.setFamilies([u"Cascadia Mono"])
        self.pbtn_widthdraw.setFont(font)
        self.pbtn_widthdraw.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(249, 191, 73);\n"
"	color: rgb(4, 15, 19);	\n"
"	icon: url(:/Feather-Blue/feather_blue/dollar-sign.svg);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Feather-Icons/feather/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_widthdraw.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.pbtn_widthdraw)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pbtn_deposit = QPushButton(self.frame_4)
        self.pbtn_deposit.setObjectName(u"pbtn_deposit")
        self.pbtn_deposit.setFont(font)
        self.pbtn_deposit.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(249, 191, 73);\n"
"	color: rgb(4, 15, 19);	\n"
"	icon: url(:/Feather-Blue/feather_blue/archive.svg);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Feather-Icons/feather/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_deposit.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.pbtn_deposit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pbtn_accBal = QPushButton(self.frame_4)
        self.pbtn_accBal.setObjectName(u"pbtn_accBal")
        self.pbtn_accBal.setFont(font)
        self.pbtn_accBal.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(249, 191, 73);\n"
"	color: rgb(4, 15, 19);	\n"
"	icon: url(:/Feather-Blue/feather_blue/pocket.svg);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Feather-Icons/feather/pocket.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_accBal.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.pbtn_accBal)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.pbtn_transBal = QPushButton(self.frame_4)
        self.pbtn_transBal.setObjectName(u"pbtn_transBal")
        self.pbtn_transBal.setFont(font)
        self.pbtn_transBal.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(249, 191, 73);\n"
"	color: rgb(4, 15, 19);	\n"
"	icon: url(:/Feather-Blue/feather_blue/users.svg);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Feather-Icons/feather/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_transBal.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.pbtn_transBal)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)

        self.pbtn_LOGOUT = QPushButton(self.frame_4)
        self.pbtn_LOGOUT.setObjectName(u"pbtn_LOGOUT")
        self.pbtn_LOGOUT.setFont(font)
        self.pbtn_LOGOUT.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(221, 0, 49);\n"
"	color: rgb(4, 15, 19);	\n"
"	icon: url(:/Feather-Blue/feather_blue/archive.svg);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(221, 96, 98);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Feather-Icons/feather/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_LOGOUT.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.pbtn_LOGOUT)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.side_menu)

        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setFont(font)
        self.main_body.setStyleSheet(u"#main_body{\n"
"	background-color: #071e26;\n"
"	border-radius: 10px;\n"
"}")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.main_body)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_3 = QGroupBox(self.main_body)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;")
        self.gridLayout_16 = QGridLayout(self.groupBox_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.keypad_3 = QPushButton(self.groupBox_3)
        self.keypad_3.setObjectName(u"keypad_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.keypad_3.sizePolicy().hasHeightForWidth())
        self.keypad_3.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Cascadia Mono"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.keypad_3.setFont(font1)
        self.keypad_3.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_3, 0, 2, 1, 1)

        self.keypad_1 = QPushButton(self.groupBox_3)
        self.keypad_1.setObjectName(u"keypad_1")
        sizePolicy2.setHeightForWidth(self.keypad_1.sizePolicy().hasHeightForWidth())
        self.keypad_1.setSizePolicy(sizePolicy2)
        self.keypad_1.setFont(font1)
        self.keypad_1.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_1, 0, 0, 1, 1)

        self.keypad_9 = QPushButton(self.groupBox_3)
        self.keypad_9.setObjectName(u"keypad_9")
        sizePolicy2.setHeightForWidth(self.keypad_9.sizePolicy().hasHeightForWidth())
        self.keypad_9.setSizePolicy(sizePolicy2)
        self.keypad_9.setFont(font1)
        self.keypad_9.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_9, 2, 2, 1, 1)

        self.keypad_4 = QPushButton(self.groupBox_3)
        self.keypad_4.setObjectName(u"keypad_4")
        sizePolicy2.setHeightForWidth(self.keypad_4.sizePolicy().hasHeightForWidth())
        self.keypad_4.setSizePolicy(sizePolicy2)
        self.keypad_4.setFont(font1)
        self.keypad_4.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_4, 1, 0, 1, 1)

        self.keypad_10 = QPushButton(self.groupBox_3)
        self.keypad_10.setObjectName(u"keypad_10")
        sizePolicy2.setHeightForWidth(self.keypad_10.sizePolicy().hasHeightForWidth())
        self.keypad_10.setSizePolicy(sizePolicy2)
        self.keypad_10.setFont(font1)
        self.keypad_10.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_10, 3, 1, 1, 1)

        self.keypad_8 = QPushButton(self.groupBox_3)
        self.keypad_8.setObjectName(u"keypad_8")
        sizePolicy2.setHeightForWidth(self.keypad_8.sizePolicy().hasHeightForWidth())
        self.keypad_8.setSizePolicy(sizePolicy2)
        self.keypad_8.setFont(font1)
        self.keypad_8.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_8, 2, 1, 1, 1)

        self.keypad_2 = QPushButton(self.groupBox_3)
        self.keypad_2.setObjectName(u"keypad_2")
        sizePolicy2.setHeightForWidth(self.keypad_2.sizePolicy().hasHeightForWidth())
        self.keypad_2.setSizePolicy(sizePolicy2)
        self.keypad_2.setFont(font1)
        self.keypad_2.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_2, 0, 1, 1, 1)

        self.keypad_5 = QPushButton(self.groupBox_3)
        self.keypad_5.setObjectName(u"keypad_5")
        sizePolicy2.setHeightForWidth(self.keypad_5.sizePolicy().hasHeightForWidth())
        self.keypad_5.setSizePolicy(sizePolicy2)
        self.keypad_5.setFont(font1)
        self.keypad_5.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_5, 1, 1, 1, 1)

        self.keypad_6 = QPushButton(self.groupBox_3)
        self.keypad_6.setObjectName(u"keypad_6")
        sizePolicy2.setHeightForWidth(self.keypad_6.sizePolicy().hasHeightForWidth())
        self.keypad_6.setSizePolicy(sizePolicy2)
        self.keypad_6.setFont(font1)
        self.keypad_6.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_6, 1, 2, 1, 1)

        self.keypad_7 = QPushButton(self.groupBox_3)
        self.keypad_7.setObjectName(u"keypad_7")
        sizePolicy2.setHeightForWidth(self.keypad_7.sizePolicy().hasHeightForWidth())
        self.keypad_7.setSizePolicy(sizePolicy2)
        self.keypad_7.setFont(font1)
        self.keypad_7.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(249, 190, 74);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 109, 109);\n"
"	color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_16.addWidget(self.keypad_7, 2, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.receipt_window = QWidget()
        self.receipt_window.setObjectName(u"receipt_window")
        self.gridLayout_14 = QGridLayout(self.receipt_window)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox_8 = QGroupBox(self.receipt_window)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_13 = QGridLayout(self.groupBox_8)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_9 = QFrame(self.groupBox_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.receipt_output = QLabel(self.frame_9)
        self.receipt_output.setObjectName(u"receipt_output")
        self.receipt_output.setFont(font1)
        self.receipt_output.setStyleSheet(u"color: rgb(70, 70, 70);\n"
"background-color: rgb(185, 185, 185);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;")
        self.receipt_output.setFrameShape(QFrame.Box)
        self.receipt_output.setFrameShadow(QFrame.Raised)
        self.receipt_output.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.receipt_output.setMargin(10)

        self.gridLayout_4.addWidget(self.receipt_output, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_9, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.frame = QFrame(self.receipt_window)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.non_clear = QPushButton(self.frame)
        self.non_clear.setObjectName(u"non_clear")
        sizePolicy2.setHeightForWidth(self.non_clear.sizePolicy().hasHeightForWidth())
        self.non_clear.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Cascadia Mono"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.non_clear.setFont(font2)
        self.non_clear.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(250, 191, 73);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(250, 208, 83);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.non_clear)

        self.no_delete = QPushButton(self.frame)
        self.no_delete.setObjectName(u"no_delete")
        sizePolicy2.setHeightForWidth(self.no_delete.sizePolicy().hasHeightForWidth())
        self.no_delete.setSizePolicy(sizePolicy2)
        self.no_delete.setFont(font1)
        self.no_delete.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(239, 73, 88);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(239, 104, 113);\n"
"	color: rgb(0, 0, 0)\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Feather-Blue/feather_blue/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.no_delete.setIcon(icon6)
        self.no_delete.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.no_delete)

        self.non_submit = QPushButton(self.frame)
        self.non_submit.setObjectName(u"non_submit")
        sizePolicy2.setHeightForWidth(self.non_submit.sizePolicy().hasHeightForWidth())
        self.non_submit.setSizePolicy(sizePolicy2)
        self.non_submit.setFont(font1)
        self.non_submit.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(41, 172, 59);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(50, 209, 71);\n"
"	color: rgb(0, 0, 0)\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Feather-Blue/feather_blue/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.non_submit.setIcon(icon7)
        self.non_submit.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.non_submit)


        self.gridLayout_14.addWidget(self.frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.receipt_window)
        self.withdrawals = QWidget()
        self.withdrawals.setObjectName(u"withdrawals")
        self.gridLayout_6 = QGridLayout(self.withdrawals)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_4 = QGroupBox(self.withdrawals)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.output_withdraw = QLabel(self.frame_5)
        self.output_withdraw.setObjectName(u"output_withdraw")
        font3 = QFont()
        font3.setFamilies([u"Cascadia Mono"])
        font3.setPointSize(40)
        font3.setBold(True)
        self.output_withdraw.setFont(font3)
        self.output_withdraw.setStyleSheet(u"color: rgb(70, 70, 70);\n"
"background-color: rgb(185, 185, 185);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;")
        self.output_withdraw.setFrameShape(QFrame.Box)
        self.output_withdraw.setFrameShadow(QFrame.Raised)
        self.output_withdraw.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.output_withdraw.setMargin(10)

        self.gridLayout_2.addWidget(self.output_withdraw, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.withdrawals)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 60))
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.clear_output_w = QPushButton(self.frame_7)
        self.clear_output_w.setObjectName(u"clear_output_w")
        sizePolicy2.setHeightForWidth(self.clear_output_w.sizePolicy().hasHeightForWidth())
        self.clear_output_w.setSizePolicy(sizePolicy2)
        self.clear_output_w.setFont(font2)
        self.clear_output_w.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(250, 191, 73);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(250, 208, 83);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.clear_output_w)

        self.delete_number_w = QPushButton(self.frame_7)
        self.delete_number_w.setObjectName(u"delete_number_w")
        sizePolicy2.setHeightForWidth(self.delete_number_w.sizePolicy().hasHeightForWidth())
        self.delete_number_w.setSizePolicy(sizePolicy2)
        self.delete_number_w.setFont(font1)
        self.delete_number_w.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(239, 73, 88);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(239, 104, 113);\n"
"	color: rgb(0, 0, 0)\n"
"}")
        self.delete_number_w.setIcon(icon6)
        self.delete_number_w.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.delete_number_w)

        self.submit_output_w = QPushButton(self.frame_7)
        self.submit_output_w.setObjectName(u"submit_output_w")
        sizePolicy2.setHeightForWidth(self.submit_output_w.sizePolicy().hasHeightForWidth())
        self.submit_output_w.setSizePolicy(sizePolicy2)
        self.submit_output_w.setFont(font1)
        self.submit_output_w.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(41, 172, 59);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(50, 209, 71);\n"
"	color: rgb(0, 0, 0)\n"
"}")
        self.submit_output_w.setIcon(icon7)
        self.submit_output_w.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.submit_output_w)


        self.gridLayout_6.addWidget(self.frame_7, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.withdrawals)
        self.deposits = QWidget()
        self.deposits.setObjectName(u"deposits")
        self.gridLayout_12 = QGridLayout(self.deposits)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_5 = QGroupBox(self.deposits)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_10 = QGridLayout(self.groupBox_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_6 = QFrame(self.groupBox_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.output_deposit = QLabel(self.frame_6)
        self.output_deposit.setObjectName(u"output_deposit")
        self.output_deposit.setFont(font3)
        self.output_deposit.setStyleSheet(u"color: rgb(70, 70, 70);\n"
"background-color: rgb(185, 185, 185);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;")
        self.output_deposit.setFrameShape(QFrame.Box)
        self.output_deposit.setFrameShadow(QFrame.Raised)
        self.output_deposit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.output_deposit.setMargin(10)

        self.gridLayout_11.addWidget(self.output_deposit, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_6, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.deposits)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 60))
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.clear_output_d = QPushButton(self.frame_10)
        self.clear_output_d.setObjectName(u"clear_output_d")
        sizePolicy2.setHeightForWidth(self.clear_output_d.sizePolicy().hasHeightForWidth())
        self.clear_output_d.setSizePolicy(sizePolicy2)
        self.clear_output_d.setFont(font2)
        self.clear_output_d.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(250, 191, 73);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(250, 208, 83);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_5.addWidget(self.clear_output_d)

        self.delete_number_d = QPushButton(self.frame_10)
        self.delete_number_d.setObjectName(u"delete_number_d")
        sizePolicy2.setHeightForWidth(self.delete_number_d.sizePolicy().hasHeightForWidth())
        self.delete_number_d.setSizePolicy(sizePolicy2)
        self.delete_number_d.setFont(font1)
        self.delete_number_d.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(239, 73, 88);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(239, 104, 113);\n"
"	color: rgb(0, 0, 0)\n"
"}")
        self.delete_number_d.setIcon(icon6)
        self.delete_number_d.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.delete_number_d)

        self.submit_output_d = QPushButton(self.frame_10)
        self.submit_output_d.setObjectName(u"submit_output_d")
        sizePolicy2.setHeightForWidth(self.submit_output_d.sizePolicy().hasHeightForWidth())
        self.submit_output_d.setSizePolicy(sizePolicy2)
        self.submit_output_d.setFont(font1)
        self.submit_output_d.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(41, 172, 59);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(50, 209, 71);\n"
"	color: rgb(0, 0, 0)\n"
"}")
        self.submit_output_d.setIcon(icon7)
        self.submit_output_d.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.submit_output_d)


        self.gridLayout_12.addWidget(self.frame_10, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.deposits)
        self.acc_bal = QWidget()
        self.acc_bal.setObjectName(u"acc_bal")
        self.gridLayout_7 = QGridLayout(self.acc_bal)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_6 = QGroupBox(self.acc_bal)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.groupBox_6)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.FieldRole, self.verticalSpacer_12)

        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/Feather-Icons/feather/user-check.svg"))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.user_name = QLabel(self.groupBox_6)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setFont(font1)
        self.user_name.setStyleSheet(u"QLabel{\n"
"	padding: 10px;\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.user_name)

        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/Feather-Icons/feather/gitlab.svg"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.unique_id = QLabel(self.groupBox_6)
        self.unique_id.setObjectName(u"unique_id")
        self.unique_id.setFont(font1)
        self.unique_id.setStyleSheet(u"QLabel{\n"
"	padding: 10px;\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.unique_id)

        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/Feather-Icons/feather/credit-card.svg"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.current_balance = QLabel(self.groupBox_6)
        self.current_balance.setObjectName(u"current_balance")
        self.current_balance.setFont(font1)
        self.current_balance.setStyleSheet(u"QLabel{\n"
"	padding: 10px;\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.current_balance)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_13)


        self.gridLayout_7.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.acc_bal)
        self.trans_bal = QWidget()
        self.trans_bal.setObjectName(u"trans_bal")
        self.gridLayout_8 = QGridLayout(self.trans_bal)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_3 = QFrame(self.trans_bal)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clear_output_t = QPushButton(self.frame_3)
        self.clear_output_t.setObjectName(u"clear_output_t")
        sizePolicy2.setHeightForWidth(self.clear_output_t.sizePolicy().hasHeightForWidth())
        self.clear_output_t.setSizePolicy(sizePolicy2)
        self.clear_output_t.setFont(font2)
        self.clear_output_t.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(250, 191, 73);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(250, 208, 83);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.clear_output_t)

        self.delete_number_t = QPushButton(self.frame_3)
        self.delete_number_t.setObjectName(u"delete_number_t")
        sizePolicy2.setHeightForWidth(self.delete_number_t.sizePolicy().hasHeightForWidth())
        self.delete_number_t.setSizePolicy(sizePolicy2)
        self.delete_number_t.setFont(font1)
        self.delete_number_t.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(239, 73, 88);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(239, 104, 113);\n"
"	color: rgb(0, 0, 0)\n"
"}")
        self.delete_number_t.setIcon(icon6)
        self.delete_number_t.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.delete_number_t)

        self.submit_output_t = QPushButton(self.frame_3)
        self.submit_output_t.setObjectName(u"submit_output_t")
        sizePolicy2.setHeightForWidth(self.submit_output_t.sizePolicy().hasHeightForWidth())
        self.submit_output_t.setSizePolicy(sizePolicy2)
        self.submit_output_t.setFont(font1)
        self.submit_output_t.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(41, 172, 59);\n"
"	border-radius: 10px;\n"
"	color: rgb(56, 74, 81)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(50, 209, 71);\n"
"	color: rgb(0, 0, 0)\n"
"}")
        self.submit_output_t.setIcon(icon7)
        self.submit_output_t.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.submit_output_t)


        self.gridLayout_8.addWidget(self.frame_3, 3, 0, 1, 1)

        self.search_transac_id = QLineEdit(self.trans_bal)
        self.search_transac_id.setObjectName(u"search_transac_id")
        self.search_transac_id.setMinimumSize(QSize(0, 0))
        self.search_transac_id.setStyleSheet(u"border: 2px solid rgb(250, 191, 73);\n"
"border-radius: 10px;\n"
"background-color: rgb(4, 15, 19);")
        self.search_transac_id.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.search_transac_id, 1, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.trans_bal)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_3 = QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_8 = QFrame(self.groupBox_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.output_transfer = QLabel(self.frame_8)
        self.output_transfer.setObjectName(u"output_transfer")
        self.output_transfer.setFont(font3)
        self.output_transfer.setStyleSheet(u"color: rgb(70, 70, 70);\n"
"background-color: rgb(185, 185, 185);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;")
        self.output_transfer.setFrameShape(QFrame.Box)
        self.output_transfer.setFrameShadow(QFrame.Raised)
        self.output_transfer.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.output_transfer.setMargin(10)

        self.gridLayout_15.addWidget(self.output_transfer, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_8, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.trans_bal)

        self.gridLayout_9.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        self.lb_message = QLabel(self.centralwidget)
        self.lb_message.setObjectName(u"lb_message")

        self.verticalLayout.addWidget(self.lb_message)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SwiftTrust - Dashboard", None))
        self.groupBox.setTitle("")
        self.label.setText("")
        self.pbtn_widthdraw.setText(QCoreApplication.translate("MainWindow", u"Withdrawals     ", None))
        self.pbtn_deposit.setText(QCoreApplication.translate("MainWindow", u"Deposits        ", None))
        self.pbtn_accBal.setText(QCoreApplication.translate("MainWindow", u"Account         ", None))
        self.pbtn_transBal.setText(QCoreApplication.translate("MainWindow", u"Transfer Balance", None))
        self.pbtn_LOGOUT.setText(QCoreApplication.translate("MainWindow", u"LOGOUT          ", None))
        self.groupBox_3.setTitle("")
        self.keypad_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.keypad_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.keypad_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.keypad_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.keypad_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.keypad_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.keypad_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.keypad_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.keypad_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.keypad_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Receipt Window", None))
        self.receipt_output.setText("")
        self.non_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.no_delete.setText("")
        self.non_submit.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Withdrawals", None))
        self.output_withdraw.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clear_output_w.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.delete_number_w.setText("")
        self.submit_output_w.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Deposits", None))
        self.output_deposit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clear_output_d.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.delete_number_d.setText("")
        self.submit_output_d.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_4.setText("")
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.label_6.setText("")
        self.unique_id.setText(QCoreApplication.translate("MainWindow", u"Unique ID:", None))
        self.label_5.setText("")
        self.current_balance.setText(QCoreApplication.translate("MainWindow", u"Current Balance:", None))
        self.clear_output_t.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.delete_number_t.setText("")
        self.submit_output_t.setText("")
        self.search_transac_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Here:", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Transfer Balance", None))
        self.output_transfer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_message.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
    # retranslateUi

