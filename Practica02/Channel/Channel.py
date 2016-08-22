#! /usr/bin/env python
# -*- coding: utf-8 -*-
from ApiServer import MyApiServer
from ApiClient import MyApiClient

"""**************************************************
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
**************************************************"""
class Channel:
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
    def __init__(self, contact_ip = None, contact_port = None):
        self.contact_ip =  contact_ip
        self.contact_port = contact_port
        self.MyApiClient = MyApiClient("Marco", "127.0.0.1" ,"8000" )
        self.MyApiServerApiServer = xmlrpclib.ServerProxy("http://"+self.contact_ip+":"+self.contact_port,allow_none=True)
        self.hiloClient = threading.Thread(target=self.escucha)
        self.hiloClient.start()

    def escucha():
       while True:
           time.sleep(1)
           server = xmlrpclib.ServerProxy("http://"+self.MyApiClient.ip1+":"+self.MyApiClient.port,allow_none=True) 
           msj = server.vaciaBuffer()
           if(len(msj)!=0):
               #self.chat.setTexto(msj)
               print 'MI mensaje es :'+msj

    """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""
    def send_text(self, text):
        print 'Mando mensaje'
        if(self.ApiServer.ping()):
            print 'Entramos'
            msj = self.usr+' : '+ text# text lo tomamos de la interfaz
            self.ApiServer.sendMessage_wrapper(msj)
            #self.chat.setTexto(msj)
            print 'se hizo ping con exito'