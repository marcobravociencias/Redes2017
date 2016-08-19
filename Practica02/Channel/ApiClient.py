#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import time
#from chatN import Chat

class MyApiClient():
	def __init__(self, usr, ip1, port):
		self.usr = usr
		self.ip1 = ip1
		self.port = port
		#self.ip2 = ip2
		#self.ApiServer = xmlrpclib.ServerProxy("http://"+self.ip2+":8000",allow_none=True) 
		#self.tem = threading.Event()
		#self.chat = Chat(self.tem)
		#self.chat.show()
		#self.chat.boton_send.clicked.connect(self.enviar)
		#self.hiloClient = threading.Thread(target=self.escucha)
		#self.hiloClient.start()

	#def escucha():
	#	while True:
	#		time.sleep(1)
	#		server = xmlrpclib.ServerProxy("http://"+self.ip1+":8000",allow_none=True) 
	#		msj = server.vaciaBuffer()
	#		if(len(msj)!=0):
	#			#self.chat.setTexto(msj)
	#			print 'MI mensaje es :'+msj
		
	def enviar():
		print 'Mando mensaje'
		if(self.ApiServer.ping()):
			print 'Entramos'
			msj = self.usr+' : '#+str(self.chat.text_send.toPlainText())+'\n'
			self.ApiServer.sendMessage_wrapper(msj)
			#self.chat.setTexto(msj)
			print 'se hizo ping con exito'
		
		
