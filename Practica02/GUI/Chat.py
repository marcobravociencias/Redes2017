import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
""" **************************************************
Clase que inicia la ventana del chat.
************************************************** """

main_class = uic.loadUiType("./GUI/ChatGUI.ui")[0]
class Chat(QMainWindow,main_class):
	def __init__(self,espera_mensaje_local,parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		
	""" **************************************************
	Metodo que obtiene el texto de la casilla para escribir
	y lo regresa.
	************************************************** """
	def getTexto(self): 	
		msj = str(self.text_send.toPlainText())
		self.text_send.clear()
		return msj
	""" **************************************************
	Metodo que pone el texto en la interfaz del chat.
	************************************************** """
	def setTexto(self,mensaje):
		self.text_receive.insertPlainText(mensaje) #interfaz