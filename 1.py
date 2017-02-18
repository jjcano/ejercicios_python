a=int(input("Ingrese Numero 1:"))
b=int(input("Ingrese Numero 2:"))

def max(pri,seg):
    if pri > seg:
        print ("El numero mayor es el primer valor: "+ str(a))
    else:
        print ("El numero mayor es el segundo valor: "+ str(b))

print max(a,b)