print("-------------------------------------------------------")
print("DIA SIGUIENTE.")
print("-------------------------------------------------------")


print("Ingrese el año:")
ano = int(input("Año: "))
print("Ingrese el mes:")
mes = int(input("Mes: "))
print(input("Ingrese el dia:"))
dia = int("Día: ")

if dia>0 and dia<30 :
    print(dia+1)
    print(mes)
    print(ano)
else:
    if mes>0 and mes<12:
        print("1")
        print(mes+1)
        print(ano)
    else:
        print("1")
        print("1")
        print(ano+1)