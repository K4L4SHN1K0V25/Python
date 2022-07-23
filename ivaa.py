productos = []
precio1 = []

def iva(n, productos, precio1):
    for i in range(n):
        produ = input("Ingrese el nombre del producto: ")
        productos.append(produ)
        precio = float(input("Ingrese el precio del producto: "))
        precio1.append(precio)
    return

def sumar(precio1):
    suma = 0
    for i in precio1:
        suma += i

    ti = suma * .16
    tn = suma + ti

    print("EL total sin IVA es: ", suma)
    print("El IVA total es: " , ti)
    print("EL total con IVA es: ",tn)

    return 

    
n = int(input("Ingrese la cantidad de productos: "))
iva(n, productos, precio1)

print("Los productos son: ", productos)
sumar(precio1)



