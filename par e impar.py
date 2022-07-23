resultado = 0

for i in range(20):
    n = int(input("Ingrese un numero: "))
    if n % 2 == 0:
        resultado += n
    else:
        resultado *= n

print("El resultado total es: ", resultado)
