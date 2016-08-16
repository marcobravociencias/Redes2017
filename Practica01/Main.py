# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
#Importamos las rutas de nuestros archivos 
sys.path.insert(0, './Code/')
sys.path.insert(1, './GUI/')

from ScientificCalculatorGUI import VentanaCalculadora
from archiva import archiva

regisError = uic.loadUiType("./GUI/regisError.ui")[0] #Cargamos la interfaz en un arreglo
#
#Clase que despliega una ventana de error al no poder iniciar sesion
#
class Error(QtGui.QMainWindow, regisError):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self) #Inicializamos la interfaz 
		self.botonRegresaLogin.clicked.connect(self.salir)#Linkeamos el boton al evento
	#
	#Metodo que oculta la ventana
	#
	def salir(self):
		self.hide()

main_class = uic.loadUiType("./GUI/login.ui")[0] #Cargamos la interfaz en un arreglo
#
#Clase que despliega la ventana de login 
#
class Ventana(QMainWindow,main_class):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.botonLogin.clicked.connect(self.OK)
		self.w = None
		self.c = None

	def OK(self):
		usuario = str(self.usserLogin.text()).replace(' ','')
		password = str(self.passLogin.text()).replace(' ','')
		log = archiva(usuario,password)
		if log.login():
			#abrir otra interfaz
			self.c = VentanaCalculadora()
			self.c.show()
			self.hide()
		else:
			self.w = Error()
			self.w.show()

class App(QApplication):
	def __init__(self, *args):
		QApplication.__init__(self, *args)
		self.main = Ventana()
		self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye )
		self.main.show()

	def byebye( self ):
		self.exit(0)    
 
def main(args):
	global app
	app = App(args)
	app.exec_()

if __name__ == "__main__":
	main(sys.argv)