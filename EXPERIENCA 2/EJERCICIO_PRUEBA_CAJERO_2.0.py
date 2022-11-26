class Banco():
    def __init__(self):
        self.dinero = 0
    
    def deposito(self):
        cantidad = int(input('Ingresa la cantidad a depositar: '))
        self.dinero = cantidad + self.dinero
        print(f'{cantidad} clp depositados en tu cuenta bancaria ')

    def retiro(self):
        retiro = int(input('Ingresa la cantidad a retirar: '))
        self.dinero = self.dinero - retiro
        print(f'{retiro} clp retirados exitosamente de tu cuenta bancaria ')

    def balance(self):
        print(f'{self.dinero} clp disponibles en tu cuenta bancaria ')
        
banco = Banco()



dineroAdmin=0
dineroJose=0
resp=''

while  True :
    usuario = str(input('ingresa tu usuario: '))
    pin = int(input('ingresa tu pin de 4 digitos: '))

    if usuario == 'admin' and pin == 0000:
        continuarOperacion =1
        print('bienvenido administrador')
        banco.dinero=dineroAdmin
        
        while continuarOperacion == 1:
            print("""
            
            Selecciona que operacion deseas realizar:
                
            1.Deposito
            2.Retiro
            3.Consultar Balance
            
            """)
            
            opcion = int(input('ingresa el numero de tu elección: '))
            
            if opcion == 1:
                banco.deposito()
            elif opcion == 2:
                banco.retiro()
            elif opcion == 3:
                banco.balance()
            else:
                print('opción invalida')
            
            #agg loop de salida con while
            continuarOperacion = int(input('desea relizar otra operación? \n ingresa 1 para continuar ó 0 para salir: '))
    
        dineroAdmin=banco.dinero


    elif usuario == 'jose' and pin == 1234:
        continuarOperacion =1
        print('bienvenido jose')
        banco.dinero=dineroJose

        while continuarOperacion == 1:

            print("""
            
            Selecciona que operacion deseas realizar:
                
            1.Deposito
            2.Retiro
            3.Consultar Balance
            
            """)
            
            opcion = int(input('ingresa el numero de tu elección: '))
            
            if opcion == 1:
                banco.deposito()
            elif opcion == 2:
                banco.retiro()
            elif opcion == 3:
                banco.balance()
            else:
                print('opción invalida')
            
            #agg loop de salida con while
            continuarOperacion = int(input('desea relizar otra operación? \n ingresa 1 para continuar ó 0 para salir: '))

        dineroJose=banco.dinero
    else: 
        print('Usuario o contraseña invalida.')

while resp == 'S' or 's' or 'n' or 'N':
                resp = input('desea relizar otra operación? \n ingresa S para continuar ó N para salir: ')
                if resp == 'S' or 's':
                    continuarOperacion = 0
                    resp=''
                elif resp == 'n' or 'N':
                    continuarOperacion = 1
                    resp=''
                else:
                    print('Ingresa un valor valido.')