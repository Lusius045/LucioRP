print ("Ingrese la cantidad de empleados:")
emp = int(input())

i = 1
smayor = 0.0

print("Ingrese los sueldos: ")

while i <= emp :
    suel = float(input("Ingrese sueldo {0}: ".format(i)))
    
    if suel > smayor :
        smayor = suel
        c = i
    
    i = i + 1

print ("El empleado numero ",c, " tiene el mayor sueldo que es:", smayor)