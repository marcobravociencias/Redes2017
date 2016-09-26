#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import xmlrpclib
from Mensaje import *
from InterfazLlamada import *


chat_class = uic.loadUiType("Chat.ui")[0]

class Chat(QtGui.QMainWindow, chat_class):
    """
    Clase que define la interfaz de Chat.ui
    """
    def __init__(self,ip_remoto,parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.ip_remoto = ip_remoto
        #self.servidor_remoto = xmlrpclib.ServerProxy("http://"+self.ip_remoto+":8000",allow_none=True)
        
    def texto_actual(self):
        """
        Metodo que recibe texto de cajaChat de la clase Chat.ui, lo borra una vez insertado y lo regresa
        """
        texto = str(self.cajaChat.toPlainText())
        self.cajaChat.clear()
        return texto
    def ponTexto(self,fecha,autor,texto):
        """
        Muestra el texto en el chat en el formato deseado, poniendo primero fecha, autor y el texto
        """
        self.chat.insertPlainText(" "+fecha+" "+autor+ " : "+texto+"\n")