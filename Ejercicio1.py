n1 = int(input("Ingresa el número de tablas: "))
n2 = int(input("Ingresa el límite de la tabla: "))
tabla = 1;
suma = 0;
while tabla != n1 + 1:
    cont = 1
    print("Tabla del ",tabla)
    while cont != n2 + 1:
        suma += tabla * cont
        print(tabla * cont)
        cont += 1
    print("Suma total:",suma)
    tabla += 1
