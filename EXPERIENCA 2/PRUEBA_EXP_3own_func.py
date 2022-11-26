import random
import numpy as np
import os
vehiculos=[];marcavehis=[];patentevehis=[];preciovehis=[];dueniovehis=[]

    #MENÚ.

def menuvehiculos():


    os.system('cls')
    print("_.MENÚ._")
    print('1. REGISTRAR VEHÍCULO. ')
    print('2. BUSCAR VEHÍCULO. ')
    print('3. IMPRIMIR CERTIFICADOS.')
    print('4. SALIR.')
    return input("INGRESE OPCIÓN.")

    #REGISTRO.

def registrarvehiculos():
    while True:
        patenteveh=input("INGRESE LA PATENTE: ")
        if len(patenteveh) == 6 and patenteveh[0:4].isalpha() and patenteveh [4:5].isnumeric():
            patentevehis.append(patenteveh)
        else:
            print("INGRESE UNA PATENTE VÁLIDA. INTÉNTELO DE NUEVO.")

    while True:
        marcaveh=("INGRESE LA MARCA DEL VEHÍCULO: ")
        if len(marcaveh)>=2 and len(marcaveh)<=15:
            marcavehis.append
        else:
            print("INGRESE UNA MARCA DE VEHÍCULO VÁLIDA.")
            
    while True:
        precioveh=int(input('INGRESE PRECIO DEL VEHÍCULO: '))
        if precioveh>100000000:
            preciovehis.append(precioveh)
            print("PRECIO DEL VEHÍCULO INGRESADO CORRECTAMENTE.")
        else:
            print("EL PRECIO DEBE SER MAYOR A $1.000.000 MILLONES DE PESOS, INTÉNTELO NUEVAMENTE.")
    duenio=input("INGRESE NOMBRE DEL DUEÑO: ")
    dueniovehis.append(duenio)

    input("REGISTRO FINALIZADO, PRESIONE ENTER PARA CONTINUAR.")
    
    #FIN REGISTRO.

    #BÚSQUEDA AUTO.

def buscarvehiculos():
    busqueda=input('INGRESE LA PATENTE REGISTRADA: ')
    if patentevehis.count(busqueda)>0:
        i = patentevehis.index(busqueda)
        print(f"PATENTE DEL VEHÍCULO: {vehiculos[0][i]}")
        print(f"MARCA DEL VEHÍCULO: {vehiculos[1][i]}")
        print(f"PRECIO DEL VEHÍCULO: {vehiculos[2][i]}")
        print(f"DUEÑO DEL VEHÍCULO: {vehiculos[3][i]}")
        input("PRESIONE ENTER PARA VOLVER AL MENÚ.")
    elif busqueda=="":
        print("NO HA INGRESADO NINGÚN DATO, VUELVA A INTENTARLO.")
    
    else:
        print("VEHÍCULO NO REGISTRADO, VUELVA A INTENTARLO.")

    
    #IMPRESIÓN CERTIFICADOS.

def impresioncertificadoauto():
    certificado=input("INGRESE LA PATENTE REGISTRADA EN EL SISTEMA: ")
    if patentevehis.count(certificado)>0:

        print("PATENTE ENCONTRADA.")
        print("1. EMISIÓN DE CONTAMINANTES.")
        print("2. ANOTACIONES VIGENTES.")
        print("3. MULTAS")
        opcion=input("INGRESE OPCIÓN A IMPRIMIR.")

        if opcion == '1':
            i = patentevehis.index(certificado)
            print("EMISIÓN DE CONTAMINANTES.")
            print(f'{vehiculos[0][i]}{vehiculos[3][i]}')
            print("VALOR DEL CERTIFICADO: ",random.randrange(1500,3500))

        if opcion == '2':
            i = patentevehis.index(certificado)
            print("EMISIÓN DE ANOTACIONES VIGENTES.")
            print(f'{vehiculos[0][i]}{vehiculos[3][i]}')
            print("VALOR DEL CERTIFICADO: ",random.randrange(1500,3500))

        if opcion == '3':
            i = patentevehis.index(certificado)
            print("EMISIÓN DE MULTAS.")
            print(f'{vehiculos[0][i]}{vehiculos[3][i]}')
            print("VALOR DEL CERTIFICADO: ",random.randrange(1500,3500))