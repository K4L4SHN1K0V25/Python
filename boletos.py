def venbol():
    CanBolA = int(input("Cuantos boletos en clase A desea? "))
    CanBolB = int(input("Cuantos boletos en clase B desea? "))
    CanBolC = int(input("Cuantos boletos en clase C desea? "))
    
    BolA = 300
    BolB = 240
    BolC = 180

    TBolA = CanBolA * BolA
    TBolB = CanBolB * BolB
    TBolC = CanBolC * BolC

    TBole = TBolA + TBolB + TBolC

    print("Total de boletos de clase A", CanBolA)
    print("Precio total de boletos de clase A", TBolA)
    print("")
    print("Total de boletos de clase A", CanBolB)
    print("Precio total de boletos de clase A", TBolB)
    print("")
    print("Total de boletos de clase A", CanBolC)
    print("Precio total de boletos de clase A", TBolC)
    print("")
    print("Precio total de todos los boletos", TBole)

    return

print("VENTA DE BOLETOS")
print("")
print("Precio de los boletos")
print("Boleto clase A $300")
print("Boleto clase B $240")
print("Boleto clase C $180")
print("")
venbol()
