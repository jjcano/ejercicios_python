#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Determinar la cantidad de digitos de un numero (1- 100000)
num = 0
numero = ""

while num < 1 or num > 100000 or numero.isdigit() == True :
    try:
        num = int(raw_input("ingresa un número entre 1 a 100000 :\n>>"))

        if num < 1 or num > 100000 :
            print "numero incorrecto!!!!"

    except ValueError:
        print 'ooops!!!'
        print 'ingresa solo numeros!!!'

#pasar a cadena
cont=0
numero = str(num)

for i in numero:
    cont+=1

print "el numero consta de ", cont," digitos "
num = int(numero)