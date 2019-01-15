# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sip
import qdarkstyle
import pymysql
host_entry = "localhost"
password_entry = ""
main_alter_record = ''
class CustomerInformationSettings(QWidget):
    def __init__(self, parent=None):
        super(CustomerInformationSettings, self).__init__()
        self.setUpUI()

    def setUpUI(self):
        # 查询数据
        self.queryResults = None
        # 数据表
        self.tableWidget = None

        self.resize(1100, 700)
        self.layout = QVBoxLayout()
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()
        # Hlayout1控件的初始化
        font = QFont()
        font.setPixelSize(15)
        self.addButton = QPushButton(" 添加")
        self.addButton.setIcon(QIcon('.//image//添加.png'))
        self.addButton.setFont(font)
        self.addButton.setFixedHeight(25)
        self.addButton.setFixedWidth(140)

        self.alterButton = QPushButton(" 修改")
        self.alterButton.setIcon(QIcon('.//image//修改.png'))
        self.alterButton.setFont(font)
        self.alterButton.setFixedHeight(25)
        self.alterButton.setFixedWidth(140)

        self.deleteButton = QPushButton(" 删除")
        self.deleteButton.setIcon(QIcon('.//image//删除.png'))
        self.deleteButton.setFont(font)
        self.deleteButton.setFixedHeight(25)
        self.deleteButton.setFixedWidth(140)

        self.Hlayout1.addWidget(self.addButton)
        self.Hlayout1.addWidget(self.alterButton)
        self.Hlayout1.addWidget(self.deleteButton)
        # Hlayout2控件的初始化
        font.setPixelSize(15)
        self.searchEdit = QLineEdit()
        self.searchEdit.setFixedHeight(32)
        self.searchEdit.setFont(font)
        self.searchButton = QPushButton("查询")
        self.searchButton.setIcon(QIcon('.//image//查询.png'))
        self.searchButton.setFixedHeight(32)
        self.searchButton.setFont(font)

        self.condisionComboBox = QComboBox()
        searchCondision = ['按客户编号查询', '按名称查询', '按地址查询']
        self.condisionComboBox.setFixedHeight(32)
        self.condisionComboBox.setFont(font)
        self.condisionComboBox.addItems(searchCondision)

        self.Hlayout2.addWidget(self.searchEdit)
        self.Hlayout2.addWidget(self.searchButton)
        self.Hlayout2.addWidget(self.condisionComboBox)

        # tableWidget
        # 序号，书名，书号，作者，分类，出版社，出版时间，库存，剩余可借
        global host_entry
        global password_entry
        self.db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        self.cur = self.db.cursor()
        sql = "SELECT * FROM 顾客信息表"
        self.cur.execute(sql)
        self.queryResults = self.cur.fetchall()
        self.col_lst = [tup[0] for tup in self.cur.description]

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(len(self.col_lst))
        self.tableWidget.setRowCount(len(self.queryResults))
        font = QFont('微软雅黑', 10)
        self.tableWidget.horizontalHeader().setFont(font)
        self.tableWidget.setHorizontalHeaderLabels(self.col_lst)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setStyleSheet("QTableWidget{border:1px solid #696969}")

        # 插入初始表格
        for i in range(len(self.queryResults)):
            for j in range(len(self.col_lst)):
                temp_data = self.queryResults[i][j]  # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                data1.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, j, data1)

        self.layout.addLayout(self.Hlayout1)
        self.layout.addLayout(self.Hlayout2)
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.searchEdit.returnPressed.connect(self.searchButtonClicked)
        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.addButton.clicked.connect(self.addButtonClicked)
        self.alterButton.clicked.connect(self.alterButtonClicked)
        self.deleteButton.clicked.connect(self.deleteButtonClicked)

    def searchButtonClicked(self):
        queryCondition = ""
        conditionChoice = self.condisionComboBox.currentText()
        if (conditionChoice == "按客户编号查询"):
            conditionChoice = '客户编号'
        elif (conditionChoice == "按名称查询"):
            conditionChoice = '名称'
        else:
            conditionChoice = '地址'

        if (self.searchEdit.text() == ""):
            self.begin()
            return
        # 得到模糊查询条件
        temp = self.searchEdit.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%"
        queryCondition = ("SELECT * FROM 顾客信息表 WHERE %s LIKE '%s' ORDER BY %s " % (
        conditionChoice, s, conditionChoice))
        self.cur.execute(queryCondition)
        self.queryResults = self.cur.fetchall()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(self.queryResults))
        for i in range(len(self.queryResults)):
                for j in range(len(self.col_lst)):
                    temp_data = self.queryResults[i][j]  # 临时记录，不能直接插入表格
                    data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    data1.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, data1)
        # 当查询无记录时的操作
        if (not self.queryResults):
            print(QMessageBox.information(self, "提醒", "查询无记录", QMessageBox.Yes, QMessageBox.Yes))
            self.begin()
            return

    def addButtonClicked(self):
        addDialog = addCustomerInformationSettings(self)
        addDialog.show()
        addDialog.exec_()
        self.begin()

    def alterButtonClicked(self):
        index = self.tableWidget.currentIndex()
        if not index.isValid():
            return
        row = self.tableWidget.currentRow()
        id = self.tableWidget.item(row, 0).text()
        global main_alter_record
        main_alter_record = id
        alterDialog = alterCustomerInformationSetting(self)
        alterDialog.show()
        alterDialog.exec_()
        self.begin()

    def deleteButtonClicked(self):
        index = self.tableWidget.currentIndex()
        if not index.isValid():
            return
        row = self.tableWidget.currentRow()
        id = self.tableWidget.item(row, 0).text()
        if (QMessageBox.warning(self, "警告", "是否删除此行", QMessageBox.Yes, QMessageBox.No) ==
                QMessageBox.No):
            return
        sql = "DELETE FROM 顾客信息表 WHERE 客户编号 = '%s'" % (id)
        cur = self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        self.begin()
        return

    def begin(self):
        self.tableWidget.clearContents()
        global host_entry
        global password_entry
        db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        cur = db.cursor()
        sql = "SELECT * FROM 顾客信息表"
        cur.execute(sql)
        self.queryResults = cur.fetchall()
        self.tableWidget.setRowCount(len(self.queryResults))
        # 插入初始表格
        for i in range(len(self.queryResults)):
            for j in range(len(self.col_lst)):
                temp_data = self.queryResults[i][j]  # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                data1.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, j, data1)
        return
