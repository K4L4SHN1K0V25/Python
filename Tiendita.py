productos=[]
opc = 0

while opc < 5:
    print("1.-Agregar")
    print("2.-Eliminar")
    print("3.-Ordenar")
    print("4.-Mostrar")
    print("5.-Salir")
    opc= int(input("Elige una opcion: "))
    if opc == 1:
        x=input("¿Cual es el nombre del producto? ")
        productos.append(x)

    if opc == 2:
        x=input("¿Que elemento deseas eliminar? ")
        if x in productos:
            productos.remove(x)

    if opc == 3:
        productos.sort()

    if opc == 4:
        print(productos)

    if opc >= 5:
        print("Usted ha salido de la lista")
