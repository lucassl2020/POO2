from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit, QPushButton, 
							QRadioButton, QGroupBox, QMessageBox, QVBoxLayout, QHBoxLayout)
import sys


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.set_settings()
		self.create_widgets()
		self.set_layout()

	def set_settings(self):
		self.resize(350, 200)
		self.setWindowTitle("Mensagem")

	def create_widgets(self):
		self.button = QPushButton("Exibir mensagem")
		self.button.clicked.connect(self.exibir)
		self.line_edit = QLineEdit()

		self.groupbox = QGroupBox("Opções de Diálogo")

		self.option_information = QRadioButton("Information")
		self.option_warning = QRadioButton("Warning")
		self.option_critical = QRadioButton("Critical")
		self.option_critical.setChecked(True)

	def set_layout(self):
		self.layout_groupbox = QVBoxLayout()
		self.layout_groupbox.addWidget(self.option_information)
		self.layout_groupbox.addWidget(self.option_warning)
		self.layout_groupbox.addWidget(self.option_critical)

		self.groupbox.setLayout(self.layout_groupbox)

		self.layout_first_widgets = QHBoxLayout()
		self.layout_first_widgets.addWidget(self.line_edit)
		self.layout_first_widgets.addWidget(self.button)
    
		self.layout_master = QVBoxLayout()
		self.layout_master.addLayout(self.layout_first_widgets)
		self.layout_master.addWidget(self.groupbox)

		self.setLayout(self.layout_master)

	def exibir(self):
		self.text = self.line_edit.text()

		if self.option_information.isChecked():
			self.messsage_box = QMessageBox.information(self, "Texto", self.text)
		elif self.option_warning.isChecked():
			self.messsage_box = QMessageBox.warning(self, "Texto", self.text)
		else:
			self.messsage_box = QMessageBox.critical(self, "Texto", self.text)

	def closeEvent(self, e):
		e.ignore()

		question_close = QMessageBox.question(self, "Fechamento", "Deseja realmente fechar a aplicação?", QMessageBox.Yes, QMessageBox.No)

		if question_close == QMessageBox.Yes:
			exit(0)


if __name__ == '__main__':
	root = QApplication([])
	app = Window()
	app.show()
	sys.exit(root.exec_())
