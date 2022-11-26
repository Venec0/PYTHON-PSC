from operator import truediv
import os
clientesus=[]

while True:
    try:
      
        print("1. _.REGISTRAR CLIENTE._")
        print("2. _.SUSCRIPCIÓN DEL CLIENTE._")
        print("3. _.CONSULTAR DATOS DEL CLIENTE._")
        print("4. _.SALIR._")

        opcionmenu = int(input(" _:SELECCIONE UNA OPCIÓN DEL MENú:_ "))

                #REGISTRO:

        if opcionmenu == 1:
            existe=False
            xrun=input("INGRESE RUT SIN DÍGITO VERIFICADOR NI PUNTOS: ")

            if ("." not in xrun) and xrun.isnumeric() and (int(xrun)>=4000000 and int(xrun) <=99999999):
                print("RUN INGRESADO CORRECTAMENTE...")
            else:
                print("RUN INGRESADO INCORRECTAMENTE... ")
                break;
            nombrec=input("INGRESE SU NOMBRE COMPLETO: ")
            direc=input("INGRESE DIRECCIÓN EN LA QUE VIVE: ")
            comuna=input("INGRESE LA COMUNA EN DÓNDE VIVE: ")
            correo=input("INGRESE SU CORREO ELECTRÓNICO: ")
            if "@" in correo:
                pass
            else:
                break;
            xedad=int(input("INGRESE SU EDAD: "))
            if xedad>=0 and xedad<=110:
                pass
            else:
                break;
            genero=input("INGRESE SU GÉNERO [M] O [F]: ")
            if genero.upper() == "M" or genero.upper() == "F":
                pass
            celu=input("INGRESE SU TELÉFONO CELULAR: ")
            tipo=input("INGRESE SU TIPO DE SUSCRIPCIÓN [PREMIUM] , [GOLD] , [SILVER]: ")
            if tipo.upper() == "PREMIUM" or tipo.upper() == "GOLD" or tipo.upper() == "SILVER":
                pass
            else:
                break;

                #VERIFICAR QUE NO EXISTA:

            for cliente in clientesus:
                if xrun in cliente:
                    existe = True
            
            if existe == False:
                clientesus.append([xrun, nombrec, direc, comuna, correo, xedad, genero, celu, tipo])
                input("_.CLIENTE YA REGISTRADO, PRESIONE CUALQUIER TECLA PARA CONTINUAR._")
            else:
                input("_.CLIENTE YA EXISTENTE, POR FAVOR INTENTE CON OTRO RUN, PRESIONE CUALQUIER TECLA PARA CONTINUAR._")

            os.system("cls")

                #SUSCRIPCIÓN


        elif opcionmenu == 3:

               #CONSULTAR DATOS DEL CLIENTE

             xrun = input("INGRESE RUN CLIENTE: ")
             existe = False
               #VERIFICAR QUE NO EXISTA.

             for cliente in clientesus:
                 if xrun == cliente[0]:
                     existe = True
                     print(cliente)
                     print(f"RUN: {cliente[0]}")
                     print(f"NOMBRE COMPLETO: {cliente[1]}") 
                     print(f"DIRECCIÓN: {cliente[2]}")
                     print(f"COMUNA: {cliente[3]}")
                     print(f"CORREO ELECTRÓNICO: {cliente[4]}") 
                     print(f"EDAD: {cliente[5]}")
                     print(f"GÉNERO: {cliente[6]}")
                     print(f"CELULAR: {cliente[7]}")
                     print(f"TIPO DE SUSCRIPCIÓN: {cliente[8]}")
                     input("PRESIONE ENTER PARA CONTINUAR.")
                     os.system("cls")
             if existe == False:
                 input("CLIENTE NO EXISTE, PRESIONE CUALQUIER TECLA PARA CONTINUAR.")
                 os.system("cls")
        elif opcionmenu == 4:

              #SALIR.
            
            break;
        else:
            input("_.OPCIÓN INVÁLIDA, PRESIONE CUALQUIER TECLA PARA CONTINUAR._")  
    except:
        input("_.OPCIÓN INVÁLIDA, PRESIONE CUALQUIER TECLA PARA CONTINUAR._")
        os.system("cls")
        