
# **2)	Cree 2 listas, en las cuales se guardarán 4 nombres y 4 apellidos respectivamente. 
# **El sistema deberá mostrar un listado de los nombres con su correspondiente apellido.

nombres= list()
apellidos= list()
n=4
for i in range(n):
    nom = input("INGRESE NOMBRE: ")
    ape = input("INGRESE APPELIDO:")
    nombres.append(nom)
    apellidos.append(ape)

    
print("__________________________________________________________________________________________________________")
for i in range(n):
    print (f"{nombres[i]} {apellidos[i]}")