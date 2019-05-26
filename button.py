import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon

class App(QWidget):
	def __init__(self):
		super().__init__()
		print('__init__')
		self.title = 'Hello World'
		self.left = 200
		self.top = 100
		self.width = 400
		self.height = 200
		self.initUI()

	def initUI(self):
		print('initUI')
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.label = QLabel('Hello World', self)
		self.label.move(60, 80)
		self.label2 = QLabel('Hello World', self)
		self.label2.move(60, 100)
		self.button = QPushButton('Click', self)
		self.button.move(60, 120)
		self.button.clicked.connect(self.onClick)
		self.button2 = QPushButton('Click 2', self)
		self.button2.move(60, 140)
		self.button2.clicked.connect(self.onClick2)

		self.show()

	# @pyqtSlot()
	def onClick(self):
		print('Button click!')

	def onClick2(self):
		print('Button 2 click!')
if __name__ == '__main__':
	print('__main__')
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
