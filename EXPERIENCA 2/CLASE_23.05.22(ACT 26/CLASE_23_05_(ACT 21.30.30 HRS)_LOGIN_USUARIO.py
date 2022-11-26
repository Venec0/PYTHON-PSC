import os
run=list();nombre=list();edad=list();nota=list()
alumno=[run,nombre,edad,nota]
while True:
    os.system("cls")
    print(".:MENÚ PRINCIPAL:.")
    print("1. AGREGAR. ")
    print("2. CONSULTAR POR RUN.")
    print("3. MOSTRAR TODOS.")
    print("4. ELIMINAR ALUMNO POR SU RUN.")
    print("5. SALIR.")
    op=input("INGRESE OPCIÓN.")
    if op=='1':
        while True:
            try:
                xrun=input("INGRESE RUN: ")
                if xrun in run:
                    print("RUT EXISTENTE...")
                else:
                    xnombre=input("INGRESE NOMBRE: ")
                    xedad=int(input("INGRESE EDAD: "))
                    xnota=float(input("INGRESE NOTA: "))
                    if xrun.isnumeric() and len(xrun)==2:
                        if len(xnombre)>=3 and len(xnombre)<=100:
                            if xedad>=1 and xedad<=130:
                                if xnota>=1.0 and xnota<=7.0:
                                    break;
                input("ALGÚN DATO NO CUMPLE CON LO SOLICITADO... INTÉNTELO NUEVAMENTE. ")
            except Exception as e:
                print("ALGÚN DATO ES INCORRECTO... INTÉNTELO NUEVAMENTE. ")
                print("PULSE UNA TECLA. ")
#******************************************AFUERA DEL CICLO AGREGA DATOS A LA LISTA******************************************
        run.append(xrun);nombre.append(xnombre);edad.append(xedad);nota.append(xnota)
        input("DATO INGRESADO CORRECTAMENTE, PULSE UNA TECLA PARA CONTINUAR...")
    elif op=='2':
        try:
            xrun=input("INGRESE RUN: ")
            i = run.index(xrun)
            print(f'{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}')
            input('PULSE UNA TECLA PARA CONTINUAR... ')
        except:
            input('RUN NO EXISTE EN LA LISTA. ')
    elif op=='3':
        n=len(nota)
        print('LISTA DE ALUMNOS \n ***************************')
        for i in range(n):
            print(f'{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}')
        input('PULSE UNA TECLA PARA CONTINUAR. ')
    elif op=='4':
        try:
            xrun=input("INGRESE RUN: ")
            i = run.index(xrun)
            n=len(alumno)
            for j in range(n):
                alumno[j].pop(i)
            input('PULSE UNA TECLA PARA CONTINUAR CON LA ELIMINACIÓN... ')
        except:
            input('RUN NO EXISTE EN LA LISTA. ')
    elif op=='5':
        break
    else:
        input('OPCIÓN NO VÁLIDA. PULSE UNA TECLA PARA CONTINUAR. ')