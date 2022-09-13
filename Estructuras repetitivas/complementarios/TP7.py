print("Ingrese un número:")
num = int(input())

const = 0

for i in range(2,num):
    if num % i == 0:
        const = const+1

if const == 0:
    print(num," es un número primo.")
else:
    print(num," no es un número primo.")