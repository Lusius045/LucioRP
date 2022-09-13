print("---------------------------------")
print("Ejercicio 3: Respuestas")
print("---------------------------------")


print("Ingrese el número de respuestas correctas")
RC = int (input())
print("Ingrese el número de respuestas incorrectas")
RI = int(input())
print("Ingrese el número de respuestas en blanco")
RB = int(input())

PRC = RC*3
PRI = RI*-1
PRB = RB*0

#Puntaje Final
PF = PRC+PRI+PRB

print(PF)