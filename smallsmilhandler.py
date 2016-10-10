#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.datos = []  # lista de listas. cada sublista tiene dos elementos:
# el primero es el nombre de etiqueta, el segundo el dicc de atributos
        attrs_rootlayout = ['width', 'height', 'background-color']
        attrs_region = ['id', 'top', 'bottom', 'left', 'right']
        attrs_img = ['src', 'region', 'begin', 'dur']
        attrs_audio = ['src', 'begin', 'dur']
        attrs_textstream = ['src', 'region', 'fill']
        self.dicc_etiquetas = {'root-layout': attrs_rootlayout,
                               'region': attrs_region, 'img': attrs_img,
                               'audio': attrs_audio,
                               'textstream': attrs_textstream}

    def startElement(self, name, attrs):

        if name in self.dicc_etiquetas:
            dicc = {}
            for attr in self.dicc_etiquetas[name]:
                dicc[attr] = attrs.get(attr, "")

            self.datos.append([name, dicc])

    def get_tags(self):

        return self.datos

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
