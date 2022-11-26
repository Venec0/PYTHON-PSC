#Ejercicio 3:

#Ingresar 10 números a una lista, luego muestre la suma y promedio de los elementos.

import random as rm
azar=list()
for i in range(10):
    x=rm-rm.randint(0,100)
    azar.append(x)
    acum=acum+azar[i]
print(azar)
prom=acum/10
print(f"EL PROMEDIO DE LA SUMA {acum} es {prom}")