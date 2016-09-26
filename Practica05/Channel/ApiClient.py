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

    def __init__(self, contact_ip=None, contact_port=None):
        self.my_ip = get_ip_address()
        try:
            if contact_port:
                # ip local + puerto indicado
                self.remote_ip = self.my_ip
                self.remote_server = xmlrpclib.ServerProxy("http://" + self.my_ip + ":" + contact_port, allow_none=True)
            elif contact_ip:
                # ip indicado + PORT
                self.remote_ip = contact_ip
                self.remote_server = xmlrpclib.ServerProxy("http://"+contact_ip+":"+Constants.PORT, allow_none=True)
            else:
                raise ValueError('The values of fields are not consistent MyApiClient.__init__')
            self.username_remote = username  # TODO
        except Exception, e:
            raise e

    def send_text(self, message):
        wrapped_message = Message(self.username, self.my_ip, message)
        try:
            self.remote_server.sendMessage_wrapper(wrapped_message)
            # TODO dibuja el mensaje en la ventana de chat correspondiente
            return True
        except Exception, e:
            raise e

    def start_chat(self, my_ip, my_port, my_username):
        self.my_username = my_username
        self.remote_server.new_chat_wrapper(self, contact_ip, contact_port, self.my_username)
