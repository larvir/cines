from __future__ import annotations
from dataclasses import dataclass
import datetime as dt
import os
import platform
import pickle
import lara as l
import joan as j
import clases_generals as cg





#==========================================================================================================
# Menú principal.
#==========================================================================================================
def mostra_menu() -> None:
    '''Mostra el menú principal. El primer punt no està implementat. Per a simplificar assumirem
    que tenim 2 cines amb dos sales cadascuna.'''
    while True:
        cg.cls('- MENÚ PRINCIPAL -')
        print('------------------')
        print('1- Cines i sales (no implementat)')
        print('2- Manteniment de pel·lícules')
        print('3- Manteniment sessions i reserves')
        print('4- Reservar una pel·lícula')
        print()

        try:
            opc = cg.input_type('Opció?', intro_cancellar=False)
            if opc=='1':
                pass                            # Opció no implementada
            elif opc=='2':
                l.menu_pel_licules()
            elif opc=='3':
                cine = j.selecciona_cine()
                if cine:
                    j.manteniment_sessions(cine)
            elif opc=='4':
                j.reserva_pel_licula()
        except cg.input_type_cancel·lat:
            continue

#==========================================================================================================
# Per a simplificar el programa, assumirem que els cines amb les sales estan creats.
        
# p1 = cg.Pel_licula('La guerra de les galaxies')
# p2 = cg.Pel_licula('Jocs de guerra')
# p3 = cg.Pel_licula('Encontres en la 3a fase')
# p4 = cg.Pel_licula('Indiana Jones')

# cg.pel_licules.append(p1)
# cg.pel_licules.append(p2)
# cg.pel_licules.append(p3)
# cg.pel_licules.append(p4)

# c1 = cg.Cine('La salera')
# c2 = cg.Cine('Estepark')
# cg.cines.append(c1)
# cg.cines.append(c2)

# sala1_1 = cg.Sala(c1, 'sala 1', 4, 4)
# sala2_1 = cg.Sala(c1, 'sala 2', 5, 5)
# sala1_2 = cg.Sala(c2, 'sala 1', 4, 4)
# sala2_2 = cg.Sala(c2, 'sala 2', 5, 5)

# data1= dt.datetime(2024, 1, 1, 16, 0, 0)
# data2= dt.datetime(2024, 1, 1, 20, 0, 0)

# cg.Sessio(sala1_1,data1,p1,5)
# cg.Sessio(sala1_1,data2,p1,6)
# cg.Sessio(sala2_1,data1,p2,5)
# cg.Sessio(sala2_1,data2,p2,6)

# cg.Sessio(sala1_2,data1,p1,5)
# cg.Sessio(sala1_2,data2,p2,6)
# cg.Sessio(sala2_2,data1,p3,5)
# cg.Sessio(sala2_2,data2,p3,6)



if __name__ == "__main__":
    cg.llig_arxiu()
    mostra_menu()
