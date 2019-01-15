# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import qdarkstyle

from purchasing.产品管理.ProductManagement import ProductManagement
from purchasing.物资管理.MaterialManagement import MaterialManagement
from purchasing.生产计划.ProductionPlan import ProductionPlan
from purchasing.农户管理.FarmerManagement import FarmerManagement

import sip
'''代购点 '''
class purchasingViewer(QWidget):
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
        self.publicButton = QPushButton("产品管理")
        self.produceButton = QPushButton("物资管理")
        self.applicationButton = QPushButton("生产计划")
        self.finaButton = QPushButton("农户管理")


        self.publicButton.setFont(font)
        self.produceButton.setFont(font)
        self.applicationButton.setFont(font)
        self.finaButton.setFont(font)

        self.publicButton.setFixedWidth(110)
        self.publicButton.setFixedHeight(42)
        self.produceButton.setFixedWidth(110)
        self.produceButton.setFixedHeight(42)
        self.applicationButton.setFixedWidth(110)
        self.applicationButton.setFixedHeight(42)
        self.finaButton.setFixedWidth(110)
        self.finaButton.setFixedHeight(42)
        self.publicButton.setFixedHeight(42)



        self.buttonlayout.addWidget(self.publicButton)
        self.buttonlayout.addWidget(self.produceButton)
        self.buttonlayout.addWidget(self.applicationButton)
        self.buttonlayout.addWidget(self.finaButton)
        self.buttonlayout.addStretch()


        self.layout.addLayout(self.buttonlayout)


        self.publicButton.setStyleSheet("QPushButton{background: ;}")
        self.produceButton.setStyleSheet("QPushButton{background: 	DimGray;}")
        self.applicationButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.finaButton.setStyleSheet("QPushButton{background: DimGray;}")


        self.storageView = ProductManagement()
        self.layout.addWidget(self.storageView)
        self.layout_all.addLayout(self.layout)

        self.publicButton.clicked.connect(self.publicButtonClicked)
        self.produceButton.clicked.connect(self.produceButtonClicked)
        self.applicationButton.clicked.connect(self.applicationButtonClicked)
        self.finaButton.clicked.connect(self.finaButtonClicked)

    def publicButtonClicked(self):
        self.publicButton.setStyleSheet("QPushButton{background:  ;}")
        self.produceButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.applicationButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.finaButton.setStyleSheet("QPushButton{background: DimGray;}")

        self.layout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = ProductManagement()
        self.layout.addWidget(self.storageView)

    def produceButtonClicked(self):
        self.publicButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.produceButton.setStyleSheet("QPushButton{background:  ;}")
        self.applicationButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.finaButton.setStyleSheet("QPushButton{background:DimGray ;}")

        self.layout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = MaterialManagement()
        self.layout.addWidget(self.storageView)

    def applicationButtonClicked(self):
        self.publicButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.produceButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.applicationButton.setStyleSheet("QPushButton{background:  ;}")
        self.finaButton.setStyleSheet("QPushButton{background: DimGray;}")

        self.layout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = ProductionPlan()
        self.layout.addWidget(self.storageView)

    def finaButtonClicked(self):
        self.publicButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.produceButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.applicationButton.setStyleSheet("QPushButton{background: DimGray;}")
        self.finaButton.setStyleSheet("QPushButton{background:  ;}")

        self.layout.removeWidget(self.storageView)
        sip.delete(self.storageView)
        self.storageView = FarmerManagement()
        self.layout.addWidget(self.storageView)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = purchasingViewer(123)
    mainMindow.show()
    sys.exit(app.exec_())
