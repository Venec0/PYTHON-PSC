import os
listaVehiculos=[]
while True:
    try:

        print("1. registrar vehiculo")
        print("2. registro mantenimiento")
        print("3. consultar vehículo")
        print("4. salir")

        opcion = int(input("ingrese una opcion del menu: "))

        #REGISTRO

        if opcion == 1:
                marca = input("Ingrese marca del vehiculo: ")
                modelo = input("Ingrese modelo del vehiculo: ")
                ano = int(input("Ingrese año del vehiculo: "))
                if ano>=1900 and ano<=2021:
                    pass
                else:
                    print("AÑO INCORRECTO INTENTE DE NUEVO.")

                propietario = input("Ingrese propietario del vehiculo: ")
                patente = input("Ingrese patente del vehiculo: ")
                tipoveh = input("Ingrese el tipo de vehículo teniendo en cuenta las letras: b, d, e y h. ")
                if tipoveh.lower() == "b" or tipoveh.lower() == "d" or tipoveh.lower() == "e" or tipoveh.lower() == "h":
                    pass
                else:
                    break

                    #VERIFICAR QUE NO EXISTA
                for vehiculos in listaVehiculos:
                    if patente in vehiculos:
                        existe = True
                if existe == False:
                    listaVehiculos.append([patente, marca, modelo, tipoveh, ano, propietario])
                    input("Vehiculo registrado correctamente, presione cualquier tecla para continuar...")

                else:
                    input("PATENTE CON VEHÍCULO YA REGISTRADA.")

        elif opcion == 2:
                patente=input("Ingrese la patente del vehículo: ")
                existe = False
                fechaman=int(input("Ingrese la fecha para la cita de mantenimiento, use: dd/mm/aa. "))
                observaman=input("Ingrese las observaciones para el mecánico: ")
                registros= fechaman + observaman
                if existe == False:
                    print("Patente no existente, inténtelo nuevamente.")
                    os.system("cls")

        elif opcion == 3:
            print("Ingrese la patente del vehículo: ")
            existe = False
            for vehiculos in listaVehiculos:
                if patente == vehiculos[0]:
                    existe = True
                    print(f"PATENTE: {vehiculos[0]}")
                    print(f"MARCA: {vehiculos[1]}")
                    print(f"MODELO: {vehiculos[2]}")
                    print(f"TIPO DE VEHÍCULO: {vehiculos[3]}")
                    print(f"AÑO DEL VEHÍCULO: {vehiculos[4]}")
                    print(f"PROPIETARIO DEL VEHÍCULO: {vehiculos[5]}")
                    print("PRESIONE ENTER PARA CONTINUAR.")
                    os.system("cls")
            if existe == False:
                input("PATENTE DE VEHÍCULO NO EXISTENTE, INTÉNTELO DE NUEVO. ") 
        elif opcion == 4:
            os.system("cls")  
            break;
           
    except:
        input("Opción inválida, presione cualquier tecla para intentarlo de nuevo.")