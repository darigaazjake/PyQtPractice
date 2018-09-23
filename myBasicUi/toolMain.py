#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
自分用のPyQtツール GUI基本形を作る
2018.09.24
枠だけ作ってみる
"""

import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QFileDialog,
    qApp)
from workDir.basicForm import Ui_MainWindow

from os.path import expanduser
homeDir = expanduser("~")

class Test(QMainWindow):
    def __init__(self, parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Toolbar action
        self.ui.actionOpen.triggered.connect(self.fileOpenCmd)
        self.ui.actionOption.triggered.connect(self.toolOptionCmd)
        self.ui.actionEnd.triggered.connect(qApp.quit)
    
    def fileOpenCmd(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', homeDir)
        print("[fileOpenCmd] '{}' specified".format(fname))
    
    def toolOptionCmd(self):
        print("[toolOptionCmd] Not coded yet")

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())