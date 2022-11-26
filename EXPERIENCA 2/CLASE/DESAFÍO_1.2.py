a = int(input("INGRESE UN NÚMERO: "))
b = int(input("INGRESE UN NÚMERO: "))
c = int(input("INGRESE UN NÚMERO: "))
#________________________________________________________________
aux = 0
if b>=a:
    a = aux
    a = b
    b = aux
if c>=b:
    b = aux
    b = c
    c = aux
if b>=a:
    a = aux
    a = b
    b = aux
print(f"EL ORDEN DE MAYOR A MENOR ES: {a}-{b}-{c}")