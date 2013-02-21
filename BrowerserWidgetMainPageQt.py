# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import pyqtSlot, Qt, QThread, pyqtSignal
from PyQt4.QtGui import QMainWindow, QApplication, QStandardItemModel, QStandardItem
from  Ui_BrowerserWidgetMainPageQt import Ui_MainWindow
import MenuPath
import urllib.request
from html.parser import HTMLParser
import LoginWidgetQt

class ProcessorThread(QThread):
    finishLoading=pyqtSignal(int)

    def __init__(self, func, args, name,parent = None):
        super(ProcessorThread, self).__init__(parent)
        self.func = func
        self.args = args
        self.name = name
        self.moveToThread(self)

    def run(self):
        self.func(*self.args)
        self.finishLoading.emit(2)
        self.stop()
        


class CjParser(HTMLParser):
    getData = False
    getDatelData1 = 0
    tdIter = -1
    userViewState = ''
    tagflag = {'span':False,
               'td':False,
               'tr':False,
               'input':False}
    dataflag = {'span id="lbl_xy"':False,
                'span id="lbl_zy"':False,
                'span id="lbl_zyfx"':False,
                'span id="lbl_xzb:':False}
    cjData = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    Cj = []
    xy = ''
    zy = ''
    zyfx = ''
    xzb = ''
    def handle_starttag(self,tag,attrs):
        if self.getData:
            if tag == 'span':
                for name,value in attrs:
                    if name == 'id':
                        if value == 'lbl_xy':
                            self.tagflag['span'] = True
                            self.dataflag['span id="lbl_xy"']=True
                        elif value == 'lbl_zy':
                            self.tagflag['span'] = True
                            self.dataflag['span id="lbl_zy"']=True
                        elif value == 'lbl_zyfx':
                            self.tagflag['span'] = True
                            self.dataflag['span id="lbl_zyfx"']=True
                        elif value == 'lbl_xzb':
                            self.tagflag['span'] = True
                            self.dataflag['span id="lbl_xzb"']=True
            elif tag == 'table':
                for name,value in attrs:
                    if name == 'class':
                        if value == 'datelist':
                            self.getDatelData1 = 1
            elif tag == 'tr':
                if self.getDatelData1 == 2:
                    self.tagflag['tr'] = True
                    self.tdIter = -1
            elif tag == 'td':
                if self.tagflag['tr']:
                    self.tagflag['td'] = True
                    self.tdIter += 1
        else:
            if tag == 'input':
                for name,value in attrs:
                    if name == 'name' and value == '__VIEWSTATE':
                        self.userViewState = attrs[2][1]
                        self.userViewState = urllib.parse.quote(self.userViewState, safe = '')
                        break

    def handle_endtag(self,tag):
        if tag == 'span':
            self.tagflag['span'] = False
            for key in self.dataflag:
                if 'span' in key:
                    self.dataflag[key] = False
        elif tag == 'table':
            if self.getDatelData1 == 2:
                self.getDatelData1 = 0
        elif tag == 'tr':
            self.tagflag['tr'] = False
            if self.getDatelData1 == 1:
                self.getDatelData1 = 2
            elif self.getDatelData1 == 2:
                self.Cj.append(self.cjData)
                self.cjData = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            for key in self.dataflag:
                if 'tr' in key:
                    self.dataflag[key] = False
        elif tag == 'td':
            self.tagflag['td'] = False
            
    def handle_data(self,data):
        if self.tagflag['span']:
            if self.dataflag['span id="lbl_xy"']:
                self.xy = data
            elif self.dataflag['span id="lbl_zy"']:
                self.zy = data
            elif self.dataflag['span id="lbl_zyfx"']:
                self.zyfx = data
            elif self.dataflag['span id="lbl_xzb"']:
                self.xzb = data
        elif self.tagflag['td']:
                self.cjData[self.tdIter] = data

    def handle_comment(self,data):
        if data == ' 查询得到的数据量显示区域 ':
            self.getData = True

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    userName = ''
    userCode = ''
    userCookie = ''
    mainUrl = ''
    userXm = ''
    mainPath = ''
    menuPath = MenuPath.MenuPath()
    
    Cj = []
    showCjdataFlag = 0
    loadCjdataFlag = 0
    iid = 0
    progressUpdated=pyqtSignal(int)
    
    def __init__(self, parent=None, loginW = None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        self.loginW = loginW
        super().__init__(parent)
        self.setupUi(self)
        self.tabel = QStandardItemModel()
        s = ['学年','学期','课程代码','课程名称','课程性质','课程归属','学分','绩点','成绩','辅修标记','补考成绩','重修成绩','开课学院','备注','重修标记','排名']
        self.tabel.setHorizontalHeaderLabels(s)
        self.t1 = ProcessorThread(self.loadCjdata, (), self.loadCjdata.__name__)
        self.t1.finishLoading.connect(self.showCjPage,Qt.QueuedConnection) 
        self.progressUpdated.connect(self.showProgressing,Qt.QueuedConnection)
        
    @pyqtSlot()
    def creatWidget(self):
        if self.loginW != None:
            self.userName = self.loginW.userName
            self.userCode = self.loginW.userCode
            self.userCookie = self.loginW.userCookie
            self.mainUrl = self.loginW.mainUrl
            self.mainPath = self.loginW.mainPath
            self.menuPath = self.loginW.menuPath
            self.userXm = self.loginW.userXm
            self.userWelcomeLabel.setText(self.userName+'      '+self.userXm)
            del self.loginW
            self.show()
        else:
            self.userWelcomeLabel.setText("登陆失败！")
            self.show()
            
    @pyqtSlot()
    def on_cjAction_triggered(self):
        """
        Slot documentation goes here.
        """
        if self.loadCjdataFlag == 0:
            self.t1.start()
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(1)
        
    @pyqtSlot(int)
    def showCjPage(self, index):
        self.stackedWidget.setCurrentIndex(index)
    
    @pyqtSlot(int)
    def showProgressing(self, value):
        self.progressBar.setValue(value) 
        
    @pyqtSlot()
    def on_kbAction_triggered(self):
        """
        Slot documentation goes here.
        """
        self.progressBar.setValue(50) 
        self.stackedWidget.setCurrentIndex(1)
    
    @pyqtSlot()
    def on_xsxkAction_triggered(self):
        """
        Slot documentation goes here.
        """
        self.progressBar.setValue(50) 
        self.stackedWidget.setCurrentIndex(1)
    
    @pyqtSlot()
    def on_zyAction_triggered(self):
        """
        Slot documentation goes here.
        """
        self.progressBar.setValue(50) 
        self.stackedWidget.setCurrentIndex(0)
    
    @pyqtSlot()
    def on_logoutAction_triggered(self):
        """
        Slot documentation goes here.
        """
        self.logout()
        self.destroy()
    
    @pyqtSlot(str)
    def on_xnOpptionComboBox_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        self.showCjdata1()
    
    @pyqtSlot(str)
    def on_xqOpptionComboBox_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        self.showCjdata1()
    
    @pyqtSlot()
    def on_lnCjPushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.showCjdata2()
    
    @pyqtSlot(int)
    def updateProgress(self, value):
        self.lblProgress=str(value)
        
    def loadCjdata(self):
        self.progressUpdated.emit(35)
        cjHeaders = {'Host':'jw2005.scuteo.com',
                           'Connection':'keep-alive',
                           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17',
                           'Referer':self.mainUrl+self.menuPath.cjcx,
                           'Accept-Encoding':'gzip,deflate,sdch',
                           'Accept-Language':'zh-CN,zh;q=0.8',
                           'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',
                           'Cookie':self.userCookie}
        cjReq = urllib.request.Request(url =self.mainUrl+self.menuPath.cjcx,headers = cjHeaders)
        cjData = urllib.request.urlopen(url = cjReq)
        self.progressUpdated.emit(45)
        cjParser = CjParser()
        cjParser.feed(cjData.read().decode('gb2312'))
        userViewState = cjParser.userViewState
        self.progressUpdated.emit(65)
        cjBody = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE='+userViewState+'&hidLanguage=&ddlXN=&ddlXQ=&ddl_kcxz=&btn_zcj=%C0%FA%C4%EA%B3%C9%BC%A8'
        cjBody = cjBody.encode('ISO-8859-1')
        cjHeaders = {'Host':'jw2005.scuteo.com',
                           'Connection':'keep-alive',
                           'Content-Length':len(cjBody),
                           'Cache-Control':'max-age=0',
                           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Origin':'http://jw2005.scuteo.com',
                           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17',
                           'Content-Type':'application/x-www-form-urlencoded',
                           'Referer':self.mainUrl+self.menuPath.cjcx,
                           'Accept-Encoding':'gzip,deflate,sdch',
                           'Accept-Language':'zh-CN,zh;q=0.8',
                           'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',
                           'Cookie':self.userCookie}
        cjReq = urllib.request.Request(url =self.mainUrl+self.menuPath.cjcx,data = cjBody,headers = cjHeaders)
        self.progressUpdated.emit(75)
        cjData = urllib.request.urlopen(url = cjReq)
        self.progressUpdated.emit(99)
        cjParser.feed(cjData.read().decode('gb2312'))
        self.xy = cjParser.xy
        self.xzb = cjParser.xzb
        self.zy = cjParser.zy
        self.zyfx = cjParser.zyfx
        for cjdata in cjParser.Cj:
            self.Cj.append(cjdata)
        self.userImformationLabel.setText('     '+self.userName+'    '+self.userXm+'    '+self.xy+'     '+self.zy+'     '+self.xzb)
        del cjParser
        del cjBody
        del cjHeaders
        del cjReq
        del cjData
    
    def logout(self):
        logoutHeaders = {'Host':'jw2005.scuteo.com', 
                                    'Connection':'keep-alive', 
                                    'Cache-Control':'max-age=0', 
                                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
                                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17', 
                                    'Referer':self.mainUrl+self.mainPath, 
                                    'Accept-Encoding':'gzip,deflate,sdch', 
                                    'Accept-Language':'zh-CN,zh;q=0.8', 
                                    'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3', 
                                    'Cookie':self.userCookie}
        logoutUrl = self.mainUrl+'logout.aspx'
        logoutReq = urllib.request.Request(url =logoutUrl,headers = logoutHeaders)
        urllib.request.urlopen(url = logoutReq)
        
    def showCjdata1(self):
        Xn = self.xnOpptionComboBox.currentText()
        Xq = self.xqOpptionComboBox.currentText()
        self.Gpa = 0
        self.Zhiy = 0
        self.Point = 0
        if self.showCjdataFlag == 0:
            self.showCjdataFlag = 1
        else:
            for i in range(1,self.iid):
                self.tabel.removeRow(0)
        i = 1
        for cjdata in self.Cj:
            Xnflag = 0
            Xqflag = 0
            if  cjdata[0] == Xn:
                Xnflag = 1
            if cjdata[1] == Xq or Xq == '全部学期' : 
                Xqflag = 1
            if Xnflag == 1 and Xqflag == 1:
                if cjdata[4] == '必修课' or cjdata[4] == '选修课':
                    self.Point = self.Point+float(cjdata[6]) 
                    self.Gpa = self.Gpa+ float(cjdata[6])*float(cjdata[7])
                    self.Zhiy = self.Zhiy + float(cjdata[6])*self.cjTransfer(cjdata[8])*0.02
                j = 1
                self.tabel.insertRow(i-1)
                for item in cjdata:
                    item = QStandardItem(cjdata[j-1])
                    self.tabel.setItem(i-1,j-1,item)
                    j = j + 1
                i =i + 1
        try:
            self.Gpa = self.Gpa/self.Point
        except:
            self.Gpa = 0
        finally:
            self.cjTabelWidget.setModel(self.tabel)
            self.cjTabelWidget.resizeColumnsToContents ()
            self.userGPALabel.setText('以上科目的平均Gpa为    :'+str(self.Gpa)+'                    以上科目的智育成绩 为     :'+str(self.Zhiy))
            self.iid = i
        
    def showCjdata2(self):
        self.Gpa = 0
        self.Zhiy = 0
        self.Point = 0
        if self.showCjdataFlag == 0:
            self.showCjdataFlag = 1
        else:
            for i in range(1,self.iid):
                self.tabel.removeRow(0)
        i = 1
        for cjdata in self.Cj:
            if cjdata[4] == '必修课' or cjdata[4] == '选修课':
                self.Point = self.Point+float(cjdata[6]) 
                self.Gpa = self.Gpa+ float(cjdata[6])*float(cjdata[7])
                self.Zhiy = self.Zhiy + float(cjdata[6])*self.cjTransfer(cjdata[8])*0.02
            j = 1
            self.tabel.insertRow(i-1)
            for item in cjdata:
                item = QStandardItem(cjdata[j-1])
                self.tabel.setItem(i-1,j-1,item)
                j = j+1
            i += 1
        
        try:
            self.Gpa = self.Gpa/self.Point
        except:
            self.Gpa = 0
        finally:
            self.cjTabelWidget.setModel(self.tabel)
            self.cjTabelWidget.resizeColumnsToContents ()
            self.userGPALabel.setText('以上科目的平均Gpa为    :'+str(self.Gpa)+'                    以上科目的智育成绩 为     :'+str(self.Zhiy))
            self.iid = i
    
    def cjTransfer(self,s):
        if s == '优秀':
            return 95
        elif s == '良好':
            return 85
        elif s == '中等':
            return 75
        elif s == '及格':
            return 65
        elif s == '不及格':
            return 0
        elif s == '通过':
            return 60
        elif s == '不通过':
            return 0
        else:
            return float(s)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    l = LoginWidgetQt.loginDialog()
    l.show()
    a = MainWindow(loginW = l)
    l.loginSuccessfulSignal_NoParameters.connect(a.creatWidget,Qt.QueuedConnection) 
    sys.exit(app.exec_())
    

