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

from Application_Login.UI.login_design import Ui_w_LoginForm
from Application_Sign_Up.SignUp import SignUpForm
class LoginForm(qtw.QWidget, Ui_w_LoginForm):
    login_success = qtc.Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pbtn_sign_in.clicked.connect(self.check_login)
        self.pbtn_sign_up.clicked.connect(self.signUp)
    @qtc.Slot()

    def check_login(self):
        mycursor.execute("SELECT cardNo, pin FROM accTable")
        mydb.commit()
        myListCard = mycursor.fetchall()
        zero_tuple = (0, 0)
        try:
            input_c = int(self.input_cardNo.text())
            input_p = int(self.input_pin.text())
        except ValueError:
            input_c = 0
            input_p = 0
        c_and_p_tuple = (input_c, input_p)

        if c_and_p_tuple in myListCard:
            #Login Successful
            self.loggedIn()
        elif c_and_p_tuple == zero_tuple:
            self.lb_message.setText("Message: Field are Empty or Invalid Input!")
        else:
            self.lb_message.setText("Message: Incorrect Card No. or Pin!")

    def loggedIn(self):
        self.login_success.emit()
        self.close()

    def signUp(self):
        self.sign_up = SignUpForm()
        self.sign_up.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = LoginForm()
    window.show()

    sys.exit(app.exec())

