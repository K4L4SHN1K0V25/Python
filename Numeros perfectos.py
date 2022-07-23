def numper(num, nom):
    while num <= nom:
        suma = 0

        for i in range(1, num):
            if num % i == 0:
                suma += i

        if suma == num:
            print(num, "Es numero perfecto")
        else:
            print(num, "No es numero perfecto")

        num += 1

num=int(input("Inserte un numero: "))
nom=int(input("Inserte un numero: "))
numper(num, nom)


