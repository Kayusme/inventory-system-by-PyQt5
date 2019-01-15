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

main_alter_record = ''
class PCMateral(QWidget):
    def __init__(self, parent=None):
        super(PCMateral, self).__init__()
        self.setUpUI()
    def setUpUI(self):
        # 查询数据
        self.queryResults = None
        # 数据表
        self.tableWidget = None

        self.resize(1100, 700)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 49)
        self.Hlayout2 = QHBoxLayout()
        # Hlayout1控件的初始化
        font = QFont()
        font.setPixelSize(15)
        self.addButton = QPushButton("盘存")
        self.addButton.setIcon(QIcon('.//image//盘存.png'))
        self.addButton.setFont(font)
        self.addButton.setFixedHeight(32)

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
        searchCondision = ['按物资编号查询']
        self.condisionComboBox.setFixedHeight(32)
        self.condisionComboBox.setFont(font)
        self.condisionComboBox.addItems(searchCondision)

        self.Hlayout2.addWidget(self.searchEdit)
        self.Hlayout2.addWidget(self.searchButton)
        self.Hlayout2.addWidget(self.condisionComboBox)
        self.Hlayout2.addWidget(self.addButton)


        # tableWidget
        # 序号，书名，书号，作者，分类，出版社，出版时间，库存，剩余可借
        global host_entry
        global password_entry
        self.db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        self.cur = self.db.cursor()
        sql = "SELECT * FROM 物资盘存信息表"
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

        self.layout.addLayout(self.Hlayout2)
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.searchEdit.returnPressed.connect(self.searchButtonClicked)
        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.addButton.clicked.connect(self.addButtonClicked)

    def searchButtonClicked(self):
        queryCondition = ""
        conditionChoice = '物资编号'


        if (self.searchEdit.text() == ""):
            self.begin()
            return
        # 得到模糊查询条件
        temp = self.searchEdit.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%"
        queryCondition = ("SELECT * FROM 物资盘存信息表 WHERE %s LIKE '%s' ORDER BY %s " % (conditionChoice, s, conditionChoice))
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
        addDialog = addPCMateral(self)
        addDialog.show()
        addDialog.exec_()
        self.begin()
        return

    def begin(self):
        self.tableWidget.clearContents()
        global host_entry
        global password_entry
        db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        cur = db.cursor()
        sql = "SELECT * FROM 物资盘存信息表"
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

class addPCMateral(QDialog):

    def __init__(self, parent=None):
        super(addPCMateral, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("盘存")

    def setUpUI(self):
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel(" 物资盘存")
        self.label_1 = QLabel("物资编号:")
        self.label_2 = QLabel("物资名称:")
        self.label_3 = QLabel("数量:")
        self.label_4 = QLabel("备注:")

        # button控件
        self.button = QPushButton("盘 存")

        # lineEdit控件
        self.lineedit_1 = QLineEdit()
        self.lineedit_2 = QLineEdit()
        self.lineedit_3 = QLineEdit()
        self.lineedit_4 = QLineEdit()


        self.lineedit_1.setMaxLength(10)
        self.lineedit_2.setMaxLength(10)
        self.lineedit_3.setMaxLength(10)
        self.lineedit_4.setMaxLength(10)


        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.label_1, self.lineedit_1)
        self.layout.addRow(self.label_2, self.lineedit_2)
        self.layout.addRow(self.label_3, self.lineedit_3)
        self.layout.addRow(self.label_4, self.lineedit_4)
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
        self.lineedit_1.setFont(font)
        self.lineedit_2.setFont(font)
        self.lineedit_3.setFont(font)
        self.lineedit_4.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.button.setFont(font)
        self.button.setFixedHeight(32)
        self.button.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        # self.lineedit_2.textChanged.connect(self.handleTextChanged)
        self.button.clicked.connect(self.buttonCicked)
        self.db= pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")

    # def handleTextChanged(self):
    #     text_2 = self.lineedit_2.text()
    #     cur = self.db.cursor()
    #     sql = "SELECT * FROM 物资库存信息表 WHERE 物资编号='%s'" % (text_2)
    #     cur.execute(sql)
    #     queryResults = cur.fetchall()
    #     if not queryResults:
    #         self.lineedit_3.setText('')
    #         self.lineedit_4.setText('')
    #         return
    #     sql = "SELECT * FROM 物资信息表 WHERE 物资编号='%s'" % (text_2)
    #     cur.execute(sql)
    #     queryResults = cur.fetchall()
    #     if not queryResults:
    #         self.lineedit_3.setText('')
    #         self.lineedit_4.setText('')
    #         return
    #     self.lineedit_3.setText(queryResults[0][1])
    #     self.lineedit_4.setText(queryResults[0][4])
    #     return

    def buttonCicked(self):
        text_1 = self.lineedit_1.text()
        text_2 = self.lineedit_2.text()
        text_3 = self.lineedit_3.text()
        text_4 = self.lineedit_4.text()

        if (text_1 == "" or text_2 == "" or text_3 == "" ):
            print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            global host_entry
            global password_entry

            # 打开数据库连接

            db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
            cur = db.cursor()
            sql = "INSERT INTO 物资盘存信息表 VALUES ('%s','%s','%s','%s')" % (text_1, text_2, text_3,text_4)
            cur.execute(sql)
            db.commit()

            print(QMessageBox.information(self, "提示", "盘存成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.close()
            self.clearEdit()
            return


    def clearEdit(self):
        self.lineedit_1.clear()
        self.lineedit_2.clear()
        self.lineedit_3.clear()
        self.lineedit_4.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = PCMateral()
    mainMindow.show()
    sys.exit(app.exec_())