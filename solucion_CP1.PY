import os
while True:
    print('1 DIA DE SEMANA   2 FIN DE SEMANA')
    dia = int(input('INGRESE OPCION'))
    if dia==1 or dia==2:
        break
    input('Pulse un tecla para continuar....')

tan=0;tap=0
while True:
    while True:
        os.system('cls')
        print('1.motocicleta   2. auto - camioneta  3.camion-bus')
        tipo=int(input('INGRESE TIPO DE VEHICULO:'))
        if tipo==1:
            ntipo='1-MOTOCICLETA'
            break
        elif tipo==2:
            ntipo='2-auto-camioneta'
            break
        elif tipo==3:
            ntipo='3-camion- bus'
            break
        else:
            print('tipo no valido')
        input('Pulse un tecla para continuar....')
    minutos = int(input('INGRESE CANTIDA DE MINUTOS:'))
    total=0
    if tipo==1:
        if dia==1:
            tan=tan+minutos*5
            total=minutos*5
            ndia='NORMAL'
        else:
            tap=tap+minutos*10
            total=minutos*10
            ndia="PUNTA"

    if tipo==2:
        if dia==1:
            tan=tan + minutos*15
            total=minutos*15
            ndia='NORMAL'
        else:
            tap=tap+minutos*30
            total=minutos*30
            ndia="PUNTA"

    if tipo==3:
        if dia==1:
            tan=tan+minutos*50
            total=minutos*50
            ndia='NORMAL'
        else:
            tap=tap+minutos*90
            total=minutos*90
            ndia="PUNTA"

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