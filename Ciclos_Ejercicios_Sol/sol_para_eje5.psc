Algoritmo sin_titulo		
	escribir "INGRESE TIPO DE ANIMAL";
	escribir "1 ) elefante  2) Jirafa  3) Chimpance";
	leer ta
	si ta=1 entonces 
		n=20		
	FinSi
	
	si ta=2 entonces 
		n=15		
	FinSi
	si ta=1 entonces 
		n=40		
	FinSi
	
	cc1=0;cc2=0;cc3=0
	para i=1 hasta n Hacer
		escribir "INGRESE EDAD DEL ANIMAL"
		leer edad 
		si edad>=3 entonces
			cc3=cc3+1
		FinSi
		si edad>1 y edad<3 entonces
			cc2=cc2+1
		FinSi
		si edad<=1 Entonces
			cc1=cc+1
		FinSi			
	FinPara
	t=cc1+cc2+cc3
	pc1=cc1/t*100
	pc2=cc2/t*100
	pc3=cc3/t*100
	escribir "porcentaje c1 ",pc1
	escribir "porcentaje c2 ",pc2
	escribir "porcentaje c3 ",pc3

	
FinAlgoritmo
