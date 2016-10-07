#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SSHv2(SmallSMILHandler):

    def get_tags_v2(self):
        for i in range(len(self.etiquetas)):
            linea = self.etiquetas[i]
            for atributo, valor in self.attrs[i].items():
                linea = linea + '\t' + atributo + '=' + '"' + valor + '"'

            print(linea)

try:
    fichero_leido = open(sys.argv[1])
except:
    sys.exit("Usage: python3 karaoke.py file.smil")

with fichero_leido as fichero:

    parser = make_parser()
    cHandler = SSHv2()
    parser.setContentHandler(cHandler)
    parser.parse(fichero)
    cHandler.get_tags_v2()
