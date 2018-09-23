"""
Level 6
widgetの閉じる確認画面
"""

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QToolTip, QMessageBox)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import QCoreApplication
import sys

class myWidgetClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.resize(400, 300)
        self.setWindowTitle('QtSample Level6 MessageBox')
        self.setWindowIcon(QIcon('../pythonicon.png'))

        btn = QPushButton('Quit', self)
        
        #ボタンのclickedシグナルにquitをconnect
        btn.clicked.connect(QCoreApplication.instance().quit)

        #当然、closeにconnectしておけば、closeEventを経由できるよ
        #btn.clicked.connect(self.close)

        #ボタンのサイズをいい感じに設定してもらう
        btn.resize(btn.sizeHint())

        #ボタンに吹き出しを追加
        QToolTip.setFont(QFont('SansSerif', 10))
        btn.setToolTip('This will <b>Close</b> widget without message')

        self.show()
    
    #QWidgetのcloseEventをオーバーライドする
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = myWidgetClass()
    sys.exit(app.exec_()) 