#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE: Clase que representa la abstracción de   #
#         Un canal bidireccional, con uso de la     #
#          biblioteca xmlRpc                        #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   16-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################

from ApiServer import *
from ApiClient import *
from RecordAudio import record_audio_queue
"""**************************************************
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
**************************************************"""


class RequestChannel():

    """**************************************************
    Convencion: Si trabajamos de manera local, entonces
    haremos uso de los campos de contact_port y my_port
    por lo que el campo de contact_ip puede ser nulo.
    Si trabajamos con instancias en la red solo se hara uso
    del campo de contact_ip
    **************************************************"""
    """**************************************************
    Constructor de la clase
    @param <str> contact_ip: Si no se trabaja de manera local
                representa la ip del contacto con el que se
                establecera la conexion
    @param <int> my_port: De trabajar de manera local puerto
                de la instancia del cliente
    @param <int> contact_port: De trabajar de manera local
                representa el puerto de la instancia del contacto
    **************************************************"""

    def __init__(self, contact_ip=None, contact_port=None):
        if contact_port:
            self.api_client = ApiClient(None, contact_port)
        elif contact_ip:
            self.api_client = ApiClient(contact_ip)
        else:
            raise ValueError('The values of fields are not consistent RequestChannel.__init__')

    """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""

    def send_text(self, text):
        return self.api_client.send_text(text)
    """**************************************************
    Metodo que se encarga de mandar iniciar una conversacion
    con un nuevo contacto 
    **************************************************"""

    def new_connection(self, my_ip, my_port, my_username):
        return self.api_client.start_chat(my_ip, my_port, my_username)
    """**************************************************
    Metodo que se encarga de mandar audio y video al contacto 
    con el cual se estableció la conexion
    **************************************************"""

    def begin_call(self):
        return True
    """**************************************************
    Metodos Get
    **************************************************"""

    def get_api_client(self):
        return self.api_client


class BidirectionalChannel(RequestChannel):

    def __init__(self, Qparent, contact_ip=None,  contact_port=None, my_port=None):
        if my_port and contact_port:
            # El objeto api server necesita correr en un hilo aparte
            return True
        elif contact_ip:
            return True
        else:
            raise ValueError('The values of fields are not consistent BidirectionalChannel.__init__')
        return True
    """**************************************************
    Metodos Get
    **************************************************"""

    def get_api_server(self):
        return self.api_server_thread
