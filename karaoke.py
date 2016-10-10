#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import json
from urllib.request import urlretrieve


class KaraokeLocal(SmallSMILHandler):

    def inicializador(self, fich, handler):
        parser = make_parser()
        parser.setContentHandler(handler)
        with fichero_leido as fichero:
            parser.parse(fichero)

    def __str__(self):
        self.str_lineas = ''
        for i in range(len(self.datos)):
            linea = self.datos[i][0]  # coge el nombre de etiqueta
            for atributo, valor in self.datos[i][1].items():
                if valor != "":
                    linea = linea + '\t' + atributo + '=' + '"' + valor + '"'

            self.str_lineas = self.str_lineas + linea + '\n'

        print(self.str_lineas)

    def to_json(self, json_name):
        self.name_fich = sys.argv[1]
        if json_name == '':
            self.name_json = self.name_fich.split('.')[0] + '.json'
        else:
            self.name_json = json_name

        fich_json = open(self.name_json, 'w')
        codigo_json = json.dumps(self.datos)
        fich_json.write(codigo_json)
        fich_json.close()

    def do_local(self):
        self.lista_remotos = []
        for i in range(len(self.datos)):
            for atributo, valor in self.datos[i][1].items():
                if valor[:7] == 'http://':
                    self.lista_remotos.append(valor)
                    self.datos[i][1][atributo] = valor.split('/')[-1]
        for remoto in self.lista_remotos:
            name_fich_local = remoto.split('/')[-1]
            urlretrieve(remoto, name_fich_local)

if __name__ == "__main__":
    try:
        fichero_leido = open(sys.argv[1])
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")

    kar_loc = KaraokeLocal()
    kar_loc.inicializador(fichero_leido, kar_loc)
    kar_loc.__str__()
    kar_loc.to_json('')  # como parametro se pasa el nombre del fichero json
    kar_loc.do_local()
    kar_loc.to_json('local.json')
    kar_loc.__str__()
