print("Oprima 1 para el area del circulo")
print("Oprima 2 para el area del cuadrado")
print("Oprima 3 para el area del triangulo")
opcion = int(input("Ingresa una opcion: "))

if opcion == 1:
    area = float(input("Ingrese el valor del area: "))
    r=(area*area)*3.1416
    print(r)

if opcion == 2:
    cua = float(input("Ingrese el valor de una cara: "))
    e=cua*cua
    print(e)

if opcion == 3:
    tri = float(input("Ingrese el valor de la altura: "))
    ang = float(input("Ingrese el valor de la base: "))
    t=(ang*tri)/2
    print(t)
