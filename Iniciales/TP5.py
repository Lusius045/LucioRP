import math

print("----------------------------------")
print("Ejercicio 5: Micro Discos")
print("----------------------------------")

print("Ingrese GB")
GB=float(input())

MG = GB*1024
MD = MG/1.44


print("\nSALIDA")
print("----------------------------------")
print(MD)

print("Numero de Discos necesarios:", math.ceil(MD))