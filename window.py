import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class App(QWidget):
	def __init__(self):
		super().__init__()
		print('__init__')
		self.title = 'PyQt5 Window'
		self.left = 200
		self.top = 100
		self.width = 400
		self.height = 200
		self.initUI()

	def initUI(self):
		print('initUI')
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.show()

if __name__ == '__main__':
	print('__main__')
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
