# -*- coding: utf-8 -*-
__author__ = 'Red_Labs'

import sys
from PyQt4 import QtGui, QtCore
from FormESA import Ui_MainForm
from SecondFormESA import Ui_MainForm_second
from esa_database import esa_db
from Generator import Generator

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.model = esa_db()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        self.initUI()


    def initUI(self):
        self.setGeometry(400, 100, 890, 690)
        self.setMaximumSize(490, 590)

        #Signals&Slots for FormESA.py
        QtCore.QObject.connect(self.ui.pushButtonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.WindClose)
        QtCore.QObject.connect(self.ui.pushButtonGeneric, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Generate)
        QtCore.QObject.connect(self.ui.checkBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Check)

    #Functions for FormESA.py
    def WindClose(self):
        MainWindow.close(self)

    def Generate(self):
            self.close()
            global  sw
            sw = SecondWindow()
            sw.show()
            gen = Generator()
            gen.checking(self.ui.lineEdit_FIO.text(),self.ui.comboBox_Grupa.currentText(),self.ui.comboBox_Object.currentText())
            sw.ui_sec.label_5.setText(gen.rez.decode('utf8'))

    def Check(self):
        self.ui.pushButtonGeneric.setEnabled(True)

class SecondWindow(QtGui.QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.ui_sec = Ui_MainForm_second()
        self.ui_sec.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100, 890, 690)
        self.setMaximumSize(490, 590)

    #Signals&Slots for SecondFormESA.py
        QtCore.QObject.connect(self.ui_sec.pushButtonClose, QtCore.SIGNAL(_fromUtf8("clicked()")), self.WindClose)

    def WindClose(self):
        self.close()




def main():

    app = QtGui.QApplication(sys.argv)
    td = MainWindow()
    td.show()

    sys.exit(app.exec_())

if __name__=="__main__":
    main()
