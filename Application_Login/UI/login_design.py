# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_design.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import all_images_rc

class Ui_w_LoginForm(object):
    def setupUi(self, w_LoginForm):
        if not w_LoginForm.objectName():
            w_LoginForm.setObjectName(u"w_LoginForm")
        w_LoginForm.resize(771, 484)
        icon = QIcon()
        icon.addFile(u":/Main/window_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        w_LoginForm.setWindowIcon(icon)
        w_LoginForm.setWindowOpacity(2.000000000000000)
        w_LoginForm.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(83, 83, 83);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(w_LoginForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 6, 1, 1, 2)

        self.groupBox_2 = QGroupBox(w_LoginForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"border: 0;\n"
"background: transparent;")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/Bg/title.png"))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 5, 1, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 4, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 10, 1, 1, 2)

        self.lb_message = QLabel(w_LoginForm)
        self.lb_message.setObjectName(u"lb_message")
        self.lb_message.setEnabled(True)
        self.lb_message.setStyleSheet(u"color: rgb(98, 255, 90);\n"
"background-color: rgb(38, 38, 38);")

        self.gridLayout.addWidget(self.lb_message, 9, 1, 1, 2)

        self.pbtn_sign_up = QPushButton(w_LoginForm)
        self.pbtn_sign_up.setObjectName(u"pbtn_sign_up")
        self.pbtn_sign_up.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/sign_up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_sign_up.setIcon(icon1)

        self.gridLayout.addWidget(self.pbtn_sign_up, 8, 2, 1, 1)

        self.groupBox = QGroupBox(w_LoginForm)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"Cascadia Mono"])
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;\n"
"")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.input_cardNo = QLineEdit(self.groupBox)
        self.input_cardNo.setObjectName(u"input_cardNo")
        self.input_cardNo.setMouseTracking(True)
        self.input_cardNo.setFocusPolicy(Qt.ClickFocus)
        self.input_cardNo.setStyleSheet(u"QLineEdit:hover{\n"
"	border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(247, 191, 75)\n"
"}")
        self.input_cardNo.setReadOnly(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.input_cardNo)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.input_pin = QLineEdit(self.groupBox)
        self.input_pin.setObjectName(u"input_pin")
        self.input_pin.setMouseTracking(True)
        self.input_pin.setTabletTracking(False)
        self.input_pin.setFocusPolicy(Qt.ClickFocus)
        self.input_pin.setStyleSheet(u"QLineEdit:hover{\n"
"	border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(247, 191, 75)\n"
"}")
        self.input_pin.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.input_pin)


        self.gridLayout.addWidget(self.groupBox, 7, 1, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 2)

        self.pbtn_sign_in = QPushButton(w_LoginForm)
        self.pbtn_sign_in.setObjectName(u"pbtn_sign_in")
        self.pbtn_sign_in.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/sign-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_sign_in.setIcon(icon2)

        self.gridLayout.addWidget(self.pbtn_sign_in, 8, 1, 1, 1)

        QWidget.setTabOrder(self.pbtn_sign_in, self.pbtn_sign_up)

        self.retranslateUi(w_LoginForm)

        QMetaObject.connectSlotsByName(w_LoginForm)
    # setupUi

    def retranslateUi(self, w_LoginForm):
        w_LoginForm.setWindowTitle(QCoreApplication.translate("w_LoginForm", u"SwiftTrust - Login", None))
        self.groupBox_2.setTitle("")
        self.label_4.setText("")
        self.lb_message.setText(QCoreApplication.translate("w_LoginForm", u"Message:", None))
        self.pbtn_sign_up.setText(QCoreApplication.translate("w_LoginForm", u"Sign-Up", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_LoginForm", u"Welcome, Login Here!", None))
        self.label.setText(QCoreApplication.translate("w_LoginForm", u"CARD NO:", None))
        self.input_cardNo.setText("")
        self.input_cardNo.setPlaceholderText(QCoreApplication.translate("w_LoginForm", u"xxxxx", None))
        self.label_2.setText(QCoreApplication.translate("w_LoginForm", u"PIN:", None))
        self.input_pin.setText("")
        self.input_pin.setPlaceholderText(QCoreApplication.translate("w_LoginForm", u"xxxxx", None))
        self.pbtn_sign_in.setText(QCoreApplication.translate("w_LoginForm", u"Sign-In", None))
    # retranslateUi

