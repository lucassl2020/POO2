from PyQt5.QtWidgets import QWidget, QProgressBar, QApplication
from PyQt5.QtCore import QBasicTimer
import sys

class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.set_setting()
		self.create_widgets()

	def set_setting(self):
		self.resize(350, 200)

	def create_widgets(self):
		self.progress_bar = QProgressBar(self)
		self.progress_bar.setFixedWidth(300)
		self.progress_bar.move(30, 80)#Mover posição na tela (X, Y)
		#timer creating
		self.timer = QBasicTimer()
		self.step = 0
		self.timer.start(100, self)

	def timerEvent(self, e):
		if self.step >= 100:
			self.timer.stop()
		self.step += 1
		self.progress_bar.setValue(self.step)

if __name__ == '__main__':
	root = QApplication([])
	app = Window()
	app.show()
	sys.exit(root.exec_())