x = int(input("Ingresa un número: "))
n1 = int(0)
n2 = int(1)
n3 = int()
print(n1,end=", ")
print(n2,end=", ")
for i in range(x):
        n3 = n1 + n2
        print(n3,end=", ")
        n1 = n2
        n2 = n3
