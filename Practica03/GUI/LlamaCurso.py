import wave
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
""" **************************************************
Clase que inicia la ventana del chat.
************************************************** """

llama = uic.loadUiType("./GUI/LlamaCursoGUI.ui")[0]
class LlamadaCurso(QMainWindow,llama):
	def __init__(self,espera_mensaje_local,parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
