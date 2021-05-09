from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
	def __init__(self, parent=none):
		super().__init__(parent)
		self.setWindowTitle(“Hello World”)
		self.resize(800, 600)
		#self.setWIndowIcon(QIcon(“/static/logo.ico”))
		
if __name__ == '__main__':
	root = QApplication(sys.argv)
	app = Window()
	app.show()
	sys.exit(root.exec_())