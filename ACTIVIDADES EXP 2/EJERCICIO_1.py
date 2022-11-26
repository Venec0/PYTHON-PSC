# INGRESAR POR TECLADO 5 NÚMEROS ENTEROS, LUEGO DEBE INDICAR:
# Cuántos números son mayores a 0
# Cuántos números son menores a 0
# Cuántos números son iguales a 0


numeros = []
for i in range (5):
    numero = int((input("INTRODUCE EL NÚMERO #{}: ".format(i+1))))
    numeros.append(numero)

mayor = numeros[0]
menor = numeros[0]
igual = 0

for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    if numero == igual:
       igual = numero
    if numero < igual:
        menorcero = numero

print("MAYOR: ", mayor)
print("MENOR", menor)
print("IGUAL", igual)