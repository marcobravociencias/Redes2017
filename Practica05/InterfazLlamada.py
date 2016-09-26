# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *

llamada = uic.loadUiType("Llamada.ui")[0]

class InterfazLlamada(QtGui.QMainWindow, llamada):
	"""
	Metodo que define la interfaz de la ventana emergente para llamada
	"""
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)