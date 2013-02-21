'''
Created on 2013-2-13
Login Widget
@author: unhealthy
'''
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import urllib.request
import urllib.parse
import urllib.error
import MenuPath
from html.parser import HTMLParser

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

class loginWidget(object):

    userName = ''
    userCode = ''
    userCookie = ''
    checkCode = ''
    mainUrl = ''
    userXm = ''
    checkCodePath = 'CheckCode.aspx'
    loginPath = 'default2.aspx'
    mainPath = ''
    loginError = 0
    loginState = False
    menuPath = MenuPath.MenuPath()
    
    
    
    def __init__(self, event = None):
        f = urllib.request.urlopen('http://jw2005.scuteo.com/')
        p = (urllib.parse.urlparse(f.geturl()))[2]
        self.mainUrl = 'http://jw2005.scuteo.com/'+ p[1:p.rfind('/')+1]
        Cookie = f.info()['Set-Cookie']
        self.userCookie = Cookie[:Cookie.find(';')]
        self.loginParser = LoginParser()
        self.event = event
        self.creatWidget()
        
    def creatWidget(self):
        localjpg = ""+('checkCode.gif')
        urllib.request.urlretrieve(self.mainUrl+self.checkCodePath,localjpg)
        
        self.top = tk.Tk()
        self.loginFrame = ttk.Frame(self.top)
        self.loginFrame.grid(row = 0,column = 0)
        
        self.userNamelabel = ttk.Label(self.loginFrame,text = '用户名')
        self.userNamelabel.grid(row = 0,column = 0,sticky = tk.W)
        self.userNameEntry = ttk.Entry(self.loginFrame)
        self.userNameEntry.grid(row = 0,column = 1,columnspan = 2,sticky = tk.E)

        self.userCodelabel = ttk.Label(self.loginFrame,text = '密码')
        self.userCodelabel.grid(row = 1,column = 0,sticky = tk.W)
        self.userCodeEntry = ttk.Entry(self.loginFrame,show = '*')
        self.userCodeEntry.grid(row = 1,column = 1,columnspan = 2,sticky = tk.E)
        
        self.checkCodelabel = ttk.Label(self.loginFrame,text = '验证码')
        self.checkCodelabel.grid(row = 2,column = 0,sticky = tk.W)
        self.checkCodeEntry = ttk.Entry(self.loginFrame,width = 10)
        self.checkCodeEntry.grid(row = 2,column = 1,sticky = tk.E+tk.W)
        self.checkCodeImage = tk.PhotoImage(file = './checkCode.gif')
        self.checkCodeImageLabel = ttk.Label(self.loginFrame,image = self.checkCodeImage)
        self.checkCodeImageLabel.grid(row = 2,column = 2,sticky = tk.E)
        
        self.loginButton = ttk.Button(self.loginFrame,text = '登陆',width = 7,command = self.login)
        self.loginButton.grid(row = 3,column = 1)
        self.quitButton = ttk.Button(self.loginFrame,text = '退出',width = 7,command = self.top.destroy)
        self.quitButton.grid(row = 3,column = 2)
        
        self.top.bind('<Return>',self.login)
        self.top.minsize(189,103)
        self.top.maxsize(189,103)
    
    def login(self,event = None):
        self.userName = self.userNameEntry.get()
        self.userCode = self.userCodeEntry.get()
        self.checkCode = self.checkCodeEntry.get()
        
        if len(self.userName) != 12:
            tkinter.messagebox.showwarning('错误', '用户名长度不对')
        elif len(self.userCode) == 0:
            tkinter.messagebox.showwarning('错误', '密码不能为空')
        elif len(self.checkCode) != 5:
            tkinter.messagebox.showwarning('错误', '验证码不正确')
        else:
            self.mainPath = 'xs_main.aspx?xh='+self.userName
            
            bodypart1 = '__VIEWSTATE=dDwtMTg3MTM5OTI5MTs7PkfLdDpkwXkZwjVjoRLwfK%2BL%2FuEU&TextBox1='
            bodypart2 = '&TextBox2='
            bodypart3 = '&TextBox3='
            bodypart4 = '&RadioButtonList1=%D1%A7%C9%FA&Button1=&lbLanguage='
            self.body = bodypart1+self.userName+bodypart2+self.userCode+bodypart3+self.checkCode+bodypart4
            self.body = self.body.encode('ISO-8859-1')
            
            self.headers = {'Host':'jw2005.scuteo.com',
                           'Connection':'keep-alive',
                           'Content-Length':len(self.body),
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
            
            self.req = urllib.request.Request(url = self.mainUrl+self.loginPath,data = self.body,headers = self.headers)
            try:
                self.data = urllib.request.urlopen(url = self.req)
            except urllib.error.HTTPError as e:
                self.loginError = e.getcode()
            else:
                loginParser = LoginParser()
                loginParser.feed(self.data.read().decode('gb2312'))
                if loginParser.loginError != '' :
                    tkinter.messagebox.showwarning('错误', loginParser.loginError)
                else:
                    self.userXm = loginParser.xm
                    self.menuPath = loginParser.path
                    self.loginState = True
                    self.top.destroy()
def main():
    loginWidget()
    tk.mainloop()

if __name__ == '__main__':
    main()
    
    
