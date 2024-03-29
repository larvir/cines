from __future__ import annotations
from dataclasses import dataclass
import datetime as dt
import clases_generals as cg

#==========================================================================================================
# Manteniment de pel·lícules
#==========================================================================================================
def menu_pel_licules() -> None:
    ''' Mostra la llista de pel·ícules y després un menú per al seu manteniment.
    El menú permet crear, modificar i esborrar pel·lícules. Si polsem intro tanquem el menú (return).
    No podrem esborrar una pel·lícula que s'estiga projectan en alguna sessió de qualsevol cine.
    '''
    while True:
        try:
            cg.cls('- LLISTA DE PEL·LÍCULES -')
            print(cg.msg_error)
            cg.msg_error = ''
            mostra_pel_licules()

            opcio = cg.input_type('1-Crea, 2-Modifica, 3-Esborra. Opció?', 'int')

            if opcio == 1:
                crea_pel_licula()
            elif opcio == 2:
                modifica_pel_licula()
            elif opcio == 3:
                esborra_pel_licula()
            else:
                cg.msg_error = 'No existeix aquesta opcio'
            
            cg.grava_arxiu()

        except cg.input_type_cancel·lat:
            break

        


#------------------------------------------------------------------------
def mostra_pel_licules() -> None:
    ''' Mostra informació de la llista de pel·lícules (id y info)
    '''

    for pel_licula in cg.pel_licules:
        print(f'({pel_licula.id}): {pel_licula.info}')


#------------------------------------------------------------------------
def crea_pel_licula() -> None:
    ''' Crea una pel·licula i la grava. Demana la seua descripció.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'. Grava els canvis.
    '''
    while True:
        try:
            cg.cls('- CREA PEL·LICULA -\n--------------------------')
            info = cg.input_type('Quina es la pel·licula')
            cg.pel_licules.append(cg.Pel_licula(info))
            cg.input_type('Fet. Intro per a continuar', intro_cancellar= False)
            

        except cg.input_type_cancel·lat:
            break
#------------------------------------------------------------------------
def busca_pel_licula(id: int) -> cg.Pel_licula:
    ''' Busca una pel·lícula pel seu id en la llista de pel·lícules.
    Si la troba retorna la pel·lícula, sinó llança l'excepció 'pelicula_no_trobada'
    '''

    for pel_licula in cg.pel_licules:
        if id == pel_licula.id:
            return pel_licula
            
    raise cg.pelicula_no_trobada
    


#------------------------------------------------------------------------
def demana_pel_licula(txt:str) -> cg.Pel_licula:
    ''' Demana l'id d'una pel·lícula, la busca en la llista de pel·lícules i retorna la Pel·lícula.
    Si polsem intro llança l'excepció 'input_type_cancel·lat' 
    '''
    while True:
        try:
            id = cg.input_type(txt,'int')
            return busca_pel_licula(id)
        except cg.pelicula_no_trobada:
            print('No se ha trovat la pel·licula')

#------------------------------------------------------------------------
def modifica_pel_licula() -> None:
    ''' Modifica una pel·lícula. Primer demana un id de pel·licula a l'usuari i la busca entre la llista de pel·lícules.
    Demana a l'usuari una descripció nova i la reemplaça la descripció vella. Grava els canvis en disc.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''
    while True:
        try:
            cg.cls()
            mostra_pel_licules()
            print('- MODIFICA LA PEL·LICULA -\n--------------------------')
            pel_licula = demana_pel_licula('ID de la pel·licula:')
            descripcio = cg.input_type('Descripció nova:')
            pel_licula.info = descripcio
            cg.input_type('Fet. Intro per a continuar', intro_cancellar= False)
            

        except cg.input_type_cancel·lat:
            break



#------------------------------------------------------------------------
def pel_licula_utilitzada_en_alguna_sessio(pel_licula:cg.Pel_licula) -> bool:
    '''No podem esborrar una pel·lícula si hi ha una sessió en qualsevol sala que la projecta.
    Retorna True si alguna sala la projecta, False si no.
    '''
    for cine in cg.cines:
        for sala in cine.sales:
            for sessio in sala.sessions:
                if sessio.pel_licula == pel_licula:
                    raise cg.pel_licula_utilitzada_en_una_sessio
                    return True
    
    return False


#------------------------------------------------------------------------
def esborra_pel_licula():
    ''' Esborra una pel·lícula de la llista de pel·lícules. Demana l'id de la pel·licula a esborrar.
    La busca d'entre la llista de pel·lícules. Avisa si la pel·lícula es projecta en alguna sessió.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'. Grava els canvis en disc.
    '''

    while True:
        try:
            cg.cls()
            mostra_pel_licules()
            print('- BORRA LA PEL·LICULA -\n--------------------------')
            print(cg.msg_error)
            cg.msg_error = ''
            pel_licula = demana_pel_licula('ID de la pel·licula:')
            if not pel_licula_utilitzada_en_alguna_sessio(pel_licula):
                cg.pel_licules.remove(pel_licula)
                cg.input_type('Fet. Intro per a continuar', intro_cancellar= False)
            
            

        except cg.input_type_cancel·lat:
            break
        except cg.pel_licula_utilitzada_en_una_sessio:
            cg.msg_error = 'No es pot borrar la pel·licula, ja esta en alguna sessio'

