num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))

if num1 == num2 and num1 == num3:
    print("Estos numero son iguales")
    print(num1, num2, num3)

if num1 == num2 and num1 != num3:
    print("Estos numero son iguales")
    print(num1, num2)
    print("Este numero es distinto")
    print(num3)

if num1 == num3 and num1 != num2:
    print("Estos numero son iguales")
    print(num1, num3)
    print("Este numero es distinto")
    print(num2)

if num1 != num2 and num1 != num3:
    print("Ningun numero es igual")
    print(num1)
    print(num2)
    print(num3)
