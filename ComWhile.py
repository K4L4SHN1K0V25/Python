n = 0

while n < 7:
    print("1 - Convertir a Euros")
    print("2 - Convertir a Libras")
    print("3 - Convertir a Yen")
    print("4 - Convertir a Yuan")
    print("5 - Convertir a Dolar americano")
    print("6 - Convertir a Dolar canadiense")
    print("7 - Salir")
    n = int(input("Escoga una opcion: "))

    if n == 1:
        m = 0
        while m == 0:
            pesos = float(input("Ingrese la cantidad de Pesos a convertir: "))
            euro=pesos*24.45
            print("La cantidad de Pesos a Euros es: ")
            print(euro)
            m = int(input("Digite cero si desea continuar: "))

    if n == 2:
        m = 0
        while m == 0:
            pesos = float(input("Ingrese la cantidad de Pesos a convertir: "))
            libras=pesos*28.47
            print("La cantidad de Pesos a Libras es: ")
            print(libras)
            m = int(input("Digite cero si desea continuar: "))

    if n == 3:
        m = 0
        while m == 0:
            pesos = float(input("Ingrese la cantidad de Pesos a convertir: "))
            yen=pesos*0.19
            print("La cantidad de Pesos a Yenes es: ")
            print(yen)
            m = int(input("Digite cero si desea continuar: "))

    if n == 4:
        m = 0
        while m == 0:
            pesos = float(input("Ingrese la cantidad de Pesos a convertir: "))
            yuan=pesos*0.19
            print("La cantidad de Pesos a Yuanes es: ")
            print(yuan)
            m = int(input("Digite cero si desea continuar: "))

    if n == 5:
        m = 0
        while m == 0:
            pesos = float(input("Ingrese la cantidad de Pesos a convertir: "))
            dolar=pesos*20.53
            print("La cantidad de Pesos a Dolares Americanos es: ")
            print(dolar)
            m = int(input("Digite cero si desea continuar: "))
        
    if n == 6:
        m = 0
        while m == 0:
            pesos = float(input("Ingrese la cantidad de Pesos a convertir: "))
            dolarc=pesos*16.43
            print("La cantidad de Pesos a Dolares Canadienses es: ")
            print(dolarc)
            m = int(input("Digite cero si desea continuar: "))
        
