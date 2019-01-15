# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sip
from wholesale.信息查询.InventoryInformationInquiry import InventoryInformationInquiry
from wholesale.信息查询.ProductInformationInquiry import ProductInformationInquiry

class InformationInquiry(QWidget):
    def __init__(self):
        super(InformationInquiry, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.Information = InformationInquiryOption()
        self.layout.addWidget(self.Information)

        self.Information.is_product_signal.connect(self.productCheck)
        self.Information.is_material_signal.connect(self.materialCheck)


    def productCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = InventoryInformationInquiry()
        self.layout.addWidget(self.storageView)

    def materialCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = ProductInformationInquiry()
        self.layout.addWidget(self.storageView)

class InformationInquiryOption(QWidget):
    is_product_signal = pyqtSignal()
    is_material_signal = pyqtSignal()
    def __init__(self):
        super(InformationInquiryOption, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QVBoxLayout()
        self.layout1 = QHBoxLayout()
        self.setLayout(self.layout)
        font = QFont()
        font.setPixelSize(20)
        self.product = QPushButton("产品信息查询")
        self.product.setIcon(QIcon('.//image//产品信息查询.png'))
        self.material = QPushButton("产品库存查询")
        self.material.setIcon(QIcon('.//image//产品库存查询.png'))

        self.product.setFixedWidth(160)
        self.product.setFixedHeight(40)
        self.material.setFixedWidth(160)
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
    mainMindow = InformationInquiry()
    mainMindow.show()
    sys.exit(app.exec_())