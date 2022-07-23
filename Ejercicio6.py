x = int(input("Ingresa un número: "))
for i in range(x):
    print("*",end="")
print("")
for i in range(x-2):
    print("*",end="")
    for i in range(x-2):
        print(" ",end="")
    print("*")
for i in range(x):
    print("*",end="")