class addCustomerInformationSettings(QDialog):

    def __init__(self, parent=None):
        super(addCustomerInformationSettings, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("添加")

    def setUpUI(self):
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel(" 信息添加：")
        self.label_1= QLabel("客户编号:")
        self.label_2 = QLabel("名称:")
        self.label_3 = QLabel("地址:")
        self.label_4 = QLabel("邮编:")
        self.label_5 = QLabel("电话:")
        self.label_6 = QLabel("信誉度:")

        # button控件
        self.button = QPushButton("添 加")

        # lineEdit控件
        self.lineedit_1 = QLineEdit()
        self.lineedit_2 = QLineEdit()
        self.lineedit_3 = QLineEdit()
        self.lineedit_4 = QLineEdit()
        self.lineedit_5 = QLineEdit()
        self.lineedit_6 = QLineEdit()


        self.lineedit_1.setMaxLength(10)
        self.lineedit_2.setMaxLength(10)
        self.lineedit_3.setMaxLength(10)
        self.lineedit_4.setMaxLength(10)
        self.lineedit_5.setMaxLength(10)
        self.lineedit_6.setMaxLength(10)


        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.label_1, self.lineedit_1)
        self.layout.addRow(self.label_2, self.lineedit_2)
        self.layout.addRow(self.label_3, self.lineedit_3)
        self.layout.addRow(self.label_4, self.lineedit_4)
        self.layout.addRow(self.label_5, self.lineedit_5)
        self.layout.addRow(self.label_6, self.lineedit_6)
        self.layout.addRow("", self.button)
        print("1")
        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(14)

        self.label_1.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_5.setFont(font)
        self.label_6.setFont(font)
        self.lineedit_1.setFont(font)
        self.lineedit_2.setFont(font)
        self.lineedit_3.setFont(font)
        self.lineedit_4.setFont(font)
        self.lineedit_5.setFont(font)
        self.lineedit_6.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.button.setFont(font)
        self.button.setFixedHeight(32)
        self.button.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.button.clicked.connect(self.buttonCicked)

    def buttonCicked(self):
        text_1 = self.lineedit_1.text()
        text_2 = self.lineedit_2.text()
        text_3 = self.lineedit_3.text()
        text_4 = self.lineedit_4.text()
        text_5 = self.lineedit_5.text()
        text_6 = self.lineedit_6.text()

        if (text_1 == "" or text_2 == "" or text_3 == "" or text_4 == ""  or text_5 == "" or text_6 == ""):
            print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            global host_entry
            global password_entry
            db_0 = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
            cur_0 = db_0.cursor()
            sql = "SELECT * FROM 顾客信息表 WHERE 客户编号='%s'" % (text_1)
            cur_0.execute(sql)
            queryResults_0 = cur_0.fetchall()
            print(queryResults_0)
            if queryResults_0:
                print(QMessageBox.warning(self, "警告", "编号为[ " + text_1 + " ]已经存在！", QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
            # 打开数据库连接
            db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
            cur = db.cursor()
            sql = "INSERT INTO 顾客信息表 VALUES ('%s','%s','%s','%s','%s','%s')" % (text_1, text_2, text_3,text_4,text_5,text_6)
            cur.execute(sql)
            db.commit()
            print(QMessageBox.information(self, "提示", "添加成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.close()
            self.clearEdit()
        return

    def clearEdit(self):
        self.lineedit_1.clear()
        self.lineedit_2.clear()
        self.lineedit_3.clear()
        self.lineedit_4.clear()
        self.lineedit_5.clear()
        self.lineedit_6.clear()
class alterCustomerInformationSetting(QDialog):

    def __init__(self,parent=None):
        super(alterCustomerInformationSetting, self).__init__(parent)
        global main_alter_record
        self.id = main_alter_record
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("修改")


    def setUpUI(self):
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        global host_entry
        global password_entry
        self.db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        self.cur = self.db.cursor()
        sql = "SELECT * FROM 顾客信息表 WHERE 客户编号='%s'" % (self.id)
        self.cur.execute(sql)
        self.queryResults = self.cur.fetchall()

        # Label控件
        self.titlelabel = QLabel(" 信息修改")
        self.label_1 = QLabel("客户编号:")
        self.label_2 = QLabel("名称:")
        self.label_3 = QLabel("地址:")
        self.label_4 = QLabel("邮编:")
        self.label_5 = QLabel("电话:")
        self.label_6 = QLabel("信誉度:")

        # button控件
        self.button = QPushButton("修 改")

        # lineEdit控件
        self.lineedit_1 = QLineEdit(self.queryResults[0][0])
        self.lineedit_1.setEnabled(False)
        self.lineedit_2 = QLineEdit(self.queryResults[0][1])
        self.lineedit_3 = QLineEdit(self.queryResults[0][2])
        self.lineedit_4 = QLineEdit(self.queryResults[0][3])
        self.lineedit_5 = QLineEdit(self.queryResults[0][4])
        self.lineedit_6 = QLineEdit(self.queryResults[0][5])

        self.lineedit_1.setMaxLength(10)
        self.lineedit_2.setMaxLength(10)
        self.lineedit_3.setMaxLength(10)
        self.lineedit_4.setMaxLength(10)
        self.lineedit_5.setMaxLength(10)
        self.lineedit_6.setMaxLength(10)

        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.label_1, self.lineedit_1)
        self.layout.addRow(self.label_2, self.lineedit_2)
        self.layout.addRow(self.label_3, self.lineedit_3)
        self.layout.addRow(self.label_4, self.lineedit_4)
        self.layout.addRow(self.label_5, self.lineedit_5)
        self.layout.addRow(self.label_6, self.lineedit_6)
        self.layout.addRow("", self.button)
        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(14)

        self.label_1.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_5.setFont(font)
        self.label_6.setFont(font)
        self.lineedit_1.setFont(font)
        self.lineedit_2.setFont(font)
        self.lineedit_3.setFont(font)
        self.lineedit_4.setFont(font)
        self.lineedit_5.setFont(font)
        self.lineedit_6.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.button.setFont(font)
        self.button.setFixedHeight(32)
        self.button.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.button.clicked.connect(self.buttonCicked)

    def buttonCicked(self):
        text_1 = self.lineedit_1.text()
        text_2 = self.lineedit_2.text()
        text_3 = self.lineedit_3.text()
        text_4 = self.lineedit_4.text()
        text_5 = self.lineedit_5.text()
        text_6 = self.lineedit_6.text()

        if (text_1 == "" or text_2 == "" or text_3 == "" or text_4 == ""  or text_5 == "" or text_6 == ""):
            print(QMessageBox.warning(self, "警告", "有字段为空，修改失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            global host_entry
            global password_entry
            # 打开数据库连接
            db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
            cur = db.cursor()
            sql = "UPDATE 顾客信息表 SET 名称='%s',地址='%s',邮编='%s',电话='%s',信誉度='%s' WHERE 客户编号='%s'" % (text_2,text_3,text_4,text_5,text_6,text_1)
            cur.execute(sql)
            db.commit()
            print(QMessageBox.information(self, "提示", "添加成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.close()
            self.clearEdit()
        return

    def clearEdit(self):
        self.lineedit_1.clear()
        self.lineedit_2.clear()
        self.lineedit_3.clear()
        self.lineedit_4.clear()
        self.lineedit_5.clear()
        self.lineedit_6.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = CustomerInformationSettings()
    mainMindow.show()
    sys.exit(app.exec_())