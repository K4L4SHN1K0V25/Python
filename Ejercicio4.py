print("Mostrar 10 divisores de un número pedido al usuario")
x = int(input("Ingresa el número: "))
divisores = int(1)
for i in range(1,x):
    if x % i == 0 and 10 >= divisores:
        print("Divisor ",divisores,": ",i)
        divisores = divisores + 1
    
