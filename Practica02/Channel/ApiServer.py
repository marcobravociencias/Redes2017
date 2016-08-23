#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys

#class MyApiServer():
#    def __init__(self, my_port = None):
#    	pass

class FunctionWrapper:
    def __init__(self):
        self.buffer = list()

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        self.buffer.append(message)
    """ **************************************************
    Metodo que nos indica si el servidor se encuentra en servicio.
    ************************************************** """
    def ping(self):
        return True
    
    """ **************************************************
    Metodo que nos deja vacio el buffer del servidor donde guarda
    los mensajes y lo regresa. 
    ************************************************** """
    def vaciaBuffer(self):
        buffer = ''
        for m in self.buffer:
            buffer += m
            print buffer
            self.buffer = list()
        return buffer
        