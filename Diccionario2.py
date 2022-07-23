print("Ejercicio 2.")
datosEstetica = {}
datosVacunas = {}
datosMedico = {}
datosOtro = {}
menu = True
esteticaInvalid,vacunasInvalid,medicoInvalid,otroInvalid = True,True,True,True

def captEstetica():
    nombreInvalid,telInvalid,mascotaInvalid,entradaInvalid,salidaInvalid = True,True,True,True,True
    esteticaInvalid = True
    while esteticaInvalid:
            while nombreInvalid:
                nombre = input("Ingresa el nombre del dueño: ")
                if nombre == "":
                    print("Nombre inválido.",end=" ")
                else:
                    datosEstetica['Nombre'] = nombre
                    nombreInvalid = False
            while telInvalid:
                tel = input("Ingresa el teléfono: ")
                if len(tel) < 10 or tel == "":
                    print("Telefono invalido (tiene que ser 10 números).",end=" ")
                else:
                     datosEstetica['Telefono'] = tel
                     telInvalid = False
            while mascotaInvalid:
                mascota = input("Ingresa el nombre de la mascota: ")
                if mascota == "":
                    print("Nombre inválido.",end=" ")
                else:
                     datosEstetica['Mascota'] = mascota
                     mascotaInvalid = False
            while entradaInvalid:
                entrada = input("Ingresa la hora de entrada: ")
                if entrada == "":
                    print("Hora inválida.",end=" ")
                else:
                     datosEstetica['Hora de entrada'] = entrada
                     entradaInvalid = False
            while salidaInvalid:
                salida = input("Ingresa la hora de salida: ")
                if salida == "":
                    print("Hora inválida.",end=" ")
                else:
                    datosEstetica['Hora de salida'] = salida
                    salidaInvalid = False
                    esteticaInvalid = False
    print("Datos estética:")
    for key, value in datosEstetica.items():
        print(key,":", value)



def captVacunas():
    nombreInvalid,edadInvalid,vacunasInvalid,fechaInvalid,nombreDInvalid,correoInvalid,telInvalid = True,True,True,True,True,True,True
    while nombreInvalid:
        nombre = input("Ingresa el nombre de la mascota: ")
        if nombre == "":
            print("Nombre inválido.",end=" ")
        else:
            datosVacunas['Nombre'] = nombre
            nombreInvalid = False
    while edadInvalid:
        edad = input("Ingresa la edad: ")
        if edad == "":
            print("Edad inválida.",end=" ")
        else:
                datosVacunas['Edad'] = edad
                edadInvalid = False
    while vacunasInvalid:
        vacunas = input("Ingresa las vacunas aplicadas: ")
        if vacunas == "":
            print(".",end=" ")
        else:
            datosVacunas['Vacunas aplicadas'] = vacunas
            vacunasInvalid = False
    while fechaInvalid:
        fecha = input("Ingresa la fecha de aplicación: ")
        if fecha == "":
            print("Valor inválido.",end=" ")
        else:
            datosVacunas['Fecha de aplicación'] = fecha
            fechaInvalid = False
    while nombreDInvalid:
        nombreD = input("Ingresa el nombre del dueño: ")
        if nombreD == "":
            print("Valor invalido.",end=" ")
        else:
            datosVacunas['Nombre del dueño'] = nombreD
            nombreDInvalid = False
    while correoInvalid:
        correo = input("Ingresa el correo: ")
        if correo == "":
            print("Correo inválido.",end=" ")
        else:
            datosVacunas['Correo'] = correo
            correoInvalid = False
    while telInvalid:
        tel = input("Ingresa el teléfono: ")
        if tel == "":
            print("Teléfono inválido.",end=" ")
        else:
            datosVacunas['Telefono'] = tel
            telInvalid = False
    print("Datos vacunas:")
    for key, value in datosVacunas.items():
        print(key,":", value)

def captMedico():
    invalid1,invalid2,invalid3,invalid4,invalid5,invalid6,invalid7,invalid8 = True,True,True,True,True,True,True,True
    while invalid1:
        nombre = input("Ingresa el nombre: ")
        if nombre == "":
            print("Nombre inválido.",end=" ")
        else:
            datosMedico['Nombre'] = nombre
            invalid1 = False
    while invalid2:
        tel = input("Ingresa el teléfono: ")
        if tel == "":
            print("Teléfono inválido.",end=" ")
        else:
                datosMedico['Telefono'] = tel
                invalid2 = False
    while invalid3:
        mascota = input("Ingresa el nombre de la mascota: ")
        if mascota == "":
            print("Valor inválido.",end=" ")
        else:
            datosMedico['Mascota'] = mascota
            invalid3 = False
    while invalid4:
        raza = input("Ingresa la raza: ")
        if raza == "":
            print("Valor inválido.",end=" ")
        else:
            datosMedico['Raza'] = raza
            invalid4 = False
    while invalid5:
        edad = input("Ingresa la edad: ")
        if edad == "":
            print("Valor inválido.",end=" ")
        else:
            datosMedico['Edad'] = edad 
            invalid5 = False
    while invalid6:
        problem = input("Ingresa la problemática: ")
        if problem == "":
            print("Valor inválido.",end=" ")
        else:
            datosMedico['Problematica'] = problem
            invalid6 = False
    while invalid7:
        tratamiento = input("Ingresa el tratamiento: ")
        if tratamiento == "":
            print("Valor inválido.",end=" ")
        else:
            datosMedico['Tratamiento'] = tratamiento
            invalid7 = False
    while invalid8:
        fecha = input("Ingresa la fecha: ")
        if fecha == "":
            print("Valor inválido.",end=" ")
        else:
            datosMedico['Fecha'] = fecha
            invalid8 = False
    print("Datos medicos:")
    for key, value in datosMedico.items():
        print(key,":", value)

def captOtro():
    invalid1,invalid2,invalid3,invalid4 = True,True,True,True
    while invalid1:
        fecha = input("Ingresa la fecha: ")
        if fecha == "":
            print("Valor inválido.",end=" ")
        else:
            datosOtro['Fecha'] = fecha
            invalid1 = False
    while invalid2:
        servicio = input("Ingresa el servicio: ")
        if servicio == "":
            print("Valor inválido.",end=" ")
        else:
            datosOtro['Servicio'] = servicio
            invalid2 = False
    while invalid3:
        mascota = input("Ingresa el nombre de la mascota: ")
        if mascota == "":
            print("valor inválido.",end=" ")
        else:
            datosOtro['Mascota'] = mascota
            invalid3 = False
    while invalid4:
        descripcion = input("Ingresa una breve descripción: ")
        if descripcion == "":
            print("Valor inválido.",end=" ")
        else:
            datosOtro['Descripcion'] = descripcion
            invalid4 = False
    print("Datos:")
    for key, value in datosOtro.items():
        print(key,":", value)

while menu:
    print("¿Donde desea capturar la información?")
    print("1. Estética")
    print("2. Vacunas")
    print("3. Médico")
    print("4. Otro")
    print("5. Salir")
    opcion = int(input("Ingresa una opción: "))
    print("-------------------------")
    if opcion == 1:
        captEstetica()
    elif opcion == 2:
        captVacunas()
    elif opcion == 3:
        captMedico()
    elif opcion == 4:
        captOtro() 
    elif opcion == 5:
        menu = False
    else:
        print("Ingresa una opción válida")
    if opcion != 5:    
        print("-------------------------")
print("Fin del programa")
print("-------------------------")
