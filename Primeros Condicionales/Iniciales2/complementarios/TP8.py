print("-------------------------------------------------------")
print("AREA DE UN CÍRCULO:")
print("-------------------------------------------------------")

pi=3.1416

print("Presione 1 para calcular el área de un triángulo")
print("Presione 2 para calcular el área de un círculo")

opcion = int(input())

if opcion==1:
    print("Area de un triángulo:")
    lt = float(input())
    at = ((3**0,5)/4)* lt**2

    print("Area del triángulo: ",at)
else:
    if opcion==2:
        print("Area del círculo:")

        print("Ingrese el radio del círculo:")
        r = float(input())
        ac = pi*r**2
        
        print("Area del círculo: ",ac)
    else:
        print("Seleccióne 1 u 2 para una opción válida.")

