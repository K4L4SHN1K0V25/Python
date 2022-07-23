print("Convertir a Euros, presione 1")
print("Convertir a Libras, presione 2")
print("Convertir a Yen, presione 3")
print("Convertir a Yuan, presione 4")
print("Convertir a Dolar americano, presione 5")
print("Convertir a Dolar canadiense, presione 6")
opcion = int(input("A que moneda convertir? "))
pesos = float(input("Ingrese la cantidad de Pesos a convertir: "))

if opcion == 1:
    euro=pesos*24.45
    print("La cantidad de Pesos a Euros es: ")
    print(euro)

if opcion == 2:
    libras=pesos*28.47
    print("La cantidad de Pesos a Libras es: ")
    print(libras)

if opcion == 3:
    yen=pesos*0.19
    print("La cantidad de Pesos a Yenes es: ")
    print(yen)

if opcion == 4:
    yuan=pesos*0.19
    print("La cantidad de Pesos a Yuanes es: ")
    print(yuan)

if opcion == 5:
    dolar=pesos*20.53
    print("La cantidad de Pesos a Dolares Americanos es: ")
    print(dolar)

if opcion == 6:
    dolarc=pesos*16.43
    print("La cantidad de Pesos a Dolares Canadienses es: ")
    print(dolarc)
