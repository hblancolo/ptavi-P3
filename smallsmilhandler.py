#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.etiquetas = []  # lista de nombres de etiqueta, empiezan en [1]
        self.attrs = []  # lista de diccionarios de atributos asociados

    def startElement(self, name, attrs):

        attrs_rootlayout = ['width', 'height', 'background-color']
        attrs_region = ['id', 'top', 'bottom', 'left', 'right']
        attrs_img = ['src', 'region', 'begin', 'dur']
        attrs_audio = ['src', 'begin', 'dur']
        attrs_textstream = ['src', 'region', 'fill']
        dicc_etiquetas = {'root-layout': attrs_rootlayout,
                          'region': attrs_region, 'img': attrs_img,
                          'audio': attrs_audio, 'textstream': attrs_textstream}

        if (name == 'root-layout' or name == 'region' or name == 'img'
           or name == 'audio' or name == 'textstream'):
            self.etiquetas.append(name)
            # diccionario de los atributos de la etiqueta en la que me
            # encuentro actualmente. Luego lo añado a la lista de diccionarios
            dicc = {}
            for attr in dicc_etiquetas[name]:
                if attrs.get(attr, "") != "":  # excluyo atributos vacios
                    dicc[attr] = attrs.get(attr, "")

            self.attrs.append(dicc)

    def get_tags(self):

        for i in range(len(self.etiquetas)):
            print(self.etiquetas[i] + ' ' + str(self.attrs[i]))
            print()

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    cHandler.get_tags()
