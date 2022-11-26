#Escribir un algoritmo que ordene ascendentemente tres números.'''
# --- Ingresar numeros
Numero1 = float(input('Ingrese primer numero = '))
Numero2 = float(input('Ingrese segundo numero = '))
Numero3 = float(input('Ingrese tercer numero = '))
# --- Posibles arreglos
# --- 1 (esta ordenado)
# --- 2 
if Numero1<Numero2>Numero3 and Numero1<Numero3:
    Temp = Numero2
    Numero2 = Numero3
    Numero3 = Temp
# --- 3
if Numero1>Numero2<Numero3 and Numero1<Numero3:
    Temp = Numero1
    Numero1 = Numero2
    Numero2 = Temp
# --- 4
if Numero1<Numero2>Numero3 and Numero1>Numero3:
    Temp = Numero3
    Numero3 = Numero2
    Numero2 = Numero1
    Numero1 = Temp
# --- 5
if Numero1>Numero2<Numero3 and Numero1>Numero3:
    Temp = Numero1
    Numero1 = Numero2
    Numero2 = Numero3
    Numero3 = Temp
# --- 6
if Numero1>Numero2>Numero3:
    Temp = Numero3
    Numero3 = Numero1
    Numero1 = Temp
# --- Mostrar numeros ordenados
print('Mostrar los numeros ordenados: ',Numero1,' ',Numero2,' ',Numero3)
# --- Fin