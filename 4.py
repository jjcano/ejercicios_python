#!/usr/bin/env python
# -*- coding: utf-8 -*-
def esvocal(vocal):

    vocales = ['\xc3\xa1', '\xc3\xa9', '\xc3\xad', '\xc3\xb3', '\xc3\xba','\xc3\xbc',
               'a', 'e', 'i', 'o', 'u',
               '\xc3\x81', '\xc3\x89', '\xc3\x8d', '\xc3\x93', '\xc3\x9a','\xc3\x9c',
               'A', 'E', 'I', 'O', 'U']

    if vocal in vocales:
        print "Es una vocal"
    else:
        print "No es una vocal"

vocal = raw_input("Ingrese una opción letra: ")
print esvocal(vocal)
