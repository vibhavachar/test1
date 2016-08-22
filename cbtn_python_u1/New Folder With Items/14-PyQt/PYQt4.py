import sys
from PyQt4 import QtGui

class MyForm(QtGui.QWidget):

	def __init__(self):
		super(MyForm, self).__init__()

		lbl = QtGui.QLabel('My First UI Element!', self)
		lbl.move(15,20)

		le = QtGui.QLineEdit('Some text in the line edit', self)
		le.move(15, 50)
		le.setFixedWidth(175)

		self.setGeometry(300,300,250,150)
		self.setWindowTitle('My Form')
		self.show()


app = QtGui.QApplication(sys.argv)
mainWindow = MyForm()
status = app.exec_()
sys.exit(status)