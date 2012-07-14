#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Joseph
@email:liseor@gmail.com
Created on 2012-7-14
'''
import sys
from PySide.QtGui import *
from PySide.QtCore import *

#greetin
def sayHello():
    print "Hello World!!"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    btn = QPushButton("Click Me!")
    btn.clicked.connect(sayHello)
    btn.resize(100,50)
    btn.show()
    app.exec_()
    sys.exit()
    