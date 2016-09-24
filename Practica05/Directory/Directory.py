#!/usr/bin/env python
#-*- coding: utf-8 -*-

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Mensaje import *
import sys
import getopt


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# class ServidorContactos:
class GeneralDirectory:

    """
    Servidor que mantiene una lista de usuarios conectados en la red
    """

    def __init__(self):
        # lista de tuplas (alias, ip)
        # self.contactos = list()
        # lista de tuplas (alias, ip, puerto)
        self.users = list()

    def ping(self):
        """
        Sirve para saber si el servidor está activo
        """
        return True

    # def login(self, contacto):
    def connect_wrapper(self, username):
        """
        Agrega un contacto a la lista de contactos disponibles
        """
        if username in self.users:
            return None
        else:
            self.users.append(username)
            return self.users

    # def logout(self, contacto):
    def disconnect_wrapper(self, username):
        """
        Quita un contacto a la lista de contactos disponibles
        """
        self.users.remove(username)

    # def disponibles(self):
    def get_contacts_wrapper(self, username):
        """
        Regresa la lista de contactos conectados
        """
        return self.users


def main():
    # parseo de los argumentos de la línea de comandos
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        sys.exit(2)
    ip = args[0]  # obtenemos la ip del servidor de contactos con el primer argumento
    # iniciamos el servidor de contactos con la ip obtenida en el puerto 8001
    server = SimpleXMLRPCServer((ip, 8001), requestHandler=RequestHandler, allow_none=True)
    server.register_introspection_functions()
    server.register_instance(GeneralDirectory())
    try:
        print 'Usar Control-C para terminar el servidor'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Terminando'

if __name__ == "__main__":
    main()
