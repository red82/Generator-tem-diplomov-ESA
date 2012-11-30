__author__ = 'red'
import sys
from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()

widget.setGeometry(200, 100, 400, 300)
widget.setWindowTitle('PyQt Application')

cb = QtGui.QComboBox(widget)
label = QtGui.QLabel(widget)

lang = ['Python','Java','Javascript','PHP','C','C++','Ruby']
for i in lang:
    cb.addItem(i)

cb.setGeometry(10, 10, 150, 20)
label.setGeometry(170, 10, 100, 20)

def hello(text):
    label.setText(text)

widget.connect(cb, QtCore.SIGNAL('activated(QString)'), hello)

widget.show()
sys.exit(app.exec_())