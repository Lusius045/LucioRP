from tkinter import N


print("Ingrese la cantidad de números que se van a comparar:")
lim = int(input())
print("Ingrese los números:")
num = int(input())

men = num
may = num

for i in range(1, lim):
    num = int(input("Ingrese el número:"))

    if num<men:
        men=num
    else:
        if num>may:
            may=num

print("El número menor es: ",men)    
print("El número mayor es: ",may)    