print("-------------------------------------------------------")
print("NUMEROS NEGATIVOS:")
print("-------------------------------------------------------")

print("Ingrese 3 números:")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

if num1<0:
    pro = num1*num2*num3
    print("Producto: ",pro)
else:
    pro = num1+num2+num3
    print("Suma: ",pro)