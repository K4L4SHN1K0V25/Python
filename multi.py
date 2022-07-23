n = 0

while n < 6:
    print("1 - Multiplos de 2")
    print("2 - Multiplos de 3")
    print("3 - Multiplos de 5")
    print("4 - Multiplos de 7")
    print("5 - Multiplos de 11")
    print("6 - Salir")
    n = int(input("Escoga una opcion: "))

    if n == 1:
        m = 2
        for i in range(1, 101):
            print(f'{i} x {m} = {i * m}')

    if n == 2:
        m = 3
        for i in range(1, 101):
            print(f'{i} x {m} = {i * m}')

    if n == 3:
        m = 5
        for i in range(1, 101):
            print(f'{i} x {m} = {i * m}')

    if n == 4:
        m = 7
        for i in range(1, 101):
            print(f'{i} x {m} = {i * m}')

    if n == 5:
        m = 11
        for i in range(1, 101):
            print(f'{i} x {m} = {i * m}')
