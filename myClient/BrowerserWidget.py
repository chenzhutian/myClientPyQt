'''
Created on 2013-2-14
BrowerserWidget
@author: unhealthy
'''

import tkinter as tk
from tkinter import ttk
import urllib.request
from html.parser import HTMLParser
import LoginWidget
import MenuPath
import threading

class MyThread(threading.Thread):
    def __init__(self,Var,BrowerserWidget):
        threading.Thread.__init__(self)
        self.Var = Var
        self.b = BrowerserWidget
        
    def run(self):
        while True:
            if self.Var.get() != '99.0':
                print(self.Var.get())
            else:
                self.b.creatCjWidget()
                break


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


class browerserWidget(object):
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
    
    def __init__(self,event = None,loginW = None):
        self.event = event
        self.loginW = loginW
        
    def creatMainWindow(self):        
        self.MainWindow = tk.Tk()
        self.MainWindow.minsize(160*6, 90*6)
        self.MainWindow.maxsize(160*6, 90*6)
        self.menuBar = tk.Menu(self.MainWindow)
        self.MainFrame = tk.Frame(self.MainWindow)
        
        self.MainWindow.config(menu = self.menuBar)
        self.menuBar.add_command(label = '查询成绩',command = self.cjControllerStart)
        self.menuBar.add_command(label = '选课',command = self.creatXkWidget)
        self.MainFrame.grid(row = 0,column = 0)
        
        self.userName = self.loginW.userName
        self.userCode = self.loginW.userCode
        self.userCookie = self.loginW.userCookie
        self.mainUrl = self.loginW.mainUrl
        self.mainPath = self.loginW.mainPath
        self.menuPath = self.loginW.menuPath
        self.userXm = self.loginW.userXm
        del self.loginW
        
    def initMainFrame(self):
        self.MainFrame.destroy()
        self.MainFrame = ttk.Frame(self.MainWindow)
        self.MainFrame.grid(row = 0,column = 0)
    
    def loadingPage(self):
        self.initMainFrame()
        self.pbFrame = ttk.LabelFrame(self.MainFrame)
        self.pLabel = ttk.Label(self.pbFrame,text = 'Loading...',font = "Helvetica 14 bold")
        self.progressBar = ttk.Progressbar(self.pbFrame,orient=tk.HORIZONTAL,mode='determinate',length = 600)
        self.progressBar.start()
        self.pbFrame.grid(row = 0,column = 0,rowspan = 2,padx = 190,pady=140)
        self.pLabel.grid(row = 0,column = 0,pady = 20)
        self.progressBar.grid(row = 1,column = 0)
    
    def cjControllerStart(self):
        if self.loadCjdataFlag == 0:
            self.cjUserImformationLabelVar = tk.StringVar(self.MainWindow)
            self.cjUserImformationLabelVar.set('   '*20+'Loading...请稍等')
            t1 = threading.Thread(target = self.loadCjdata,args = ())
            t1.start()
            self.creatCjWidget()
            self.loadCjdataFlag = 1
        else:
            self.creatCjWidget()
            
    def creatCjWidget(self):
        self.initMainFrame()
        
        self.showCjdataFlag = 0
        self.cjFrame = ttk.Frame(self.MainFrame,height = 90*6,width = 160*6)
        self.cjFrame.grid(column=0, row=0,columnspan = 6,rowspan = 4,sticky = tk.W+tk.E+tk.S+tk.N)
        
        self.cjLabelFrame1 = ttk.LabelFrame(self.cjFrame,height = 90,width = 160*6-1)
        self.cjLabelFrame2 = ttk.LabelFrame(self.cjFrame,height = 90*5, width = 160*6-1)
        self.cjLabelFrame1.grid(column = 0,row = 0,columnspan = 6,rowspan = 2,sticky = tk.W+tk.E+tk.S+tk.N)
        self.cjLabelFrame2.grid(column = 0,row = 2,columnspan = 6,sticky = tk.W+tk.E+tk.S+tk.N)
        
        
        self.cjUserImformationLabel = ttk.Label(self.cjLabelFrame1,font = "Helvetica 14 bold",textvariabl = self.cjUserImformationLabelVar)
        self.cjXnOpptionLabel = ttk.Label(self.cjLabelFrame1,text = '学年')
        self.cjXnOpption = ttk.Combobox(self.cjLabelFrame1,state = tk.DISABLED)
        self.cjXnOpption.config(value = ('2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014'))
        self.cjXqOpptionLabel = ttk.Label(self.cjLabelFrame1,text = '学期')
        self.cjXqOpption = ttk.Combobox(self.cjLabelFrame1,state = tk.DISABLED)
        self.cjXqOpption.config(value = (' ','1','2','3'))
        self.cjLncjButton = ttk.Button(self.cjLabelFrame1,text = '历年成绩',command = self.showCjdata2,state = 'disabled')
        self.cjUserImformationLabel.grid(row = 0,column = 0,columnspan = 6,sticky = tk.E+tk.W+tk.S+tk.N)
        self.cjXnOpptionLabel.grid(row = 1,column = 0,sticky = tk.E)
        self.cjXnOpption.grid(row = 1,column = 1,sticky = tk.W)
        self.cjXqOpptionLabel.grid(row = 1,column = 2,sticky = tk.E)
        self.cjXqOpption.grid(row = 1,column = 3,sticky = tk.W)
        self.cjLncjButton.grid(row = 1,column = 4,sticky = tk.W)
        
        
        self.listYScrollbar = ttk.Scrollbar(self.cjLabelFrame2)
        self.listXScrollbar = ttk.Scrollbar(self.cjLabelFrame2, orient=tk.HORIZONTAL)
        self.list = ttk.Treeview(self.cjLabelFrame2,height = 18,show = 'headings',yscrollcommand = self.listYScrollbar.set,xscrollcommand = self.listXScrollbar.set,
                                 columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15','16'))
        columnTitle = ('学年','学期','课程代码','课程名称','课程性质','课程归属','学分','绩点','成绩','辅修标记','补考成绩','重修成绩','开课学院','备注','重修标记','排名')
        for i in range(1,17):
            self.list.column(str(i),width = 62,anchor = tk.CENTER )
            self.list.heading(str(i), text = columnTitle[i-1])
        self.list.column('1',width = 80)
        self.list.column('2',width = 40)
        self.list.column('4',width = 115)
        self.list.column('7',width = 40)
        self.list.column('8',width = 40)
        self.list.column('9',width = 40)
        self.list.column('14',width = 40)
        self.list.column('16',width = 40)
        self.listYScrollbar.config(command = self.list.xview)
        self.listYScrollbar.config(command = self.list.yview)
        self.list.grid(column = 0,row = 2,columnspan = 5,sticky = tk.E+tk.W+tk.S+tk.N)
        self.listXScrollbar.grid(row = 3,column = 0,columnspan = 5,sticky = tk.W+tk.E)
        self.listYScrollbar.grid(column = 5,row = 2,sticky = tk.S+tk.N)
        
        self.cjXnOpption.bind('<<ComboboxSelected>>',self.showCjdata1)
        self.cjXqOpption.bind('<<ComboboxSelected>>',self.showCjdata1)
            

        self.cjGPAString = tk.StringVar(self.cjFrame)
        self.cjGPALabel = ttk.Label(self.cjFrame, font = "Helvetica 12 bold",textvariable = self.cjGPAString)
        self.cjGPALabel.grid(row = 4,column = 0,columnspan = 6,sticky = tk.W+tk.E)
#        if self.loadCjdataFlag == 1:
#            self.cjXqOpption.state(['!disabled', 'readonly'])
#            self.cjXnOpption.state(['!disabled', 'readonly'])
#            self.cjLncjButton.state(['!disabled'])
            
    def loadCjdata(self):
        self.cjHeaders = {'Host':'jw2005.scuteo.com',
                           'Connection':'keep-alive',
                           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17',
                           'Referer':self.mainUrl+self.menuPath.cjcx,
                           'Accept-Encoding':'gzip,deflate,sdch',
                           'Accept-Language':'zh-CN,zh;q=0.8',
                           'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',
                           'Cookie':self.userCookie}
        self.cjReq = urllib.request.Request(url =self.mainUrl+self.menuPath.cjcx,headers = self.cjHeaders)
        self.cjData = urllib.request.urlopen(url = self.cjReq)
        cjParser = CjParser()
        cjParser.feed(self.cjData.read().decode('gb2312'))
        self.userViewState = cjParser.userViewState
        
        self.cjBody = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE='+self.userViewState+'&hidLanguage=&ddlXN=&ddlXQ=&ddl_kcxz=&btn_zcj=%C0%FA%C4%EA%B3%C9%BC%A8'
        self.cjBody = self.cjBody.encode('ISO-8859-1')
        self.cjHeaders = {'Host':'jw2005.scuteo.com',
                           'Connection':'keep-alive',
                           'Content-Length':len(self.cjBody),
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
        self.cjReq = urllib.request.Request(url =self.mainUrl+self.menuPath.cjcx,data = self.cjBody,headers = self.cjHeaders)
        self.cjData = urllib.request.urlopen(url = self.cjReq)
        cjParser.feed(self.cjData.read().decode('gb2312'))
        self.xy = cjParser.xy
        self.xzb = cjParser.xzb
        self.zy = cjParser.zy
        self.zyfx = cjParser.zyfx
        for cjdata in cjParser.Cj:
            self.Cj.append(cjdata)
            
        del cjParser
        del self.cjBody
        del self.cjHeaders
        del self.cjReq
        del self.cjData
#        self.cjUserImformationLabelVar.set('     '+self.userName+'    '+self.userXm+'    '+self.xy+'     '+self.zy+'     '+self.xzb)
#        self.cjXqOpption.state(['!disabled', 'readonly'])
#        self.cjXnOpption.state(['!disabled', 'readonly'])
#        self.cjLncjButton.state(['!disabled'])
        
    def showCjdata1(self,event):
        
        Xn = self.cjXnOpption.get()
        Xq = self.cjXqOpption.get()
        self.Gpa = 0
        self.Zhiy = 0
        self.Point = 0
        if self.showCjdataFlag == 0:
            self.showCjdataFlag = 1
        else:
            for i in range(1,self.iid):
                self.list.delete(str(i))
        i = 1
        for cjdata in self.Cj:
            Xnflag = 0
            Xqflag = 0
            if  cjdata[0] == Xn:#Xn == ' ' or Xn == '' or :
                Xnflag = 1
            if cjdata[1] == Xq or Xq == ' ' : #or Xq == '' or 
                Xqflag = 1
            if Xnflag == 1 and Xqflag == 1:
                if cjdata[4] == '必修课' or cjdata[4] == '选修课':
                    self.Point = self.Point+float(cjdata[6]) 
                    self.Gpa = self.Gpa+ float(cjdata[6])*float(cjdata[7])
                    self.Zhiy = self.Zhiy + float(cjdata[6])*self.cjTransfer(cjdata[8])*0.02
                self.list.insert('', 'end', str(i), text=str(i),value = cjdata)
                i += 1
        try:
            self.Gpa = self.Gpa/self.Point
        except:
            self.Gpa = 0
        finally:
            self.cjGPAString.set('以上科目的平均Gpa为    :'+str(self.Gpa)+'                    以上科目的智育成绩 为     :'+str(self.Zhiy))
            self.iid = i
            
    def showCjdata2(self):
        self.Gpa = 0
        self.Zhiy = 0
        self.Point = 0
        if self.showCjdataFlag == 0:
            self.showCjdataFlag = 1
        else:
            for i in range(1,self.iid):
                self.list.delete(str(i))
        i = 1
        for cjdata in self.Cj:
            if cjdata[4] == '必修课' or cjdata[4] == '选修课':
                self.Point = self.Point+float(cjdata[6]) 
                self.Gpa = self.Gpa+ float(cjdata[6])*float(cjdata[7])
                self.Zhiy = self.Zhiy + float(cjdata[6])*self.cjTransfer(cjdata[8])*0.02
            self.list.insert('', 'end', str(i), text=str(i),value = cjdata)
            i += 1
        
        try:
            self.Gpa = self.Gpa/self.Point
        except:
            self.Gpa = 0
        finally:
            self.cjGPAString.set('以上科目的平均Gpa为    :'+str(self.Gpa)+'                    以上科目的智育成绩 为     :'+str(self.Zhiy))
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
    def creatXkWidget(self):
        self.loadingPage()
        
def main():
    browerserWidget(LoginWidget.loginWidget())
    tk.mainloop()

if __name__ == '__main__':
    main()
    
