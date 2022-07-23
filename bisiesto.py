def bisiesto (inicio, fin):
    while inicio <= fin:

        if inicio % 4 == 0 and inicio % 100 != 0 or inicio % 400 == 0:
            print(inicio)
        inicio += 1

inicio=int(input("Dame un año con el que quieras iniciar: "))
fin=int(input("Dame un año con el que quieras terminar: "))
if inicio < fin:
    bisiesto(inicio, fin)
