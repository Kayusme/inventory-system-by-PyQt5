# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sip
# import qdarkstyle
import pymysql
host_entry = "localhost"
password_entry = ""


class examine(QWidget):
    def __init__(self, parent=None):
        super(examine, self).__init__()
        self.setUpUI()
    def setUpUI(self):
        # 查询数据
        self.queryResults = None
        # 数据表
        self.tableWidget = None

        self.resize(1100, 700)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 49)
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()
        # Hlayout1控件的初始化
        font = QFont()
        font.setPixelSize(15)
        self.addButton = QPushButton("全部同意")
        self.addButton.setIcon(QIcon('.//image//全部同意.png'))
        self.addButton.setFont(font)
        self.addButton.setFixedHeight(25)
        self.addButton.setFixedWidth(140)

        self.alterButton = QPushButton(" 同意")
        self.alterButton.setIcon(QIcon('.//image//同意.png'))
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
        searchCondision = ['按用户名查询']
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
        sql = "SELECT * FROM 用户申请"
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

        #插入初始表格
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
        conditionChoice = '用户名'



        if (self.searchEdit.text() == ""):
            self.begin()
            return
        # 得到模糊查询条件
        temp = self.searchEdit.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%"
        queryCondition = ("SELECT * FROM 用户申请 WHERE %s LIKE '%s' ORDER BY %s " % (conditionChoice, s, conditionChoice))
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
        if (QMessageBox.warning(self, "警告", "是否全部同意！", QMessageBox.Yes, QMessageBox.No) ==
                QMessageBox.No):
            return
        cur = self.db.cursor()
        sql = "SELECT * FROM 用户申请"
        cur.execute(sql)
        queryResults = cur.fetchall()
        for Result in queryResults:
            text_1 = Result[0]
            text_2 = Result[1]
            text_3 = Result[2]
            text_4 = Result[3]
            text_5 = Result[4]
            text_6 = Result[5]
            sql = "INSERT INTO 用户管理 VALUES ('%s','%s','%s','%s','%s','%s')" % (text_1, text_2, text_3,text_4,text_5,text_6)
            cur.execute(sql)
            self.db.commit()
            sql = "DELETE FROM 用户申请 WHERE 用户名 = '%s'" % (text_1)
            cur.execute(sql)
            self.db.commit()
        self.begin()
        return
    def alterButtonClicked(self):
        index = self.tableWidget.currentIndex()
        if not index.isValid():
            return
        row = self.tableWidget.currentRow()
        text_1 = self.tableWidget.item(row, 0).text()
        text_2 = self.tableWidget.item(row, 1).text()
        text_3 = self.tableWidget.item(row, 2).text()
        text_4 = self.tableWidget.item(row, 3).text()
        text_5 = self.tableWidget.item(row, 4).text()
        text_6 = self.tableWidget.item(row, 5).text()
        cur = self.db.cursor()
        sql = "INSERT INTO 用户管理 VALUES ('%s','%s','%s','%s','%s','%s')" % (
        text_1, text_2, text_3, text_4, text_5, text_6)
        cur.execute(sql)
        self.db.commit()
        sql = "DELETE FROM 用户申请 WHERE 用户名 = '%s'" % (text_1)
        cur.execute(sql)
        self.db.commit()
        self.begin()
        return
    def deleteButtonClicked(self):
        index = self.tableWidget.currentIndex()
        if not index.isValid():
            return
        row = self.tableWidget.currentRow()
        id = self.tableWidget.item(row, 0).text()
        sql = "DELETE FROM 用户申请 WHERE 用户名 = '%s'" % (id)
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
        sql = "SELECT * FROM 用户申请"
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = examine()
    mainMindow.show()
    sys.exit(app.exec_())