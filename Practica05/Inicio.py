#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import xmlrpclib
import threading
from Cliente import *
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Servidor import *

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

inicio_class = uic.loadUiType("Inicio.ui")[0]

class Inicio(QtGui.QMainWindow, inicio_class):
    """
    Clase que define la interfaz de la pantalla de Inicio
    """
    def __init__(self, parent=None):
        """
        Define los parametros para Inicio
        """
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.ok.clicked.connect(self.verifica)#Hace la conexión del boton "ok" con el metodo verifica
        self.clientesito = None

    def verifica(self):
        """
        Recibe de los campos de entrada la ip local, la remota y el nombre, crea un threading que hace la
        conexion con correServidor en la Clase Servidor y inicializa el threading. Tambien establece un
        cliente con el nombre que le pasan
        """
    	local = str(self.local.text())
        contactos = str(self.contactos.text())
        nombre = str(self.nombre.text())
        self.hilo_servidor = threading.Thread(target=self.correServidor,args=(local,), name='hilo_servidor')
        self.hilo_servidor.start()
        self.clientesito = Cliente(nombre,local,contactos)

    def correServidor(self,ip):
        """
        Metodo que comienza a correr el servidor con la ip que le pasan
        """
    	ip_local = ip
    	print ip_local
    	server = SimpleXMLRPCServer((ip_local, 8000),requestHandler=RequestHandler,allow_none=True)
    	server.register_introspection_functions()
    	server.register_instance(ServidorChat())
    	try:
    		print 'Use Control-C to exit'
    		server.serve_forever()
    	except KeyboardInterrupt:
    		print 'Exiting'

def main():
    app = QtGui.QApplication(sys.argv)
    miVentana = Inicio(None)
    miVentana.show()
    app.exec_()

if __name__ == "__main__":
    main()
