n = 0

while n == 0:
    print("Determinar si es un rectangulo por medio de sus vertices")
    print(" ")
    print("Valores del Primer Vertice")
    x1 = int(input("Ingrese el valor X: "))
    y1 = int(input("Ingrese el valor Y: "))
    print(" ")
    print("Valores del Segundo Vertice")
    x2 = int(input("Ingrese el valor X: "))
    y2 = int(input("Ingrese el valor Y: "))
    print(" ")
    print("Valores del Tercer Vertice")
    x3 = int(input("Ingrese el valor X: "))
    y3 = int(input("Ingrese el valor Y: "))
    print(" ")
    print("Valores del Cuarto Vertice")
    x4 = int(input("Ingrese el valor X: "))
    y4 = int(input("Ingrese el valor Y: "))
    print(" ")

    if x1 == x2:
        if x3 == x4:
            if y1 == y3:
                if y2 == y4:
                    print("SI representan los vertices de un rectangulo")
                    print(" ")

                else:
                    print("NO representan los vertices de un rectangulo")
                    print(" ")
        else:
            print("NO representan los vertices de un rectangulo")
            print(" ")
