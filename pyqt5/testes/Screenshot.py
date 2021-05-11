from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QGridLayout, QFileDialog)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import sys

class MainWindow(QWidget):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__()
		self.preview_screen = QApplication.primaryScreen().grabWindow(0)
		self.settings()
		self.create_widgets()
		self.set_layout()

	def settings(self):
		self.resize(370, 270)
		self.setWindowTitle("Screenshoter")

	def create_widgets(self):
		self.img_preview = QLabel()
		self.img_preview.setPixmap(self.preview_screen.scaled(720, 720, Qt.KeepAspectRatio, Qt.SmoothTransformation))

		self.btn_save_screenshot = QPushButton("Save screenshot")
		self.btn_new_screenshot = QPushButton("New screenshot")

		# signals connections
		self.btn_save_screenshot.clicked.connect(self.save_screenshot)
		self.btn_new_screenshot.clicked.connect(self.new_screenshot)

	def set_layout(self):
		self.gridLayout = QGridLayout()
		self.gridLayout.addWidget(self.img_preview, 0, 0, 1, -1)
		self.gridLayout.addWidget(self.btn_save_screenshot, 1, 0)
		self.gridLayout.addWidget(self.btn_new_screenshot, 1, 1)

		self.setLayout(self.gridLayout)

	def save_screenshot(self):
		img, _ = QFileDialog.getSaveFileName(self,"Salvar Arquivo", filter="PNG(*.png);; JPEG(*.jpg)")
		if img[-3:] == "png":
			self.preview_screen.save(img, "png")
		elif img[-3:] == "jpg":
			self.preview_screen.save(img, "jpg")

	def new_screenshot(self):
		self.hide()
		QTimer.singleShot(100, self.take_screenshot)

	def take_screenshot(self):
		self.preview_screen = QApplication.primaryScreen().grabWindow(0)
		self.img_preview.setPixmap(self.preview_screen.scaled(720, 720, Qt.KeepAspectRatio, Qt.SmoothTransformation))
		self.show()


if __name__ == '__main__':
	root = QApplication([])
	app = MainWindow()
	app.show()
	sys.exit(root.exec_())
