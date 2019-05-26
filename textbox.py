import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):
	def __init__(self):
		super().__init__()
		print('__init__')
		self.title = 'Textbox Example'
		self.left = 200
		self.top = 100
		self.width = 400
		self.height = 120
		self.initUI()

	def initUI(self):
		print('initUI')
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.label = QLabel('Name:', self)
		self.label.move(60, 20)
		self.textbox = QLineEdit(self)
		self.textbox.move(60, 40)
		self.button = QPushButton('Click Me', self)
		self.button.move(60, 70)
		self.button.clicked.connect(self.onClick)

		self.show()

	def onClick(self):
		QMessageBox.question(self, 'Clicked', 'Hello ' + self.textbox.text(), QMessageBox.Ok, QMessageBox.Ok)

if __name__ == '__main__':
	print('__main__')
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
