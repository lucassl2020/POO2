from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


if __name__ == '__main__':
	root = QApplication(sys.argv)

	tela_principal = uic.loadUi("telaPrincipal.ui")
	tela_principal.show()

	buscar_tela = uic.loadUi("buscar_tela.ui")
	buscar_tela.show()

	cadastrar_tela = uic.loadUi("cadastrar_tela.ui")
	cadastrar_tela.show()


	sys.exit(root.exec_())