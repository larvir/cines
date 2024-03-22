from __future__ import annotations
from dataclasses import dataclass
import datetime as dt
import clases_generals as cg
import lara as l


#==========================================================================================================
# Reserves
#==========================================================================================================
def busca_cine(id: int) -> cg.Cine:
    ''' Busca un cine pel seu id en la llista de cines.
    Si ela troba retorna el cine, sinó llança l'excepció 'cine_no_trobat'
    '''
    for cine in cg.cines:
        if id == cine.id:
            return cine
    raise cg.cine_no_trobat


#------------------------------------------------------------------------
def mostra_cine_i_sales() -> None:
    ''' Mostra els cines (id i descripció) i les sales d'estos cines (id, descripció).
    '''
    for cine in cg.cines:
        print(f'CINE: ({cine.id}): {cine.descripcio}')
        for sala in cine.sales:
            print(f'   SALA ({sala.id}): sala {sala.id}')

#------------------------------------------------------------------------
def selecciona_cine() -> None:
    '''Mostra una llista de cines i les seues sales.
    Demana un id de cine i el busca. Si el troba retorna el cine.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''
    try:
        while True:
            cg.cls('- LLISTA DE CINES -\n---------------------------')
            mostra_cine_i_sales()

            id:int = cg.input_type('Selecciona un cine:','int')


            cine:cg.Cine = busca_cine(id)

            if cine:
                manteniment_sessions(cine)

            else:
                print('No se ha trobat cap cine')

    except cg.input_type_cancel·lat:
        pass
    except cg.cine_no_trobat():
        print('No se ha trovat el cine')





#------------------------------------------------------------------------
def demana_sessio(sala: cg.Sala) -> cg.Sessio:
    ''' Demana l'id d'una sessió, la busca d'entre la llista de sessions de la sala i retorna la sala.
    Si no la troba llança l'excepció 'sessio_no_trobada'. Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''

    id:int = cg.input_type('Selecciona una sesió:','int')

    for sessio in sala.sessions:
        if id == sessio.id:
            return sessio
    raise cg.sessio_no_trobada

#------------------------------------------------------------------------
def demana_seient(sala: cg.Sala) -> tuple[int,int]:
    ''' Demana una fila (int) i un seient (int). Estos valors es verifiquen contra 
        els valors de files i seient de la sala que li passem. Retorna una fila i
        seient vàlids per a la sala. Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''
    
#==========================================================================================================
# Manteniment de sessions
#==========================================================================================================

def manteniment_sessions(cine: cg.Cine) -> None:  
    ''' Mostra la informació de les sales i les seues sessions del cine indicat.
    Demana l'id d'una sala i mostra una menú amb les opciones de crear, modificar, esborrar i mantinedre les reserves
    per a esta sala seleccionada. 
    '''
    
    try:
        while True:
            cg.cls('- LLISTA DE SESSIONS -')
            mostra_sales_i_sessions(cine)


            sala = demana_sala(cine)
            
            if sala:
                print(f'MANTENIMENT DE SESSIONS: SALA({sala.id}) sala {sala.id}')
                opcio = cg.input_type('1-Crea, 2-Modifica, 3-Esborra, 4-Reserves. Opció?','int')
                if opcio == 1:
                    crea_sessio(sala)
                elif opcio == 2:
                    modifica_sessio(sala)
                elif opcio == 3:
                    esborra_sessio(sala)
                elif opcio == 4:
                    mateniment_reserves(cine,sala)
                else:
                    print('Opció incorrecta')
        
    except cg.input_type_cancel·lat:
        pass
    except cg.sala_no_trobada():
        print('No se ha trovat la sala')



#------------------------------------------------------------------------
def mostra_sales_i_sessions(cine: cg.Cine) -> None:
    ''' Mostra informació del cine que li passem com a paràmetre (id i descripció).
    A continuació, mostra informaciño de les sales del cine (id i descripció) i de cadascuna de les
    seues sessions (id, data y hora, info de la pel·licula y el preu).
    '''
    print(f'Cine({cine.id}): {cine.descripcio}')
    for sala in cine.sales:
        print('----------------------------------')
        print(f'SALA ({sala.id}): sala {sala.id}')
        for sessio in sala.sessions:
            print(f'    SESSIÓ ({sessio.id}): {sessio.data_hora} {sessio.pel_licula.info} {sessio.preu_entrada}')



#------------------------------------------------------------------------
def demana_sala(cine: cg.Cine) -> cg.Sala:
    ''' Demana l'id d'un sala, la busca d'entre la llista de sales del cine i retorna la sala.
    Si no la troba llança l'excepció 'sala_no_trobada'. Si polsem intro llança l'excepció 'input_type_cancel·lat'
    '''
    id:int = cg.input_type('Selecciona una sala:','int')

    for sala in cine.sales:
        if id == sala.id:
            return sala
    raise cg.sala_no_trobada
        
   
#------------------------------------------------------------------------
def crea_sessio(sala: cg.Sala) -> None:
    ''' Crea un objete sessió. Demana data y hora de la sessió, l'id de la pel·lícula que es projecta i el preu de l'entrada.
    La sessió s'afegix a llista de sessions de la sala que li passem. Si polsem intro eixim i es cancel·la la creació.
    '''
    try:
        while True:
            data_hora = cg.obtin_data_hora()
            if not data_hora:
                raise cg.input_type_cancel·lat
            pel_licula = l.demana_pel_licula()
            preu_entrada = cg.input_type('Quin sera el preu', 'float')
            cg.Sessio(sala,data_hora,pel_licula,preu_entrada)

    except cg.input_type_cancel·lat:
        pass




#------------------------------------------------------------------------
def modifica_sessio(sala: cg.Sala) -> None:
    ''' Modica una de les sessions de la sala que li passem.
    Demana l'id d'una sessio i la busca en la sala. A continuació la modifiquem, preguntant data y hora de la sessió,
    l'id de la pel·lícula que es projecta i el preu d'entrada. Es graven els canvis en disc.
    Si polsem intro es cancel·la la modificació de la sessió.
    '''
    try:
        while True:
            sessio:cg.Sessio = demana_sessio(sala)
            data_hora = cg.obtin_data_hora()
            if not data_hora:
                raise cg.input_type_cancel·lat
            sessio.data_hora = data_hora
            sessio.pel_licula = l.demana_pel_licula()
            sessio.preu_entrada = cg.input_type('Quin sera el preu', 'float')
    
    except cg.input_type_cancel·lat:
        pass
    except cg.sessio_no_trobada():
        print('No se ha trobat la sessio')

#------------------------------------------------------------------------
def esborra_sessio(sala: cg.Sala) -> None:
    ''' Esborra una de les sessions de la sala que li passem.
    Demana l'id d'una sessio i la busca en la sala. A continuació l'esborra. Es graven els canvis en disc.
    Si polsem intro es cancel·la l'esborrat de la sessió.
    '''
    try:
        while True:
            sessio = demana_sessio(sala)
            sala.sessions.remove(sessio)
    
    except cg.input_type_cancel·lat:
        pass
    except cg.sessio_no_trobada():
        print('No se ha trobat la sessio')

#------------------------------------------------------------------------
def demana_dades_reserva() -> cg.Reserva:
    ''' Demna un dni i crea una Reseerva amb ell. Retorna la reserva.
    '''
    try:
        while True:
            dni = cg.input_type('Quin es el teu dni')
            return cg.Reserva(dni)

    except cg.input_type_cancel·lat:
        pass


#------------------------------------------------------------------------
def mateniment_reserves(cine: cg.Cine, sala: cg.Sala) -> None:
    ''' Recorrer les sessions de la sala indicada i mostra de cadascuna d'elles l'estat de les reserves.
    A continuació, demana l'id d'una de le sessions, busca la sessió que correspon a este id, i demana
    un fila i seient. Si la fila/seient ja està reservada pregunta si volem esborrar-la i, si constestem que S, 
    l'esborra i grava els canvis en disc. Per contra, si la fila/seient no està reservada, demana un dni
    amb què crea una reserva per a esta fila/seient i grava els canvis. Si polsem intro al demanar 
    l'id de sessió, fila, seient, dni ens eixim.
    '''

#==========================================================================================================
# Reserva d'una pel·lícula
#==========================================================================================================
@dataclass
class Resultat:
    '''Esta classe és una classe temporal que s'utilitza per a filtrar sessions'''
    cine: cg.Cine
    sala: cg.Sala
    sessio: cg.Sessio

