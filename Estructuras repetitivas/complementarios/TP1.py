print("-------------------------------------------------------")
print("100 NÚMEROS PARES.")
print("-------------------------------------------------------")

cont = 0

print("Ingrese 10 números:")

for i in range (1,10 + 1):
    num = int(input("Número:"))

    if num % 2 == 0:
        cont = cont+1


print("Hay ",cont," números pares.")
