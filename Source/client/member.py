from PyQt5 import QtCore, QtGui, QtWidgets
from client_utils import *

class Ui_Member(object):
    def show_detail(self, data, connection):
        receive_user_image(connection, data['user_id'])
        img = "border-image: url(" + data['image'] + ");"
        self.show_frame.image.setStyleSheet("border-radius: 80px;\n " + img)
        self.show_frame.id.setText('ID: ' + data['user_id'])
        self.show_frame.name.setText('Name: ' + data['name'])
        self.show_frame.phone_num.setText('Phone number: ' + data['phone'])
        self.show_frame.email.setText('Email: ' + data['email'])
        self.show_frame.gender.setText('Gender: ' + data['gender'])
    
    def setupUi(self, Member, data, show_frame, connection):
        Member.setObjectName("Member")
        Member.resize(350, 180)
        Member.setMinimumSize(QtCore.QSize(350, 180))
        Member.setMaximumSize(QtCore.QSize(350, 180))
        self.show_frame = show_frame
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Member)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nested = QtWidgets.QFrame(Member)
        self.nested.setMinimumSize(QtCore.QSize(350, 180))
        self.nested.setMaximumSize(QtCore.QSize(350, 180))
        self.nested.setStyleSheet("QFrame#nested{    \n"
"    border-style: solid;    \n"
"    border-width: 3px;\n"
"    border-color: gray;\n"
"    border-radius: 20px;\n"
"    background-color: white;\n"
"}")
        self.nested.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nested.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nested.setObjectName("nested")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.nested)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QPushButton(self.nested)
        self.icon.setMinimumSize(QtCore.QSize(80, 80))
        self.icon.setMaximumSize(QtCore.QSize(80, 80))
        self.icon.setStyleSheet("border-radius: 40px;")
        self.icon.setText("")
        self.icon.setIconSize(QtCore.QSize(100, 100))
        self.icon.setFlat(False)
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.frame = QtWidgets.QFrame(self.nested)
        self.frame.setStyleSheet("QFrame#frame{    \n"
"    border-style: outset;    \n"
"    border-width: 2px;\n"
"    border-color: gray;\n"
"    border-radius: 10px;\n"
"    background-color: #eeeeee;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(10, 20, 10, 20)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Name = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.verticalLayout.addWidget(self.Name)
        self.Phone = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.Phone.setFont(font)
        self.Phone.setObjectName("Phone")
        self.verticalLayout.addWidget(self.Phone)
        self.detail = QtWidgets.QPushButton(self.frame, clicked=lambda: self.show_detail(data, connection))
        self.detail.setMinimumSize(QtCore.QSize(0, 30))
        self.detail.setMaximumSize(QtCore.QSize(16777215, 30))
        self.detail.setStyleSheet("color: blue;\n"
"text-align: left;")
        self.detail.setFlat(True)
        self.detail.setObjectName("detail")
        self.verticalLayout.addWidget(self.detail)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.nested)

        self.retranslateUi(Member)

        self.Phone.setText('Phone: ' + data['phone'])
        self.Name.setText('Name: ' + data['name'])
        thumn = "border-image: url(" + data['thumbnail'] + ");"
        self.icon.setStyleSheet("border-radius: 40px;\n " + thumn)

        QtCore.QMetaObject.connectSlotsByName(Member)

    def retranslateUi(self, Member):
        _translate = QtCore.QCoreApplication.translate
        Member.setWindowTitle(_translate("Member", "Frame"))
        self.Name.setText(_translate("Member", "Name: Nguyen Van A"))
        self.Phone.setText(_translate("Member", "Phone: 01234567"))
        self.detail.setText(_translate("Member", ">> More details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Member = QtWidgets.QFrame()
    ui = Ui_Member()
    ui.setupUi(Member)
    Member.show()
    sys.exit(app.exec_())
