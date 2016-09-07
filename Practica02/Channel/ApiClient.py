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
sys.path.insert(0, '../GUI')
from Chat import *


class MyApiClient():

    """ **************************************************
    Clase cliente del chat.
    ************************************************** """

    def __init__(self, usr, ip1, ip2):
        self.usr = usr
        self.ip1 = ip1
        self.ip2 = ip2
        self.server = xmlrpclib.ServerProxy(
            "http://"+self.ip2+":8000", allow_none=True)
        self.tem = threading.Event()
        self.chat = Chat(self.tem)
        self.chat.show()
        self.chat.boton_send.clicked.connect(self.enviar)
        self.hiloCliente = threading.Thread(target=self.escucha)
        self.hiloCliente.start()

    def escucha(self):
        """ **************************************************
        Metodo que inicia un hilo para tener el servidor siempre activo y si hay un mensaje
        en el buffer lo pasa a la interfaz.
        ************************************************** """
        while True:
            time.sleep(1)
            serverCli = xmlrpclib.ServerProxy(
                "http://"+self.ip1+":8000", allow_none=True)
            msj = serverCli.vaciaBuffer()
            if(len(msj) != 0):
                self.chat.setTexto(msj)
                print 'MI mensaje es :'+msj

    def enviar(self):
        """ **************************************************
        Metodo que envia un mensaje al servidor destino.
        ************************************************** """
        print 'Mando mensaje'
        if(self.server.ping()):
            print 'Entramos'
            msj = self.usr+' : '+str(self.chat.text_send.toPlainText())+'\n'
            self.server.sendMessage_wrapper(msj)
            self.chat.setTexto(msj)
            print 'se hizo ping con exito'
