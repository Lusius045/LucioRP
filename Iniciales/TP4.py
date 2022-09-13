print("----------------------------------")
print("Ejercicio 4:Partidos")
print("----------------------------------")

print("Ingrese el número de partidos ganados")
PG = int (input())
print("Ingrese el número de partidos empatados")
PE = int (input())
print("Ingrese el número de partidos perdidos")
PP = int (input())

PPG = PG*3
PPE = PE*1
PPP = PP*0

PT = PPG + PPE + PPP

print(PT)