
# ** 3)	Considere la actividad 2, ahora la lista deberá ser mostrada en orden alfabético por el apellido.

l=int(input("INGRESE CANTIDAD DE NOMBRES: "))
nom=list()
ape=list()
for i in range(l):
    n=input("INGRESE NOMBRE: ")
    a=input("INGRESE APELLIDO: ")
    nom.append(n)
    ape.append(a)

for i in range(l):
    print (f"{nom[i]} {ape[i]}")

#

nom_com=list()
for i in range(l):
    aux=ape[i]+' ' +nom[i]
    nom_com.append(aux)
nom_com.sort()
print("LISTA ORDENADA.")
for i in range(l):
    print(f"{nom_com[i]}")