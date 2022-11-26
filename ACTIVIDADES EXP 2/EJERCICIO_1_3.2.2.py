#Ejercicio 1:

#Ingrese un número por teclado y guarde en una lista su tabla de multiplicar hasta el 10. 
#Ejemplo, si ingresa el número 3, la lista debe contener: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30

n=int(input("INGRESE TABLA"))
tb=list()
for i in range(1,11):
    tb.append(1*n)
print(tb)