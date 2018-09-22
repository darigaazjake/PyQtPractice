"""
Level 5
ボタンに機能追加
"""

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import QCoreApplication
import sys

class myWidgetClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        

        self.resize(400, 300)
        self.setWindowTitle('QtSample Level5 Button Function')
        self.setWindowIcon(QIcon('../pythonicon.png'))

        btn = QPushButton('Quit', self)
        
        #ボタンのclickedシグナルにquitをconnect
        btn.clicked.connect(QCoreApplication.instance().quit)

        #ボタンのサイズをいい感じに設定してもらう
        btn.resize(btn.sizeHint())

        #ボタンに吹き出しを追加
        QToolTip.setFont(QFont('SansSerif', 10))
        btn.setToolTip('This will <b>Close</b> widget')

        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = myWidgetClass()
    sys.exit(app.exec_()) 