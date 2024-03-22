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


#------------------------------------------------------------------------
def mostra_pel_licules() -> None:
    ''' Mostra informació de la llista de pel·lícules (id y info)
    '''


#------------------------------------------------------------------------
def crea_pel_licula() -> None:
    ''' Crea una pel·licula i la grava. Demana la seua descripció.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'. Grava els canvis.
    '''

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
    try:
        id = cg.input_type('Selecciona una pel.licula:','int')
        return busca_pel_licula(id)
    except cg.input_type_cancel·lat():
        pass
    except cg.pelicula_no_trobada():
        pass


        
    print('No se ha trovat la pel·licula')

#------------------------------------------------------------------------
def modifica_pel_licula() -> None:
    ''' Modifica una pel·lícula. Primer demana un id de pel·licula a l'usuari i la busca entre la llista de pel·lícules.
    Demana a l'usuari una descripció nova i la reemplaça la descripció vella. Grava els canvis en disc.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''

#------------------------------------------------------------------------
def pel_licula_utilitzada_en_alguna_sessio(pel_licula:cg.Pel_licula) -> bool:
    '''No podem esborrar una pel·lícula si hi ha una sessió en qualsevol sala que la projecta.
    Retorna True si alguna sala la projecta, False si no.
    '''

#------------------------------------------------------------------------
def esborra_pel_licula():
    ''' Esborra una pel·lícula de la llista de pel·lícules. Demana l'id de la pel·licula a esborrar.
    La busca d'entre la llista de pel·lícules. Avisa si la pel·lícula es projecta en alguna sessió.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'. Grava els canvis en disc.
    '''

