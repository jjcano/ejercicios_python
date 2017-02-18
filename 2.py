a=int(input("Ingrese Numero 1:"))
b=int(input("Ingrese Numero 2:"))
c=int(input("Ingrese Numero 3:"))

def max_de_tres(A,B,C):

    if (A > B and A > C):
        print("El numero mayor es el primer valor " + str(A))
    else:
        if (B > A and B > C):
            print("El numero mayor es el segundo valor " + str(B))
        else:
            print("El numero mayor es el tercer valor " + str(C))

print max_de_tres(a,b,c)