#!/usr/bin/env python
#-*- coding: utf-8 -*-

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Mensaje import *
import sys
import getopt
import Constants
import xmlrpclib
import threading
import errno
from socket import error as socket_error
from AuxiliarFunctions import Autentica


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class ServidorContactos:

    """
    Servidor que mantiene una lista de usuarios conectados en la red
    """

    def __init__(self):
        # lista de tuplas (alias, ip)
        self.contactos = list()
        # hilo que hace ping a los que hayan hecho login y no han hecho logout
        # para tener actualizada la lista de contactos conectados
        self.hilo_pings = threading.Thread(target=self.pinguea, name='hilo_pings')
        self.hilo_pings.start()

    def pinguea(self):
        while(True):
            # espera 5 segundos
            time.sleep(5)
            for c in self.contactos:
                ip = c[1]
                print ip
                try:
                    s = xmlrpclib.ServerProxy('http://' + ip + ':' + str(Constants.CONTACT_PORT))
                    s.ping()
                except socket_error as err:
                    self.logout(c)
                    print err
                    print "el servidor " + ip + " no responde, se ha desconectado"

    def ping(self):
        """
        Sirve para saber si el servidor está activo
        """
        return True

    def usuario_valido(self, contacto):
        usr = contacto[0]
        pas = contacto[-1]
        a = Autentica(usr, pas)
        return a.login()

    def login(self, contacto):
        """
        Agrega un contacto a la lista de contactos disponibles
        """
        if contacto in self.contactos:
            return Constants.LOGUEADO
        else:
            if self.usuario_valido(contacto):
                print 'usuario ' + str(contacto) + ' valido'
                self.contactos.append(contacto)
                return self.contactos
            else:
                print 'usuario ' + str(contacto) + ' invalido'
                return Constants.USUARIO_INVALIDO

    def logout(self, contacto):
        """
        Quita un contacto de la lista de contactos disponibles
        """
        if contacto in self.contactos:
            self.contactos.remove(contacto)
        else:
            return None

    def disponibles(self):
        """
        Regresa la lista de contactos conectados
        """
        return self.contactos

    def agrega_usuario(self, usuario, password):
        regis = Autentica(usuario, password)
        if regis.registra():
            return True
        else:
            return False


def main():
    # parseo de los argumentos de la línea de comandos
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        sys.exit(2)
    ip = args[0]  # obtenemos la ip del servidor de contactos con el primer argumento
    # iniciamos el servidor de contactos con la ip obtenida en el puerto DIRECTORY_PORT
    server = SimpleXMLRPCServer((ip, Constants.DIRECTORY_PORT), requestHandler=RequestHandler, allow_none=True)
    server.register_introspection_functions()
    server.register_instance(ServidorContactos())
    try:
        print 'Usar Control-C para terminar el servidor'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Terminando'

if __name__ == "__main__":
    main()
