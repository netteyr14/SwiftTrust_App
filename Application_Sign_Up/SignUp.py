import sys
import mysql.connector as sql
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

mydb = sql.connect(
    host='127.0.0.1',
    user='root',
    password='Ambin123456123456',
    database='users'
)
mycursor = mydb.cursor(buffered=True)
from Application_Sign_Up.UI.sign_up_design import Ui_d_SignUp

class SignUpForm(qtw.QDialog, Ui_d_SignUp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pbtn_submit.clicked.connect(self.process_form)
        self.pbtn_cancel.clicked.connect(self.close)

    @qtc.Slot()
    def process_form(self):
        mycursor.execute("SELECT fname, lname FROM accTable")
        myListNames = mycursor.fetchall()
        firstName = self.signUp_fname.text()
        lastName = self.signUp_lname.text()

        f_and_l = (firstName, lastName)

        if f_and_l in myListNames:
            self.lb_message.setText("Message: User Already Exists!")
        else:
            fnameI = self.signUp_fname.text()
            lnameI = self.signUp_lname.text()
            try:
                cardNoI = int(self.signUp_cardNo.text())
                pinI = int(self.signUp_pin.text())
                balance_default = 0
            except ValueError:
                fnameI = ''
                lnameI = ''
                cardNoI = ''
                pinI = ''
                balance_default = ''

            forms = [fnameI, lnameI, cardNoI, pinI, balance_default]
            empty_list = ["", "", "", "",""]
            if forms != empty_list:
                sqlFormula = "INSERT INTO accTable (fname, lname, cardNo, pin, usrbln) VALUES (%s, %s, %s, %s, %s)"
                myForms = (fnameI, lnameI, cardNoI, pinI, balance_default)

                mycursor.execute(sqlFormula, myForms)
                mydb.commit()

                self.signUp_fname.clear()
                self.signUp_lname.clear()
                self.signUp_cardNo.clear()
                self.signUp_pin.clear()


                self.lb_message.setText("""Message: User Added!\nMessage: Application Complete!""")
            else:
                self.lb_message.setText("Message: Field are Empty or Invalid Input!")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = SignUpForm()
    form.open()

    sys.exit(app.exec())