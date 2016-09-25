#! /usr/bin/env python
# -*- coding: utf-8 -*-


class DirectoryChannel():

    """
    Comunicación entre un cliente y el direcrio de ubicación (internamente
    BidirectionalChannel donde el ApiClient se dirige hacia el servidor de contactos).
    """

    def __init__(self, arg):
        self.arg = arg
