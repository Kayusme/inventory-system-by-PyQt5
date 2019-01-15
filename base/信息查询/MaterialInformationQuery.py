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
class MaterialInformationQuery(QWidget):
    def __init__(self, parent=None):
        super(MaterialInformationQuery, self).__init__()
        self.setUpUI()

    def setUpUI(self):
        self.queryResults = None
        # 数据表
        self.tableWidget = None

        self.resize(1100, 700)
        self.layout = QVBoxLayout()

        self.Hlayout1 = QHBoxLayout()
        font = QFont()
        font.setPixelSize(15)
        self.searchEdit = QLineEdit()
        self.searchEdit.setFixedHeight(32)
        self.searchEdit.setFont(font)
        self.searchButton = QPushButton("查询")
        self.searchButton.setIcon(QIcon('.//image//查询.png'))
        self.searchButton.setFixedHeight(32)
        self.searchButton.setFont(font)

        self.condisionComboBox = QComboBox()
        searchCondision = ['物资编号', '物资名称']
        self.condisionComboBox.setFixedHeight(32)
        self.condisionComboBox.setFont(font)
        self.condisionComboBox.addItems(searchCondision)

        self.Hlayout1.addWidget(self.searchEdit)
        self.Hlayout1.addWidget(self.searchButton)
        self.Hlayout1.addWidget(self.condisionComboBox)

        global host_entry
        global password_entry
        self.db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        self.cur = self.db.cursor()
        sql = "SELECT * FROM 物资信息表"
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
        for i in range(len(self.queryResults)):
            for j in range(len(self.col_lst)):
                temp_data = self.queryResults[i][j]  # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                data1.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, j, data1)

        self.layout.addLayout(self.Hlayout1)
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.searchEdit.returnPressed.connect(self.searchButtonClicked)
        self.searchButton.clicked.connect(self.searchButtonClicked)
    def searchButtonClicked(self):
        queryCondition = ""
        conditionChoice = self.condisionComboBox.currentText()
        if (conditionChoice == "按物资编号查询"):
            conditionChoice = '物资编号'
        elif (conditionChoice == "按物资名称查询"):
            conditionChoice = '物资名称'

        if (self.searchEdit.text() == ""):
            self.begin()
            return
        # 得到模糊查询条件
        temp = self.searchEdit.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%"
        queryCondition = ("SELECT * FROM 物资信息表 WHERE %s LIKE '%s' ORDER BY %s " % (
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
    def begin(self):
        self.tableWidget.clearContents()
        global host_entry
        global password_entry
        db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        cur = db.cursor()
        sql = "SELECT * FROM 物资信息表"
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
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = MaterialInformationQuery()
    mainMindow.show()
    sys.exit(app.exec_())