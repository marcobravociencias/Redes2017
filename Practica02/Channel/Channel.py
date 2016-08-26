#! /usr/bin/env python
# -*- coding: utf-8 -*-
from ApiServer import MyApiServer
from ApiClient import MyApiClient


class Channel:

    """**************************************************
    Las instancias de esta clase contendran los metodos
    necesarios para hacer uso de los metodos
    del api de un contacto. Internamente Trabajara
    con una proxy apuntando hacia los servicios del
    servidor xmlrpc del contacto
    **************************************************"""

    def __init__(self, contact_ip=None, contact_port=None):
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
        self.contact_ip = contact_ip
        self.contact_port = contact_port

    def send_text(self, text):
        """**************************************************
        Metodo que se encarga de mandar texto al contacto con
        el cual se estableció la conexion
        **************************************************"""
        pass
