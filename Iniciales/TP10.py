from string import whitespace
from webbrowser import BackgroundBrowser


print("-----------------------------")
print("AREA Y VOLUMEN DE UN CILINDRO")
print("-----------------------------")

PI = 3.1416

print("Ingrese el radio:")
R = float(input("Radio:"))

print("Ingrese la altura del cilindro:")
A = float(input("Altura: "))

vol = PI*R**2*A

ar = 2*PI*R(A+R)

print("-----------------------------")
print("Volumen: ",vol)
print("Area: ",ar)
