def contarletras(frase):
    letras = 0

    for i in frase:
        if i != " ":
            if i.isalpha():
                letras += 1

    return letras

cadena=input("Escribe una frase: ")
cantidad = contarletras(cadena)
print(cantidad)
