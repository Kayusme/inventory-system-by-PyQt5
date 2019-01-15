# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sip
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import pymysql
import numpy as np
import pandas as pd

host_entry = "localhost"
password_entry = ""


class SalesStatistics(QWidget):
    def __init__(self, parent=None):
        super(SalesStatistics, self).__init__()
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
        self.graphcombobox = QComboBox()
        graphCondision = ['柱状图', '饼状图', '折线图']
        self.graphcombobox.addItems(graphCondision)
        self.graphcombobox.setFont(font)
        self.graphcombobox.setFixedHeight(30)
        self.graphcombobox.setFixedWidth(75)

        self.graphway = QComboBox()
        graphwayCondision = ['按不同品种统计', '按不同时间段统计']
        self.graphway.addItems(graphwayCondision)
        self.graphway.setFont(font)
        self.graphway.setFixedHeight(30)
        self.graphway.setFixedWidth(150)

        self.deleteButton = QPushButton(" 统计")
        self.deleteButton.setIcon(QIcon('.//image//统计.png'))
        self.deleteButton.setFont(font)
        self.deleteButton.setFixedHeight(30)
        self.deleteButton.setFixedWidth(100)

        self.Hlayout1.addWidget(self.graphcombobox)
        self.Hlayout1.addWidget(self.graphway)
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
        searchCondision = ['按销售单号查询', '按产品编号查询', '按销售日期查询', '按客户编号查询']
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
        sql = "SELECT * FROM 销售统计表"
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
        self.deleteButton.clicked.connect(self.deleteButtonClicked)

    def searchButtonClicked(self):
        queryCondition = ""
        conditionChoice = self.condisionComboBox.currentText()
        if (conditionChoice == "按销售单号查询"):
            conditionChoice = '销售单号'
        elif (conditionChoice == "按产品编号查询"):
            conditionChoice = '产品编号'
        elif (conditionChoice == "按销售日期查询"):
            conditionChoice = '销售日期'
        else:
            conditionChoice = '客户编号'

        if (self.searchEdit.text() == ""):
            self.begin()
            return
        # 得到模糊查询条件
        temp = self.searchEdit.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%"
        queryCondition = ("SELECT * FROM 销售统计表 WHERE %s LIKE '%s' ORDER BY %s " % (conditionChoice, s, conditionChoice))
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

    def deleteButtonClicked(self):
        # 获得统计方式
        graph = self.graphcombobox.currentText()
        way = self.graphway.currentText()
        self.x = []
        self.y = []
        if graph == "柱状图":
            if way=="按不同品种统计":
                self.graphResults = np.array(self.queryResults)
                self.graphResults = pd.DataFrame(self.graphResults, columns=["a", "b", "c", "d", "e", "f", "g"])
                self.graphResults.d = self.graphResults.d.apply(pd.to_numeric)
                self.x = list(self.graphResults.c.value_counts().keys())
                for x in self.x:
                    a = self.graphResults.d[self.graphResults.c == x].sum()
                    self.y.append(a)
                plt.figure("柱状图-按不同品种统计")
                rects = plt.bar(self.x, self.y)
                plt.xticks(rotation=90)
                plt.title("柱状图-按不同品种统计")
                for rect in rects:
                    height = rect.get_height()
                    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
                plt.show()
            else:
                pass

        elif graph == "饼状图":
            if way=="按不同品种统计":
                self.graphResults = np.array(self.queryResults)
                self.graphResults = pd.DataFrame(self.graphResults, columns=["a", "b", "c", "d", "e", "f", "g"])
                self.graphResults.d = self.graphResults.d.apply(pd.to_numeric)
                self.x = list(self.graphResults.c.value_counts().keys())
                for x in self.x:
                    a = self.graphResults.d[self.graphResults.c == x].sum()
                    self.y.append(a)
                plt.figure("饼状图-按不同品种统计")
                plt.title("饼状图-按不同品种统计")
                plt.pie(self.y, labels=self.x, autopct='%1.2f%%')
                plt.show()
            else:
                pass
        else:
            if way=="按不同品种统计":
                pass
            else:
                pass
        # 图表数量计算



        # addDialog = addProductInformation(self)
        # addDialog.show()
        # addDialog.exec_()
        self.begin()

    def begin(self):
        self.tableWidget.clearContents()
        global host_entry
        global password_entry
        db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        cur = db.cursor()
        sql = "SELECT * FROM 销售统计表"
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
    mainMindow = SalesStatistics()
    mainMindow.show()
    sys.exit(app.exec_())
