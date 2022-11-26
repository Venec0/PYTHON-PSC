import random
import numpy as np

patenteveh=[];marcavehis=[];preciovehis=[];dueniosvehis=[];tipo=[];rfechavehis=[];robs=[];registrosvehis=[];vehiculos=[]
#FUNCION MENÚ
def menuAuto():
    print("Seleccione una Opcion \n1)Registrar Automovil\n2)Buscar Automovil\n3)Imprimir Certificados\n4)Salir\n")

    #REGISTRO VEHÍCULO:

def registrarauto():
    while True:
        patentevehveh=input('INGRESE LA PATENTE: \n')
        if len(patenteveh) == 6 and patenteveh[0:4].isalpha() and patenteveh[4:5].isnumeric():
            patenteveh.append(patenteveh)
            break
        else:
            input("INGRESE UNA PATENTE VÁLIDA, INTÉNTELO DE NUEVO.")
            break
    while True:        
        marcaveh=input('Ingrese marcaveh: \n')
        if len(marcaveh)>=2 and len(marcaveh)<=15:
            marcavehis.append(marcaveh)
            break
        else:
            input("Ingrese una marcaveh valida, enter para continuar")
    while True:        
        precioveh=int(input('INGRESE PRECIO DEL VEHÍCULO: \n'))
        precioveh=int(precioveh)
        if  precioveh>1000000:
            preciovehis.append(precioveh)
            break
        else:
            input("INGRESE UN PRECIO VÁLIDO, INTÉNTELO DE NUEVO.")
            break
    while True:
        duenho=input('Ingrese dueño del vehiculo (nombre y apellido): \n')
        if duenho != "":
            dueniosvehis.append(duenho)
            break
        else:
            input("INGRESE UN DUEÑO VÁLIDO, INTÉNTELO DE NUEVO.")     
            break
    input("Registro Realizado!, Enter para volver al menu")
vehiculos = [patenteveh,marcavehis,preciovehis,dueniosvehis]

    #BÚSQUEDA:

def buscarauto():
    busqueda=input("INGRESE LA PATENTE REGISTRADA: \n")
    if patenteveh.count(busqueda)>0:
        i = patenteveh.index(busqueda)
        print(f'{vehiculos[0][i]}\t{vehiculos[1][i]}\t{vehiculos[2][i]}\t{vehiculos[3][i]}')
        input("\nENTER PARA VOLVER AL MENU!")
    elif busqueda=="":
        input("NO HA INGRESADO NINGÚN DATO, ENTER PARA VOLVER AL MENU!!!")
    else:
        input("PATENTE NO REGISTRADA, POR FAVOR REGISTRE PRIMERO, ENTER PARA VOLVER AL MENU.")    

#IMPRESIÓN CERTIFICADOS:

def certificadoAuto():
    encuentra=input("INGRESE PATENTE REGISTRADA PARA VALIDAR CERTIFICADOS: \n")
    if patenteveh.count(encuentra)>0:
        print("La patenteveh se ha encontrado")
        option=input("1) EMISIÓN DE CONTAMINANTES \n2) ANOTACIONES VIGENTES \n3) MULTAS\n")
        if option == "1":
            i = patenteveh.index(encuentra)
            print("EMISIÓN CONTAMINANTES")
            print(f'{vehiculos[0][i]}\t\t{vehiculos[3][i]}', '\tvalor del certificado:',random.randrange(1500, 3500))
            input("\nENTER PARA VOLVER AL MENÚ!")
        elif option== "2":
            i = patenteveh.index(encuentra)
            print("EMISIÓN ANOTACIONES VIGENTES")
            print(f'{vehiculos[0][i]}\t\t{vehiculos[3][i]}', 'valor del certificado:',random.randrange(1500, 3500))
            input("\nENTER PARA VOLVER AL MENU!")
        elif option =="3":
            i = patenteveh.index(encuentra)
            print("EMISIÓN DE MULTAS")
            print(f'{vehiculos[0][i]}\t\t{vehiculos[3][i]}', '\tvalor del certificado:',random.randrange(1500, 3500))
            input("\nENTER PARA VOLVER AL MENU!")
    else: 
        input("PATENTE INVÁLIDA. INTÉNTELO DE NUEVO.")