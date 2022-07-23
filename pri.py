m = 0

while m == 0:

    n = int(input("Inserte un numero: "))

    if n > 0:
        if n == 2:
            print(n, "es numero primo")
            m = int(input("Si desea continuar digite cero: "))
        
        if n == 3:
            print(n, "es numero primo")
            m = int(input("Si desea continuar digite cero: "))

        if n == 5:
            print(n, "es numero primo")
            m = int(input("Si desea continuar digite cero: "))

        if n == 7:
            print(n, "es numero primo")
            m = int(input("Si desea continuar digite cero: "))


        if n % 2 != 0:
            if n % 3 != 0:
                if n % 5 != 0:
                    if n % 7 != 0:
                        print(n, "es numero primo")
                    else:
                        print(n, "no es numero primo")
                else:
                    print(n, "no es numero primo")
            else:
                print(n, "no es numero primo")

        else:
            print(n, "no es numero primo")
