import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# import qdarkstyle
import time
from PyQt5.QtSql import *
import hashlib
import pymysql

host_entry = "localhost"
password_entry = ""

class changePasswordDialog(QDialog):
    def __init__(self, parent=None):
        super(changePasswordDialog, self).__init__(parent)
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("修改密码")
        self.setUpUI()

    def setUpUI(self):
        self.resize(300, 280)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.titlelabel = QLabel(" 修改密码")
        self.studentIdLabel = QLabel("账    号：")
        self.oldPasswordLabel = QLabel("旧 密 码：")
        self.passwordLabel = QLabel("新 密 码：")
        self.confirmPasswordLabel = QLabel("确认密码：")

        self.studentIdEdit = QLineEdit()
        self.oldPasswordEdit = QLineEdit()
        self.passwordEdit = QLineEdit()
        self.confirmPasswordEdit = QLineEdit()

        self.changePasswordButton = QPushButton("确认修改")
        self.changePasswordButton.setFixedWidth(140)
        self.changePasswordButton.setFixedHeight(32)

        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.studentIdLabel, self.studentIdEdit)
        self.layout.addRow(self.oldPasswordLabel, self.oldPasswordEdit)
        self.layout.addRow(self.passwordLabel, self.passwordEdit)
        self.layout.addRow(self.confirmPasswordLabel, self.confirmPasswordEdit)
        self.layout.addRow("", self.changePasswordButton)

        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(16)
        self.studentIdLabel.setFont(font)
        self.oldPasswordLabel.setFont(font)
        self.passwordLabel.setFont(font)
        self.confirmPasswordLabel.setFont(font)

        font.setPixelSize(16)
        self.studentIdEdit.setFont(font)
        self.changePasswordButton.setFont(font)
        font.setPixelSize(10)
        self.oldPasswordEdit.setFont(font)
        self.passwordEdit.setFont(font)
        self.confirmPasswordEdit.setFont(font)

        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        # 设置长度
        self.studentIdEdit.setMaxLength(10)
        self.oldPasswordEdit.setMaxLength(16)
        self.passwordEdit.setMaxLength(16)
        self.confirmPasswordEdit.setMaxLength(16)
        # 设置密码掩膜
        self.oldPasswordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.confirmPasswordEdit.setEchoMode(QLineEdit.Password)

        # 设置校验
        reg = QRegExp("PB[0~9]{8}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.studentIdEdit.setValidator(pValidator)

        reg = QRegExp("[a-zA-z0-9]+$")
        pValidator.setRegExp(reg)
        self.oldPasswordEdit.setValidator(pValidator)
        self.passwordEdit.setValidator(pValidator)
        self.confirmPasswordEdit.setValidator(pValidator)

        # 设置信号与槽
        self.changePasswordButton.clicked.connect(self.changePasswordButtonClicked)

    def changePasswordButtonClicked(self):
        studentId = self.studentIdEdit.text()
        oldPassword = self.oldPasswordEdit.text()
        password = self.passwordEdit.text()
        confirmPassword = self.confirmPasswordEdit.text()
        if (studentId == "" or oldPassword == "" or password == "" or confirmPassword == ""):
            print(QMessageBox.warning(self, "警告", "输入不可为空，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            return
        global host_entry
        global password_entry
        db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        cur = db.cursor()

        sql = "SELECT * FROM 用户管理 WHERE 用户名='%s'" % (studentId)
        cur.execute(sql)
        # 如果用户不存在
        results = cur.fetchall()
        if (not results):
            print(QMessageBox.warning(self, "警告", "该用户不存在，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            self.studentIdEdit.clear()
            return
            # 如果密码错误
        sql = "SELECT * FROM 用户管理 WHERE 密码='%s' AND 用户名='%s'" %(oldPassword,studentId)
        cur.execute(sql)
        results = cur.fetchall()
        if (not results):
            print(QMessageBox.warning(self, "警告", "原密码输入错误,请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            self.oldPasswordEdit.clear()
            return
        # 密码与确认密码不同
        if(password!=confirmPassword):
            print(QMessageBox.warning(self,"警告","两次输入密码不同,请确认输入",QMessageBox.Yes,QMessageBox.Yes))
            self.passwordEdit.clear()
            self.confirmPasswordEdit.clear()
            return
        # 修改密码
        sql="UPDATE 用户管理 SET 密码='%s' WHERE 用户名='%s'"%(password,studentId)
        cur.execute(sql)
        db.commit()
        QMessageBox.information(self,"提醒","修改密码成功，请登录系统!",QMessageBox.Yes,QMessageBox.Yes)
        self.close()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = changePasswordDialog()
    mainMindow.show()
    sys.exit(app.exec_())
