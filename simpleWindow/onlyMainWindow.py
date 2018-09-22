"""
Level 4
ボタンに吹き出し
"""

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import (QIcon, QFont)
import sys

class myWidgetClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        #吹き出しの設定
        QToolTip.setFont(QFont('SansSerif', 10))

        #selfに吹き出し追加
        self.setToolTip('This is a <b>QWidget</b> widget')

        self.resize(400, 300)
        self.setWindowTitle('QtSample Level4 ToolChips')
        self.setWindowIcon(QIcon('../pythonicon.png'))

        btn = QPushButton('Button', self)

        #ボタンのサイズをいい感じに設定してもらう
        btn.resize(btn.sizeHint())

        #ボタンに吹き出しを追加
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = myWidgetClass()
    sys.exit(app.exec_()) 