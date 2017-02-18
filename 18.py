#! /usr/bin/env python
# -*- coding: utf-8 -*-
def c_mayusculas (cadena):
    cont = 0
    for i in cadena:
        if i != i.lower(): #Recordar que lower() convierte una cadena en minúsculas
            cont += 1
    print "La cadena tiene", cont, "mayuscula/s"

cadena = 'esto es una prueba de letras con MaYuSCuLaS'
c_mayusculas(cadena)