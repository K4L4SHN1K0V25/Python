n = 0
def mostrar(n):
    lista = ["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez","once","doce",
             "trece","catorce","quince","dieciseis","diecisiete","dieciocho","diecinueve","veinte"]

    print(lista[n])

while n >= 0:
    n=int(input("Escriba un numero del 1 al 20: "))
    mostrar(n)
