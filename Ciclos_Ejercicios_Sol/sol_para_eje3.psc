Proceso sin_titulo	
	para i = 1 hasta 10 Hacer
		escribir "INGRESE NIVEL DE CONTAMINACION CAMION N°:",i
		leer nc
		si i=1 Entonces
			alto=nc;bajo=nc			
		FinSi
		si nc<=bajo Entonces
			bajo=nc
		FinSi
		si nc >= alto Entonces
			alto=nc	
		FinSi		
	FinPara
	escribir "El Nivel de contaminación más bajo fue de :",bajo
	escribir "El Nivel de contaminación más alto fue de :",alto
FinProceso
