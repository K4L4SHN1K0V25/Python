n = 0

while n == 0:
    a = float(input("Ingrese el primer numemro: "))
    b = float(input("Ingrese el segundo numemro: "))

    if a == b:
        c = a * b
        print(c, "es el resultado de la multiplicacion")

    if a > b:
        d = a - b
        print(d, "es el resultado de la resta")

    if a < b:
        e = a + b
        print(e, "es el resultado de la suma")
