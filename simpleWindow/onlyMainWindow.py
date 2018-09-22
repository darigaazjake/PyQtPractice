"""
Level 2
クラスにする
"""

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
import sys

class myWidgetClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.resize(250, 150)
        self.setWindowTitle('QtSample')
        self.setWindowIcon(QtGui.QIcon('../pythonicon.png'))
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = myWidgetClass()
    sys.exit(app.exec_()) 