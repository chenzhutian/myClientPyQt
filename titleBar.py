#include "TitleBar.h"
#include <QHBoxLayout>
#include <QPixmap>
#include <QLabel>
#include <QToolButton>
#include <QStyle>
#include <QMouseEvent>
#include <QLabel>

from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QWidget, QIcon, QApplication, QLabel, QStyle, QHBoxLayout, QPixmap, QToolButton, QSizePolicy


class TitleBar(QWidget):

    maxNormal = False
    def __init__(self):
        super().__init__()
        self.minimize = QToolButton(self)
        self.maximize = QToolButton(self);
        self.close= QToolButton(self);
        self.iconLabel = QLabel(self);
        self.titleLabel = QLabel(self);

        self.objPixmap = QPixmap("src\logo_school.png")
        self.iconLabel.setPixmap(self.objPixmap.scaled(20,20))
        self.titleLabel.setText("unhealthy")

        pix = QIcon(self.style().standardPixmap(QStyle.SP_TitleBarCloseButton))
        self.close.setIcon(pix)
        self.maxPix = QIcon(self.style().standardPixmap(QStyle.SP_TitleBarMaxButton))
        self.maximize.setIcon(self.maxPix)
        pix = QIcon(self.style().standardPixmap(QStyle.SP_TitleBarMinButton))
        self.minimize.setIcon(pix)
        self.restorePix = QIcon(self.style().standardPixmap(QStyle.SP_TitleBarNormalButton))


        self.minimize.setMinimumHeight(20)
        self.close.setMinimumHeight(20)
        self.maximize.setMinimumHeight(20)
#        set.setMinimumHeight(20)

        self.hbox =QHBoxLayout(self)
        self.hbox.addWidget(self.iconLabel)
        self.hbox.addWidget(self.titleLabel)
#        hbox.addWidget(set)
        self.hbox.addWidget(self.minimize)
        self.hbox.addWidget(self.maximize)
        self.hbox.addWidget(self.close)
        self.hbox.insertStretch(2, 500)
        self.hbox.setMargin(2)
        self.hbox.setSpacing(0)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #设置标签的文本颜色，大小
        self.setStyleSheet("QLabel{color:#FF3333;font-size:12px;font-weight:bold;}")
        #设置左边距
        self.titleLabel.setStyleSheet("margin-left:3px;")
        self.setWindowFlags(Qt.FramelessWindowHint)
 
    @pyqtSlot()
    def on_minimize_clicked(self):
        self.parentWidget().showMinimized()

    @pyqtSlot()
    def on_maximize_clicked(self):
        if self.maxNormal :
            self.parentWidget().showNormal()
            self.maxNormal = not self.maxNormal
            self.maximize.setIcon(self.maxPix)
        else:
            self.parentWidget().showMaximized()
            self.maxNormal = not self.maxNormal
            self.maximize.setIcon(self.restorePix)

    def mousePressEvent(self, e):
        self.startPos = e.globalPos()
        self.clickPos = self.mapToParent(e.pos())
        #self.clickPos = e.pos()

    def mouseMoveEvent(self, e):
        if self.maxNormal:
           return
        self.parentWidget().move(e.globalPos() - self.clickPos)
        #self.move(e.globalPos() - self.clickPos)

    def mouseDoubleClickEvent(self, e):
        if (e.button() == Qt.LeftButton and e.y() <= self.height()):
            if not self.maxNormal:
                self.parentWidget().showMaximized()
                self.maxNormal = not self.maxNormal
                self.maximize.setIcon(self.restorePix)
            else:
                self.parentWidget().showNormal()
                self.maxNormal = not self.maxNormal
                self.maximize.setIcon(self.maxPix)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    t = TitleBar()
    t.show()
    sys.exit(app.exec_())

