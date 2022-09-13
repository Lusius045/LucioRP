print("-------------------------------------------------------")
print("SUMA DE SERIE.")
print("-------------------------------------------------------")

print("Ingrese el número de terminos:")
n = int(input())

s = 5
ser = 0

for i in range(1,n):
    s = s+5
    ser = ser+s

print("La suma de la serie es: ",ser)