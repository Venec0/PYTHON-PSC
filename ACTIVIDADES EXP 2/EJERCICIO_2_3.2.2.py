#Ejercicio 2:
#Ingrese números enteros a una lista. Al ingresar un cero se detiene, 
# debe mostrar los elementos de ésta en forma ordenada ascendente.

b = list()
while True:
    n = int(input("INGRESE NÚMERO"))
    if n!=0:
        b.append(n)
    else:
        break
    print(b)