from datetime import date
import os
vehiculosus=[]

while True:
    try:
      
        print("1. _.REGISTRAR VEHÍCULO._")
        print("2. _.REGISTRAR MANTENIMIENTO._")
        print("3. _.CONSULTAR DATOS DEL VEHÍCULO._")
        print("4. _.SALIR._")

        opcionmenu = int(input(" _:SELECCIONE UNA OPCIÓN DEL MENú:_ "))

                #REGISTRO:

        if opcionmenu == 1:
            existe=False
            i_patente=input("INGRESE PATENTE DEL VEHÍCULO (FORMATO: AA1000 o BBBB10): ")
            if "AA" in i_patente or "BBBB" in i_patente:
                print("PATENTE INGRESADO CORRECTAMENTE...")
            else:
                print("PATENTE INGRESADO INCORRECTAMENTE... ")
                break
            i_marca=input("INGRESE MARCA DEL VEHÍCULO: ")
            i_modelo=input("INGRESE MODELO DEL VEHÍCULO: ")
            i_aniofabrica=int(input("INGRESE EL AÑO DE FABRICACIÓN (ENTRE 1900 A 2021): "))
            if i_aniofabrica>=1900 and i_aniofabrica<=2021:
                pass
            else:
                print("AÑO INGRESADO NO CORRESPONDIENTE")
                break
            i_tipoveh=input("INGRESE EL TIPO DE VEHÍCULO (D/B/E/H): ")
            if i_tipoveh.upper() =="D" or i_tipoveh.upper() == "B" or i_tipoveh.upper() == "E" or i_tipoveh.upper() == "H":
                pass
            else:
                print(i_tipoveh)
                break


            i_registros = []

                #VERIFICAR QUE NO EXISTA:

            for vehiculo in vehiculosus:
                if i_patente == vehiculo[0]:
                    existe = True
            
            if existe == False:
                vehiculosus.append([i_patente, i_marca, i_modelo, i_aniofabrica, i_tipoveh, i_registros])
                input("_.VEHÍCULO REGISTRADO CORRECTAMENTE, PRESIONE ENTER._")
            else:
                input("_.VEHÍCULO YA INGRESADO, INTÉNTELO DE NUEVO._")

            os.system("cls")

                #SUSCRIPCIÓN

        elif opcionmenu == 2:

            i_patente = input("INGRESE PATENTE VEHÍCULO: ")
            existe = False
               #VERIFICAR QUE NO EXISTA.

            for vehiculo in vehiculosus:
                if i_patente == vehiculo[0]:
                    i_observaciones=input("INGRESE COMENTARIO DEL VEHÍCULO: ")
                    i_fechareg = date.today()
                    print("OBSERVACIONES INGRESADAS CORRECTAMENTE.") 
                    vehiculo[5].append(i_observaciones, i_fechareg)
                os.system("cls")

        elif opcionmenu == 3:

               #CONSULTAR DATOS DEL CLIENTE

             i_patente = input("INGRESE PATENTE VEHÍCULO: ")
             existe = False
               #VERIFICAR QUE NO EXISTA.

             for vehiculo in vehiculosus:
                 if i_patente == vehiculo[0]:
                     existe = True
                     print(vehiculo)
                     print(f"PATENTE: {vehiculo[0]}")
                     print(f"MARCA {vehiculo[1]}") 
                     print(f"MODELO {vehiculo[2]}")
                     print(f"AÑO DE FÁBRICA {vehiculo[3]}")
                     print(f"TIPO DE VEHÍCULO {vehiculo[4]}")
                     if vehiculo[4] == "B": 
                        print("TIPO DE VEHÍCULO BENCINA")
                     elif vehiculo[4] == "D":
                        print("TIPO DE VEHÍCULO DIESEL")
                     elif vehiculo[4] == "E": 
                        print("TIPO DE VEHÍCULO ELÉCTRICO")
                     else:
                         print("TIPO DE VEHÍCULO HÍBRIDO")
                     for registros in vehiculo[5]:
                        print(f"OBSERVACIONES: {registros[0]}")
                        print(f"FECHA {registros[1]}")
                     input("PRESIONE ENTER PARA CONTINUAR.")
                     os.system("cls")
             if existe == False:
                 input("CLIENTE NO EXISTE, PRESIONE CUALQUIER TECLA PARA CONTINUAR.")
                 os.system("cls")
        elif opcionmenu == 4:

              #SALIR.
            
            break
        else:
            input("_.OPCIÓN INVÁLIDA, PRESIONE CUALQUIER TECLA PARA CONTINUAR._")  
    except:
        input("_.OPCIÓN INVÁLIDA, PRESIONE CUALQUIER TECLA PARA CONTINUAR._")
        os.system("cls")
        