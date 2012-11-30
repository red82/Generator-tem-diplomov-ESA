# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/red/ESA/ESA_diplom.py/SecondFormESA.ui'
#
# Created: Thu Nov 22 10:55:49 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainForm_second(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(490, 590)
        MainForm.setMinimumSize(QtCore.QSize(490, 590))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Charter"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainForm.setFont(font)
        MainForm.setMouseTracking(False)
        self.label_1 = QtGui.QLabel(MainForm)
        self.label_1.setGeometry(QtCore.QRect(20, 550, 64, 17))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.label_1.setToolTip('by Andrey Redkin')
        self.layoutWidget = QtGui.QWidget(MainForm)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 10, 421, 171))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setEnabled(True)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("../logoESA.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(MainForm)
        self.label_4.setGeometry(QtCore.QRect(80, 200, 349, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButtonClose = QtGui.QPushButton(MainForm)
        self.pushButtonClose.setGeometry(QtCore.QRect(360, 540, 111, 27))
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.label_5 = QtGui.QLabel(MainForm)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 421, 221))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.setWordWrap(True)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "Генератор тем дипломов ЭСА", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("MainForm", "<html><head/><body><p><span style=\" font-size:8pt;\">Alpha 1.0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; line-height:50%}\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       Программное обеспечение для </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">автоматической генерации тем </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">дипломных проектов бакалавров</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">по специальности &quot;Электромехани-</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ческие системы автоматизации и </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">электропривод&quot;, шифр специаль-</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ности 7.092203 для студентов всех</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">форм обучения, ДГМА, Краматорск.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainForm", "<html><head/><body><p><span style=\" font-weight:600;\">Результаты генератора тем дипломных проектов:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClose.setText(QtGui.QApplication.translate("MainForm", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bitstream Charter\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\';\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

