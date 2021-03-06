# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import qdarkstyle

from wholesale.信息查询.InformationInquiry import InformationInquiry
from wholesale.库存管理.InInventoryManagement import InInventoryMangement
from wholesale.销售管理.InSalesManagement import InSalesManagement

import sip

class wholesaleViewer(QWidget):
    def __init__(self,admin):
        super().__init__()
        self.admin = admin
        self.setUpUI()

    def setUpUI(self):
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        # self.setStyleSheet("QWidget{background-color: White}")
        self.layout_all = QVBoxLayout()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(13, 13, 13, 13)
        self.buttonlayout = QVBoxLayout()
        self.setLayout(self.layout_all)

        self.TP = QLabel()
        pixmap = QPixmap(".//image//深圳嘉农.jpg")  # 按指定路径找到图片
        self.TP.setPixmap(pixmap)  # 在label上显示图片
        self.TP.setScaledContents(True)  # 让图片自适应label大小
        # lbl.setPixmap(QPixmap(""))#移除label上的图片
        self.layout_all.addWidget(self.TP)

        font = QFont()
        font.setPixelSize(16)
        self.publicButton = QPushButton("信息查询")
        self.produceButton = QPushButton("库存管理")
        self.applicationButton = QPushButton("销售管理")



        self.publicButton.setFont(font)
        self.produceButton.setFont(font)
        self.applicationButton.setFont(font)


        self.publicButton.setFixedWidth(110)
        self.publicButton.setFixedHeight(42)
        self.produceButton.setFixedWidth(110)
        self.produceButton.setFixedHeight(42)
        self.applicationButton.setFixedWidth(110)
        self.applicationButton.setFixedHeight(42)




        self.buttonlayout.addWidget(self.publicButton)
        self.buttonlayout.addWidget(self.produceButton)
        self.buttonlayout.addWidget(self.applicationButton)

        self.buttonlayout.addStretch()


        self.layout.addLayout(self.buttonlayout)


        self.publicButton.setStyleSheet("QPushButton{background: ;}")
        self.produceButton.setStyleSheet("QPushButton{background: 	DimGray;}")
        self.applicationButton.setStyleSheet("QPushButton{background: DimGray;}")



        self.storageView = InformationInquiry()
        self.layout.addWidget(self.storageView)
        self.layout_all.addLayout(self.layout)

        self.publicButton.clicked.connect(self.publicButtonClicked)
        self.produceButton.clicked.connect(self.produceButtonClicked)
        self.applicationButton.clicked.connect(self.applicationButtonClicked)


    def publicButtonClicked(self):
        self.publicButton.setStyleSheet("QPushButton{background:  ;}")
        self.produceButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.applicationButton.setStyleSheet("QPushButton{background: DimGray;}")


        self.layout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = InformationInquiry()
        self.layout.addWidget(self.storageView)

    def produceButtonClicked(self):
        self.publicButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.produceButton.setStyleSheet("QPushButton{background:  ;}")
        self.applicationButton.setStyleSheet("QPushButton{background: DimGray;}")


        self.layout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = InInventoryMangement()
        self.layout.addWidget(self.storageView)

    def applicationButtonClicked(self):
        self.publicButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.produceButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.applicationButton.setStyleSheet("QPushButton{background:  ;}")


        self.layout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = InSalesManagement()
        self.layout.addWidget(self.storageView)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = wholesaleViewer(123)
    mainMindow.show()
    sys.exit(app.exec_())
