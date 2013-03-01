# -*- coding: utf-8 -*-

"""
Module implementing loginDialog.
"""

from PyQt4.QtCore import pyqtSlot, pyqtSignal, QThread, Qt, QTimer, QPlastiqueStyle
from PyQt4.QtGui import QDialog, QApplication, QMessageBox
from Ui_LoginWidgetQt import Ui_loginDialog
import urllib.request
import urllib.parse
import urllib.error
import MenuPath
from html.parser import HTMLParser
import http.client

#class SmartRedirectHandler(urllib.request.HTTPRedirectHandler):
#     
#    
#    def http_error_302(self, req, fp, code, msg, headers):
#        pass
#        p = headers["Location"]
#        self.mainUrl = 'http://jw2005.scuteo.com/'+ p[1:p.rfind('/')+1]
#        print(self.mainUrl)
#        self.cookies = headers['Set-Cookie']
#        self.cookies = self.cookies[:self.cookies.find(';')]
#        print(self.cookies)
#        #result = urllib.request.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)                                      
#        print('a')
#        return


class ProcessorThread(QThread):

    def __init__(self, func, args, name,parent = None):
        super(ProcessorThread, self).__init__(parent)
        self.func = func
        self.args = args
        self.name = name
        self.moveToThread(self)

    def run(self):
        self.func(*self.args)
        self.destroy()

class LoginParser(HTMLParser):
        
    tagflag = {'script':False,
               'span':False}
    dataflag = {'script language="javascript"':False,
                'span id="xhxm"':False}
    loginError = ''
    xm = ''
    path = MenuPath.MenuPath()
    
    def encodeUrl(self,s):
        pos = s.find(self.xm)
        targetUrl = s[:pos]+urllib.parse.quote(s[pos:pos+len(self.xm)].encode('gb2312'))+s[pos+len(self.xm):]
        return targetUrl
    
    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            for name,value in attrs:
                if name == 'language':
                    if value == 'javascript':
                        self.tagflag['script'] = True
                        self.dataflag['script language="javascript"'] = True
        elif tag == 'span':
            for name,value in attrs:
                if name == 'id':
                    if value == 'xhxm':
                        self.tagflag['span'] = True
                        self.dataflag['span id="xhxm"']=True
        elif tag == 'a':
            for name,value in attrs:
                if name == 'onclick':
                    if value == "GetMc('学生选课');":
                        self.path.xsxk = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('选体育课');":
                        self.path.xtyk = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('重修或补修选课');":
                        self.path.cxhbxxk = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('补考报名确认');":
                        self.path.bkbmqr = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('辅修报名');":
                        self.path.fxbm = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('院系选修课');":
                        self.path.yxxxk = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('个人信息');":
                        self.path.grxx = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('密码修改');":
                        self.path.mmxg = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('专业推荐课表查询');":
                        self.path.zytjkbcx = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('学生个人课表');":
                        self.path.xsgrkb = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('成绩查询');":
                        self.path.cjcx = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('培养计划');":
                        self.path.pyjh = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('教室查询');":
                        self.path.jscx = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('课程介绍查询');":
                        self.path.kcjscx = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('学生选课情况查询');":
                        self.path.xsxkqkcx = self.encodeUrl(attrs[0][1])
                    elif value == "GetMc('满意度调查');":
                        self.path.myddc = self.encodeUrl(attrs[0][1])

    def handle_data(self,data):
        if self.tagflag['script'] == True:
            if self.dataflag['script language="javascript"']:
                if data[:5] == 'alert':
                    self.loginError = data[7:]
                    self.loginError = self.loginError[:self.loginError.find("'")]
        elif self.tagflag['span']:
            if self.dataflag['span id="xhxm"']:
                self.xm = data[14:-2]
        
    def handle_endtag(self,tag):
        if tag == 'script':
            self.tagflag['script'] = False
            self.dataflag['script language="javascript"'] = False
        elif tag == 'span':
            self.tagflag['span'] = False
            self.tagflag['span id="xhxm"'] = False



class loginDialog(QDialog, Ui_loginDialog):
    """
    Class documentation goes here.
    """
    userName = ''
    userCode = ''
    userCookie = ''
    checkCode = ''
    mainUrl = ''
    userXm = ''
    checkCodePath = 'CheckCode.aspx'
    loginPath = 'default3.aspx'
    mainPath = 'xs_main.aspx?xh='
    loginError = 0
    menuPath = MenuPath.MenuPath()
    loginTimes = 0
    loginSuccessfulSignal_NoParameters = pyqtSignal() 
    loginFaledSignal_NoParameters = pyqtSignal()
    loginFinished_NoParameters = pyqtSignal()
    initialFinished_NoParameters = pyqtSignal()
    timer = QTimer()
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(1)
        
