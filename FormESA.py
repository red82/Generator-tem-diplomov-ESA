# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/red/ESA/ESA_diplom.py/FormESA.ui'
#
# Created: Fri Nov 16 17:16:30 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from esa_database import esa_db

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainForm(object):
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
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("./logoESA.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(MainForm)
        self.label_4.setGeometry(QtCore.QRect(120, 200, 272, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButtonGeneric = QtGui.QPushButton(MainForm)
        self.pushButtonGeneric.setGeometry(QtCore.QRect(240, 540, 111, 27))
        self.pushButtonGeneric.setObjectName(_fromUtf8("pushButtonGeneric"))
        self.pushButtonCancel = QtGui.QPushButton(MainForm)
        self.pushButtonGeneric.setEnabled(False)
        self.pushButtonCancel.setGeometry(QtCore.QRect(360, 540, 111, 27))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.layoutWidget1 = QtGui.QWidget(MainForm)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 250, 281, 111))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit_FIO = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_FIO.setText(_fromUtf8(""))
        self.lineEdit_FIO.setObjectName(_fromUtf8("lineEdit_FIO"))
        self.verticalLayout.addWidget(self.lineEdit_FIO)
        self.comboBox_Grupa = QtGui.QComboBox(self.layoutWidget1)
        self.comboBox_Grupa.setObjectName(_fromUtf8("comboBox_Grupa"))
        self.verticalLayout.addWidget(self.comboBox_Grupa)
        self.comboBox_Object = QtGui.QComboBox(self.layoutWidget1)
        self.comboBox_Object.setObjectName(_fromUtf8("comboBox_Object"))
        self.verticalLayout.addWidget(self.comboBox_Object)
        self.layoutWidget2 = QtGui.QWidget(MainForm)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 250, 88, 111))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.setWordWrap(True)
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.layoutWidget2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.layoutWidget2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.checkBox = QtGui.QCheckBox(MainForm)
        self.checkBox.setGeometry(QtCore.QRect(100, 480, 371, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

        self.init_data()

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
        self.label_4.setText(QtGui.QApplication.translate("MainForm", "<html><head/><body><p><span style=\" font-weight:600;\">Введите, пожалуйста, свои данные:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGeneric.setText(QtGui.QApplication.translate("MainForm", "Продолжить", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("MainForm", "Отмена", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainForm", "ФИО", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainForm", "Группа", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainForm", "Тип объекта", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainForm", "Я согласен с тем, что заполненные данные верны", None, QtGui.QApplication.UnicodeUTF8))

    def init_data(self):
        self.model = esa_db()

        groups = self.model.get_groups_list()
        self.set_groups_list(groups)

        technical_objects = self.model.get_tech_objects_list()
        self.set_tech_objects_list(technical_objects)

    def set_tech_objects_list(self, technical_objects):
       for i in technical_objects:
            self.comboBox_Object.addItem(i)

    def set_groups_list(self, groups):
        for i in groups:
            self.comboBox_Grupa.addItem(i)


