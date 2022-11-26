import os
while True:
    print(" 1 DÍA DE SEMANA  2 FIN DE SEMANA")
    dia = int(input("INGRESE OPCIÓN: "))
    if dia== 1 or dia == 2:
        break
    input("PULSE UNA TECLA PARA CONTINUAR...")

tan=0;tap=0
while True:
    while True:
        os.system("cls")
        print("1. MOTOCICLETA  2. AUTO/CAMIONETA  3. CAMIÓN/BUS")
        tipo=int(input("INGRESE EL TIPO DE VEHÍCULO: "))
        if tipo==1:
            ntipo= "1-MOTOCICLETA."
            break
        elif tipo==2:
            ntipo= "2-AUTO/CAMIONETA."
            break
        elif tipo==3:
            ntipo= "3-CAMIÓN/BUS"
            break
        else:
            print("TIPO NO VÁLIDO.")
        input("PULSE UNA TECLA PARA CONTINUAR.")
    minutos = int(input("INGRESE CANTIDAD DE MINUTOS: "))
    total = 0
    if tipo==1:
        if  dia==1:
           tan=tan+minutos*5
           total=minutos*5
           ndia="NORMAL."
        else:
            tap=tap+minutos*10
            total=minutos*10
            ndia="PUNTA."

    if tipo==2:
        if dia==1:
            tan=tan+minutos*15
            total=minutos*15
            ndia="NORMAL."
        else:
            tap=tap+minutos*30
            total=minutos*30
            ndia="PUNTA."
    if tipo==3:
        if dia==3:
            tan=tan+minutos*50
            total=minutos*50
            ndia="NORMAL."
        else:
            tap=tap+minutos*90
            total=minutos*90
            ndia="PUNTA."    
    #mostrar el ticket
    print(f'TIPO.........{ntipo}')
    print(f'TARIFA.......{ndia}')
    print(f'MINUTOS......{minutos}')
    print(f'NORMAL.......{total}')

    exit=input('INGRESE 1 PARA SALIR....')
    if exit=='1':
        break
print('INFORME')
print(f'NORMAL...:{tan}')
print(f'PUNTA...:{tap}')        