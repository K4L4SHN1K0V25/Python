n=1

while n > 0:

    print("Ingrese 0 para salir")
    n=int(input("Introduce un numero para la suma al cuadrado: "))

    for i in range(n):
        a = i**2
        b = (i+1)**2
        c = a + b
        if c != 1:
            if c%2 != 0:
                if c%3 != 3:
                    if c == 5 or c%5 != 0:
                        if c%7 != 0:
                            print(c)

    for z in range(n):
        g = (z**2)+(1**2)
        if g != 1:
            if g%2 != 0:
                if g%3 != 3:
                    if g%5 != 0:
                        if g%7 != 0:
                            print(g)
