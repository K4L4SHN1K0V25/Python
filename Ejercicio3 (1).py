filas,contador = 0,0
while filas !=5:
    filas += 1
    while contador != filas:
        print("+",end="")
        contador +=1
    contador = 0
    print("")
print("")
filas,contador = 5,0
while filas !=0:
    while contador != filas:
        print("+",end="")
        contador +=1
    contador = 0
    filas -= 1
    print("")
