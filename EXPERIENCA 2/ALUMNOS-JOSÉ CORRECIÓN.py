from os import system
alumnos = []

while True:
    try:
        print("1-> Agregar alumno")
        print("2-> Consultar alumno")
        print("3-> Eliminar alumno")
        print("4-> Actualizar alumno")
        print("5-> Listar alumno")
        print("6-> Salir")
        opcionMenu = int(input("Seleccione una opcion del menu: "))

    
        if opcionMenu == 1:
            #Registro
            existe = False
            run = input("Ingrese RUN del alumno: ")
            nombre = input("Ingrese nombre del alumno: ")
            edad = int(input("Ingrese edad del alumno: "))
            nota = int(input("Ingrese nota del alumno: "))
            
            #Verifico que no exista
            for alumno in alumnos:
                if run in alumno:
                    existe = True

            if existe == False:
                alumnos.append([run, nombre, edad, nota])
                input("Alumno agregado, presione cualquier tecla para continuar...")
            else:
                input("Alumno ya existe por favor intente con otro RUN, presione cualquier tecla para continuar...")

            system("cls")

        elif opcionMenu == 2:
            #Consulta
            run = input("Ingrese RUN del alumno: ")
            existe = False
            #Verifico que no exista
            for alumno in alumnos:
                if run == alumno[0]:
                    existe = True
                    print(f"Alumno encontrado: {alumno[1]}")
                    print(alumno)
                    input("Presione cualquier tecla para continuar...")
                    system("cls")
            if existe == False:
                input("Alumno no existe, presione cualquier tecla para continuar...")
                system("cls")

        elif opcionMenu == 3:
            #Elimina
            run = input("Ingrese RUN del alumno: ")
            existe = False
            #Verifico que no exista
            for alumno in alumnos:
                if run == alumno[0]:
                    existe = True
                    print(f"Alumno encontrado: {alumno[1]}")
                    alumnos.remove(alumno)
                    input("Alumno eliminado, presione cualquier tecla para continuar...")
                    system("cls")
            if existe == False:
                input("Alumno no existe, presione cualquier tecla para continuar...")
                system("cls")
        elif opcionMenu == 4:
            #Modifica
            run = input("Ingrese RUN del alumno: ")
            existe = False
            #Verifico que no exista
            for indice, alumno in enumerate(alumnos):
                if run == alumno[0]:
                    existe = True
                    print(f"Alumno encontrado: {alumno[1]}")
                    nombre = input("Ingrese nombre a actualizar: ")
                    edad = int(input("Ingrese edad a actualizar: "))
                    nota = int(input("Ingrese nota a actualizar: "))
                    alumnos[indice] = [run, nombre, edad, nota]
                    input("Datos de alumno actualizado, presione cualquier tecla para continuar...")
                    system("cls")
            if existe == False:
                input("Alumno no existe, presione cualquier tecla para continuar...")
                system("cls")
        elif opcionMenu == 5:
            print(" ----- LISTA DE ALUMNOS --------")
            for alumno in alumnos:
                print(alumno)
            input("Presione cualquier tecla para continuar...")
            system("cls")
        elif opcionMenu == 6:
            break
        else:
            input("Opcion invalida, presione cualquier tecla para continuar...")
            system("cls")
    except:
        input("Opcion invalida, presione cualquier tecla para continuar...")
        system("cls")