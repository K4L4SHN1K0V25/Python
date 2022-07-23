lista1 = []
lista2 = []
n = 0
x = 0

x = int(input("Cuantos valores desea agregar a cada lista? "))

for i in range(x):
    d1 = int(input("Ingrese un valor a la lista 1: "))
    lista1.append(d1)
    d2 = int(input("Ingrese un valor a la lista 2: "))
    lista2.append(d2)

while n < 5:
    print("1.- Mostrar el elemento mayor de cada lista")
    print("2.- Mostrar el elemento menor de cada lista")
    print("3.- Mostrar la cantidad de elementos de cada lista")
    print("4.- Juntar los alementos de ambas listas")
    print("5.- Salir")

    op = int(input("Que opcion desea realizar? "))

    if op == 1:
        print("El elemento mayor de la lista 1 es:")
        print(max(lista1))
        print("El elemento mayor de la lista 2 es:")
        print(max(lista2))
        print("")

    if op == 2:
        print("El elemento mayor de la lista 1 es:")
        print(min(lista1))
        print("El elemento mayor de la lista 2 es:")
        print(min(lista2))
        print("")

    if op == 3:
        print("El numero de elementos de la lista 1 es:")
        print(len(lista1))
        print("El numero de elementos de la lista 2 es:")
        print(len(lista2))
        print("")

    if op == 4:
        lista3 = [lista1 + lista2]
        print(lista3)

    if op == 5:
        n += 5
