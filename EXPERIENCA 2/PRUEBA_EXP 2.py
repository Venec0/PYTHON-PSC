listaVehiculos=[]
while True:
    try:
        system=("cls")
        print("1. registrar vehiculo")
        print("2. consultar vehiculo")
        print("3. actualizar vehiculo")
        print("4. salir")
        opcion = int(input("ingrese una opcion del menu: "))

        if opcion == 1:
            #comienza registro
            marca = input("Ingrese marca del vehiculo: ")
            modelo = input("Ingrese modelo del vehiculo: ")
            ano = int(input("Ingrese año del vehiculo: "))
            if ano>=1989 and ano<=2021:
                pass
            else:
                print("AÑO INCORRECTO INTENTE DE NUEVO.")

            propietario = input("Ingrese propietario del vehiculo: ")
            patente = input("Ingrese patente del vehiculo: ")
            tipoveh = input("Ingrese el tipo de vehículo teniendo en cuenta las letras: b, d, e y h. ")
            if tipoveh.lower() == "b" or tipoveh.lower() == "d" or tipoveh.lower() == "e" or tipoveh.lower() == "h":
                pass
            else:
                print("Ingrese un tipo de vehículo correcto. Vuelva a intentarlo.")
                break;

            listaVehiculos.append([marca, modelo, ano, propietario, patente])
            input("Vehiculo registrado correctamente, presione cualquier tecla para continuar...")
            break

        elif opcion == 2:
            system("cls")
            #consultar por patente
            existe = False
            patente = input("Ingrese patente a consultar: ")
            for vehiculo in listaVehiculos:
                if vehiculo[4] == patente:
                    existe = True
                    print(vehiculo)
                    input("Vehiculo encotrado, presione cualquier tecla para continuar...")

            if existe == False:
                input("vehiculo no encontrado, presione cualquier tecla para continuar...")        
        
        elif opcion == 3:
            system("cls")
            #actualizar por patente
            existe = False
            patente = input("Ingrese patente a actualizar: ")
            for vehiculo in listaVehiculos:
                if vehiculo[4] == patente:
                    existe = True
                    licenciaConducir = input("Ingrese año de permiso de conducir: ")
                    vehiculo.append(licenciaConducir)
                    input("Vehiculo actualizado correctamente, presione cualquier tecla para continuar...")
                    if not existe:
                        print("Patente no esta registrado.")
        
        elif opcion == 4:
            system("cls")

            for vehiculo in listaVehiculos:
                print("---------")
                for indice, dato in enumerate(vehiculo):
                    print(f"{vehiculo[indice]}")


            input("Presione cualquier tecla para continuar...")
        elif opcion == 5:
            system("cls")
            break
        else:
            system("cls")
            input("Opcion invalida, presione cualquier tecla e intente de nuevo")
    except:
        input("Opción inválida, presione cualquier tecla para intentarlo de nuevo.")