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
from Chat import *
from ThreadEx import *
import pyaudio
import numpy
from LlamaCurso import *
import Constants
import cv2
import multiprocessing
from numpy.lib import format
from cStringIO import StringIO


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
        # Conexión de la interfaz con los eventos para iniciar y
        # terminar la llamada
        self.chat.boton_llama.clicked.connect(self.iniciaLlamada)
        self.chat.boton_salir.clicked.connect(self.terminarLlamada)

    def escucha(self):
        """ **************************************************
        Método que inicia un hilo para tener el servidor siempre activo y si
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
        Método que envia un mensaje al servidor destino.
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
        Método que inicia los hilos y llama a los métodos para la llamada.
        ************************************************** """
        self.stack = multiprocessing.Queue(Constants.QUEUE_MAX_SIZE)
        self.hiloManda = ThreadEx(targetp=self.enviaAudio, namep='hiloManda')
        # self.hiloManda.start()
        self.hiloEscucha = ThreadEx(targetp=self.reprodAudio, namep='hiloEscucha')
        # self.hiloEscucha.start()
        # video
        self.stackVideo = multiprocessing.Queue(Constants.QUEUE_MAX_SIZE)
        self.hiloCapturaVideo = ThreadEx(targetp=self.capturaVideo, namep='hiloCapturaVideo')
        self.hiloCapturaVideo.start()
        self.hiloMandaVideo = ThreadEx(targetp=self.enviaVideo, namep='hiloMandaVideo')
        self.hiloMandaVideo.start()
        self.llama = LlamadaCurso(None)
        self.llama.show()

    def reprodAudio(self):
        """ **************************************************
        Método que reproduce el audio que va llegando del otro usuario.
        ************************************************** """
        CHUNK = Constants.CHUNK
        WIDTH = Constants.WIDTH
        CHANNELS = Constants.CHANNELS
        RATE = Constants.RATE
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(WIDTH)
        stream = p.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)
        while True:
            if self.hiloManda.isStopEx():
                return 1
            n = Constants.CHUNKS_BUFFER
            frame = []
            for i in range(0, n):
                frame.append(stream.read(CHUNK))
            audioBinario = numpy.fromstring(''.join(frame), dtype=numpy.uint8)
            if self.stack.full():
                self.stack.get_nowait()
            self.stack.put(audioBinario)

    def enviaAudio(self):
        """ **************************************************
        Método que envía el audio al servidor destino.
        ************************************************** """
        while True:
            if self.hiloManda.isStopEx():
                return 1
            d = self.stack.get()
            data = xmlrpclib.Binary(d)
            self.server.recibeAudio(data)

    def toString(self, data):
        f = StringIO()
        format.write_array(f, data)
        return f.getvalue()
    
    def capturaVideo(self):
        # cap = cv2.VideoCapture('TameImpalaYesImChanging_720.avi')
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            n = 30
            frame1 = []
            for i in range (0,n):
                ret, frame = cap.read()
                if(ret):
                    cv2.imshow('Cliente', frame)
                    data = xmlrpclib.Binary(self.toString(frame))
                    self.stackVideo.put(data)

    def enviaVideo(self):
        while True:
            if not self.stackVideo.empty():
                d1 = self.stackVideo.get()
                # datita2 = xmlrpclib.Binary(d1)
                self.server.recibe_video(dl)
    
    def transmite_llamada(self):
        while True:
            if not self.stackVideo.empty():
                d1 = self.stackVideo.get()
                # datita2 = xmlrpclib.Binary(d1)
                self.server.recibe_video(dl)

    def terminarLlamada(self):
        """ **************************************************
        Método que termina la llamada parando los hilos ejecución.
        ************************************************** """
        # self.hiloEscucha.stopEx()
        # self.hiloManda.stopEx()
        self.hiloMandaVideo()
        self.llama.hide()
