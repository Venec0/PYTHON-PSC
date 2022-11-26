# WHILE: tiene la característica que para comenzar a ejecutarse debe cumplir con la condición que se establece
# al inicio del bucle, en caso contrario, continuará en la siguiente introducción:

a = 1
while a <5:
       print(a)
       a = a + 1
# 1. La variable "a" se inicia con un valor 1, por lo tanto, puede ingresar al ciclo while, dado que su condición
# es menor a 5 (verdadera).
# 2. Se imprime o muestra el valor de "a", es decir 1.
# 3. Se incrementa en 1 el valor de "a".
# 4. Vuelve a la condición while y si la condición es verdadera, se ejecuta nuevamente el ciclo.
# 5. Finalmente el resultado del código.

fact = 1
i = 1
num = int(input("INGRESE UN NÚMERO: "))
while i <= num:
      fact = fact * i
      i = i + 1 
print(f"EL FACTORIAL DE {num} ES: {fact}")

while True:
    op=int(input("INGRESE 12 PARA SALIR: "))
    if op == 12:
        print("GRACIAS POR SU ATENCIÓN.")
        break

# FOR: nos permite recorrer los elementos de una secuencia sea esta una lista, tupla o cadena de caracteres, etc.
# FOR, ejecuta una secuencia de instrucciones dependiendo de la cantidad de veces que se indique. Para ello, 
# utilizaremos la función "range" que permite generar listas de números.
x = range(5)
for n in x:
    print(n)

# FUNCIÓN RANGE: esta función devuelve una secuencia de números, comenzando desde 0 de forma predeterminada y se 
# incrementa en 1 y se detiene antes de un número especificado, es decir el último número no es inclusivo.

n = 5
for i in range (n):
    print ("HOLA")