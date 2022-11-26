import os
import PRUEBA_EXP_3_2own_func as fn

    #MENÚ.

while True:
    op=fn.menuvehiculos()
    if op == '1':
        fn.registrarvehiculos()
    if op == '2':
        fn.buscarvehiculos()
    if op == '3':
        fn.impresioncertificadoauto()
    if op == '4':
        print("HASTA PRONTO.")
        break