#------------------------------------------------------------------------
def busca_sessions_on_vore_pel_licula(pel_licula: cg.Pel_licula, data_hora:dt.date|None=None) -> list[Resultat]:
    ''' Recorre els cines i les seues sales buscant aquelles sessions on es projecta una pelicula determinada, de manera 
        opcional també es pot filtrar per una data determinada. El resultat es guarda en un lista de objectes
        Resultat que guarda el cine i la sessió que casen amb el filtre de pel·lícula i data/hora indicats.
        Retorna esta llista de (cine, sessió)
    '''
#------------------------------------------------------------------------
def selecciona_sessio_on_vore_pel_licula(pel_licula: cg.Pel_licula, data:dt.date|None) -> tuple[cg.Sala,cg.Sessio]:
    ''' Busca i mostrar els cines i les sesions que projecten la pel·lícula indicada i, opcionalment, en al data indicada.
    A continuació, sol·licita l'id d'una d'este sessions. Retorna la sala i la sessió seleccionades.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''

#------------------------------------------------------------------------
def reserva_pel_licula() -> None:
    ''' Mostra la llista de pel·lícules.
    Demana l'id d'una pel·lícula i una data (ddmmaa).
    Busca en totes les sales aquelles sessions que projecten la pel·lícula i, opcionalment, en la data indicada.
    Pregunta que seleccionem la sessió en què volem fer una reserva. 
    Fa una reserva en esta sessió. Per a fer-la mostra una llista de les reserves, demana una fila i un seient.
    Demana un dni per a la reserva i assigna la reserva a la fila/seient indicades. Grava els canvis en disc.
    Si polsem intro eixem del procés de reserva.
    '''


#------------------------------------------------------------------------
def reserva_pel_licula_en_sessio(sala:cg.Sala, sessio:cg.Sessio) -> None:
    ''' Mostra una llista de reserves de la sessió indicada.
    Demana fila i seient on volem fer la reserva. Si la fila/seient ja estan reservats mostra un missate indicant-ho.
    Si la fila/seient esta lliures, demana un dni, crea la reserva i l'assigna a la fila/seient.
    Grava els canvis en disc. Si polsem intro eixem del procés de reserva.
    '''
