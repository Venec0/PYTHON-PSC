# Ingrese un número entero mayor a cero por teclado e indique si es o no “Primo”

numero = int(input("INTRODUCE UN NÚMERO ENTERO:  "))
divisor = [] 
contador = 0
for n in  range(2 , numero):
    if numero % n == 0:
        contador +=1
        divisor.append(n)

if contador > 0:
    print("EL NÚMERO NO ES PRIMO.")
else:
    print("EL NÚMERO ES PRIMO.")

print(f"Divisores: {divisor}")