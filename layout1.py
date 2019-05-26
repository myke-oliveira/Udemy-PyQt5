import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout

class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'PyQt5 layout'
		self.left = 10
		self.top = 10
		self.width = 320
		self.height = 500
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.createHorizontalLayout()
		self.show()

	def createHorizontalLayout(self):

		self.horizontalGroupBox = QGroupBox('Horizontal Layout', self)
		self.layouth = QHBoxLayout()

		self.buttonA = QPushButton('A', self)
		self.layouth.addWidget(self.buttonA)

		self.buttonB = QPushButton('B', self)
		self.layouth.addWidget(self.buttonB)

		self.buttonC = QPushButton('C', self)
		self.layouth.addWidget(self.buttonC)

		self.horizontalGroupBox.setLayout(self.layouth)

		self.verticalGroupBox = QGroupBox('Vertical Layout', self)
		self.layoutv = QVBoxLayout()

		self.buttonD = QPushButton('D', self)
		self.layoutv.addWidget(self.buttonD)

		self.buttonE = QPushButton('E', self)
		self.layoutv.addWidget(self.buttonE)

		self.buttonF = QPushButton('F', self)
		self.layoutv.addWidget(self.buttonF)

		self.verticalGroupBox.setLayout(self.layoutv)

		self.gridGroupBox = QGroupBox('Grid Layout', self)
		self.layoutg = QGridLayout()

		self.buttonG = QPushButton('G', self)
		self.layoutg.addWidget(self.buttonG, 0, 0)

		self.buttonH = QPushButton('H', self)
		self.layoutg.addWidget(self.buttonH, 0, 1)

		self.buttonI = QPushButton('I', self)
		self.layoutg.addWidget(self.buttonI, 0, 2)

		self.buttonJ = QPushButton('J', self)
		self.layoutg.addWidget(self.buttonJ, 1, 0)

		self.buttonK = QPushButton('K', self)
		self.layoutg.addWidget(self.buttonK, 1, 1)

		self.buttonL = QPushButton('L', self)
		self.layoutg.addWidget(self.buttonL, 1, 2)

		self.buttonM = QPushButton('M', self)
		self.layoutg.addWidget(self.buttonM, 2, 0)

		self.buttonN = QPushButton('N', self)
		self.layoutg.addWidget(self.buttonN, 2, 1)

		self.buttonO = QPushButton('O', self)
		self.layoutg.addWidget(self.buttonO, 2, 2)

		self.gridGroupBox.setLayout(self.layoutg)

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.horizontalGroupBox)
		self.layout.addWidget(self.verticalGroupBox)
		self.layout.addWidget(self.gridGroupBox)
		self.setLayout(self.layout)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec())