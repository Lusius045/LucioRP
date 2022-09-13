print("-------------------------------------------------------")
print("VELOCIDAD DE DOS VEHÍCULOS")
print("-------------------------------------------------------")

print("Ingrese la velocidad de dos vehículos:")
v1 = float("Vehìculo 1: ")
v2 = float("Vehìculo 2: ")

print("Ingrese la distancia:")
dis = float("Distancia: ")

if v1>0 and v2>0:
    tiem = dis/(v1+v2)
    print("Tiempo de encuentro: ",tiem)
else:
    print("Ingrese otras velocidades a los vehículos")