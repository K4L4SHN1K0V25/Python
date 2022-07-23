n = 0

while n == 0:
    print("1 - Enero")
    print("2 - Febrero")
    print("3 - Marzo")
    print("4 - Abril")
    print("5 - Mayo")
    print("6 - Junio")
    print("7 - Julio")
    print("8 - Agosto")
    print("9 - Septiembre")
    print("10 - Octubre")
    print("11 - noviembre")
    print("12 - Diciembre")

    a=int(input("Ingrese un numero que represente el dia: "))
    b=int(input("Ingrese un numero que represente el mes: "))

    if b == 3:
        if a >= 21:
            print("Tu signo es: Aries")

        if a <= 20:
            print("Tu signo es: Pcisis")

    if b == 4:
        if a >= 20:
            print("Tu signo es: Tauro")

        if a <= 19:
            print("Tu signo es: Aries")

    if b == 5:
        if a >= 21:
            print("Tu signo es: Geminis")

        if a <= 20:
            print("Tu signo es: Tauro")

    if b == 6:
        if a >= 21:
            print("Tu signo es: Cancer")

        if a <= 20:
            print("Tu signo es: Geminis")

    if b == 7:
        if a >= 23:
            print("Tu signo es: Leo")

        if a <= 22:
            print("Tu signo es: Cancer")

    if b == 8:
        if a >= 23:
            print("Tu signo es: Virgo")

        if a <= 22:
            print("Tu signo es: Leo")

    if b == 9:
        if a >= 23:
            print("Tu signo es: Libra")

        if a <= 22:
            print("Tu signo es: Virgo")

    if b == 10:
        if a >= 23:
            print("Tu signo es: Escorpio")

        if a <= 22:
            print("Tu signo es: Libra")

    if b == 11:
        if a >= 22:
            print("Tu signo es: Sagitario")

        if a <= 21:
            print("Tu signo es: Escorpio")

    if b == 12:
        if a >= 22:
            print("Tu signo es: Capricornio")

        if a <= 21:
            print("Tu signo es: Sagitario")

    if b == 1:
        if a >= 20:
            print("Tu signo es: Acuario")

        if a <= 19:
            print("Tu signo es: Capricornio")

    if b == 2:
        if a >= 19:
            print("Tu signo es: Psicis")

        if a <= 18:
            print("Tu signo es: Acuario")
