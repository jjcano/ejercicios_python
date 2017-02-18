#! /usr/bin/env python
# -*- coding: utf-8 -*-

numero = raw_input("Ingrese Numero: ")
resultado = 0

for i in numero:
    resultado = resultado + int(i)

if resultado % 2 == 0:
    print "La suma de los digitos de %d es par: %d" % (int(numero), resultado)
else:
    print "La suma de los digitos de %d es impar: %d" % (int(numero), resultado)