# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_up_design.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import all_images_rc

class Ui_d_SignUp(object):
    def setupUi(self, d_SignUp):
        if not d_SignUp.objectName():
            d_SignUp.setObjectName(u"d_SignUp")
        d_SignUp.setWindowModality(Qt.ApplicationModal)
        d_SignUp.resize(393, 218)
        icon = QIcon()
        icon.addFile(u":/Main/window_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        d_SignUp.setWindowIcon(icon)
        self.gridLayout = QGridLayout(d_SignUp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pbtn_submit = QPushButton(d_SignUp)
        self.pbtn_submit.setObjectName(u"pbtn_submit")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_submit.setIcon(icon1)

        self.gridLayout.addWidget(self.pbtn_submit, 2, 1, 1, 1)

        self.gb_SignUp = QGroupBox(d_SignUp)
        self.gb_SignUp.setObjectName(u"gb_SignUp")
        self.gb_SignUp.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.gb_SignUp)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gb_SignUp)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.signUp_fname = QLineEdit(self.gb_SignUp)
        self.signUp_fname.setObjectName(u"signUp_fname")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.signUp_fname)

        self.label_2 = QLabel(self.gb_SignUp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.signUp_lname = QLineEdit(self.gb_SignUp)
        self.signUp_lname.setObjectName(u"signUp_lname")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.signUp_lname)

        self.label_3 = QLabel(self.gb_SignUp)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.signUp_cardNo = QLineEdit(self.gb_SignUp)
        self.signUp_cardNo.setObjectName(u"signUp_cardNo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.signUp_cardNo)

        self.label_4 = QLabel(self.gb_SignUp)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.signUp_pin = QLineEdit(self.gb_SignUp)
        self.signUp_pin.setObjectName(u"signUp_pin")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.signUp_pin)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.SpanningRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.gb_SignUp, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.pbtn_cancel = QPushButton(d_SignUp)
        self.pbtn_cancel.setObjectName(u"pbtn_cancel")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_cancel.setIcon(icon2)

        self.gridLayout.addWidget(self.pbtn_cancel, 2, 2, 1, 1)

        self.lb_message = QLabel(d_SignUp)
        self.lb_message.setObjectName(u"lb_message")

        self.gridLayout.addWidget(self.lb_message, 3, 0, 1, 3)

        QWidget.setTabOrder(self.signUp_fname, self.signUp_lname)
        QWidget.setTabOrder(self.signUp_lname, self.signUp_cardNo)
        QWidget.setTabOrder(self.signUp_cardNo, self.signUp_pin)
        QWidget.setTabOrder(self.signUp_pin, self.pbtn_submit)
        QWidget.setTabOrder(self.pbtn_submit, self.pbtn_cancel)

        self.retranslateUi(d_SignUp)

        QMetaObject.connectSlotsByName(d_SignUp)
    # setupUi

    def retranslateUi(self, d_SignUp):
        d_SignUp.setWindowTitle(QCoreApplication.translate("d_SignUp", u"SwiftTrust - Sign-Up", None))
        self.pbtn_submit.setText(QCoreApplication.translate("d_SignUp", u"Submit", None))
        self.gb_SignUp.setTitle(QCoreApplication.translate("d_SignUp", u"Application Form", None))
        self.label.setText(QCoreApplication.translate("d_SignUp", u"First Name:", None))
        self.label_2.setText(QCoreApplication.translate("d_SignUp", u"Last Name:", None))
        self.label_3.setText(QCoreApplication.translate("d_SignUp", u"Card No:", None))
        self.label_4.setText(QCoreApplication.translate("d_SignUp", u"Pin:", None))
        self.pbtn_cancel.setText(QCoreApplication.translate("d_SignUp", u"Cancel", None))
        self.lb_message.setText(QCoreApplication.translate("d_SignUp", u"Message:", None))
    # retranslateUi

