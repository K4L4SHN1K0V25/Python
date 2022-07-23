n = 0

while n == 0:
    m = int(input("Ingrese su edad: "))

    if m >= 5 and  m <= 13:
        print("Etapa en la que se encuentra: Niñez")

    elif m >= 14 and m <= 17:
        print("Etapa en la que se encuentra: Adolecencia")

    elif m >= 18 and m <= 35:
        print("Etapa en la que se encuentra: Juventud")

    elif m >= 36 and m <= 64:
        print("Etapa en la que se encuentra: Adulto")

    elif m >= 65:
        print("Etapa en la que se encuentra: Adulto Mayor")

    else:
        print("Bebe")
