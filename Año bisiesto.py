año = int(input("Escriba un año entre 1900 y 2018: "))
nb = f"{año} no es un año bisiesto"
b = f"{año} es un año bisiesto"

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print(b)
        else:
            print(nb)
    else:
        print(b)

else:
    print(nb)
