#! /usr/bin/env python
# -*- coding: utf-8 -*-

numero = int(input("Ingrese Numero: "))

for i in range(numero + 1):
    if i % 2 == 0 and i != 0: # imprimir números hasta el valor ingresado sin tomar en cuenta el cero (0)
        print i
