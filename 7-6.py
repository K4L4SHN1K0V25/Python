print("Determinar si un rectangulo es mas chico que otro rectangulo")
print(" ")
print("Valores del Primer Rectangulo")
print("Valores del Segundo Vertice")
x1 = int(input("Ingrese el valor X: "))
y1 = int(input("Ingrese el valor Y: "))
print(" ")
print("Valores del Segundo Vertice")
x2 = int(input("Ingrese el valor X: "))
y2 = int(input("Ingrese el valor Y: "))
print(" ")
print("Valores del Tercer Vertice")
x3 = int(input("Ingrese el valor X: "))
y3 = int(input("Ingrese el valor Y: "))
print(" ")
print("Valores del Cuarto Vertice")
x4 = int(input("Ingrese el valor X: "))
y4 = int(input("Ingrese el valor Y: "))
print(" ")

print("Valores del Segundo Rectangulo")
x5 = int(input("Ingrese el valor X: "))
y5 = int(input("Ingrese el valor Y: "))
print(" ")
print("Valores del Segundo Vertice")
x6 = int(input("Ingrese el valor X: "))
y6 = int(input("Ingrese el valor Y: "))
print(" ")
print("Valores del Tercer Vertice")
x7 = int(input("Ingrese el valor X: "))
y7 = int(input("Ingrese el valor Y: "))
print(" ")
print("Valores del Cuarto Vertice")
x8 = int(input("Ingrese el valor X: "))
y8 = int(input("Ingrese el valor Y: "))
print(" ")

if x1 < x5 and y1 < y5:
    if x2 < x6 and y2 > y6:
        if x3 > x7 and y3 < y7:
            if x4 > x8 and y4 > y8:
                print("El primer rectangulo es mas grande que el segundo rectangulo")
                print(" ")
                                        
