from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi('firstUI.ui')
win.show()
sys.exit(app.exec())