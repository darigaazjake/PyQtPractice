"""
Level 1
窓だけ 
"""

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
import sys

app = QApplication(sys.argv)
w = QWidget()
w.resize(250, 150)
w.setWindowTitle('QtSample')
w.setWindowIcon(QtGui.QIcon('../pythonicon.png'))
w.show()
sys.exit(app.exec_())