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
        for i in range(len(self.etiquetas)):
            linea = self.etiquetas[i]
            for atributo, valor in self.attrs[i].items():
                linea = linea + '\t' + atributo + '=' + '"' + valor + '"'

            self.str_lineas = self.str_lineas + linea + '\n'

        print(self.str_lineas)

    def unir_etiqs_attrs(self):  # junto attrs y etiquetas en dicc_datos
        self.dicc_datos = {}
        for i in range(len(self.etiquetas)):
            self.dicc_datos[self.etiquetas[i]] = self.attrs[i]

    def to_json(self, json_name):
        self.name_fich = sys.argv[1]
        if json_name == '':
            self.name_json = self.name_fich.split('.')[0] + '.json'
        else:
            self.name_json = json_name

        fich_json = open(self.name_json, 'w')
        codigo_json = json.dumps(self.dicc_datos)
        fich_json.write(codigo_json)

    def do_local(self):
        self.lista_remotos = []
        for dicc in self.attrs:
            for atributo in dicc:
                if dicc[atributo][:7] == 'http://':
# esto guarda direccion recurso, y modifica valor de atributo en attrs por
# el nombre del recurso en si (ej.: smile.jpg)
                    self.lista_remotos.append(dicc[atributo])
                    dicc[atributo] = dicc[atributo].split('/')[-1]
        for remoto in self.lista_remotos:
            name_fich_local = remoto.split('/')[-1]
            urlretrieve(remoto, "/home/hector/PTAVI/P3/" + name_fich_local)

if __name__ == "__main__":
    try:
        fichero_leido = open(sys.argv[1])
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")

    kar_loc = KaraokeLocal()
    kar_loc.inicializador(fichero_leido, kar_loc)
    kar_loc.__str__()
    kar_loc.unir_etiqs_attrs()
    kar_loc.to_json('')  # como parametro se pasa el nombre del fichero json
    kar_loc.do_local()
    kar_loc.to_json('local.json')
