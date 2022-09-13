sum = 0

print("Ingrese número de términos")
num = int(input())

for i in range(1, num+1):
    if i%2 ==  0:
        sum = sum - (1/i)
    else:
        sum = sum + (1/i)


print("La suma será:", sum)