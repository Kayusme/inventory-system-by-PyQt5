# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# import qdarkstyle
import sip
from company.信息设置.ProductInformation import ProductInformation
from company.信息设置.CustomerInformation import CustomerInformation
from company.信息设置.FarmerInformation import FarmerInformation
from company.信息设置.MaterialInformation import MaterialInformation
from company.信息设置.MechanismInformation import MechanismInformation
class InformationSetup(QWidget):
    def __init__(self):
        super(InformationSetup, self).__init__()
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
        self.Information.is_mechanism_signal.connect(self.mechanismCheck)

    def productCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = ProductInformation()
        self.layout.addWidget(self.storageView)

    def materialCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = MaterialInformation()
        self.layout.addWidget(self.storageView)

    def farmerCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = FarmerInformation()
        self.layout.addWidget(self.storageView)

    def customerCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = CustomerInformation()
        self.layout.addWidget(self.storageView)

    def mechanismCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = MechanismInformation()
        self.layout.addWidget(self.storageView)

class InformationOption(QWidget):
    is_product_signal = pyqtSignal()
    is_material_signal = pyqtSignal()
    is_farmer_signal = pyqtSignal()
    is_customer_signal = pyqtSignal()
    is_mechanism_signal = pyqtSignal()
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
        self.product = QPushButton("产品信息")
        self.product.setIcon(QIcon('.//image//产品信息.png'))
        self.material = QPushButton("物资信息")
        self.material.setIcon(QIcon('.//image//物资信息.png'))
        self.farmer = QPushButton("农户信息")
        self.farmer.setIcon(QIcon('.//image//农户信息.png'))
        self.customer = QPushButton("顾客信息")
        self.customer.setIcon(QIcon('.//image//顾客信息.png'))
        self.mechanism = QPushButton("公司机构")
        self.mechanism.setIcon(QIcon('.//image//公司机构.png'))

        self.product.setFixedWidth(120)
        self.product.setFixedHeight(40)
        self.material.setFixedWidth(120)
        self.material.setFixedHeight(40)
        self.farmer.setFixedWidth(120)
        self.farmer.setFixedHeight(40)
        self.customer.setFixedWidth(120)
        self.customer.setFixedHeight(40)
        self.mechanism.setFixedWidth(120)
        self.mechanism.setFixedHeight(40)



        self.product.setFont(font)
        self.material.setFont(font)
        self.farmer.setFont(font)
        self.customer.setFont(font)
        self.mechanism.setFont(font)

        self.layout1.addWidget(self.product)
        self.layout1.addWidget(self.material)
        self.layout1.addWidget(self.farmer)
        self.layout2.addWidget(self.customer)
        self.layout2.addWidget(self.mechanism)
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)


        self.product.clicked.connect(self.productCheck)
        self.material.clicked.connect(self.materialCheck)
        self.farmer.clicked.connect(self.farmerCheck)
        self.customer.clicked.connect(self.customerCheck)
        self.mechanism.clicked.connect(self.mechanismCheck)

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

    def mechanismCheck(self):
        self.is_mechanism_signal.emit()
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = InformationSetup()
    mainMindow.show()
    sys.exit(app.exec_())