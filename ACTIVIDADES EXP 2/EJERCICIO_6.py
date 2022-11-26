# De una cantidad determinada (n) de personas, se pide generar un informe clasificado por sexo, que muestre cantidad de:
# menores de edad, 
# mayores de edad, 
# adultos mayores.
import os
n = int(input("INGRESE N° PERSONAS: "))
cmm=0;cma=0;cmv=0
chm=0;cha=0;chv=0
for i in range(1, n):
    print (i)
    while True:
        os.system("cls")
        sexo = input("INGRESE SEXO 1) MUJER - 2) HOMBRE: ")
        if sexo=="1" or sexo=="2":
            edad = int(input("INGRESE EDAD: "))
        if sexo=="1" and edad >0 and edad<150:
            break
        if sexo== "2" and edad>0 and edad<130:
            break
input(sexo)
if sexo =="1":
    if edad<18:
        cmm=cmm+1
    if edad>=18 and edad<60:
        cma=cma+1
    if edad>60:
        cmv=cmv+1
else:
    if edad<18:
        chm=chm+1
    if edad>=18 and edad<60:
        cha=cha+1
    if edad>60:
        chv=chv+1