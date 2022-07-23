n = 0

while n == 0:
    m = int(input("Ingrese una calificacion: "))

    if m >= 0 and m <= 59:
        print("Insuficiente")

    if m >= 60 and m <= 69:
        print("Suficiente")

    if m >= 70 and m <=79:
        print("Regular")

    elif m >= 80 and m <= 89:
        print("Bien")

    elif m >= 90 and m <= 100:
        print("Excelente")
