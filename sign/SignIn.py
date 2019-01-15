import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# import qdarkstyle
import hashlib
from PyQt5.QtSql import *
import pymysql

host_entry = "localhost"
password_entry = ""


class SignInWidget(QWidget):
    is_company_signal = pyqtSignal(str)
    is_wholesale_signal = pyqtSignal(str)
    is_base_signal = pyqtSignal(str)
    is_purchasing_signal = pyqtSignal(str)

    def __init__(self):
        super(SignInWidget, self).__init__()
        self.resize(900, 600)
        self.setWindowTitle("欢迎使用图书馆管理系统")
        self.setUpUI()

    def setUpUI(self):
        self.Vlayout = QVBoxLayout(self)
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()
        self.formlayout = QFormLayout()

        font = QFont()
        font.setPixelSize(15)

        self.label1 = QLabel("账号: ")
        labelFont = QFont()
        labelFont.setPixelSize(18)
        lineEditFont = QFont()
        lineEditFont.setPixelSize(16)
        self.label1.setFont(labelFont)
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setFixedHeight(32)
        self.lineEdit1.setFixedWidth(180)
        self.lineEdit1.setFont(lineEditFont)
        self.lineEdit1.setMaxLength(10)
        self.lineEdit1.setFont(font)

        self.formlayout.addRow(self.label1, self.lineEdit1)

        self.label2 = QLabel("密码: ")
        self.label2.setFont(labelFont)
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setFixedHeight(32)
        self.lineEdit2.setFixedWidth(180)
        self.lineEdit2.setMaxLength(16)

        # 设置验证
        reg = QRegExp("PB[0~9]{8}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.lineEdit1.setValidator(pValidator)

        reg = QRegExp("[a-zA-z0-9]+$")
        pValidator.setRegExp(reg)
        self.lineEdit2.setValidator(pValidator)


        self.lineEdit2.setFont(font)

        self.lineEdit2.setEchoMode(QLineEdit.Password)
        self.formlayout.addRow(self.label2, self.lineEdit2)

        self.label3 = QLabel("系统: ")
        self.label3.setFont(labelFont)
        self.condisionComboBox = QComboBox()
        searchCondision = ['公司', '批发中心', '基地', '代购点']
        self.condisionComboBox.addItems(searchCondision)
        self.condisionComboBox.setFixedHeight(32)
        self.condisionComboBox.setFixedWidth(180)
        self.condisionComboBox.setFont(font)
        self.formlayout.addRow(self.label3, self.condisionComboBox)

        self.signIn = QPushButton("登 录")
        self.signIn.setFixedWidth(80)
        self.signIn.setFixedHeight(30)
        self.signIn.setFont(labelFont)
        self.formlayout.addRow("", self.signIn)

        self.label = QLabel("欢迎使用深圳嘉农公司信息管理系统")
        fontlabel = QFont()
        fontlabel.setPixelSize(30)
        self.label.setFixedWidth(500)
        # self.label.setFixedHeight(80)
        self.label.setFont(fontlabel)
        self.Hlayout1.addWidget(self.label, Qt.AlignCenter)
        self.widget1 = QWidget()
        self.widget1.setLayout(self.Hlayout1)
        self.widget2 = QWidget()
        self.widget2.setFixedWidth(300)
        self.widget2.setFixedHeight(150)
        self.widget2.setLayout(self.formlayout)
        self.Hlayout2.addWidget(self.widget2, Qt.AlignCenter)
        self.widget = QWidget()
        self.widget.setLayout(self.Hlayout2)
        self.Vlayout.addWidget(self.widget1)
        self.Vlayout.addWidget(self.widget, Qt.AlignTop)

        self.signIn.clicked.connect(self.signInCheck)
        self.lineEdit2.returnPressed.connect(self.signInCheck)
        self.lineEdit1.returnPressed.connect(self.signInCheck)

    def signInCheck(self):
        admin = self.lineEdit1.text()
        password = self.lineEdit2.text()
        combobox = self.condisionComboBox.currentText()
        if (admin == "" or password == ""):
            print(QMessageBox.warning(self, "警告", "账号和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes))
            return
        # 打开数据库连接
        global host_entry
        global password_entry
        db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        cur = db.cursor()
        sql = "SELECT * FROM 用户管理 WHERE 用户名='%s'" % (admin)

        cur.execute(sql)
        results = cur.fetchall()

        if (not results):
            print(QMessageBox.information(self, "提示", "该账号不存在!", QMessageBox.Yes, QMessageBox.Yes))
        else:
            for row in results:
                result=row
                break
            if (admin == result[0] and password== result[1]):
                # 如果是公司
                if (combobox=="公司"):
                    if (result[2]=='1'):
                        self.is_company_signal.emit(admin)
                        print("1")
                    else:
                        print(QMessageBox.warning(self, "警告", "此账号无权限!", QMessageBox.Yes, QMessageBox.Yes))
                        return

                #批发中心
                if (combobox=="批发中心"):
                    if (result[3]=='1'):
                        self.is_wholesale_signal.emit(admin)
                        print("2")
                    else:
                        print(QMessageBox.warning(self, "警告", "此账号无权限!", QMessageBox.Yes, QMessageBox.Yes))
                        return
                # 基地
                if (combobox=="基地"):
                    if (result[4]=='1'):
                        self.is_base_signal.emit(admin)
                        print("3")
                    else:
                        print(QMessageBox.warning(self, "警告", "此账号无权限!", QMessageBox.Yes, QMessageBox.Yes))
                        return
                # 代购点
                if (combobox=="代购点"):
                    if (result[5]=='1'):
                        self.is_purchasing_signal.emit(admin)
                        print("4")
                    else:
                        print(QMessageBox.warning(self, "警告", "此账号无权限!", QMessageBox.Yes, QMessageBox.Yes))
                        return

            else:
                print(QMessageBox.information(self, "提示", "密码错误!", QMessageBox.Yes, QMessageBox.Yes))
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = SignInWidget()
    mainMindow.show()
    sys.exit(app.exec_())
