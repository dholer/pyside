#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Joseph
@email:liseor@gmail.com
Created on 2012-7-14
'''
from PySide.QtGui  import *
from PySide.QtCore import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #label = QLabel("Hello World!")
    label = QLabel("<font size=40 color=red>Hello World!!</font>")
    label.resize(200,100)
    
    label.show()
    app.exec_()
    sys.exit()