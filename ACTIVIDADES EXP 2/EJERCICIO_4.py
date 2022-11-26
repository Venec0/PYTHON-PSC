# Ingrese un número entero mayor a cero por teclado e indique si es o no “Perfecto”

numero = int(input("INTRODUCE UN NÚMERO ENTERO: "))
suma = 0

for n in range(1, numero):
    
    if numero % n == 0:
        suma += n
    
if numero == suma:
    print(f"{numero} es un numero perfecto".upper())
else:
    print(f"{numero} no es un numero perfecto".upper())
    