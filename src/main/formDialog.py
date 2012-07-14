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

class Form(QDialog):
    '''
    classdocs
    '''


    def __init__(self,parent=None):
        '''
        Constructor
        '''
        super(Form,self).__init__(parent)
        
        self.setWindowTitle("Form Dialog!")
        
        self.btn = QPushButton("click me!")
        self.edit = QLineEdit("Write your name!")
        
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.edit)
        self.resize(220,300)
        self.setLayout(layout)
        
        self.btn.clicked.connect(self.sayHello)
    def sayHello(self):
        print "Hello %s" % self.edit.text()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
    
        