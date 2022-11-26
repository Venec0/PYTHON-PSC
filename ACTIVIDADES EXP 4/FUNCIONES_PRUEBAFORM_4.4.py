import os
import FUNCIONES as fn
import numpy as np

while True:
    op=fn.menu()
    if op=='1':
        fn.ver_asientos()
    if op=='2':
        fn.compra()
    #if op=='3':
    if op=='4':
        fn.modificar()
        