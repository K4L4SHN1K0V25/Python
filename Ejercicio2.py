x = int(input("Ingresa un número: "))
x1 = int(x)
x2 = int(x)
x3 = int(x)
n1 = int(2048)
n2 = int(512)
n3 = int(256)
r1 = int(0)
r2 = int(0)
r3 = int(0)
div = int(0)
print("Hexadecimal: ",end="")
for i in range(3):
        r2 = x3 % n3
        x3 = x3 - r2
        div = x3 / n3
        if div  == 15:
            print("F",end="")
        elif div == 14:
            print("E",end="")
        elif div == 13:
            print("D",end="")
        elif div == 12:
            print("C",end="")
        elif div == 11:
            print("B",end="")
        elif div == 10:
            print("A",end="")
        else:
            print(int(x3/n3),end="")
        x3 = r2
        n3 = n3 / 16
print("")
print("Octal: ",end="")
for i in range(4):
        r1 = x2 % n2
        x2 = x2 - r1
        print(int(x2/n2),end="")
        x2 = r1
        n2 = n2 / 8
print("")
print("Binario: ",end="")
for i in range(12):
        r3 = x1 % n1
        x1 = x1 - r3
        print(int(x1/n1),end="")
        x1 = r3
        n1 = n1 / 2
    

