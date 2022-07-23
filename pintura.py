def pies():
    piesc = float(input("Cuantos pies cuadrados son los que planea pintar? "))

    ph = piesc / 14.375
    th = ph * 80
    tg = ph * 0.125
    gg = (0.00869565 * piesc) / 1

    print("Horas necesarias: ", '{0:.3f}'.format(ph))
    print("Precio por horas necesarias: ", '{0:.3f}'.format(th))
    print("Galones necesarios: ", '{0:.3f}'.format(tg))
    print("Cubeta de galon necesarias: ", '{0:.2f}'.format(gg))
    return

print("PinMEX")
print("Cotizacion de trabajo")
print("")
pies()
