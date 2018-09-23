"""
Qt Designerで作った.uiを利用する例
Level2
btnのSIGNALを、btnClickedActionにconnectする
"""

import sys
from PyQt5 import QtWidgets
from workDir.myForm import Ui_Form

class Test(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.clickedCount = 0
    
    def btnClickedAction(self):
        self.clickedCount = self.clickedCount + 1
        self.ui.lbl.setText("btn Clicked !! {}".format(self.clickedCount))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())