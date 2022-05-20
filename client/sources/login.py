from PyQt5 import QtCore, QtGui, QtWidgets
from contact import Ui_Phonebook
import socket
from client_utils import *

class Ui_Login(object):
    def open_phonebook(self, parent):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        try:
            ip_addr = self.ip.text()
            port_num = int(self.port.text())
            client.connect((ip_addr, port_num))
            client.recv(1024).decode(cfg['FORMAT']) # get response
            answer_response(client, cfg['FORMAT']) # answer response
            
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Phonebook()
            self.ui.setupUi(self.window, client)
            self.window.show()
            Login.close()
        except:
            QtWidgets.QMessageBox.about(parent, "Notification !!!", "Wrong IP Address or Port !!!")

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(350, 397)
        Login.setWindowIcon(QtGui.QIcon('./icons/phonebook.png'))
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame01 = QtWidgets.QFrame(self.centralwidget)
        self.frame01.setMinimumSize(QtCore.QSize(0, 150))
        self.frame01.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame01.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame01.setObjectName("frame01")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame01)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.icon = QtWidgets.QPushButton(self.frame01)
        self.icon.setMinimumSize(QtCore.QSize(120, 120))
        self.icon.setMaximumSize(QtCore.QSize(120, 120))
        self.icon.setStyleSheet("border-radius: 30px;")
        self.icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/ic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.setIcon(icon)
        self.icon.setIconSize(QtCore.QSize(100, 100))
        self.icon.setFlat(True)
        self.icon.setObjectName("icon")
        self.verticalLayout_3.addWidget(self.icon, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame01)
        self.frame02 = QtWidgets.QFrame(self.centralwidget)
        self.frame02.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame02.setObjectName("frame02")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame02)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ip = QtWidgets.QLineEdit(self.frame02)
        self.ip.setMinimumSize(QtCore.QSize(0, 40))
        self.ip.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.ip.setFont(font)
        self.ip.setObjectName("ip")
        self.verticalLayout_2.addWidget(self.ip)
        self.port = QtWidgets.QLineEdit(self.frame02)
        self.port.setMinimumSize(QtCore.QSize(0, 40))
        self.port.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.port.setFont(font)
        self.port.setObjectName("port")
        self.verticalLayout_2.addWidget(self.port)
        self.login = QtWidgets.QPushButton(self.frame02, clicked=lambda: self.open_phonebook(Login))
        self.login.setMinimumSize(QtCore.QSize(0, 50))
        self.login.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.verticalLayout_2.addWidget(self.login)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame02)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login Page"))
        self.ip.setPlaceholderText(_translate("Login", "IP Address"))
        self.port.setPlaceholderText(_translate("Login", "Port"))
        self.login.setText(_translate("Login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
