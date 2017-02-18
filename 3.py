def cadena(dias):

    totdias = 0

    for dia in dias:
        totdias += 1
    print("El numero de elementos de la lista es: " + str(totdias))

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
print cadena(dias)
#print("El numero de elementos de la lista segun la funcion len es", len(lista))