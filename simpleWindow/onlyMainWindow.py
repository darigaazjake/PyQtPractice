"""
Level 3
ボタンを置くだけ
"""

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton)
from PyQt5 import QtGui
import sys

class myWidgetClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.resize(300, 200)
        self.setWindowTitle('QtSample Level3 Button')
        self.setWindowIcon(QtGui.QIcon('../pythonicon.png'))

        #この1行だけでボタンがおける
        btn = QPushButton('Button', self)

        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = myWidgetClass()
    sys.exit(app.exec_()) 