#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys

class MyApiServer(SimpleXMLRPCRequestHandler):
    def __init__(self, my_port = None):
    	#TODO
    	rpc_paths = ('/RPC2',)
        
class FunctionWrapper:
    def __init__(self):
        #TODO
        self.buffer = list()

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        #TODO
        self.buffer.append(message)
    
    def ping(self):
        return True

    def vaciaBuffer(self):
        buffer = ''
        for m in self.buffer:
            buffer += m
            print buffer
            self.buffer = list()
        return buffer