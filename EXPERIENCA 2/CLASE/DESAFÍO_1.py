a = int(input("INGRESE UN NÚMERO: "))
b = int(input("INGRESE UN NÚMERO: "))
c = int(input("INGRESE UN NÚMERO: "))
#_______________________________________________________________________________________________________________________________________
if(a>b and b>c):
    print(f"EL ORDEN DE NAYOR A MENOR: {a}>{b}>{c}")
elif(b>a and a>c):
    print(f"EL ORDEN DE NAYOR A MENOR: {b}>{a}>{c}")
elif(b>c and c>a):
    print(f"EL ORDEN DE NAYOR A MENOR: {b}>{c}>{a}")
elif(c>b and b>a):
    print(f"EL ORDEN DE NAYOR A MENOR: {c}>{b}>{a}")
elif(c>a and a>b):
    print("EL ORDEN DE NAYOR A MENOR: {c}>{a}>{b}")

    #a, b = b, a
    #ES UNA MANERA MÁS FÁCIL DE INTERCAMBIAR VARIABLES, EL ROL DEL AUXILIAR EN ESTE CASO ES "a"