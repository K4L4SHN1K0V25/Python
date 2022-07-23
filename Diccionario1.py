print("Ejercicio 1.")
mascotaDatos = {}
mascota = True
while mascota:
    datosInvalid,datoInvalid = True,True
    print("Menú de opciones")
    print("1. Capturar datos")
    print("2. Mostrar datos")
    print("3. Búsqueda")
    print("4. Salir")
    opcion = int(input("Ingresa una opción: "))
    print("-------------------------")
    if opcion == 1:
        while datosInvalid:
            nombreInvalid,edadInvalid,razaInvalid,nombreDInvalid,telInvalid = False,False,False,False,False
            print("1. Nombre")                
            print("2. Edad")
            print("3. Raza")
            print("4. Nombre del dueño")
            print("5. Teléfono")
            print("6. Salir")
            dato = input("¿Qué dato quieres capturar? ")
            if dato == "1":
                nombreInvalid,edadInvalid,razaInvalid,nombreDInvalid,telInvalid = True,False,False,False,False
            elif dato == "2":
                nombreInvalid,edadInvalid,razaInvalid,nombreDInvalid,telInvalid = False,True,False,False,False
            elif dato == "3":
                nombreInvalid,edadInvalid,razaInvalid,nombreDInvalid,telInvalid = False,False,True,False,False
            elif dato == "4":
                nombreInvalid,edadInvalid,razaInvalid,nombreDInvalid,telInvalid = False,False,False,True,False
            elif dato == "5":
                nombreInvalid,edadInvalid,razaInvalid,nombreDInvalid,telInvalid = False,False,False,False,True
            elif dato == "6":
                nombreInvalid,edadInvalid,razaInvalid,nombreDInvalid,telInvalid = False,False,False,False,False
                datoInvalid,datosInvalid = False,False
            while nombreInvalid:
                nombre = input("Ingresa el nombre: ")
                if nombre == "":
                    print("Ingresa un nombre válido")
                else:
                    mascotaDatos['Nombre'] = nombre
                    nombreInvalid = False
            while edadInvalid:
                edad = input("Ingresa su edad: ")
                if edad == "":
                    print("Ingresa un edad")
                else:
                     mascotaDatos['Edad'] =edad
                     edadInvalid = False
            while razaInvalid:
                raza = input("Ingresa su raza: ")
                if raza == "":
                    print("Ingresa una raza válida")
                else:
                     mascotaDatos['Raza'] = raza
                     razaInvalid = False
            while nombreDInvalid:
                nombreD = input("Ingresa el nombre del dueño: ")
                if raza == "":
                    print("Ingresa un nombre válido")
                else:
                     mascotaDatos['Nombre del dueño'] = nombreD
                     nombreDInvalid = False
            while telInvalid:
                tel = input("Ingresa el número de teléfono: ")
                if len(tel) < 10 or tel == "":
                    print("Ingresa un teléfono válido")
                else:
                    mascotaDatos['Teléfono'] = tel
                    telInvalid = False
            print("-------------------------")
    elif opcion == 2:
        if len(mascotaDatos) == 0:
            print("No hay datos registrados")
        else:
            for key, value in mascotaDatos.items():
                print(key,":", value)
    elif opcion == 3:
        cont = 0
        print("Datos de mascota: Nombre, Edad, Raza, Nombre del dueño, Telefono")
        busq = input("¿Qué quiere saber de la mascota? ")
        print("-------------------------")
        for key, value in mascotaDatos.items():
            if key == busq:
                print(key,":", value)
                cont = +1
        if cont == 0:
            print("No se encontró nada en la búsqueda")
    elif opcion == 4:
        mascota = False
    else:
        print("Ingresa una opción válida")
    if opcion != 4:    
        print("-------------------------")
print("Fin del programa")
print("-------------------------")
