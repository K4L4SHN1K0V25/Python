lista =[]
can = 10
m = 0
n = 0
l = 1

while n == 0:
    while can <= 10 and can >= 1:
        a = int(input("Numero" + str(l) + ": "))
        lista.append(a)
        l += 1
        can -= 1

    m = max(lista)

    print("El numero mayor es: ", m)
    m = int(input("Digite cero si desea continuar: "))
    
     
