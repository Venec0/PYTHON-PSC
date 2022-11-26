Proceso  sin_titulo
	//SE DESEA CREAR UN SISTEMA COMPUTACIONAL PARA UN ESTACIONAMIENTO, EL CUAL COBRA SEGÚN EL TIPO DE VEHÍCULO (autos, camionetas, motos, camiones y buses)
	//Y LAS TARIFAS POR MINUTOS (NORMAL Y PUNTA) (DATOS INGRESADOS Y SOLICITADOS POR PANTALLA)
	Definir total, tipo_vehículo, tipo_tarifa, minutos Como Entero;
	Definir tipo_veh_tarifa, tipo_veh Como Caracter 
	Escribir "..................................................................."
	Escribir "Ingresa el tipo de vehículo: " 
	Escribir "1: Motocicleta"
	Escribir "2: Camión_bus"
	Escribir "3: Auto_camioneta"
	Escribir "..................................................................."
	Leer tipo_vehículo
	Escribir "Ingresa los minutos transcurridos: "
	Leer minutos
	Escribir "..................................................................."
	Escribir "Ingresa el tipo de tarifa"
	Leer tipo_tarifa
	Escribir "..................................................................."
	total=0
	Segun  tipo_veh Hacer
		A:
			tipo_veh="Motocicleta" 
			SI tipo_tarifa=1 Entonces
				total=minutos+300
				tipo_veh_tarifa="normal"
			FinSi
			Si tipo_tarifa=2 Entonces
				total=minutos+600
				tipo_veh_tarifa="punta"
			FinSi
		B:
			
			tipo_veh="Camión_Bus" 
			Si tipo_tarifa=1 Entonces
				total=minutos+900
				tipo_veh_tarifa="normal"
			FinSi
			Si tipo_tarifa=2 Entonces
				total=minutos+1800
				tipo_veh_tarifa="punta"
			FinSi
		C:
			
			tipo_veh="Auto_camioneta" 
			SI tipo_tarifa=1 Entonces
				total=minutos+3000
				tipo_veh_tarifa="normal"
			FinSi
			Si tipo_tarifa=2 Entonces
				total=minutos+5400
				tipo_veh_tarifa="punta"
			FinSi
    FinSegun
	Limpiar Pantalla
	Escribir "..................................................................."
	Escribir "Tipo de vehículo: ", tipo_vehículo," - " tipo_veh;
	Escribir "Tipo Tarifa: ", tipo_veh_tarifa
	Escribir "Minutos transcurridos: ", minutos
	Escribir "Total a pagar: ", total
	Escribir "..................................................................."
FinProceso