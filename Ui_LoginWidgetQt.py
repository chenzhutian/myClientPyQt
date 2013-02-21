# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\unhealthy\Documents\GitHub\myClientPyQt\LoginWidgetQt.ui'
#
# Created: Fri Feb 22 01:09:44 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName(_fromUtf8("loginDialog"))
        loginDialog.resize(332, 180)
        loginDialog.setMinimumSize(QtCore.QSize(332, 180))
        loginDialog.setMaximumSize(QtCore.QSize(332, 180))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("src/logo_school.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginDialog.setWindowIcon(icon)
        loginDialog.setAutoFillBackground(False)
        loginDialog.setSizeGripEnabled(True)
        loginDialog.setModal(False)
        self.stackedWidget = QtGui.QStackedWidget(loginDialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 331, 191))
        self.stackedWidget.setMinimumSize(QtCore.QSize(331, 191))
        self.stackedWidget.setMaximumSize(QtCore.QSize(331, 191))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.LoginFrame = QtGui.QFrame(self.page)
        self.LoginFrame.setGeometry(QtCore.QRect(0, 0, 331, 191))
        self.LoginFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.LoginFrame.setObjectName(_fromUtf8("LoginFrame"))
        self.LoginTitleabel = QtGui.QLabel(self.LoginFrame)
        self.LoginTitleabel.setGeometry(QtCore.QRect(0, 0, 332, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(22)
        font.setItalic(False)
        self.LoginTitleabel.setFont(font)
        self.LoginTitleabel.setScaledContents(False)
        self.LoginTitleabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginTitleabel.setObjectName(_fromUtf8("LoginTitleabel"))
        self.userCodeLineEdit = QtGui.QLineEdit(self.LoginFrame)
        self.userCodeLineEdit.setGeometry(QtCore.QRect(125, 80, 140, 22))
        self.userCodeLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.userCodeLineEdit.setObjectName(_fromUtf8("userCodeLineEdit"))
        self.userNameLineEdit = QtGui.QLineEdit(self.LoginFrame)
        self.userNameLineEdit.setGeometry(QtCore.QRect(125, 50, 140, 22))
        self.userNameLineEdit.setObjectName(_fromUtf8("userNameLineEdit"))
        self.checkCodeImageLabel = QtGui.QLabel(self.LoginFrame)
        self.checkCodeImageLabel.setGeometry(QtCore.QRect(205, 110, 60, 22))
        self.checkCodeImageLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.checkCodeImageLabel.setText(_fromUtf8(""))
        self.checkCodeImageLabel.setPixmap(QtGui.QPixmap(_fromUtf8("src/checkCode.gif")))
        self.checkCodeImageLabel.setObjectName(_fromUtf8("checkCodeImageLabel"))
        self.checkCodeLineEdit = QtGui.QLineEdit(self.LoginFrame)
        self.checkCodeLineEdit.setGeometry(QtCore.QRect(125, 110, 71, 22))
        self.checkCodeLineEdit.setObjectName(_fromUtf8("checkCodeLineEdit"))
        self.userNamelabel = QtGui.QLabel(self.LoginFrame)
        self.userNamelabel.setGeometry(QtCore.QRect(70, 50, 48, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.userNamelabel.setFont(font)
        self.userNamelabel.setObjectName(_fromUtf8("userNamelabel"))
        self.userCodelabel = QtGui.QLabel(self.LoginFrame)
        self.userCodelabel.setGeometry(QtCore.QRect(70, 80, 32, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.userCodelabel.setFont(font)
        self.userCodelabel.setObjectName(_fromUtf8("userCodelabel"))
        self.checkCodelabel = QtGui.QLabel(self.LoginFrame)
        self.checkCodelabel.setGeometry(QtCore.QRect(70, 110, 48, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkCodelabel.setFont(font)
        self.checkCodelabel.setObjectName(_fromUtf8("checkCodelabel"))
        self.layoutWidget = QtGui.QWidget(self.LoginFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 140, 158, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.loginButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout.addWidget(self.loginButton)
        self.quitButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.horizontalLayout.addWidget(self.quitButton)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.progressBar = QtGui.QProgressBar(self.page_2)
        self.progressBar.setGeometry(QtCore.QRect(40, 120, 261, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.stackedWidget.addWidget(self.page_2)
        self.checkCodeImageLabel.setBuddy(self.checkCodeLineEdit)
        self.userNamelabel.setBuddy(self.userNameLineEdit)
        self.userCodelabel.setBuddy(self.userCodeLineEdit)
        self.checkCodelabel.setBuddy(self.checkCodeLineEdit)

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)
        loginDialog.setTabOrder(self.userNameLineEdit, self.userCodeLineEdit)
        loginDialog.setTabOrder(self.userCodeLineEdit, self.checkCodeLineEdit)
        loginDialog.setTabOrder(self.checkCodeLineEdit, self.loginButton)
        loginDialog.setTabOrder(self.loginButton, self.quitButton)

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(_translate("loginDialog", "登陆", None))
        self.LoginTitleabel.setText(_translate("loginDialog", "绝望2005第三方登陆器", None))
        self.userNamelabel.setText(_translate("loginDialog", "用户名", None))
        self.userCodelabel.setText(_translate("loginDialog", "密码", None))
        self.checkCodelabel.setText(_translate("loginDialog", "验证码", None))
        self.loginButton.setText(_translate("loginDialog", "登陆", None))
        self.quitButton.setText(_translate("loginDialog", "退出", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    loginDialog = QtGui.QDialog()
    ui = Ui_loginDialog()
    ui.setupUi(loginDialog)
    loginDialog.show()
    sys.exit(app.exec_())

