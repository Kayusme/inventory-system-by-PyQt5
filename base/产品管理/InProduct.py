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

class InProduct(QWidget):
    def __init__(self, parent=None):
        super(InProduct, self).__init__()
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
        self.addButton = QPushButton("入库")
        self.addButton.setIcon(QIcon('.//image//产品入库.png'))
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
        searchCondision = ['按入库单号查询','按产品编号查询','按产品名称查询']
        self.condisionComboBox.setFixedHeight(32)
        self.condisionComboBox.setFont(font)
        self.condisionComboBox.addItems(searchCondision)

        self.Hlayout2.addWidget(self.searchEdit)
        self.Hlayout2.addWidget(self.searchButton)
        self.Hlayout2.addWidget(self.condisionComboBox)
        self.Hlayout2.addWidget(self.addButton)



        global host_entry
        global password_entry
        self.db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
        self.cur = self.db.cursor()
        sql = "SELECT * FROM 产品收购表"
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
        conditionChoice = self.condisionComboBox.currentText()
        if (conditionChoice == "按入库单号查询"):
            conditionChoice = '单号'
        elif (conditionChoice == "按产品编号查询"):
            conditionChoice = '产品编号'
        else:
            conditionChoice = '产品名称'


        if (self.searchEdit.text() == ""):
            self.begin()
            return
        # 得到模糊查询条件
        temp = self.searchEdit.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%"
        queryCondition = ("SELECT * FROM 产品收购表 WHERE %s LIKE '%s' ORDER BY %s " % (conditionChoice, s, conditionChoice))
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
        addDialog = addInProduct(self)
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
        sql = "SELECT * FROM 产品收购表"
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


