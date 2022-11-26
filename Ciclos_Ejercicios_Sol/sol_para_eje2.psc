Proceso EP2
	//en este ejercicio para agilizar el proceso de prueba, los datos 
	//de entrada serán generados de forma aleatoria 
	//se declaran contadores para cada categoria
	cni=0;cjo=0;cad=0;can=0;
	ani=0;ajo=0;aad=0;aan=0;
	n=50
	para i=1 hasta n Hacer
		Escribir sin saltar "EDAD :"; 
		edad = Aleatorio(1,100);
		escribir edad
		Escribir Sin Saltar "Peso :"; 
		peso = Aleatorio(1.0,200.0); 
		escribir peso
		si edad>=0 y edad<=10 Entonces
			cni=cni+1;ani=ani+edad;
		FinSi		
		si edad>=11 y edad<=39 Entonces
			cjo=cjo+1;ajo=ajo+edad;
		FinSi		
		si edad>=40 y edad<=69 Entonces
			cad=cad+1;aad=aad+edad;
		FinSi
		si edad>=70 Entonces
			can=can+1;aan=aan+edad;
		FinSi		
	FinPara
	Escribir "el promedio de edad niños es....:",redon((ani/cni*10))/10
	Escribir "el promedio de edad jovenes es..:",redon((ajo/cjo*10))/10
	Escribir "el promedio de edad adultos es..:",redon((aad/cad*10))/10
	Escribir "el promedio de edad ancianos es.:",redon((aan/can*10))/10
	
FinProceso
