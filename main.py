import sys
from PyQt6 import QtWidgets, uic
import sqlite3


class CoffeeForm(QtWidgets.QDialog):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		uic.loadUi("addEditCoffeeForm.ui", self)
		self.pushButton.clicked.connect(self.on_clicked)

	def on_clicked(self):
		db = sqlite3.connect("coffee.sqlite")
		res = db.execute(f"""INSERT INTO coffee VALUES ({self.one.text()}, '{self.two.text()}', {self.three.text()}, {self.four.text()}, '{self.five.text()}', {self.six.text()}, {self.seven.text()})""")
		db.commit()
		db.close()
		self.close()


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
		db.close()
		self.pushButton.clicked.connect(self.on_clicked)

	def on_clicked(self):
		c = CoffeeForm()
		c.exec()
		db = sqlite3.connect("coffee.sqlite")
		res = db.execute("SELECT * FROM coffee").fetchall()
		self.listWidget.clear()
		for item in res:
			self.listWidget.addItem(", ".join([str(x) for x in item]))
		db.close()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Window()
	w.show()
	sys.exit(app.exec())