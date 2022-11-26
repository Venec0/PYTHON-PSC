
# ** 1)	Ingrese n números enteros a una lista que se encuentren en el rango 1 a 1500 ambos inclusive. 
# **Al final, debe mostrar los elementos de ésta en forma ordenada ascendente.
i = 0
n = int(input("INGRESE UN NÚMERO DEL 1 AL 1500: "))
n = list(range(0,1500 + 1))
n.sort(reverse=True)
print(n)

# TODO: CORRECIÓN

numeros = list()
n=int(input("INGRESE LA CANTIDAD DE NÚMEROS: "))
i=0
while i<n:
    num=int(input("INGRESE NÚMERO RANGO 1 A 1500: "))
    if num>=1 and num<=1500:
        numeros.append(num)
        i=i+1
print(numeros)
numeros.sort()
print(numeros)