# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sip
from wholesale.库存管理.ProductInstock import ProductInstock
from wholesale.库存管理.ProductInventory import ProductInventory
from wholesale.库存管理.GoStock import GoStock
from wholesale.库存管理.InStock import InStock


class InInventoryMangement(QWidget):
    def __init__(self):
        super(InInventoryMangement, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)
        self.Information = InformationOption()
        self.layout.addWidget(self.Information)

        self.Information.is_product_signal.connect(self.productCheck)
        self.Information.is_material_signal.connect(self.materialCheck)
        self.Information.is_farmer_signal.connect(self.farmerCheck)
        self.Information.is_customer_signal.connect(self.customerCheck)

    def productCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = ProductInstock()
        self.layout.addWidget(self.storageView)

    def materialCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = ProductInventory()
        self.layout.addWidget(self.storageView)

    def farmerCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = GoStock()
        self.layout.addWidget(self.storageView)

    def customerCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = InStock()
        self.layout.addWidget(self.storageView)



class InformationOption(QWidget):
    is_product_signal = pyqtSignal()
    is_material_signal = pyqtSignal()
    is_farmer_signal = pyqtSignal()
    is_customer_signal = pyqtSignal()
    def __init__(self):
        super(InformationOption, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QVBoxLayout()
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.setLayout(self.layout)
        font = QFont()
        font.setPixelSize(20)
        self.product = QPushButton("产品入库")
        self.product.setIcon(QIcon('.//image//产品信息.png'))
        self.material = QPushButton("产品盘存")
        self.material.setIcon(QIcon('.//image//物资信息.png'))
        self.farmer = QPushButton("产品出库")
        self.farmer.setIcon(QIcon('.//image//农户信息.png'))
        self.customer = QPushButton("产品库存")
        self.customer.setIcon(QIcon('.//image//顾客信息.png'))

        self.product.setFixedWidth(120)
        self.product.setFixedHeight(40)
        self.material.setFixedWidth(120)
        self.material.setFixedHeight(40)
        self.farmer.setFixedWidth(120)
        self.farmer.setFixedHeight(40)
        self.customer.setFixedWidth(120)
        self.customer.setFixedHeight(40)



        self.product.setFont(font)
        self.material.setFont(font)
        self.farmer.setFont(font)
        self.customer.setFont(font)

        self.layout1.addWidget(self.product)
        self.layout1.addWidget(self.material)
        self.layout2.addWidget(self.farmer)
        self.layout2.addWidget(self.customer)
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)


        self.product.clicked.connect(self.productCheck)
        self.material.clicked.connect(self.materialCheck)
        self.farmer.clicked.connect(self.farmerCheck)
        self.customer.clicked.connect(self.customerCheck)

    def productCheck(self):
        self.is_product_signal.emit()
        return
    def materialCheck(self):
        self.is_material_signal.emit()
        return
    def farmerCheck(self):
        self.is_farmer_signal.emit()
        return

    def customerCheck(self):
        self.is_customer_signal.emit()
        return

    # def mechanismCheck(self):
    #     self.is_mechanism_signal.emit()
    #     return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = InInventoryMangement()
    mainMindow.show()
    sys.exit(app.exec_())