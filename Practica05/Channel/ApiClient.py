#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys
sys.path.insert(0, '../Constants')
from Constants import CHAT_PORT
from AuxiliarFunctions import *
from Message import *

"""**************************************************
Clase que genera un proxy para poder hacer uso de
los procedimientos remotos que ofrece la api del contacto
**************************************************"""


class MyApiClient:

    def __init__(self, username, contact_ip=None, contact_port=None):
        self.username_local = username
        self.ip_local = get_ip_address()
        try:
            if contact_port:
                # ip local + puerto indicado
                self.ip_remote = self.ip_local
                self.server = xmlrpclib.ServerProxy("http://" + self.ip_local + ":" + contact_port, allow_none=True)
            elif contact_ip:
                # ip indicado + PORT
                self.ip_remote = contact_ip
                self.server = xmlrpclib.ServerProxy("http://"+contact_ip+":"+Constants.PORT, allow_none=True)
            else:
                raise ValueError('The values of fields are not consistent MyApiClient.__init__')
            self.username_remote = username  # TODO
        except Exception, e:
            raise e

    def send_text(self, message):
        wrapped_message = Message(self.username, self.ip_local, message)
        try:
            self.server.sendMessage_wrapper(wrapped_message)
            # TODO dibuja el mensaje en la ventana de chat correspondiente
        except Exception, e:
            raise e
