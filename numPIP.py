n = 0

def numeros(n):
    if n % 2 == 0:
        print("2")
        if n == 2:
            print("1")

        if n % 2 != 0:
            if n % 3 != 0:
                if n % 5 != 0:
                    if n % 7 != 0:
                        print(n, "1")
                    

    if n % 2 != 0:
        print("0")
        if n == 3:
            print("1")

        if n == 5:
            print("1")

        if n == 7:
            print("1")


        if n % 2 != 0:
            if n % 3 != 0:
                if n % 5 != 0:
                    if n % 7 != 0:
                        print(n, "1")

while n >= 0:
    n=int(input("Ingrese un valor: "))
    numeros(n)
                    
