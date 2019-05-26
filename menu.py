import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction
from PyQt5.QtGui import QIcon

class App(QMainWindow):
	def __init__(self):
		super().__init__()
		print('__init__')
		self.title = 'Menu Example'
		self.left = 200
		self.top = 200
		self.width = 500
		self.heigt = 300
		self.initUI()

	def initUI(self):
		print('initUI')
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.heigt)

		self.mainMenu = self.menuBar()
		self.fileMenu = self.mainMenu.addMenu('File')
		self.editMenu = self.mainMenu.addMenu('Edit')
		self.viewMenu = self.mainMenu.addMenu('View')
		self.searchMenu = self.mainMenu.addMenu('Search')
		self.toosMenu = self.mainMenu.addMenu('Tools')
		self.helpMenu = self.mainMenu.addMenu('Help')

		self.openButton = QAction('Open', self)
		self.openButton.setShortcut('Ctrl+O')
		self.openButton.setStatusTip('Open File')
		self.openButton.triggered.connect(self.open)
		self.fileMenu.addAction(self.openButton)
		
		self.show()

	def open(self):
		print('Open file')

if __name__ == '__main__':
	print('__main__')
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
