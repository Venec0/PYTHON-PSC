import os, random

for i in range (1, 11):
    print ('PROCESO ' + repr (i))
    numero_al_azar=random.randint(0, 1000-1)
    print ('Valor de numero al azar: ' + repr (numero_al_azar))
    print ()
 