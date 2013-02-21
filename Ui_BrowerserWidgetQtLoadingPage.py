# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\unhealthy\Documents\GitHub\myClientPyQt\BrowerserWidgetQtLoadingPage.ui'
#
# Created: Thu Feb 21 22:17:20 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(960, 540)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("src/logo_school.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.loadingLabel = QtGui.QLabel(self.frame)
        self.loadingLabel.setGeometry(QtCore.QRect(190, 130, 591, 180))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Kristen ITC"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.loadingLabel.setFont(font)
        self.loadingLabel.setFrameShape(QtGui.QFrame.Box)
        self.loadingLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.loadingLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.loadingLabel.setObjectName(_fromUtf8("loadingLabel"))
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(230, 240, 520, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.BrowerserMenuBar = QtGui.QMenuBar(MainWindow)
        self.BrowerserMenuBar.setGeometry(QtCore.QRect(0, 0, 960, 23))
        self.BrowerserMenuBar.setObjectName(_fromUtf8("BrowerserMenuBar"))
        self.xyMenu = QtGui.QMenu(self.BrowerserMenuBar)
        self.xyMenu.setObjectName(_fromUtf8("xyMenu"))
        self.xkMenu = QtGui.QMenu(self.BrowerserMenuBar)
        self.xkMenu.setObjectName(_fromUtf8("xkMenu"))
        self.syMenu = QtGui.QMenu(self.BrowerserMenuBar)
        self.syMenu.setObjectName(_fromUtf8("syMenu"))
        MainWindow.setMenuBar(self.BrowerserMenuBar)
        self.cjAction = QtGui.QAction(MainWindow)
        self.cjAction.setObjectName(_fromUtf8("cjAction"))
        self.kbAction = QtGui.QAction(MainWindow)
        self.kbAction.setObjectName(_fromUtf8("kbAction"))
        self.xsxkAction = QtGui.QAction(MainWindow)
        self.xsxkAction.setObjectName(_fromUtf8("xsxkAction"))
        self.syAction = QtGui.QAction(MainWindow)
        self.syAction.setObjectName(_fromUtf8("syAction"))
        self.logoutAction = QtGui.QAction(MainWindow)
        self.logoutAction.setObjectName(_fromUtf8("logoutAction"))
        self.xyMenu.addAction(self.cjAction)
        self.xyMenu.addAction(self.kbAction)
        self.xkMenu.addAction(self.xsxkAction)
        self.syMenu.addAction(self.syAction)
        self.syMenu.addSeparator()
        self.syMenu.addAction(self.logoutAction)
        self.BrowerserMenuBar.addAction(self.syMenu.menuAction())
        self.BrowerserMenuBar.addAction(self.xyMenu.menuAction())
        self.BrowerserMenuBar.addAction(self.xkMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "绝望2005第三方登陆系统", None))
        self.loadingLabel.setText(_translate("MainWindow", "Loading", None))
        self.xyMenu.setTitle(_translate("MainWindow", "信息查询", None))
        self.xkMenu.setTitle(_translate("MainWindow", "选课", None))
        self.syMenu.setTitle(_translate("MainWindow", "首页", None))
        self.cjAction.setText(_translate("MainWindow", "成绩查询", None))
        self.kbAction.setText(_translate("MainWindow", "课表查询", None))
        self.xsxkAction.setText(_translate("MainWindow", "学生选课", None))
        self.syAction.setText(_translate("MainWindow", "首页", None))
        self.logoutAction.setText(_translate("MainWindow", "退出", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

