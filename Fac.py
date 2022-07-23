n = int(input("Ingrese un numero entero: "))
fac = 1

for i in range(n):
    print(fac, " * ", n)
    fac *= n
    n -= 1

print("El resultado final es: ", fac)
        
