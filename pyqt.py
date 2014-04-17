#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows text which 
is entered in a QtGui.QLineEdit
in a QtGui.QLabel widget.
 
author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.emailLabel = QtGui.QLabel(self)
        self.emailLabel.setText('email')
        self.passWordLabel = QtGui.QLabel(self)
        self.passWordLabel.setText('Password')
        self.emailTextBox = QtGui.QLineEdit(self)
        self.passwordTextBox = QtGui.QLineEdit(self)
        self.loginBtn = QtGui.QPushButton('Login', self)

        self.emailTextBox.move(140, 38)
        self.passwordTextBox.move(140, 73)
        self.emailLabel.move(60, 40)
        self.passWordLabel.move(60, 75)
        self.loginBtn.resize(self.loginBtn.sizeHint())
        self.loginBtn.move(180, 120) 
        # qle.textChanged[str].connect(self.onChanged)
        # emailTextBox.textEdited[str].connect(self.buttonClicked)
        self.loginBtn.clicked.connect(self.buttonClicked)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QtGui.QLineEdit')
        self.show()
        
    # def onChanged(self, text):
        
        # self.lbl.setText(text)
        # self.lbl.adjustSize()    
    def buttonClicked(self,text):
    	self.hide()
    	print self.emailTextBox.text()
    	print self.passwordTextBox.text()
    	self.ProjectDialog()
    	# email = text
    	# password = self.passwordTextBox.text()
    	# print email

    def ProjectDialog(self):
    	self.setGeometry(300, 300, 280, 170)
    	self.setWindowTitle('Choose your project')
    	self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()