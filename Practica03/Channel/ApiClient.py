#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import time
sys.path.insert(0, 'GUI') # TODO check
from Chat import *
from ThreadEx import *
import pyaudio
import numpy
from LlamaCurso import *
sys.path.insert(0, 'Constants')
import Constants

class MyApiClient():

    """ **************************************************
    Clase cliente del chat.
    ************************************************** """

    def __init__(self, usr, ip1, ip2):
        self.usr = usr
        self.ip1 = ip1
        self.ip2 = ip2
        self.server = xmlrpclib.ServerProxy(
            "http://"+self.ip2+":"+Constants.PORT, allow_none=True)
        self.tem = threading.Event()
        self.chat = Chat(self.tem)
        self.chat.show()
        self.chat.boton_send.clicked.connect(self.enviar)
        self.hiloCliente = threading.Thread(target=self.escucha)
        self.hiloCliente.start()
        # Conexcion de la interfaz con los eventos para iniciar y
        # terminar la llamada
        self.chat.boton_llama.clicked.connect(self.iniciaLlamada)
        self.chat.boton_salir.clicked.connect(self.terminarLlamada)

    def escucha(self):
        """ **************************************************
        Metodo que inicia un hilo para tener el servidor siempre activo y si
        hay un mensaje en el buffer lo pasa a la interfaz.
        ************************************************** """
        while True:
            time.sleep(Constants.SLEEP)
            serverCli = xmlrpclib.ServerProxy(
                "http://"+self.ip1+":"+Constants.PORT, allow_none=True)
            msj = serverCli.vaciaBuffer()
            if(len(msj) != 0):
                self.chat.setTexto(msj)
                print 'MI mensaje es :'+msj

    def enviar(self):
        """ **************************************************
        Metodo que envia un mensaje al servidor destino.
        ************************************************** """
        print 'Mando mensaje'
        if(self.server.ping()):
            print 'Entramos'
            msj = self.usr+' : '+str(self.chat.text_send.toPlainText())+'\n'
            self.server.sendMessage_wrapper(msj)
            self.chat.setTexto(msj)
            print 'se hizo ping con exito'

    def iniciaLlamada(self):
        """ **************************************************
        Metodo que inicia los hilos y llama a los metodos para la llamada.
        ************************************************** """
        import multiprocessing
        self.stack = multiprocessing.Queue(10000)
        self.hiloManda = ThreadEx(targetp=self.enviaAudio, namep='hiloManda')
        self.hiloManda.start()
        self.hiloEscucha = ThreadEx(
            targetp=self.reprodAudio, namep='hiloEscucha')
        self.hiloEscucha.start()
        self.llama = LlamadaCurso(self.hiloManda)
        self.llama.show()

    def reprodAudio(self):
        """ **************************************************
        Metodo que reproduce el audio que va llegando del otro usuario.
        ************************************************** """
        CHUNK = 1024
        WIDTH = 2
        CHANNELS = 2
        RATE = 44100
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(WIDTH)
        stream = p.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)
        while True:
            if self.hiloManda.isStopEx():
                return 1
            n = 50
            frame = []
            for i in range(0, n):
                frame.append(stream.read(CHUNK))
            audioBinario = numpy.fromstring(''.join(frame), dtype=numpy.uint8)
            if self.stack.full():
                self.stack.get_nowait()
            self.stack.put(audioBinario)

    def enviaAudio(self):
        """ **************************************************
        Metodo que envia el audio al servidor destino.
        ************************************************** """
        while True:
            if self.hiloManda.isStopEx():
                return 1
            d = self.stack.get()
            data = xmlrpclib.Binary(d)
            self.server.recibeAudio(data)

    def terminarLlamada(self):
        """ **************************************************
        Metodo que termina la llamada parando los hilos ejecucion.
        ************************************************** """
        self.hiloEscucha.stopEx()
        self.hiloManda.stopEx()
        self.llama.hide()
