# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sip
# import qdarkstyle
from purchasing.物资管理.InMaterialManagement import InMaterialManagement
from purchasing.物资管理.GoMaterialManagement import GoMaterialManagement
from purchasing.物资管理.NowMaterialManagement import NowMaterialManagement
from purchasing.物资管理.PCMateral import PCMateral

class MaterialManagement(QWidget):
    def __init__(self):
        super(MaterialManagement, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)
        self.Information = MaterialManagementOption()
        self.layout.addWidget(self.Information)

        self.Information.is_product_signal.connect(self.productCheck)
        self.Information.is_material_signal.connect(self.materialCheck)
        self.Information.is_farmer_signal.connect(self.farmerCheck)
        self.Information.is_PC_signal.connect(self.PCCheck)


    def productCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = NowMaterialManagement()
        self.layout.addWidget(self.storageView)

    def materialCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = InMaterialManagement()
        self.layout.addWidget(self.storageView)

    def farmerCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = GoMaterialManagement()
        self.layout.addWidget(self.storageView)
    def PCCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = PCMateral()
        self.layout.addWidget(self.storageView)

class MaterialManagementOption(QWidget):
    is_product_signal = pyqtSignal()
    is_material_signal = pyqtSignal()
    is_farmer_signal = pyqtSignal()
    is_PC_signal = pyqtSignal()

    def __init__(self):
        super(MaterialManagementOption, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QVBoxLayout()
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()

        self.setLayout(self.layout)
        font = QFont()
        font.setPixelSize(20)
        self.product = QPushButton("物资库存")
        self.product.setIcon(QIcon('.//image//物资库存.png'))
        self.PC = QPushButton("物资盘存")
        self.PC.setIcon(QIcon('.//image//物资盘点.png'))
        self.material = QPushButton("物资入库")
        self.material.setIcon(QIcon('.//image//物资入库.png'))
        self.farmer = QPushButton("物资出库")
        self.farmer.setIcon(QIcon('.//image//物资出库.png'))

        self.product.setFixedWidth(120)
        self.product.setFixedHeight(40)
        self.PC.setFixedWidth(120)
        self.PC.setFixedHeight(40)
        self.material.setFixedWidth(120)
        self.material.setFixedHeight(40)
        self.farmer.setFixedWidth(120)
        self.farmer.setFixedHeight(40)


        self.product.setFont(font)
        self.PC.setFont(font)
        self.material.setFont(font)
        self.farmer.setFont(font)


        self.layout1.addWidget(self.product)
        self.layout1.addWidget(self.PC)
        self.layout2.addWidget(self.material)
        self.layout2.addWidget(self.farmer)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.product.clicked.connect(self.productCheck)
        self.PC.clicked.connect(self.PCCheck)
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
    def PCCheck(self):
        self.is_PC_signal.emit()
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = MaterialManagement()
    mainMindow.show()
    sys.exit(app.exec_())