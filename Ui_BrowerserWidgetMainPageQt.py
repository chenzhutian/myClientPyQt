# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\unhealthy\Documents\GitHub\myClientPyQt\BrowerserWidgetMainPageQt.ui'
#
# Created: Thu Feb 21 12:23:49 2013
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
        self.centralWidget.setMinimumSize(QtCore.QSize(960, 540))
        self.centralWidget.setMaximumSize(QtCore.QSize(960, 540))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.stackedWidget.setMinimumSize(QtCore.QSize(960, 540))
        self.stackedWidget.setMaximumSize(QtCore.QSize(960, 540))
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.mainPage = QtGui.QWidget()
        self.mainPage.setObjectName(_fromUtf8("mainPage"))
        self.mainFrame = QtGui.QFrame(self.mainPage)
        self.mainFrame.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.calendarWidget = QtGui.QCalendarWidget(self.mainFrame)
        self.calendarWidget.setGeometry(QtCore.QRect(530, 110, 361, 251))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.welcomePageLabel = QtGui.QLabel(self.mainFrame)
        self.welcomePageLabel.setGeometry(QtCore.QRect(90, 110, 371, 241))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.welcomePageLabel.setFont(font)
        self.welcomePageLabel.setFrameShape(QtGui.QFrame.Box)
        self.welcomePageLabel.setFrameShadow(QtGui.QFrame.Raised)
        self.welcomePageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomePageLabel.setObjectName(_fromUtf8("welcomePageLabel"))
        self.userWelcomeLabel = QtGui.QLabel(self.mainFrame)
        self.userWelcomeLabel.setGeometry(QtCore.QRect(130, 140, 291, 51))
        self.userWelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userWelcomeLabel.setObjectName(_fromUtf8("userWelcomeLabel"))
        self.schoolLogolabel = QtGui.QLabel(self.mainFrame)
        self.schoolLogolabel.setGeometry(QtCore.QRect(90, 20, 801, 71))
        self.schoolLogolabel.setText(_fromUtf8(""))
        self.schoolLogolabel.setPixmap(QtGui.QPixmap(_fromUtf8("src/long_logo_school.png")))
        self.schoolLogolabel.setScaledContents(False)
        self.schoolLogolabel.setAlignment(QtCore.Qt.AlignCenter)
        self.schoolLogolabel.setObjectName(_fromUtf8("schoolLogolabel"))
        self.stackedWidget.addWidget(self.mainPage)
        self.loadingPage = QtGui.QWidget()
        self.loadingPage.setObjectName(_fromUtf8("loadingPage"))
        self.loadingFrame = QtGui.QFrame(self.loadingPage)
        self.loadingFrame.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.loadingFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.loadingFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.loadingFrame.setObjectName(_fromUtf8("loadingFrame"))
        self.loadingLabel = QtGui.QLabel(self.loadingFrame)
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
        self.progressBar = QtGui.QProgressBar(self.loadingFrame)
        self.progressBar.setGeometry(QtCore.QRect(230, 240, 520, 30))
        self.progressBar.setProperty("value", 33)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.stackedWidget.addWidget(self.loadingPage)
        self.cjPage = QtGui.QWidget()
        self.cjPage.setObjectName(_fromUtf8("cjPage"))
        self.cjFrame = QtGui.QFrame(self.cjPage)
        self.cjFrame.setEnabled(True)
        self.cjFrame.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.cjFrame.setMinimumSize(QtCore.QSize(960, 540))
        self.cjFrame.setMaximumSize(QtCore.QSize(960, 540))
        self.cjFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.cjFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.cjFrame.setObjectName(_fromUtf8("cjFrame"))
        self.cjGroupBox1 = QtGui.QGroupBox(self.cjFrame)
        self.cjGroupBox1.setGeometry(QtCore.QRect(10, 10, 940, 110))
        self.cjGroupBox1.setMinimumSize(QtCore.QSize(940, 110))
        self.cjGroupBox1.setMaximumSize(QtCore.QSize(940, 110))
        self.cjGroupBox1.setTitle(_fromUtf8(""))
        self.cjGroupBox1.setObjectName(_fromUtf8("cjGroupBox1"))
        self.userImformationLabel = QtGui.QLabel(self.cjGroupBox1)
        self.userImformationLabel.setGeometry(QtCore.QRect(10, 10, 921, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.userImformationLabel.setFont(font)
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
        self.xnOpptionComboBox.addItem(_fromUtf8(""))
        self.xnOpptionComboBox.addItem(_fromUtf8(""))
        self.xnOpptionComboBox.addItem(_fromUtf8(""))
        self.xnOpptionComboBox.addItem(_fromUtf8(""))
        self.xnOpptionComboBox.addItem(_fromUtf8(""))
        self.xnOpptionComboBox.addItem(_fromUtf8(""))
        self.xnOpptionComboBox.addItem(_fromUtf8(""))
        self.xnOpptionComboBox.addItem(_fromUtf8(""))
        self.xnOpptionComboBox.addItem(_fromUtf8(""))
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
        self.xqOpptioncomboBox.addItem(_fromUtf8(""))
        self.xqOpptioncomboBox.addItem(_fromUtf8(""))
        self.xqOpptioncomboBox.addItem(_fromUtf8(""))
        self.lnCjPushButton = QtGui.QPushButton(self.cjGroupBox1)
        self.lnCjPushButton.setGeometry(QtCore.QRect(620, 70, 80, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        self.lnCjPushButton.setFont(font)
        self.lnCjPushButton.setObjectName(_fromUtf8("lnCjPushButton"))
        self.cjGroupBox_2 = QtGui.QGroupBox(self.cjFrame)
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
        self.cjTableWidget.setAutoScroll(True)
        self.cjTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.cjTableWidget.setProperty("showDropIndicator", True)
        self.cjTableWidget.setAlternatingRowColors(False)
        self.cjTableWidget.setShowGrid(True)
        self.cjTableWidget.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.cjTableWidget.setWordWrap(True)
        self.cjTableWidget.setCornerButtonEnabled(True)
        self.cjTableWidget.setRowCount(0)
        self.cjTableWidget.setColumnCount(16)
        self.cjTableWidget.setObjectName(_fromUtf8("cjTableWidget"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cjTableWidget.setHorizontalHeaderItem(15, item)
        self.cjTableWidget.horizontalHeader().setVisible(True)
        self.cjTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.cjTableWidget.horizontalHeader().setDefaultSectionSize(57)
        self.cjTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.userGPALabel = QtGui.QLabel(self.cjFrame)
        self.userGPALabel.setGeometry(QtCore.QRect(10, 465, 940, 31))
        self.userGPALabel.setObjectName(_fromUtf8("userGPALabel"))
        self.stackedWidget.addWidget(self.cjPage)
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
        self.cjAction.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.cjAction.setObjectName(_fromUtf8("cjAction"))
        self.kbAction = QtGui.QAction(MainWindow)
        self.kbAction.setObjectName(_fromUtf8("kbAction"))
        self.xsxkAction = QtGui.QAction(MainWindow)
        self.xsxkAction.setObjectName(_fromUtf8("xsxkAction"))
        self.zyAction = QtGui.QAction(MainWindow)
        self.zyAction.setObjectName(_fromUtf8("zyAction"))
        self.logoutAction = QtGui.QAction(MainWindow)
        self.logoutAction.setObjectName(_fromUtf8("logoutAction"))
        self.xyMenu.addAction(self.cjAction)
        self.xyMenu.addAction(self.kbAction)
        self.xkMenu.addAction(self.xsxkAction)
        self.syMenu.addAction(self.zyAction)
        self.syMenu.addSeparator()
        self.syMenu.addAction(self.logoutAction)
        self.BrowerserMenuBar.addAction(self.syMenu.menuAction())
        self.BrowerserMenuBar.addAction(self.xyMenu.menuAction())
        self.BrowerserMenuBar.addAction(self.xkMenu.menuAction())
        self.userImformationLabel.setBuddy(self.cjTableWidget)
        self.xnOpptionLabel.setBuddy(self.xnOpptionComboBox)
        self.xqOpptionLabel.setBuddy(self.xqOpptioncomboBox)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.xnOpptionComboBox, self.xqOpptioncomboBox)
        MainWindow.setTabOrder(self.xqOpptioncomboBox, self.lnCjPushButton)
        MainWindow.setTabOrder(self.lnCjPushButton, self.cjTableWidget)
        MainWindow.setTabOrder(self.cjTableWidget, self.calendarWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "绝望2005第三方登陆系统", None))
        self.welcomePageLabel.setText(_translate("MainWindow", "绝望2005第三方登陆系统欢迎你~", None))
        self.userWelcomeLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.loadingLabel.setText(_translate("MainWindow", "Loading", None))
        self.userImformationLabel.setText(_translate("MainWindow", "<html><head/><body><p>学院 专业  姓名学号</p></body></html>", None))
        self.xnOpptionLabel.setText(_translate("MainWindow", "学年", None))
        self.xnOpptionComboBox.setItemText(0, _translate("MainWindow", "2005-2006", None))
        self.xnOpptionComboBox.setItemText(1, _translate("MainWindow", "2006-2007", None))
        self.xnOpptionComboBox.setItemText(2, _translate("MainWindow", "2007-2008", None))
        self.xnOpptionComboBox.setItemText(3, _translate("MainWindow", "2008-2009", None))
        self.xnOpptionComboBox.setItemText(4, _translate("MainWindow", "2009-2010", None))
        self.xnOpptionComboBox.setItemText(5, _translate("MainWindow", "2010-2011", None))
        self.xnOpptionComboBox.setItemText(6, _translate("MainWindow", "2011-2012", None))
        self.xnOpptionComboBox.setItemText(7, _translate("MainWindow", "2012-2013", None))
        self.xnOpptionComboBox.setItemText(8, _translate("MainWindow", "2013-2014", None))
        self.xqOpptionLabel.setText(_translate("MainWindow", "学期", None))
        self.xqOpptioncomboBox.setItemText(0, _translate("MainWindow", "1", None))
        self.xqOpptioncomboBox.setItemText(1, _translate("MainWindow", "2", None))
        self.xqOpptioncomboBox.setItemText(2, _translate("MainWindow", "3", None))
        self.lnCjPushButton.setText(_translate("MainWindow", "历年成绩", None))
        self.cjGroupBox_2.setTitle(_translate("MainWindow", "成绩", None))
        self.cjTableWidget.setSortingEnabled(False)
        item = self.cjTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学年", None))
        item = self.cjTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "学期", None))
        item = self.cjTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "课程代码", None))
        item = self.cjTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "课程名称", None))
        item = self.cjTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "课程性质", None))
        item = self.cjTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "课程归属", None))
        item = self.cjTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "学分", None))
        item = self.cjTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "绩点", None))
        item = self.cjTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "成绩", None))
        item = self.cjTableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "辅修标记", None))
        item = self.cjTableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "补考成绩", None))
        item = self.cjTableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "重修成绩", None))
        item = self.cjTableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "新建列", None))
        item = self.cjTableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "开课学院", None))
        item = self.cjTableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "备注", None))
        item = self.cjTableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "排名", None))
        self.userGPALabel.setText(_translate("MainWindow", "TextLabel", None))
        self.xyMenu.setTitle(_translate("MainWindow", "信息查询", None))
        self.xkMenu.setTitle(_translate("MainWindow", "选课", None))
        self.syMenu.setTitle(_translate("MainWindow", "首页", None))
        self.cjAction.setText(_translate("MainWindow", "成绩查询", None))
        self.kbAction.setText(_translate("MainWindow", "课表查询", None))
        self.xsxkAction.setText(_translate("MainWindow", "学生选课", None))
        self.zyAction.setText(_translate("MainWindow", "首页", None))
        self.logoutAction.setText(_translate("MainWindow", "退出", None))
        self.logoutAction.setToolTip(_translate("MainWindow", "退出", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

