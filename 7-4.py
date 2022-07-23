from math import sqrt

m = 0
while m == 0:
    n = int(input("Ingrese un numero: "))
    if ( (int(sqrt(n))*int(sqrt(n)))==n):
        print("El numero", n, "es Cuadrado Perfecto")
    else:
        print("El numero", n, "NO es Cuadrado Perfecto")
