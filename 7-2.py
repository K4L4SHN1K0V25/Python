n = 0

while n == 0:
    print("Bienvenido")
    print(" ")
    print("1) Paleta - $3")
    print("2) Gomitas - $5")
    print("3) Caramelo - $2")
    print("4) Chocolate - $4")
    print(" ")

    a = int(input("Ingrese el numero del dulce: "))

    if a == 1:
        b = int(input("Cuantas paletas desea? "))
        c = b * 3
        d = float(input("Ingrese su dinero: $"))

        if d < c:
            print("Falta dinero")
            print("$", d, " Dinero devuelto")

        elif d > c:
            e = d - c
            print("Gracias!!!")
            print("$", e, " de cambio devuelto")

    if a == 2:
        b = int(input("Cuantas gomitas desea? "))
        c = b * 5
        d = float(input("Ingrese su dinero: $"))

        if d < c:
            print("Falta dinero")
            print("$", d, " Dinero devuelto")

        elif d > c:
            e = d - c
            print("Gracias!!!")
            print("$", e, " de cambio devuelto")

    if a == 3:
        b = int(input("Cuantos caramelos desea? "))
        c = b * 2
        d = float(input("Ingrese su dinero: $"))

        if d < c:
            print("Falta dinero")
            print("$", d, " Dinero devuelto")

        elif d > c:
            e = d - c
            print("Gracias!!!")
            print("$", e, " de cambio devuelto")

    if a == 4:
        b = int(input("Cuantas paletas desea? "))
        c = b * 4
        d = float(input("Ingrese su dinero: $"))

        if d < c:
            print("Falta dinero")
            print("$", d, " Dinero devuelto")

        elif d > c:
            e = d - c
            print("Gracias!!!")
            print("$", e, " de cambio devuelto")
