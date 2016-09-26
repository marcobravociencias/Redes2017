#!/usr/bin/env python
#-*- coding: utf-8 -*-

import threading

class ThreadParable(threading.Thread):
    """
    Clase Thread con un método detener(). El hilo puede detenerse externamente
    y consultar el "estado" con el método detenido()
    """
    def __init__(self,targetp,namep):
        super(ThreadParable,self).__init__(target=targetp,name=namep)
        # usamos una bandera _stop
        self._stop = threading.Event()

    def detener(self):
        self._stop.set()

    def detenido(self):
        return self._stop.isSet()