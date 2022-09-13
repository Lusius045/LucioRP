i = 1
cont = 0
num = 10

print("Ingrese ",num," números enteros:")
while i <= num:
    n = int(input("ingrese el número:"))
    if n%2 == 0:
        cont = cont+1
    
    i = i+1


print("En ",num," números enteros hay ",cont," números pares.")