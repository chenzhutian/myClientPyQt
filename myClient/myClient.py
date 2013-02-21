'''
Created on 2013-2-18

@author: unhealthy
'''
import BrowerserWidget
import LoginWidget
import threading
import queue
import tkinter as tk
import sys

class MyPThread(threading.Thread):
    def __init__(self,l,queue = None):
        threading.Thread.__init__(self)
        self.l = l
        self.queue = queue
        self.first = 0
    def run(self):
        while True:
            if self.l.loginState == False:
                pass
            else:
                self.queue.put(self.l.loginState)
                break
            
    def getResponse(self):
        pass

class MyCThread(threading.Thread):
    def __init__(self,b,queue = None):
        threading.Thread.__init__(self)
        self.queue = queue
        self.b = b
        
    def run(self):
        while True:
            if self.queue.get() == True:
                self.b.creatMainWindow()
                break
            else:
                pass

def main():
    q = queue.Queue()
    l = LoginWidget.loginWidget()
    b = BrowerserWidget.browerserWidget(loginW = l)
    #t2 = threading.Thread(target = b.creatMainWindow,args = ())
    #t2.start()
    t1 = MyPThread(l,q)
    t2 = MyCThread(b,q)
    t1.start()
    t2.start()
    tk.mainloop()
    sys.exit(0)
    print('adf')
if __name__ == '__main__':
    main()