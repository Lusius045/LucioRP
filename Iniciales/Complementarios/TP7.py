import math

print("--------------------------------")
print("PASAR ALFA A RADIANES")
print("--------------------------------")

PI = 3.1416

print("Ingrese los lados de un triangulo:")
B = float(input("Lado B:"))
C = float(input("Lado C:"))

print("Ingrese el ángulo en grados sexagesimales:")
alfa = float(input("Angulo: "))

A = (B**2+C**2-2*B*C*math.cos(alfa*PI/180))**0.5

print("--------------------------------")
print("lado A: ",A)