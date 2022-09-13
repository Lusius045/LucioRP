from multiprocessing.connection import wait


print("-------------------------------------------------------")
print("NÚMERO MAYOR O MENOR")
print("-------------------------------------------------------")

print("Ingrese el primer número:")
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    print("El primer número es mayor.")
else:
    if num1 < num2:
        print("El segundo número es mayor.")
    else:
        if num1 == num2:
            print("Los números son iguales.")