#        conn = http.client.HTTPConnection('jw2005.scuteo.com')
#        conn.request('GET', '')
#        r1 = conn.getresponse()
#        p = r1.getheader('Location')
#        self.mainUrl = 'http://jw2005.scuteo.com/'+ p[1:p.rfind('/')+1]
#        Cookie = r1.getheader('Set-Cookie')
#        self.userCookie = Cookie[:Cookie.find(';')]
        
        self.loginParser = LoginParser()
        self.timer.timeout.connect(self.loginAgain, Qt.QueuedConnection)
        self.loginFaledSignal_NoParameters.connect(self.loginFaled, Qt.QueuedConnection)
        self.loginSuccessfulSignal_NoParameters .connect(self.loginSuccessful, Qt.QueuedConnection)
        self.initialFinished_NoParameters.connect(self.initialFinished, Qt.QueuedConnection)
        self.t1 = ProcessorThread(self.initialLogin, (), self.initialLogin.__name__)
        self.t1.start()

    
    @pyqtSlot()
    def initialFinished(self):
        #zxcvbnm,./self.checkCodeImageLabel.setPixmap(QPixmap("src/checkCode.gif"))
        self.stackedWidget.setCurrentIndex(0)

    
    @pyqtSlot()
    def loginFaled(self):
        self.stackedWidget.setCurrentIndex(0)
        self.timer.stop()
        QMessageBox.critical(self,'错误', self.loginError)
    
    @pyqtSlot()
    def loginAgain(self):
        self.t1.quit()
        self.loginTimes += 1
        self.label.setText('Loading.第'+str(self.loginTimes)+'次')
        self.t1.start()
    
    @pyqtSlot()
    def loginSuccessful(self):
        self.timer.stop()
        self.loginFinished_NoParameters.emit()
        
    @pyqtSlot()
    def on_loginButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.userName = self.userNameLineEdit.text()
        self.userCode = self.userCodeLineEdit.text()
        #self.checkCode = self.checkCodeLineEdit.text()
        
        if len(self.userName) != 12:
            QMessageBox.critical(self,'错误', '用户名长度不对')
        elif len(self.userCode) == 0:
            QMessageBox.critical(self,'错误', '密码不能为空')
#        elif len(self.checkCode) != 5:
#            QMessageBox.critical(self,'错误','验证码不正确')
        else:
            self.t1 = ProcessorThread(self.login, (), self.login.__name__)
            self.t1.start()
            self.timer.start(2000)
            self.progressBar.setValue(89)
            self.stackedWidget.setCurrentIndex(1)

            
    def login(self):
            self.mainPath = 'xs_main.aspx?xh='+self.userName
            bodypart1 = '__VIEWSTATE=dDwtMTM2MTgxNTk4OTs7PoKJpeOaMoX03GheocP91rB2QIeM&TextBox1='
            bodypart2 = '&TextBox2='
            bodypart3 = '&ddl_js=%D1%A7%C9%FA&Button1=+%B5%C7+%C2%BC+'
            body = bodypart1 +self.userName+bodypart2+self.userCode+bodypart3
            body = body.encode('ISO-8859-1')
            
            headers = {'Host':'jw2005.scuteo.com',
                           'Connection':'keep-alive',
                           'Content-Length':len(body),
                           'Cache-Control':'max-age=0',
                           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Origin':'http://jw2005.scuteo.com',
                           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17',
                           'Content-Type':'application/x-www-form-urlencoded',
                           'Referer':self.mainUrl+self.loginPath,
                           'Accept-Encoding':'gzip,deflate,sdch',
                           'Accept-Language':'zh-CN,zh;q=0.8',
                           'Accept-Chaset':'GBK,utf-8;q=0.7,*;q=0.3',
                           'Cookie':self.userCookie}
            
            req = urllib.request.Request(url = self.mainUrl+self.loginPath,data = body,headers = headers)
            try:
                urllib.request.urlopen(url = req, timeout = 1)
                data = urllib.request.urlopen(url = self.mainUrl+self.mainPath)
            except urllib.error.HTTPError as e:
                self.loginError = e.getcode()
                print(self.loginError)
            else:
                loginParser = LoginParser()
                loginParser.feed(data.read().decode('gb2312'))
                if loginParser.loginError != '' :
                    self.loginError = loginParser.loginError
                    self.loginFaledSignal_NoParameters.emit()
                    self.t1.stop()
                else:
                    self.userXm = loginParser.xm
                    self.menuPath = loginParser.path
                    self.loginSuccessfulSignal_NoParameters.emit()
                    self.close()
                    self.destroy()
    
    def initialLogin(self):
        self.progressBar.setValue(60)
        conn = http.client.HTTPConnection('jw2005.scuteo.com')
        conn.request('GET', '')
        r1 = conn.getresponse()
        p = r1.getheader('Location')
        self.progressBar.setValue(80)
        self.mainUrl = 'http://jw2005.scuteo.com/'+ p[1:p.rfind('/')+1]
        Cookie = r1.getheader('Set-Cookie')
        self.userCookie = Cookie[:Cookie.find(';')]
        self.progressBar.setValue(99)
        self.initialFinished_NoParameters.emit()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    a = loginDialog()
    a.show()
    app.setStyle(QPlastiqueStyle())
    sys.exit(app.exec_())
