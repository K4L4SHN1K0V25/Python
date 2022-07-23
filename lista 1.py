lista = [2, 4, 6, 8, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 6, 9, 12]
repetidos = []

print(lista)
print(" ")
print("La lista tiene", len(lista), "elementos")
print("El elemento mayor de la lista es", max(lista))
print("El elemento menor de la lista es", min(lista))
print(" ")
for i in range(len(lista)):
    for j in range(len(lista)):
        if i != j:
            if lista[i] == lista[j] and lista [i] not in repetidos:
                repetidos.append(lista[i])
print("Estos son los elementos repetidos", repetidos)
conjunto = set(lista)
lis = list(conjunto)
print("Estos son los elementos sin los repetidos", lis)
