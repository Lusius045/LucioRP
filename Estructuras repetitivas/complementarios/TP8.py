print("Ingrese la cantidad de números para evaluar:")
cant = int(input())

cont = 0

for i in range(1, cant+1):
    num = int("Ingrese el número:")
    if num == 0:
        cont = cont+1

print("Hay ",cont," números enteros.")