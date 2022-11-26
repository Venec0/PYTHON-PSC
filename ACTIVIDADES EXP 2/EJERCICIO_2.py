# INGRESE POR TECLADO 10 LETRAS, INDIQUE CUÁNTAS DE ELLAS SON VOCALES Y CUÁNTAS DE ELLAS SON CONSONANTES.

for letras in range(10):
    letra = input(f"ESCRIBA LA LETRA #{letras}: ")

if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("VOCAL.")
else:
    print("CONSONANTE.")