#! /usr/bin/env python
# -*- coding: utf-8 -*-

def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

lista1 = ['1','2','3','4']
lista2 = ['8','5','6','7']

print superposicion(lista1, lista2)