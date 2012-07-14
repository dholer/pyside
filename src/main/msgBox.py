#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Joseph
@email:liseor@gmail.com
Created on 2012-7-14
'''
import sys
 
import PySide
from PySide.QtGui import QApplication
from PySide.QtGui import QMessageBox
 

if __name__ == '__main__':
    # Create the application object
    app = QApplication(sys.argv)
     
    # Create a simple dialog box
    msgBox = QMessageBox()
    msgBox.setText("Hello World - using PySide version " + PySide.__version__)
    msgBox.exec_()