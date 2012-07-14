#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Joseph
@email:liseor@gmail.com
Created on 2012-7-14

pyside-uic quitter.ui -o ui_quitter.py

'''

import sys
 
from PySide.QtGui import QMainWindow, QPushButton, QApplication 
from .ui_quitter import Ui_MainWindow
 
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()    
    app.exec_()