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

from Application_Login.Login import LoginForm #for login pop up
from Main.UI.Main_Application import Ui_MainWindow
class SwiftTrustBankSuite(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.login_checking = LoginForm()
        self.login_checking.login_success.connect(self.show)
        self.login_checking.show()

        self.stackedWidget.setCurrentWidget(self.acc_bal)

        self.pbtn_widthdraw.clicked.connect(self.page1)
        self.pbtn_deposit.clicked.connect(self.page2)
        self.pbtn_accBal.clicked.connect(self.page3)
        self.pbtn_transBal.clicked.connect(self.page4)
        self.pbtn_LOGOUT.clicked.connect(self.logging_out)

        self.submit_output_w.clicked.connect(self.getWithdraw)
        self.submit_output_d.clicked.connect(self.getDeposit)
        self.submit_output_t.clicked.connect(self.getTransfer)

        self.keypad_1.clicked.connect(lambda: self.press_it_withdraw("1"))
        self.keypad_2.clicked.connect(lambda: self.press_it_withdraw("2"))
        self.keypad_3.clicked.connect(lambda: self.press_it_withdraw("3"))
        self.keypad_4.clicked.connect(lambda: self.press_it_withdraw("4"))
        self.keypad_5.clicked.connect(lambda: self.press_it_withdraw("5"))
        self.keypad_6.clicked.connect(lambda: self.press_it_withdraw("6"))
        self.keypad_7.clicked.connect(lambda: self.press_it_withdraw("7"))
        self.keypad_8.clicked.connect(lambda: self.press_it_withdraw("8"))
        self.keypad_9.clicked.connect(lambda: self.press_it_withdraw("9"))
        self.keypad_10.clicked.connect(lambda: self.press_it_withdraw("0"))
        self.clear_output_w.clicked.connect(lambda: self.press_it_withdraw("C"))
        self.delete_number_w.clicked.connect(lambda: self.delete_output_withdraw())

        self.keypad_1.clicked.connect(lambda: self.press_it_deposit("1"))
        self.keypad_2.clicked.connect(lambda: self.press_it_deposit("2"))
        self.keypad_3.clicked.connect(lambda: self.press_it_deposit("3"))
        self.keypad_4.clicked.connect(lambda: self.press_it_deposit("4"))
        self.keypad_5.clicked.connect(lambda: self.press_it_deposit("5"))
        self.keypad_6.clicked.connect(lambda: self.press_it_deposit("6"))
        self.keypad_7.clicked.connect(lambda: self.press_it_deposit("7"))
        self.keypad_8.clicked.connect(lambda: self.press_it_deposit("8"))
        self.keypad_9.clicked.connect(lambda: self.press_it_deposit("9"))
        self.keypad_10.clicked.connect(lambda: self.press_it_deposit("0"))
        self.clear_output_d.clicked.connect(lambda: self.press_it_deposit("C"))
        self.delete_number_d.clicked.connect(lambda: self.delete_output_deposit())

        self.keypad_1.clicked.connect(lambda: self.press_it_transfer("1"))
        self.keypad_2.clicked.connect(lambda: self.press_it_transfer("2"))
        self.keypad_3.clicked.connect(lambda: self.press_it_transfer("3"))
        self.keypad_4.clicked.connect(lambda: self.press_it_transfer("4"))
        self.keypad_5.clicked.connect(lambda: self.press_it_transfer("5"))
        self.keypad_6.clicked.connect(lambda: self.press_it_transfer("6"))
        self.keypad_7.clicked.connect(lambda: self.press_it_transfer("7"))
        self.keypad_8.clicked.connect(lambda: self.press_it_transfer("8"))
        self.keypad_9.clicked.connect(lambda: self.press_it_transfer("9"))
        self.keypad_10.clicked.connect(lambda: self.press_it_transfer("0"))
        self.clear_output_t.clicked.connect(lambda: self.press_it_transfer("C"))
        self.delete_number_t.clicked.connect(lambda: self.delete_output_transfer())


    @qtc.Slot()

    def getWithdraw(self):
        input_cardNo = int(self.login_checking.input_cardNo.text())
        input_pin = int(self.login_checking.input_pin.text())

        mycursor.execute(f"SELECT usrbln FROM accTable WHERE cardNo = {input_cardNo} AND pin = {input_pin}")
        user_bal = int(mycursor.fetchone()[0])

        if user_bal > int(self.output_withdraw.text()):
            self.lb_message.setText("Message: Service Fee - 85!")
            amount = int(self.output_withdraw.text()) + 85
            if amount == 85:
                self.lb_message.setText("Message: Zero Withdrawal!")
            elif amount >0:
                user_bal -= amount
                mycursor.execute(
                    f"UPDATE accTable SET usrbln = {user_bal} WHERE cardNo = {input_cardNo} AND pin = {input_pin}")
                mydb.commit()
                withdrawal_amount = amount
                self.stackedWidget.setCurrentWidget(self.receipt_window)
                self.receipt_output.setText(f"Transaction Receipt: Card No:{input_cardNo}"
                                            f"\nService Fee: 85"
                                            f"\nDispensed: {amount-85}"
                                            f"\nWithdrawal From Checking: {withdrawal_amount}"
                                            f"\nAvailable Balance: {user_bal}")
                self.lb_message.setText("Message: Thank You!")
        else:
            self.lb_message.setText("Message: Insufficient funds!")

    def getDeposit(self):

        input_cardNo = int(self.login_checking.input_cardNo.text())
        input_pin = int(self.login_checking.input_pin.text())

        mycursor.execute(f"SELECT usrbln FROM accTable WHERE cardNo = {input_cardNo} AND pin = {input_pin}")
        user_bal = int(mycursor.fetchone()[0])

        try:
            amount = int(self.output_deposit.text())
        except ValueError:
            amount = 0

        if amount > 0:
            user_bal += amount - 85

            mycursor.execute(f"UPDATE accTable SET usrbln = {user_bal} WHERE cardNo = {input_cardNo} AND pin = {input_pin}")
            mydb.commit()
            self.stackedWidget.setCurrentWidget(self.receipt_window)
            self.receipt_output.setText(f"Transaction Receipt: "
                                        f"\nCard No: {input_cardNo}"
                                        f"\nService Fee: 85"
                                        f"\nDeposited: {amount}"
                                        f"\nAvailable Balance: {user_bal}")
            self.lb_message.setText("Message: Thank You!")
        elif amount == 0:
            self.lb_message.setText("Message: Zero Deposit")
    def getTransfer(self):
        mycursor.execute("SELECT Transaction_Id FROM accTable")
        myListId = mycursor.fetchall()
        try:
            getTransacId_input = int(self.search_transac_id.text())
        except ValueError:
            getTransacId_input = 0
        getTransacId_input_tuple = (getTransacId_input, )
        if getTransacId_input_tuple in myListId:
            mycursor.execute(f"SELECT usrbln FROM accTable WHERE cardNo = {int(self.login_checking.input_cardNo.text())} AND pin = {int(self.login_checking.input_pin.text())}")
            sender = int(mycursor.fetchone()[0])

            if sender >= int(self.output_transfer.text()):
                mycursor.execute(f"SELECT Transaction_Id from accTable WHERE cardNo = {int(self.login_checking.input_cardNo.text())} AND pin = {int(self.login_checking.input_pin.text())}")
                sender_transac_id = mycursor.fetchall()[0]
                sender_transac_id_int = int(sender_transac_id[0])
                if getTransacId_input != sender_transac_id_int:
                    mycursor.execute(f"UPDATE accTable SET usrbln = {sender-int(self.output_transfer.text())} WHERE cardNo = {int(self.login_checking.input_cardNo.text())} AND pin = {int(self.login_checking.input_pin.text())}")
                    mydb.commit()

                    mycursor.execute(f"SELECT usrbln FROM accTable WHERE Transaction_Id = {getTransacId_input}")
                    receiver = mycursor.fetchall()[0]
                    receiver_int = int(receiver[0])
                    receiver_int += int(self.output_transfer.text())

                    mycursor.execute(f"UPDATE accTable SET usrbln = {receiver_int} WHERE Transaction_Id = {self.search_transac_id.text()}")
                    mydb.commit()

                    self.lb_message.setText(f"Message: Balance Added!"
                                            f"\nMessage: Balance Updated!")
                else:
                    self.lb_message.setText("Message: Cannot Transfer to the sender itself!")
            else:
                self.lb_message.setText(f"Message: Zero Transfer or Insufficient funds!!")
        else:
            self.lb_message.setText("Message: Empty or UUID does not exist!")

    def page1(self):
        self.stackedWidget.setCurrentWidget(self.withdrawals)
        self.output_withdraw.setText("0")
        self.output_deposit.setText("0")
        self.output_transfer.setText("0")

    def page2(self):
        self.stackedWidget.setCurrentWidget(self.deposits)
        self.output_withdraw.setText("0")
        self.output_deposit.setText("0")
        self.output_transfer.setText("0")

    def page3(self):
        self.stackedWidget.setCurrentWidget(self.acc_bal)
        mydb.commit()
        mycursor.execute(f"SELECT fname, lname FROM accTable WHERE cardNo = {int(self.login_checking.input_cardNo.text())} AND pin = {int(self.login_checking.input_pin.text())}")
        myresult = mycursor.fetchall()[0]
        self.user_name.setText(f"Name: {myresult[1]}, {myresult[0]}")

        mycursor.execute(f"SELECT Transaction_Id FROM accTable WHERE cardNo = {int(self.login_checking.input_cardNo.text())} AND pin = {int(self.login_checking.input_pin.text())}")
        myresult1 = mycursor.fetchall()[0]
        self.unique_id.setText(f"Unique ID: {myresult1[0]}")

        mycursor.execute(f"SELECT usrbln FROM accTable WHERE cardNo = {int(self.login_checking.input_cardNo.text())} AND pin = {int(self.login_checking.input_pin.text())}")
        myresult2 = mycursor.fetchall()[0]
        self.current_balance.setText(f"Current Balance: {myresult2[0]}")
    def page4(self):
        self.stackedWidget.setCurrentWidget(self.trans_bal)
        self.output_withdraw.setText("0")
        self.output_deposit.setText("0")
        self.output_transfer.setText("0")



    def press_it_withdraw(self, pressed):
        if pressed == "C":
                self.output_withdraw.setText("0")
        else:
                if self.output_withdraw.text() == "0":
                        self.output_withdraw.setText("")
                self.output_withdraw.setText(f'{self.output_withdraw.text()}{pressed}')
    def delete_output_withdraw(self):
        text = self.output_withdraw.text()
        self.output_withdraw.setText(text[:len(text)-1])

    def press_it_deposit(self, pressed):
        if pressed == "C":
                self.output_deposit.setText("0")
        else:
                if self.output_deposit.text() == "0":
                        self.output_deposit.setText("")
                self.output_deposit.setText(f'{self.output_deposit.text()}{pressed}')
    def delete_output_deposit(self):
        text = self.output_deposit.text()
        self.output_deposit.setText(text[:len(text)-1])

    def press_it_transfer(self, pressed):
        if pressed == "C":
                self.output_transfer.setText("0")
        else:
                if self.output_transfer.text() == "0":
                        self.output_transfer.setText("")
                self.output_transfer.setText(f'{self.output_transfer.text()}{pressed}')
    def delete_output_transfer(self):
        text = self.output_transfer.text()
        self.output_transfer.setText(text[:len(text)-1])

    def logging_out(self):
        self.login_checking.show()
        self.login_checking.input_cardNo.setText("")
        self.login_checking.input_pin.setText("")
        self.close()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = SwiftTrustBankSuite()

    sys.exit(app.exec())