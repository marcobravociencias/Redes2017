#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE: Clase que permite mandar un mensaje al   #
#           contacto                                #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   17-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
#           Mis bibliotecas
import sys
from AuxiliarFunctions import *
from Constants import *
from Message import *

# Restrict to a particular path.


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
"""**************************************************
Clase que genera un servidor de la biblioteca xmlrpc
con el cual el cliente expondra los metodos que ofrece
**************************************************"""


class MyApiServer:

    def __init__(self, Qparent, my_port=None):
        self.my_port = my_port
        self.my_ip = get_ip_address()
        self.function_wrapper = FunctionWrapper()
        self.server = SimpleXMLRPCServer((self.my_ip, self.my_port, requestHandler=RequestHandler, allow_none=True)
        self.server.register_introspection_functions()
        self.server.register_instance(self.function_wrapper)

    def run(self):
        print 'serving at ' + self.my_ip + ':' + self.my_port + '...'
        self.server.serve_forever()


class FunctionWrapper:

    """ **************************************************
    Constructor de la clase
    ************************************************** """

    def __init__(self):
        # Diccionario que contiene las conversaciones activas
        # hasta ese momento
        self.chats_dictionary={}
        self.unread_messages=list()
        self.read_messages=list()

    """**************************************************
    Metodo que sera llamado cuando un contacto quiera establecer
    conexion con este cliente
    **************************************************"""

    def new_chat_wrapper(self, contact_ip, contact_port, username):
        # Un cliente mando a llamar a esta instancia, crea una ventana de
        # chat para automaticamente
        return True
    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """

    def sendMessage_wrapper(self, message):
        print "servidor recibe mensaje: " + str(message)
        wrapped_message=Message(message['author_username'], message['author_ip'], message['content'], message['date'])
        print "servidor empaqueta mensaje: " + str(wrapped_message)
        self.unread_messages.append(wrapped_message)

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para regresar el texto
    ************************************************** """

    def echo(self, message):
        return True
    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para reproducir el audio
    ************************************************** """

    def play_audio_wrapper(self, audio):
        return True
    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para reproducir el video en la ventana adecuada
    ************************************************** """

    def play_video_wrapper(self, frame):
        return True
