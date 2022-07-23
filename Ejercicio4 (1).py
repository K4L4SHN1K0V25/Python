import random
print("Ejercicio 4.")
x = random.randrange(3,20)
c1,c2 = 0,0
print("Número aleatorio: ",x)
while c1 != x:
    while c2 != x:
        print("*",end="")
        c2 += 1
    print("")
    c2 = 0
    c1 +=1

