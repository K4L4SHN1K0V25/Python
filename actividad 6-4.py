n = 0

while n == 0:
    m = int(input("Ingrese un numero del mes de mayo del 2021: "))

    if m > 31:
        print("El mes llega a 31 dias")
        
    if m <= 7:
        if m == 1:
            print("S")

        if m == 2:
            print("D")

        if m == 3:
            print("L")

        if m == 4:
            print("M")

        if m == 5:
            print("I")

        if m == 6:
            print("J")

        if m == 7:
            print("V")

    if m > 7:
        if m%7==0:
            print("V")

        if m%7==1:
            print("S")

        if m%7==2:
            print("D")

        if m%7==3:
            print("L")

        if m%7==4:
            print("M")

        if m%7==5:
            print("I")

        if m%7==6:
            print("J")
