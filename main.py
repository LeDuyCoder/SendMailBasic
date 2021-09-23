import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
import mail
import webbrowser

Email = mail.Email()

class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("ui/login.ui", self)
        self.setWindowTitle("Send Mail Speed")
        self.Button.clicked.connect(self.login)
        self.Button_register.clicked.connect(self.register)

    def register(self):
        webbrowser.open_new_tab("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com&hl=vi&dsh=S-1727885938%3A1631675293469987&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")

    def login(self):
        rect_mail = self.rec_mail.text()
        rect_pass = self.rec_pass.text()
        print(f"User: {rect_mail}\nPassWord: {rect_pass}")

        Login = Email.loginMail(rect_mail, rect_pass)
        if Login == 235:
            print("Đăng nhập thành công")
            buttonReply = QMessageBox.question(self, "Thông Báo", "Đăng nhập thành công",QMessageBox.Ok , QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                widget.setCurrentIndex(widget.currentIndex()+1)

class SeendWindow(QDialog):
    def __init__(self):
        super(SeendWindow, self).__init__()
        loadUi("ui/SendMail.ui", self)
        self.setWindowTitle("Send Mail Speed")
        self.Button_Send.clicked.connect(self.send)

    def send(self):
        mail = self.Sender_Mail.text()
        title = self.Title.text()
        content = self.Content.text()

        print(mail)

        #Email.loginMail(Email.rect_mail, Email.rect_pass)
        Email.setMailSend(mail)
        Email.sendMail(title, content)
        buttonReply = QMessageBox.question(self, "Thông Báo", "Đang gữi mail thành công!",QMessageBox.Ok , QMessageBox.Ok)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    widget.setWindowTitle("Send Mail Speed")
    widget.setWindowIcon(QIcon('icon.png'))
    loginwindow=LoginWindow()
    sendwindow=SeendWindow()
    widget.addWidget(loginwindow)
    widget.addWidget(sendwindow)
    widget.setFixedHeight(328)
    widget.setFixedWidth(558)
    widget.show()
    sys.exit(app.exec_())
