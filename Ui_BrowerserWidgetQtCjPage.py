# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\unhealthy\Documents\GitHub\myClientPyQt\BrowerserWidgetQtCjPage.ui'
#
# Created: Sat Feb 23 12:57:07 2013
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
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.frame.setMinimumSize(QtCore.QSize(960, 540))
        self.frame.setMaximumSize(QtCore.QSize(960, 540))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.cjGroupBox1 = QtGui.QGroupBox(self.frame)
        self.cjGroupBox1.setGeometry(QtCore.QRect(10, 10, 940, 110))
        self.cjGroupBox1.setMinimumSize(QtCore.QSize(940, 110))
        self.cjGroupBox1.setMaximumSize(QtCore.QSize(940, 110))
        self.cjGroupBox1.setTitle(_fromUtf8(""))
        self.cjGroupBox1.setObjectName(_fromUtf8("cjGroupBox1"))
        self.userImformationLabel = QtGui.QLabel(self.cjGroupBox1)
        self.userImformationLabel.setGeometry(QtCore.QRect(10, 10, 921, 41))
        self.userImformationLabel.setObjectName(_fromUtf8("userImformationLabel"))
        self.xnOpptionLabel = QtGui.QLabel(self.cjGroupBox1)
        self.xnOpptionLabel.setGeometry(QtCore.QRect(10, 70, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(14)
        self.xnOpptionLabel.setFont(font)
        self.xnOpptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xnOpptionLabel.setObjectName(_fromUtf8("xnOpptionLabel"))
        self.xnOpptionComboBox = QtGui.QComboBox(self.cjGroupBox1)
        self.xnOpptionComboBox.setGeometry(QtCore.QRect(120, 73, 131, 25))
        self.xnOpptionComboBox.setEditable(False)
        self.xnOpptionComboBox.setObjectName(_fromUtf8("xnOpptionComboBox"))
        self.xqOpptionLabel = QtGui.QLabel(self.cjGroupBox1)
        self.xqOpptionLabel.setGeometry(QtCore.QRect(280, 70, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(14)
        self.xqOpptionLabel.setFont(font)
        self.xqOpptionLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.xqOpptionLabel.setScaledContents(False)
        self.xqOpptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xqOpptionLabel.setObjectName(_fromUtf8("xqOpptionLabel"))
        self.xqOpptioncomboBox = QtGui.QComboBox(self.cjGroupBox1)
        self.xqOpptioncomboBox.setGeometry(QtCore.QRect(400, 73, 131, 25))
        self.xqOpptioncomboBox.setObjectName(_fromUtf8("xqOpptioncomboBox"))
        self.lnCjPushButton = QtGui.QPushButton(self.cjGroupBox1)
        self.lnCjPushButton.setGeometry(QtCore.QRect(620, 70, 80, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        self.lnCjPushButton.setFont(font)
        self.lnCjPushButton.setObjectName(_fromUtf8("lnCjPushButton"))
        self.cjGroupBox_2 = QtGui.QGroupBox(self.frame)
        self.cjGroupBox_2.setGeometry(QtCore.QRect(10, 120, 940, 340))
        self.cjGroupBox_2.setMinimumSize(QtCore.QSize(940, 340))
        self.cjGroupBox_2.setMaximumSize(QtCore.QSize(940, 340))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.cjGroupBox_2.setFont(font)
        self.cjGroupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cjGroupBox_2.setObjectName(_fromUtf8("cjGroupBox_2"))
        self.cjTableWidget = QtGui.QTableWidget(self.cjGroupBox_2)
        self.cjTableWidget.setGeometry(QtCore.QRect(10, 20, 921, 311))
        self.cjTableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.cjTableWidget.setRowCount(5)
        self.cjTableWidget.setColumnCount(5)
        self.cjTableWidget.setObjectName(_fromUtf8("cjTableWidget"))
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.cjTableWidget.setItem(0, 0, item)
        self.userGPALabel = QtGui.QLabel(self.frame)
        self.userGPALabel.setGeometry(QtCore.QRect(10, 465, 940, 31))
        self.userGPALabel.setObjectName(_fromUtf8("userGPALabel"))
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
        self.userImformationLabel.setBuddy(self.cjTableWidget)
        self.xnOpptionLabel.setBuddy(self.xnOpptionComboBox)
        self.xqOpptionLabel.setBuddy(self.xqOpptioncomboBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "绝望2005第三方登陆系统", None))
        self.userImformationLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.xnOpptionLabel.setText(_translate("MainWindow", "学年", None))
        self.xqOpptionLabel.setText(_translate("MainWindow", "学期", None))
        self.lnCjPushButton.setText(_translate("MainWindow", "历年成绩", None))
        self.cjGroupBox_2.setTitle(_translate("MainWindow", "成绩", None))
        __sortingEnabled = self.cjTableWidget.isSortingEnabled()
        self.cjTableWidget.setSortingEnabled(False)
        item = self.cjTableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "111222", None))
        self.cjTableWidget.setSortingEnabled(__sortingEnabled)
        self.userGPALabel.setText(_translate("MainWindow", "TextLabel", None))
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

