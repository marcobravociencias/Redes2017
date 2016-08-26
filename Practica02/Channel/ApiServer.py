#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys


class FunctionWrapper:

    def __init__(self):
        self.buffer = list()

    def sendMessage_wrapper(self, message):
        """ **************************************************
        Procedimiento que ofrece nuestro servidor, este metodo sera llamado
        por el cliente con el que estamos hablando, debe de
        hacer lo necesario para mostrar el texto en nuestra pantalla.
        ************************************************** """
        self.buffer.append(message)

    def ping(self):
        """ **************************************************
        Metodo que nos indica si el servidor se encuentra en servicio.
        ************************************************** """
        return True

    def vaciaBuffer(self):
        """ **************************************************
        Metodo que nos deja vacio el buffer del servidor donde guarda
        los mensajes y lo regresa.
        ************************************************** """
        buffer = ''
        for m in self.buffer:
            buffer += m
            print buffer
            self.buffer = list()
        return buffer