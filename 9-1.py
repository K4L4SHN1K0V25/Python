n = int(input("Ingrese hasta que numero quiere llegar: "))
cont = 0

for i in range(1,n+1):
    m = i ** 3
    cont += m
print(cont, "Es la suma total")
