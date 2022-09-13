cont = 0

num = 10
print("Ingrese ",num," letras:")

for i in range(1,num):
    m = input("Ingrese la letra:")
    if m == "a":
        cont = cont+1


print("En ",num," caracteres hay ",cont," caracteres a")