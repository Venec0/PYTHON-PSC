import imp
import os
from datetime import date
import numpy as np
clientes=[] 
rut=[]

tarifap = 0
tarifag = 0
tarifasil = 0

asientos = np.array(range(1,101),dtype='str')

    #MENÚ:


def menu():

    os.system('cls')
    print(".-MENÚ._")
    print('1.- COMPRAR ENTRADAS: ')
    print('2.- MOSTRAR UBICACIONES DISPONIBLES. ')
    print('3.- VER LISTADO DE ASISTENTES ')
    print('4.- MOSTRAR GANANCIAS TOTALES. ')
    print('5.- SALIR. ')
    return input("INGRESE OPCIÓN: ")

    #1. COMPRAR ENTRADAS

def compra():

    existe=False
    while True:
        rutcliente=(input('INGRESE RUT DEL CLIENTE: '))
        if len(rutcliente) == 8 and rutcliente[7].isnumeric():
            rut.append(rutcliente)
            break
        else:
            print('INGRESE UN RUT VÁLIDO PARA LA COMPRA: ')

    nombrecliente=input('INGRESE NOMBRE DEL CLIENTE: ')

    print('1. PLATINUM = $120,000 (ASIENTO DEL 1 AL 20)')
    print('2. GOLD = $80,000 (ASIENTOS DEL 21 AL 50)')
    print('3. SILVER = $50,000 (ASIENTOS DEL 51 AL 100)')
    opcion=input('INGRESE OPCIÓN: ')
    while True:    
        num=input('INGRESE NÚMERO DEL ASIENTO: ')
        if num in asientos:
            i=int(num)-1
            asientos[i]='x'
            if int(num) >= 1 and int(num)<=19:
                print('PLATINUM SELECCIONADO.')
                tarifap = 120000
                break
            elif int(num) >= 21 and int(num)<=49:
                print('GOLD SELECCIONADO. ')
                tarifag = 80000
                break
            elif int(num) >= 51 and int(num) <=101:
                print('SILVER SELECCIONADO.')
                tarifasil = 50000
                break
        else:
            print('ASIENTO YA SELECCIONADO, INGRESE OTRO. ')


    #VERIFICAR QUE NO EXISTA.

    for cliente in clientes:
        if rut in cliente:
            existe=True

    while True:
        if existe == False:
            clientes.append([nombrecliente, rutcliente])
            input('CLIENTE AGREGADO A LA BASE DE DATOS. PRESIONE ENTER PARA CONTINUAR')
            break
        else:
            input('CLIENTE YA AGREGADO, POR FAVOR VUELVA A INTENTARLO.')

    #2. UBICACIONES DISPONIBLES.

def ver_asientos():
    c=1
    for i in range(len(asientos)):
        print(f'|{asientos[i].center(5)}',end='')
        if c==6:
            c=0
            print('')

    #3. LISTADO ASISTENTES.

def listado():
    paso=len(rut)
    rut.sort(reverse=False)
    print(f'NOMBRE DEL CLIENTE: {clientes}')
    print(f'RUT DEL CLIENTE: {rut}')
    input('INGRESE CUALQUIER LETRA PARA CONTINUAR')


    #4. MOSTRAR GANANCIAS TOTALES.

#def gananciastotales():


    #ganancias= tarifap + tarifag + tarifasil

    #5. SALIR

def salir():
    while True:
        print(f'CLIENTE: {clientes}')
        hoy=date.today()
        print(hoy)
        input('HASTA PRONTO, GRACIAS POR HABER ESCOGIDO NUESTROS SERVICIOS, PRESIONE CUALQUIER TECLA PARA EL MENÚ.')
    