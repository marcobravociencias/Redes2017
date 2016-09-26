#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time


class Message():

    """Clase que define el formato para un mensaje"""

    def __init__(self, author_username, author_ip, content):
        self.date = time.strftime("%H:%M:%S")
        self.author_username = author_username
        self.author_ip = author_ip
        self.content = content
        self.read = False

    def setRead(self, read):
        self.read = read

    def getRead(self):
        return self.read

    def __str__(self):
        return '[date:'+ self.date +']' + ' [author:'+ self.author_username +']' + ' [addr:'+ self.author_ip +']' + ' [content:'+ self.content +']' + ' [read:'+ str(self.read) +']'