class addInProduct(QDialog):

    def __init__(self, parent=None):
        super(addInProduct, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("添加")

    def setUpUI(self):
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel(" 物资入库")
        self.label_1= QLabel("产品编号:")
        self.label_2 = QLabel("产品名称:")
        self.label_3 = QLabel("单价:")
        self.label_4 = QLabel("数量:")
        self.label_5 = QLabel("金额:")
        self.label_6 = QLabel("检验人:")
        self.label_7 = QLabel("经手人:")
        self.label_8 = QLabel("入库时间:")
        self.label_9 = QLabel("片名:")
        self.label_10 = QLabel("农户编号:")
        self.label_11 = QLabel("备注:")

        # button控件
        self.button = QPushButton("入 库")

        # lineEdit控件
        self.lineedit_1 = QLineEdit()
        self.lineedit_2 = QLineEdit()
        self.lineedit_2.setEnabled(False)
        self.lineedit_3 = QLineEdit()
        self.lineedit_3.setEnabled(False)
        self.lineedit_4 = QLineEdit()
        self.lineedit_5 = QLineEdit()
        self.lineedit_5.setEnabled(False)
        self.lineedit_6 = QLineEdit()
        self.lineedit_7 = QLineEdit()
        self.lineedit_8 = QLineEdit()
        self.lineedit_9 = QLineEdit()
        self.lineedit_10 = QLineEdit()
        self.lineedit_11 = QLineEdit()



        self.lineedit_1.setMaxLength(10)
        self.lineedit_2.setMaxLength(10)
        self.lineedit_3.setMaxLength(10)
        self.lineedit_4.setMaxLength(10)
        self.lineedit_5.setMaxLength(10)
        self.lineedit_6.setMaxLength(10)
        self.lineedit_7.setMaxLength(10)
        self.lineedit_8.setMaxLength(10)
        self.lineedit_9.setMaxLength(10)
        self.lineedit_10.setMaxLength(10)
        self.lineedit_11.setMaxLength(10)



        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.label_1, self.lineedit_1)
        self.layout.addRow(self.label_2, self.lineedit_2)
        self.layout.addRow(self.label_3, self.lineedit_3)
        self.layout.addRow(self.label_4, self.lineedit_4)
        self.layout.addRow(self.label_5, self.lineedit_5)
        self.layout.addRow(self.label_6, self.lineedit_6)
        self.layout.addRow(self.label_7, self.lineedit_7)
        self.layout.addRow(self.label_8, self.lineedit_8)
        self.layout.addRow(self.label_9, self.lineedit_9)
        self.layout.addRow(self.label_10, self.lineedit_10)
        self.layout.addRow(self.label_11, self.lineedit_11)

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
        self.label_7.setFont(font)
        self.label_8.setFont(font)
        self.label_9.setFont(font)
        self.label_10.setFont(font)
        self.label_11.setFont(font)

        self.lineedit_1.setFont(font)
        self.lineedit_2.setFont(font)
        self.lineedit_3.setFont(font)
        self.lineedit_4.setFont(font)
        self.lineedit_5.setFont(font)
        self.lineedit_6.setFont(font)
        self.lineedit_7.setFont(font)
        self.lineedit_8.setFont(font)
        self.lineedit_9.setFont(font)
        self.lineedit_10.setFont(font)
        self.lineedit_11.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.button.setFont(font)
        self.button.setFixedHeight(32)
        self.button.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.lineedit_1.textChanged.connect(self.handleTextChanged)
        self.lineedit_4.textChanged.connect(self.lineedit_4_TextChanged)
        self.button.clicked.connect(self.buttonCicked)
        self.db= pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")

    def handleTextChanged(self):
        text_1 = self.lineedit_1.text()
        cur = self.db.cursor()
        sql = "SELECT * FROM 产品收购表 WHERE 产品编号='%s'" % (text_1)
        cur.execute(sql)
        queryResults = cur.fetchall()
        if not queryResults:
            self.lineedit_2.setText('')
            self.lineedit_3.setText('')
            return
        self.lineedit_2.setText(queryResults[0][2])
        self.lineedit_3.setText(queryResults[0][3])
        return
    def lineedit_4_TextChanged(self):
        text_3 = self.lineedit_3.text()
        if not self.lineedit_4.text():
            return
        text_4 = self.lineedit_4.text()
        self.lineedit_5.setText(str(float(text_4) * float(text_3)))

        return
    ####
    def buttonCicked(self):
        text_1 = self.lineedit_1.text()
        text_2 = self.lineedit_2.text()
        text_3 = self.lineedit_3.text()
        text_4 = self.lineedit_4.text()
        text_5 = self.lineedit_5.text()
        text_6 = self.lineedit_6.text()
        text_7 = self.lineedit_7.text()
        text_8 = self.lineedit_8.text()
        text_9 = self.lineedit_9.text()
        text_10 = self.lineedit_10.text()
        text_11 = self.lineedit_11.text()

        if (text_1 == "" or text_2 == "" or text_3 == "" or text_4 == ""  or text_5 == "" or text_6 == ""or text_7 == ""or text_8 == ""or text_9 == ""or text_10 == ""or text_11 == ""):
            print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            global host_entry
            global password_entry
            db_0 = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
            cur_0 = db_0.cursor()
            sql = "SELECT * FROM 农户信息表 WHERE 农户编号='%s'" % (text_10)
            cur_0.execute(sql)
            queryResults_0 = cur_0.fetchall()
            if not queryResults_0:
                print(QMessageBox.warning(self, "警告", "机构编号为[ " + text_10 + " ]不存在！", QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
            # 打开数据库连接
            print("1")
            db_v = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
            cur_v = db_v.cursor()
            sql = "SELECT * FROM 产品收购表"
            cur_v.execute(sql)
            queryResults_v = cur_v.fetchall()
            id = len(queryResults_v)
            db = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
            cur = db.cursor()
            sql = "INSERT INTO 产品收购表 VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (str(id+1),text_1, text_2, text_3,text_4,text_5,text_6,text_7,text_8,text_9,text_10,text_11)
            cur.execute(sql)
            db.commit()
            #库存
            print("2")
            db_c = pymysql.connect(host=host_entry, user="root", password=password_entry, db="sleep")
            cur_c = db_c.cursor()
            sql = "SELECT * FROM 基地产品库存信息"
            cur_c.execute(sql)
            queryResults_c = cur_c.fetchall()
            print("3")
            for Result in queryResults_c:
                if Result[0]==text_1:
                    print("4")
                    sql ="UPDATE 基地产品库存信息 SET 数量='%s' WHERE 产品编号='%s'" % (str(int(text_4)+int(Result[2])),text_1)
                    cur_c.execute(sql)
                    db_c.commit()
                    print(QMessageBox.information(self, "提示", "添加成功!", QMessageBox.Yes, QMessageBox.Yes))
                    self.close()
                    self.clearEdit()
                    return

            print("5")
            sql = "INSERT INTO 基地产品库存信息 VALUES ('%s','%s','%s','%s','%s','%s')" % (text_1, text_2, text_4,'0','0',text_11)
            cur_c.execute(sql)
            db_c.commit()
            print("6")
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
        self.lineedit_7.clear()
        self.lineedit_8.clear()
        self.lineedit_9.clear()
        self.lineedit_10.clear()
        self.lineedit_11.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = InProduct()
    mainMindow.show()
    sys.exit(app.exec_())