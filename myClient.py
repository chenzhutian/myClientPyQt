
import urllib.request
from html.parser import HTMLParser

class XkParser(HTMLParser):
    getData = False
    tdIter = 0
    trIter = 0
    userViewState = ''
    tagflag = {'table':False,
               'td':False,
               'tr':False,
               'input':False}
    xkData = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    Xk = []
    def handle_starttag(self,tag,attrs):
        if self.getData:
            if tag == 'table':
                for name, value in attrs:
                    if name == 'id' and value == 'DBGrid':
                        self.tagflag['table'] = True
                        self.trIter = 0
            elif tag == 'tr':
                if self.tagflag['table']:
                    self.tagflag['tr'] = True
                    self.tdIter = 0
                    self.trIter += 1
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
        if tag == 'table':
            self.tagflag['table'] = False
        elif tag == 'tr':
            self.tagflag['tr'] = False
            if self.trIter > 1:
                self.Xk.append(self.xkData)
                self.xkData = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        elif tag == 'td':
            self.tagflag['td'] = False
            
    def handle_data(self,data):
        if self.tagflag['td']:
            self.xkData[self.tdIter-1] = data

    def handle_comment(self,data):
        if data == ' 查询得到的数据量显示区域 ':
            self.getData = True
