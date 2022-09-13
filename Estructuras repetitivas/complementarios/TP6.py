aux = 0
aux2 = 0

print("Ingrese un número entero:")
num = int(input())

i = 10

while i <= num:
    aux = num%10
    num = num//10
    aux2 = aux2*10 + aux

aux2 = aux2*10 + num

print("El número invertido es: ",aux2)

