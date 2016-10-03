#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.etiquetas = ['']  # lista de nombres de etiqueta, empiezan en [1]
        self.attrs = ['']  # lista de diccionarios de atributos asociados 

    def startElement(self, name, attrs):

        attrs_rootlayout = ['width', 'height', 'background-color']
        attrs_region = ['id', 'top', 'bottom', 'left', 'right']
        attrs_img = ['src', 'region', 'begin', 'dur']
        attrs_audio = ['src', 'begin', 'dur']
        attrs_textstream = ['src', 'region']
        dicc_etiquetas = {'root-layout': attrs_rootlayout,
                          'region': attrs_region, 'img': attrs_img,
                          'audio': attrs_audio,
                          'textstream': attrs_textstream}

        if name == 'root-layout' or name == 'region' or name == 'img' or name == 'audio' or name == 'textstream':
            self.etiquetas.append(name)
            dicc = {}
            for attr in dicc_etiquetas[name]:
                dicc[attr] = attrs.get(attr, "")

            self.attrs.append(dicc)       


if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.xml'))
    print(cHandler.attrs)
