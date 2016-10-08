#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import json


class SSHv2(SmallSMILHandler):

    def get_tags_v2(self):
        for i in range(len(self.etiquetas)):
            linea = self.etiquetas[i]
            for atributo, valor in self.attrs[i].items():
                linea = linea + '\t' + atributo + '=' + '"' + valor + '"'

            print(linea)

    def unir_etiqs_attrs(self):  # junto attrs y etiquetas en dicc_datos
        self.dicc_datos = {}
        for i in range(len(self.etiquetas)):
            self.dicc_datos[self.etiquetas[i]] = self.attrs[i]

    def smil_to_json(self):
        name_fich = sys.argv[1].split('.')[0]
        self.fich_json = open(name_fich + '.json', 'w')
        codigo_json = json.dumps(self.dicc_datos)
        self.fich_json.write(codigo_json)

if __name__ == "__main__":
    try:
        fichero_leido = open(sys.argv[1])
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    cHandler = SSHv2()
    parser.setContentHandler(cHandler)
    with fichero_leido as fichero:
        parser.parse(fichero)

    cHandler.get_tags_v2()
    cHandler.unir_etiqs_attrs()
    cHandler.smil_to_json()
    cHandler.fich_json.close()
