#!/usr/bin/env python
# -*- coding: utf-8 -*-
def sumarLista(lista):
    sum = 0
    for i in range(0, len(lista)):
        sum = sum + lista[i]

    return sum

def multip(x):
    mult = 1
    for i in range(0, len(x)):
        mult = mult * x[i]
        #x[i] = x[i] * 2
    return mult

A = [1, 2, 3, 5]
print "La Suma de los elementos es: " + str(sumarLista(A))
print "La Multiplicación de los elementos es: " + str(multip(A))
