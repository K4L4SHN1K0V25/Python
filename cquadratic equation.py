a = float(input("Escriba el valor de a: "))
b = float(input("Escriba el valor de b: "))
c = float(input("Escriba el valor de c: "))

if a==0:
    print("a no debería ser 0")
    
x1 = ((-1)*b)+((b**2-4*a*c)**(1/2))/(2*a)
x2 = ((-1)*b)-((b**2-4*a*c)**(1/2))/(2*a)

if x1 == x2:
    print(f"una sola raíz {x1}")

else:
    print(f"raíz 1: {x1}")
    print(f"raíz 2: {x2}")
        
if x1 or x2 <= 1j:
    print("Raices imaginarias")

            
        




    



    



