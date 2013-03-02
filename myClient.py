import titleBar
import BrowerserWidgetMainPageQt
from PyQt4.QtCore import  Qt
from PyQt4.QtGui import QWidget, QVBoxLayout, QApplication


class MyClient(QWidget):
    
    def __init__(self):
        super().__init__()
        self.Browerser = BrowerserWidgetMainPageQt.MainWindow()
        self.titleBar =titleBar.TitleBar()
        self.mouseDown = False

        self.tlayout = QVBoxLayout()
        self.tlayout.addWidget(self.titleBar)
        self.tlayout.addWidget(self.Browerser)
        self.tlayout.setMargin(0)
        self.tlayout.setSpacing(0)

        self.setLayout(self.tlayout)
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAutoFillBackground(True)
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    t = MyClient()
    t.show()
    sys.exit(app.exec_())
