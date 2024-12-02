import sys
from PyQt6 import QtWidgets, uic
import sqlite3


class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		uic.load_ui.loadUi("main.ui", self)
		db = sqlite3.connect("coffee.sqlite")
		res = db.execute("SELECT * FROM coffee").fetchall()
		for item in res:
			self.listWidget.addItem(", ".join([str(x) for x in item]))

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Window()
	w.show()
	sys.exit(app.exec())