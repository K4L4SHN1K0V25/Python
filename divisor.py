dividendo = float(input("Ingresa el valor del dividendo: "))
divisor = float(input("Ingresa el valor del divisor: "))

re=dividendo/divisor

if re%2==0 or re%3==0 or re%5==0 or re%7==0:
    print("El segundo numero SI es divisor del primero")

else:
    print("El segundo numero NO es divisor del primero")




