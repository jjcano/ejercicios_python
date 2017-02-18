#! /usr/bin/env python
# -*- coding: utf-8 -*-
def tabla(numero,rango):

    n= 1
    for n in range(rango + 1):
        if(n !=0): # se valida para no multiplicar desde cero (0)
            resultado = n * numero
            print numero," * ", n, " = ", resultado

a = int(input("Ingrese el número de la tabla que desea multiplicar:"))
b = int(input("Ingrese hasta qué número lo multiplicará :"))

tabla(a,b)