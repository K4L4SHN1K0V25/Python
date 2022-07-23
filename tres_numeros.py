n1 = int(input("Ingresa el primer valor: "))
n2 = int(input("Ingresa el segundo valor: "))
n3 = int(input("Ingresa el tercer valor: "))

if n1 < n2 and n1 < n3:
    print(n1)
    if n2 < n3:
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)

if n2 < n1 and n2 < n3:
    print(n2)
    if n1 < n3:
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)

if n3 < n2 and n3 < n1:
    print(n3)
    if n2 < n1:
        print(n2)
        print(n1)
    else:
        print(n1)
        print(n2)
