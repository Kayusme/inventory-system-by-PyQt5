import sys
from PyQt5.QtWidgets import *
import qdarkstyle
from sign.SignIn import SignInWidget
from sign.SignUp import SignUpWidget
from sign.changePasswordDialog import changePasswordDialog
from company.companyViewer import companyViewer
from wholesale.wholesaleViewer import wholesaleViewer
from base.baseViewer import baseViewer
from purchasing.purchasingViewer import purchasingViewer
import sip

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.resize(1100, 700)
        self.setWindowTitle("欢迎登陆深圳嘉农公司信息管理系统")
        self.bar = self.menuBar()

        self.signUpAction = QAction("注册", self)
        self.changePasswordAction = QAction("修改密码", self)
        self.signInAction = QAction("登录", self)
        self.quitSignInAction = QAction("退出登录", self)
        self.quitAction = QAction("退出", self)


        self.Menu = QMenu("登陆/注册", self)
        self.bar.addMenu(self.Menu)
        self.Menu.addAction(self.signUpAction)
        self.Menu.addAction(self.changePasswordAction)
        self.Menu.addAction(self.signInAction)
        self.Menu.addAction(self.quitSignInAction)
        self.Menu.addAction(self.quitAction)
        self.Menu.triggered[QAction].connect(self.menuTriggered)
        self.signin()

    def signin(self):
        self.widget = SignInWidget()
        self.setCentralWidget(self.widget)
        self.signUpAction.setEnabled(True)
        self.changePasswordAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(False)
        self.widget.is_company_signal[str].connect(self.companySignIn)
        self.widget.is_wholesale_signal[str].connect(self.wholesaleSignIn)
        self.widget.is_base_signal[str].connect(self.baseSignIn)
        self.widget.is_purchasing_signal[str].connect(self.purchasingSignIn)
    def companySignIn(self,admin):
        sip.delete(self.widget)
        self.widget = companyViewer(admin)
        self.setCentralWidget(self.widget)
        self.changePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(False)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)
        self.updatebar(admin+'  欢迎~')
    def wholesaleSignIn(self,admin):
        sip.delete(self.widget)
        self.widget = wholesaleViewer(admin)
        self.setCentralWidget(self.widget)
        self.changePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(False)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)
        self.updatebar(admin+'  欢迎~')
    def baseSignIn(self,admin):
        sip.delete(self.widget)
        self.widget = baseViewer(admin)
        self.setCentralWidget(self.widget)
        self.changePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(False)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)
        self.updatebar(admin+'  欢迎~')
    def purchasingSignIn(self,admin):
        sip.delete(self.widget)
        self.widget = purchasingViewer(admin)
        self.setCentralWidget(self.widget)
        self.changePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(False)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)
        self.updatebar(admin+'  欢迎~')
    def menuTriggered(self, q):
        if(q.text()=="修改密码"):
            changePsdDialog=changePasswordDialog(self)
            changePsdDialog.show()
            changePsdDialog.exec_()
            self.signin()
            self.signUpAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
            return
        if (q.text() == "注册"):
            sip.delete(self.widget)
            self.widget = SignUpWidget()
            self.setCentralWidget(self.widget)
            self.widget.student_signup_signal.connect(self.signin)
            self.signUpAction.setEnabled(False)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(True)
            self.quitSignInAction.setEnabled(False)
            return
        if (q.text() == "退出登录"):
            self.updatebar("登录/注册")
            sip.delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.signUpAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
            self.widget.is_company_signal[str].connect(self.companySignIn)
            self.widget.is_wholesale_signal[str].connect(self.wholesaleSignIn)
            self.widget.is_base_signal[str].connect(self.baseSignIn)
            self.widget.is_purchasing_signal[str].connect(self.purchasingSignIn)
            return
        if (q.text() == "登录"):
            sip.delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.updatebar("登录/注册")
            self.signin()
            self.widget.is_company_signal[str].connect(self.companySignIn)
            self.widget.is_wholesale_signal[str].connect(self.wholesaleSignIn)
            self.widget.is_base_signal[str].connect(self.baseSignIn)
            self.widget.is_purchasing_signal[str].connect(self.purchasingSignIn)
            self.signUpAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
            return
        if (q.text() == "退出"):
            qApp = QApplication.instance()
            qApp.quit()
            return
    def updatebar(self,admin):
        self.bar.clear()
        sip.delete(self.Menu)
        self.Menu = QMenu(admin, self)
        self.bar.addMenu(self.Menu)
        self.Menu.addAction(self.signUpAction)
        self.Menu.addAction(self.changePasswordAction)
        self.Menu.addAction(self.signInAction)
        self.Menu.addAction(self.quitSignInAction)
        self.Menu.addAction(self.quitAction)
        self.Menu.triggered[QAction].connect(self.menuTriggered)
        return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Main()
    mainMindow.show()
    sys.exit(app.exec_())
