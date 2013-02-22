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
                'span id="lbl_xzb:':False, 
                'span id="lbl_zymc"':False}
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
                        elif value == 'lbl_zymc':
                            self.tagflag['span'] = True
                            self.dataflag['span id="lbl_zymc"']=True
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
        elif tag == 'input':
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
            elif self.dataflag['span id="lbl_zymc"']:
                self.zymc = data
            elif self.dataflag['span id="lbl_zyfx"']:
                self.zyfx = data
            elif self.dataflag['span id="lbl_xzb"']:
                self.xzb = data
        elif self.tagflag['td']:
                self.cjData[self.tdIter] = data

    def handle_comment(self,data):
        if data == ' 查询得到的数据量显示区域 ':
            self.getData = True

class KbParser(HTMLParser):
    getData = False
    getData2 = False
    getData3 = False
    getData4 = False
    tdIter = 0
    trIter = 0
    TdIter = 0
    TrIter = 0
    userViewState = ''
    xnd = []
    xqd = []
    Kb = []
    kbData = ['', '', '', '', '', '', '']
    Sjk = []
    sjkData = ['' ,'', '' ,'' ,'', '']
    Sxk = []
    sxkData = ['' ,'' ,'' ,'', '', '', '']
    Wap =[]
    wapData = ['' ,'', '' ,'', '']
    tagflag = {'span':False,
               'td':False,
               'tr':False,
               'input':False, 
               'table':False, 
               'select':0, 
               'option':0}
    
    def handle_starttag(self,tag,attrs):
        if tag == 'body':
            self.getData = True
        if self.getData:
            if tag == 'input':
                for name,value in attrs:
                    if name == 'name' and value == '__VIEWSTATE':
                        self.userViewState = attrs[2][1]
                        self.userViewState = urllib.parse.quote(self.userViewState, safe = '')
                        break
            elif tag == 'table':
                for name,value in attrs:
                    if name == 'id' and value == 'Table1':
                        self.tagflag['table'] = True
                        self.trIter = 0
                    if name == 'id' and value == 'DataGrid1':
                        self.tagflag['table'] = True
                        self.TrIter = 0
                        self.getData2 = True
                    if name == 'id' and value == 'DBGridYxkc':
                        self.tagflag['table'] = True
                        self.TrIter = 0
                        self.getData2 = False
                        self.getData4 = True
                    if name == 'id' and value == 'Datagrid2':
                        self.tagflag['table'] = True
                        self.TrIter = 0
                        self.getData4 = False
                        self.getData3 = True
            elif tag == 'select':
                for name, value in attrs:
                    if name == 'name' and value == 'xnd':
                        self.tagflag['select'] =1
                    if name == 'name' and value == 'xqd':
                        self.tagflag['select'] = 2
            elif tag == 'option':
                if self.tagflag['select'] == 1:
                    for name, value in attrs:
                        if name == 'value':
                           self.xnd.append(value) 
                elif self.tagflag['select'] == 2:
                    for name, value in attrs:
                        if name == 'value':
                            self.xqd.append(value)

            elif tag == 'tr':
                if self.tagflag['table']:
                    self.tagflag['tr'] = True
                    self.trIter += 1
                    self.tdIter = 0
                    if self.getData2 or self.getData3 or self.getData4:
                        self.TrIter += 1
                        self.TdIter = 0
            elif tag == 'td':
                if self.tagflag['tr'] and self.trIter>2 and (self.trIter%2 == 1 or self.trIter == 12):
                    self.tagflag['td'] = True
                    self.tdIter += 1
                if self.tagflag['tr'] and self.TrIter>1 :
                    self.tagflag['td'] = True
                    self.TdIter += 1
            
    def handle_data(self,data):
        if self.tagflag['td']:
            if (not self.getData2) and (not self.getData3)and(not self.getData4):
                if self.trIter == 3 or self.trIter == 7 or self.trIter ==12:
                    if self.tdIter >2:
                        self.kbData[self.tdIter-3] += ('\n'+data)
                else:
                    if self.tdIter >1:
                        self.kbData[self.tdIter-2] += ('\n'+data)
            if self.getData2:
                if self.TrIter>1:
                    self.sjkData[self.TdIter-1] += data
            if self.getData3:
                if self.TrIter>1:
                    self.wapData[self.TdIter-1] += data
            if self.getData4:
                if self.TrIter>1:
                    self.sxkData[self.TdIter-1] += data
                
    def handle_endtag(self,tag):
        if tag == 'table':
            self.tagflag['table'] = False
        elif tag == 'tr':
            self.tagflag['tr'] = False
            if self.tagflag['table'] == True:
                if self.tdIter>1 and not (self.getData2 or self.getData3 or self.getData4):
                    self.Kb.append(self.kbData)
                    self.kbData = ['', '', '', '', '', '', '']
                if self.TdIter>1 and self.getData2:
                    self.Sjk.append(self.sjkData)
                    self.sjkData = ['' ,'', '' ,'' ,'', '']
                if self.TdIter>1 and self.getData3:
                    self.Wap.append(self.wapData)
                    self.wapData = ['' ,'', '' ,'', '']
                if self.TdIter>1 and self.getData4:
                    self.Sxk.append(self.sxkData)
                    self.sxkData = ['' ,'' ,'' ,'', '', '', '']
                    
        elif tag == 'td':
            self.tagflag['td'] = False
            
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
    Kb = []
    Sjk = []
    Wap = []
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
        
        self.cjTable = QStandardItemModel()
        s = ['学年','学期','课程代码','课程名称','课程性质','课程归属','学分','绩点','成绩','辅修标记','补考成绩','重修成绩','开课学院','备注','重修标记','排名']
        self.cjTable.setHorizontalHeaderLabels(s)
        for i in range(0, 16):
            self.cjTable.horizontalHeaderItem(i).setTextAlignment(Qt.AlignCenter) 
            
        self.kbTable = QStandardItemModel()
        s = ['周一','周二', '周三', '周四', '周五', '周六', '周日']
        self.kbTable.setHorizontalHeaderLabels(s)
        s = ['\n第1节\n8:50-9:35\n\n\n第2节\n9:40-10:25\n' ,'\n第3节\n10:40-11:25\n\n\n第4节\n11:30-12:15\n','\n第5节\n14:00-14:45\n\n\n第6节\n14:50-15:35\n', '\n第7节\n15:45-16:30\n\n\n第8节\n16:35-17:20\n', '\n第9节\n', '\n第10节\n19:00-19:45\n\n第11节\n19:50-20:35\n\n第12节\n20:40-21:25\n']
        self.kbTable.setVerticalHeaderLabels(s)
        for i in range(0, 6):
            self.kbTable.verticalHeaderItem(i).setTextAlignment(Qt.AlignCenter)
            
        self.sjkTable = QStandardItemModel()
        s = ['课程名称', '教师', '学分','起止周', '上课时间', '上课地点']
        self.sjkTable.setHorizontalHeaderLabels(s)
        for i in range(0, 6):
            self.sjkTable.horizontalHeaderItem(i).setTextAlignment(Qt.AlignCenter)
        
        self.wapTable = QStandardItemModel()
        s = ['学年', '学期', '课程名称', '教师姓名', '学分']
        self.wapTable.setHorizontalHeaderLabels(s)
        for i in range(0, 5):
            self.wapTable.horizontalHeaderItem(i).setTextAlignment(Qt.AlignCenter)
            
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
        self.loadKbdata()
    
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
        self.close()
    
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
        self.zymc = cjParser.zymc
        self.zyfx = cjParser.zyfx
        for cjdata in cjParser.Cj:
            self.Cj.append(cjdata)
        self.userImformationLabel.setText('    '+self.userXm+'    '+self.xy+'     '+self.zy+self.zymc+'     '+self.xzb)
        del cjParser
        del cjBody
        del cjHeaders
        del cjReq
        del cjData
    
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
                self.cjTable.removeRow(0)
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
                self.cjTable.insertRow(i-1)
                for data in cjdata:
                    item = QStandardItem(data)
                    self.cjTable.setItem(i-1,j-1,item)
                    j = j + 1
                i =i + 1
        try:
            self.Gpa = self.Gpa/self.Point
        except:
            self.Gpa = 0
        finally:
            self.cjTabelWidget.setModel(self.cjTable)
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
                self.cjTable.removeRow(0)
        i = 1
        for cjdata in self.Cj:
            if cjdata[4] == '必修课' or cjdata[4] == '选修课':
                self.Point = self.Point+float(cjdata[6]) 
                self.Gpa = self.Gpa+ float(cjdata[6])*float(cjdata[7])
                self.Zhiy = self.Zhiy + float(cjdata[6])*self.cjTransfer(cjdata[8])*0.02
            j = 1
            self.cjTable.insertRow(i-1)
            for data in cjdata:
                item = QStandardItem(data)
                self.cjTable.setItem(i-1,j-1,item)
                j = j+1
            i += 1
        
        try:
            self.Gpa = self.Gpa/self.Point
        except:
            self.Gpa = 0
        finally:
            self.cjTabelWidget.setModel(self.cjTable)
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
    
    def loadKbdata(self):
        kbHeaders = {'Host':'jw2005.scuteo.com', 
                             'Connection':'keep-alive', 
                             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
                             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17', 
                             'Referer':self.mainUrl+self.mainPath, 
                             'Accept-Encoding':'gzip,deflate,sdch', 
                             'Accept-Language':'zh-CN,zh;q=0.8', 
                             'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3', 
                             'Cookie':self.userCookie}
        kbUrl = self.mainUrl+self.menuPath.xsgrkb
        kbReq = urllib.request.Request(url =kbUrl,headers = kbHeaders)
        kbData = urllib.request.urlopen(url = kbReq)
        s = kbData.read().decode('gb2312')
        kbParser = KbParser()
        kbParser.feed(s)
        self.Kb = kbParser.Kb
        self.Sjk = kbParser.Sjk
        self.Wap = kbParser.Wap
        self.userKbViewState = kbParser.userViewState
        self.kbXnComboBox.addItems(kbParser.xnd)
        self.kbXqComboBox.addItems(kbParser.xqd)
        self.showKbdata()
        
    def showKbdata(self):
        i = 0
        for kbdata in self.Kb:
            j = 0
            for data in kbdata:
                item = QStandardItem(data)
                item.setTextAlignment(Qt.AlignCenter)
                self.kbTable.setItem(i,j,item)
                j +=1
            if i ==5:
                break
            i +=1
        self.kbTableView.setModel(self.kbTable)
        self.kbTableView.resizeColumnsToContents ()
        self.kbTableView.resizeRowsToContents()
        
        i = 0
        for sjkdata in self.Sjk:
            j = 0
            for data in sjkdata:
                item = QStandardItem(data)
                item.setTextAlignment(Qt.AlignCenter)
                self.sjkTable.setItem(i, j, item)
                j +=1
            i +=1
        self.sjkTableView.setModel(self.sjkTable)
        self.sjkTableView.resizeColumnsToContents ()
        self.sjkTableView.resizeRowsToContents()

        i = 0
        for wapdata in self.Wap:
            j = 0
            for data in wapdata:
                item = QStandardItem(data)
                item.setTextAlignment(Qt.AlignCenter)
                self.wapTable.setItem(i, j, item)
                j +=1
            i +=1
        self.wapTableView.setModel(self.wapTable)
        self.wapTableView.resizeColumnsToContents ()
        self.wapTableView.resizeRowsToContents()
    @pyqtSlot(str)
    def on_kbXnComboBox_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(str)
    def on_kbXqComboBox_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    l = LoginWidgetQt.loginDialog()
    l.show()
    a = MainWindow(loginW = l)
    l.loginSuccessfulSignal_NoParameters.connect(a.creatWidget,Qt.QueuedConnection) 
    sys.exit(app.exec_())
    

