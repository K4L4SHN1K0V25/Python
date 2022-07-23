segundo,minuto,hora = 0,0,0
while (hora < 24):
    segundo = 0
    minuto = 0
    while minuto != 60:
        segundo = 0
        while segundo != 60:
            if hora < 10:    
                print(end="0")    
            print(hora,end=":")
            if minuto < 10:
                print(end="0")
            print(minuto,end=":")
            if segundo < 10:
                print(end="0")
            print(segundo)
            segundo += 1
        minuto += 1
    hora += 1
