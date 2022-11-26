import os
import numpy as np
clientes=[]

asientos = np.array(range(1,43),dtype='str')
def gasientos():
    return asientos

def menu():

    #MENU PARA CLIENTE.

    os.system('cls')
    print(".-MENÚ._")
    print('1.- VER ASIENTOS DISPONIBLES: ')
    print('2.- COMPRAR ASIENTOS. ')
    print('3.- ANULAR VUELO. ')
    print('4.- MODIFICAR DATOS PASAJERO. ')
    print('5.- SALIR. ')
    return input("INGRESE OPCIÓN: ")

        
def ver_asientos():
    c=1
    for i in range(len(asientos)):
        print(f'|{asientos[i].center(5)}',end='')
        if c==6:
            c=0
            print('')

def compra():

    #REGISTRO Y COMPRA DE ASIENTOS DEL CLIENTE.
    tarifa=79000
    descuento = 0
    existe=False
    nombrePasaj=input('INGRESE NOMBRE DEL PASAJERO: ')
    rutPasaj=input('INGRESE RUT DE PASAJERO: ')
    fonoPasaj=input('INGRESE FONO DEL PASAJERO: ')
    print('1. Banco Santander.')
    print('2. Banco Estado.')
    print('3. Banco Duoc.')
    bancoPasaj=input('INGRESE SU BANCO DE PREFERENCIA: ')
    num=input('INGRESE NÚMERO DEL ASIENTO: ')
    
    
    #VERIFICAR QUE NO EXISTA.
    
    for cliente in clientes:
        if rutPasaj in cliente:
            existe = True
        
    if existe == False:
        clientes.append([nombrePasaj, rutPasaj, fonoPasaj, bancoPasaj])
        print('CLIENTE AGREGADO A LA BASE DE DATOS. PRESIONE CUALQUIER TECLA PARA CONTINUAR.')
    else:
        input('CLIENTE YA AGREGADO, POR FAVOR VUELVA A INTENTARLO.')

        
    if num in asientos:
        i=int(num)-1
        asientos[i]='x'
        #CONVERTIR NUM EN INTEGER EN LA MISMA LÍNEA DE CÓDIGO, SINO NO EVALÚA.
        if int(num) >= 31 and int(num) <= 41:
            print('ASIENTO CLIENTE VIP SELECCIONADO. ')
            input("espera")
            tarifa = 240000
        if bancoPasaj == '4':
            print('DESCUENTO DEL 15% APLICADO.')
            descuento = 0.15
        print(f'TOTAL A PAGAR CON DESCUENTO BANCODUOC: {tarifa-(tarifa*descuento)}')
        
    else:
        print('ASIENTO NO DISPONIBLE O NO EXISTE, INTÉNTELO DE NUEVO.')

def modificar():
    print(clientes)

    #MODIFICACIÓN DE DATOS.

    existe=False

    rutPasaj=input('INGRESE EL RUT CON EL QUE SE REGISTRÓ.')
    fonoPasaj=input('INGRESE EL FONO CON EL QUE SE REGISTRÓ')

    #VERIFICAR QUE NO EXISTA.

    for indice, cliente in enumerate(clientes):
        if rutPasaj == cliente[1]:
            existe=True
            print(f'CLIENTE ENCONTRADO: {cliente[1]}')
            print('¿QUÉ OPCIÓN DESEA MODIFICAR?')
            print('1. NOMBRE DEL PASAJERO.')
            print('2. FONO DEL PASAJERO.')
            nombrePasaj=input('INGRESE EL NOMBRE A ACTUALIZAR: ')
            fonoPasaj=int(input('INGRESE EL FONO A ACTUALIZAR: '))
            clientes[indice][0] = nombrePasaj
            clientes[indice][2] = fonoPasaj

            input('DATOS ACTUALIZADOS CORRECTAMENTE.')
            os.system('cls')
    if existe == False:
        input('CLIENTE NO EXISTE. PRESIONE CUALQUIER TECLA PARA CONTINUAR.')
        os.system('cls')