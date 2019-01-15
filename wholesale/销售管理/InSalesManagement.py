# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sip
from wholesale.销售管理.CustomerInformationSettings import CustomerInformationSettings
from wholesale.销售管理.SalesStatisticss import SalesStatisticss


class InSalesManagement(QWidget):
    def __init__(self):
        super(InSalesManagement, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.Information = InSalesManagementOption()
        self.layout.addWidget(self.Information)

        self.Information.is_product_signal.connect(self.productCheck)
        self.Information.is_material_signal.connect(self.materialCheck)


    def productCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = CustomerInformationSettings()
        self.layout.addWidget(self.storageView)

    def materialCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = SalesStatisticss()
        self.layout.addWidget(self.storageView)

class InSalesManagementOption(QWidget):
    is_product_signal = pyqtSignal()
    is_material_signal = pyqtSignal()
    def __init__(self):
        super(InSalesManagementOption, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QVBoxLayout()
        self.layout1 = QHBoxLayout()
        self.setLayout(self.layout)
        font = QFont()
        font.setPixelSize(20)
        self.product = QPushButton("顾客信息")
        self.product.setIcon(QIcon('.//image//顾客信息.png'))
        self.material = QPushButton("销售统计")
        self.material.setIcon(QIcon('.//image//销售统计.png'))

        self.product.setFixedWidth(120)
        self.product.setFixedHeight(40)
        self.material.setFixedWidth(120)
        self.material.setFixedHeight(40)



        self.product.setFont(font)
        self.material.setFont(font)


        self.layout1.addWidget(self.product)
        self.layout1.addWidget(self.material)

        self.layout.addLayout(self.layout1)


        self.product.clicked.connect(self.productCheck)
        self.material.clicked.connect(self.materialCheck)

    def productCheck(self):
        self.is_product_signal.emit()
        return
    def materialCheck(self):
        self.is_material_signal.emit()
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = InSalesManagement()
    mainMindow.show()
    sys.exit(app.exec_())