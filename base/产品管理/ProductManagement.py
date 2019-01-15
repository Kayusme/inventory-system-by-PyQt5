# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sip
# import qdarkstyle
from base.产品管理.InProduct import InProduct
from base.产品管理.OutProduct import OutProduct
from base.产品管理.ProductInventory import ProductInventory

class ProductManagement(QWidget):
    def __init__(self):
        super(ProductManagement, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)
        self.Information = ProductManagementOption()
        self.layout.addWidget(self.Information)

        self.Information.is_product_signal.connect(self.productCheck)
        self.Information.is_material_signal.connect(self.materialCheck)
        self.Information.is_farmer_signal.connect(self.farmerCheck)


    def productCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = ProductInventory()
        self.layout.addWidget(self.storageView)

    def materialCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = InProduct()
        self.layout.addWidget(self.storageView)

    def farmerCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = OutProduct()
        self.layout.addWidget(self.storageView)

class ProductManagementOption(QWidget):
    is_product_signal = pyqtSignal()
    is_material_signal = pyqtSignal()
    is_farmer_signal = pyqtSignal()

    def __init__(self):
        super(ProductManagementOption, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QVBoxLayout()
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.setLayout(self.layout)
        font = QFont()
        font.setPixelSize(20)
        self.product = QPushButton("产品盘点")
        self.product.setIcon(QIcon('.//image//产品盘点.png'))
        self.material = QPushButton("产品入库")
        self.material.setIcon(QIcon('.//image//产品入库.png'))
        self.farmer = QPushButton("产品出库")
        self.farmer.setIcon(QIcon('.//image//产品出库.png'))

        self.product.setFixedWidth(120)
        self.product.setFixedHeight(40)
        self.material.setFixedWidth(120)
        self.material.setFixedHeight(40)
        self.farmer.setFixedWidth(120)
        self.farmer.setFixedHeight(40)


        self.product.setFont(font)
        self.material.setFont(font)
        self.farmer.setFont(font)


        self.layout1.addWidget(self.product)
        self.layout2.addWidget(self.material)
        self.layout2.addWidget(self.farmer)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)


        self.product.clicked.connect(self.productCheck)
        self.material.clicked.connect(self.materialCheck)
        self.farmer.clicked.connect(self.farmerCheck)


    def productCheck(self):
        self.is_product_signal.emit()
        return
    def materialCheck(self):
        self.is_material_signal.emit()
        return
    def farmerCheck(self):
        self.is_farmer_signal.emit()
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = ProductManagement()
    mainMindow.show()
    sys.exit(app.exec_())