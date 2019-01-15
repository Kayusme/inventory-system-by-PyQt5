# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# import qdarkstyle
import sip
from base.信息查询.ProductionPlanningQuery import ProductionPlanningQuery
from base.信息查询.ProductInventoryQuery import ProductInventoryQuery
from base.信息查询.MaterialInformationQuery import MaterialInformationQuery
from base.信息查询.MaterialInventoryQuery import MaterialInventoryQuery

class InformationQuery(QWidget):
    def __init__(self):
        super(InformationQuery, self).__init__()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎使用设计管理系统")
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)
        self.Information = InformationOption()
        self.layout.addWidget(self.Information)

        self.Information.is_production_signal.connect(self.productionCheck)
        self.Information.is_product_signal.connect(self.ProductCheck)
        self.Information.is_MaterialF_signal.connect(self.MaterialFCheck)
        self.Information.is_MaterialV_signal.connect(self.MaterialVCheck)

    def productionCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = ProductionPlanningQuery()
        self.layout.addWidget(self.storageView)

    def ProductCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = ProductInventoryQuery()
        self.layout.addWidget(self.storageView)

    def MaterialFCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = MaterialInformationQuery()
        self.layout.addWidget(self.storageView)

    def MaterialVCheck(self):
        self.layout.removeWidget(self.Information)
        sip.delete(self.Information)
        self.storageView = MaterialInventoryQuery()
        self.layout.addWidget(self.storageView)

class InformationOption(QWidget):
    is_production_signal = pyqtSignal()
    is_product_signal = pyqtSignal()
    is_MaterialF_signal = pyqtSignal()
    is_MaterialV_signal = pyqtSignal()
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
        self.production = QPushButton("生产计划")
        self.production.setIcon(QIcon('.//image//生产计划.png'))
        self.product = QPushButton("产品库存")
        self.product.setIcon(QIcon('.//image//产品库存.png'))
        self.MaterialF = QPushButton("物资信息")
        self.MaterialF.setIcon(QIcon('.//image//物资信息.png'))
        self.MaterialV = QPushButton("物资库存")
        self.MaterialV.setIcon(QIcon('.//image//物资库存.png'))

        self.production.setFixedWidth(120)
        self.production.setFixedHeight(40)
        self.product.setFixedWidth(120)
        self.product.setFixedHeight(40)
        self.MaterialF.setFixedWidth(120)
        self.MaterialF.setFixedHeight(40)
        self.MaterialV.setFixedWidth(120)
        self.MaterialV.setFixedHeight(40)



        self.production.setFont(font)
        self.product.setFont(font)
        self.MaterialF.setFont(font)
        self.MaterialV.setFont(font)

        self.layout1.addWidget(self.production)
        self.layout1.addWidget(self.product)
        self.layout2.addWidget(self.MaterialF)
        self.layout2.addWidget(self.MaterialV)
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)


        self.production.clicked.connect(self.productionCheck)
        self.product.clicked.connect(self.productCheck)
        self.MaterialF.clicked.connect(self.MaterialFCheck)
        self.MaterialV.clicked.connect(self.MaterialVCheck)

    def productionCheck(self):
        self.is_production_signal.emit()
        return
    def productCheck(self):
        self.is_product_signal.emit()
        return
    def MaterialFCheck(self):
        self.is_MaterialF_signal.emit()
        return

    def MaterialVCheck(self):
        self.is_MaterialV_signal.emit()
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = InformationQuery()
    mainMindow.show()
    sys.exit(app.exec_())