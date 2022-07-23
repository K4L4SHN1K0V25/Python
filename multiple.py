num1 = int(input("Escribe un número entero: "))
num2 = int(input("Escribe otro número entero: "))

if num1 > num2:
    if num1 % num2 == 0:
        print(f"{num1} es un múltiplo de {num2}")
    else:
        print(f"{num1} no es un múltiplo de {num2}")

if num2 >= num1:
    if num2 % num1 == 0:
        print(f"{num2} es un múltiplo de {num1}")

    else:
        print(f"{num2} no es un múltiplo de {num1}")
        
