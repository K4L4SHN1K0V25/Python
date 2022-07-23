print("Elevar x a la potencia y")
x = int(input("Ingresa x: "))
y = int(input("Ingresa y: "))
z = int(x)
print(x,"a la potencia ",y)
for i in range(y-1):
    z = z * x
print("Resultado: ",z)
