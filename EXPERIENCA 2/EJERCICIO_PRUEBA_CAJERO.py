#LOG IN DE USUARIO POR MEDIO DE CAJERO AUTOMÁTICO CON:.

# 1. INGRESAR DINERO A CUENTA.
# 2. RETIRAR DINERO DE LA CUENTA.
# 3. MOSTRAR DINERO DISPONIBLE.
# 4. SALIR DEL CAJERO.

import os
saldo = 0

os.system("cls")
print()

p=int(input("INGRESE SU PIN DE 4 DíGITOS: "))

continuarsesion = ''
while continuarsesion == 's' or 'S':

    print("\t.:MENU:.")
    print("1. INGRESAR DINERO A CUENTA.")
    print("2. RETIRAR DINERO DE LA CUENTA.")
    print("3. MOSTRAR DINERO DISPONIBLE.")
    print("4. SALIR DEL CAJERO.")

    opcion=int(input("DIGITE UNA OPCIÓN DE MENÚ. "))

    if opcion==1:
        extra = float(input("¿CUÁNTO DINERO DESEA INGRESAR EN LA CUENTA? ->"))
        saldo += extra
        print(f"SU DINERO EN LA CUENTA AHORA ES DE: {saldo}")
    elif opcion==2:
        retirar = float(input("¿CUÁNTO DINERO DESEA RETIRAR DE LA CUENTA? ->"))
        if retirar>saldo:
            print("NO TIENE SA CANTIDAD DE DINERO A RETIRAR: ")
        else:
            saldo -= retirar
    elif opcion==3:
        print(f"DINERO EN LA CUENTA: {saldo}")
    elif opcion==4:
        print("GRACIAS POR UTILIZAR SU CAJERO AUTOMÁTICO.")
    else: 
        print("OPCIÓN INVÁLIDA.")

    continuarsesion=input('¿DESEA CONTINUAR? \n INGRESA S PARA CONTINUAR, PRESIONA 4 PARA SALIR.')
