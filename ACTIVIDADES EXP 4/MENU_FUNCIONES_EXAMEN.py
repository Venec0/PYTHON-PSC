import os
import FUNCIONES_EXAMEN as fn
import numpy as np

while True:
    op=fn.menu()

    #MENÚ:
    if op=='1':
        fn.compra()
    
    if op =='2':
        fn.ver_asientos()

    if op == '3':
        fn.listado()
    
    #if op == '4':
        #fn.gananciastotales()

    if op == '5':
        fn.salir()