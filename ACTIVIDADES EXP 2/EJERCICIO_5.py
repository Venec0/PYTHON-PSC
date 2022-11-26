# Genere las 10 primeras tablas de multiplicar, cada una de ellas de 1 a 10

for n in range(1,11):
    print(f"--- TABLA DEL {n} ----")
    for x in range(1,11):
        print(f"{n}x{x}={n*x}")