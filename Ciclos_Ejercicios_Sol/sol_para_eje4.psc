Proceso sin_titulo
	ct=0;at=0
	para i=1 hasta 5 Hacer
		escribir "Ingrese tiempo para el día :",i
		leer t
		si t>16 Entonces
			ct=ct+1 //contador 
		FinSi
		at=at+t //acumulador de tiempo
	FinPara
	apto='NO'
	si (at/5)<=15 Entonces  //promedio menor o igual a 15
		apto='SI'
	FinSi
	si ct<=1 Entonces
		apto='SI'  // solo 1 supera los 16 minutos
	FinSi
	escribir "El Atleta ",apto, " es apto para la prueba"
FinProceso
