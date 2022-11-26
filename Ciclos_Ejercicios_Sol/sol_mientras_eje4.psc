Proceso sin_titulo
	//4) Obtener el promedio de calificaciones de un grupo de n alumnos. 
	//(cada alumno tiene una cantidad distinta de calificaciones)
	op=1;
	ca=0; //contador alumno
	cc=1; //contador curso
	aa=0; //acumulador por alumno
	ac=0; //acumulador curso
	i=0
	Mientras op=1 Hacer
		escribir sin saltar "Ingrese cantidad de notas del alumno :",cc,":"
		leer n
		aa=0
		para i=1 hasta n Hacer
			escribir sin saltar "Ingrese nota ",i,":"
			leer nota
			aa=aa+nota
		FinPara
		pa=aa/n
		escribir "El promedio del alumno es:",pa
		ac=ac+pa
		Escribir sin saltar "Ingrese 1 para continuar, otra tecla para salir:"
		leer op
		si op=1 Entonces
			cc=cc+1
		FinSi		
	FinMientras
	Escribir "El Promedio del curso es:",ac/cc
	
FinProceso
