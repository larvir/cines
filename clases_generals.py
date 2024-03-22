from __future__ import annotations
from dataclasses import dataclass
import datetime as dt
import os
import platform
import pickle

#==========================================================================================================
# Excepcions
#==========================================================================================================
class pelicula_no_trobada(Exception):           # type: ignore
    pass
class sessio_no_trobada(Exception):
    pass
class sala_no_trobada(Exception):
    pass
class cine_no_trobat(Exception):
    pass
class input_type_cancel·lat(Exception):
    pass
class pel_licula_utilitzada_en_una_sessio(Exception):
    pass
class Data_incorrecta(Exception):
    pass
#==========================================================================================================
# VARIABLES GLOBALS
#==========================================================================================================
pel_licules:list[Pel_licula] = []
cines:list[Cine] = []

#==========================================================================================================
# CLASSES
#==========================================================================================================
class Reserva:
    def __init__(self, dni:str) -> None:
        self.dni = dni

    def __str__(self) -> str:
        return self.dni
    
    __repr__ = __str__

#==========================================================================================================
class Pel_licula:
    id:int = 1
    def __init__(self, info:str) -> None:
        self.id = Pel_licula.id
        Pel_licula.id += 1
        self.info = info

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Pel_licula):
            return False
        return obj.id==self.id
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['id_'] = Pel_licula.id
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        Pel_licula.id = state['id_']

#==========================================================================================================
class Cine:
    id:int = 1
    def __init__(self, descripcio:str) -> None:
        self.id = Cine.id
        Cine.id += 1
        self.descripcio = descripcio
        self.sales:list[Sala] = []

    def busca_sala(self, id_sala:int) -> Sala:
        '''Busca una sala pel seu id en la llista de sales del cine.
        Si la troba retorna la llista, sinó llança l'excepció 'sala_no_trobada'
        '''
        for sala in self.sales:
            if sala.id == id_sala:
                return sala
        raise sala_no_trobada
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['id_'] = Cine.id
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        Cine.id = state['id_']

#==========================================================================================================
class Sala:
    id:int = 1
    def __init__(self, cine: Cine, descripcio:str, files: int, seients_per_fila:int) -> None:
        self.id = Sala.id
        Sala.id += 1
        self.descripcio = descripcio
        self.files = files
        self.seients_per_fila = seients_per_fila
        self.sessions:list[Sessio] = []
        cine.sales.append(self)
    
    def busca_sessio(self, id_sessio: int) -> Sessio:
        ''' Busca una sessio pel seu id en la llista de sessions de la sala.
        Si la troba retorna la sala, sinó llança l'excepció 'sessio_no_trobada'
        '''
        for sessio in self.sessions:
            if sessio.id==id_sessio:
                return sessio
        raise sessio_no_trobada
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['id_'] = Sala.id
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        Sala.id = state['id_']

#==========================================================================================================
class Sessio:
    id:int = 1
    def __init__(self, sala:Sala, data_hora:dt.datetime, pel_licula:Pel_licula, preu_entrada:float) -> None:
        self.id = Sessio.id
        Sessio.id += 1
        self.data_hora:dt.datetime = data_hora
        self.pel_licula = pel_licula
        self.preu_entrada = preu_entrada
        self.reserves:list[list[Reserva|None]] = [[None] * sala.seients_per_fila for _ in range(sala.files)]
        sala.sessions.append(self)
    
    def mostra_reserves(self) -> None:
        '''Mostra per pantalla les reserves de la sessió per fila '''
        for i, fila in enumerate(self.reserves):
            print(f'fila {i}: {fila}')
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['id_'] = Sessio.id
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        Sessio.id = state['id_']

#==========================================================================================================
# Funcions generals
#==========================================================================================================
def cls(txt:str|None=None):
    comando = 'cls' if platform.system()=='Windows' else 'clear'
    os.system(comando)
    if txt:
        print(txt)

#------------------------------------------------------------------------
def input_type(text:str, type:str='str', excepcio:bool=True, intro_cancellar:bool=True) -> int|str|float|None:
    '''Funció ampliació de l'input de Python. Demana a l'usuari un valor que convertix a un tipus de dada determinat
    segons el valor del paràmetre type, el qual pot ser 'int','str' o 'float'. Si l'usuari no introduix res (intro)
    segons el valor del paràmetre excepcio generarà l'excepció 'input_type_cancel·lat' o retonarà el str ''.
    Al fer l'input mostra de manera automàtica el text (Intro=cancel·lar). Este text es pot ocultar amb el parametre intro_cancellar=False.
    '''
    try:
        while True:
            mensage = '(Intro=cancel·lar) ' if intro_cancellar else ''

            entrada = input(mensage + text + ' ')

            if entrada == '':
                if excepcio:
                    raise input_type_cancel·lat
                
                return ''

    
            if type == 'str':
                return entrada
            elif type == 'int':
                return int(entrada)
            elif type == 'float':
                return float(entrada)
    
    except ValueError:
        print('Valor incorrecte')


#------------------------------------------------------------------------
def obtin_data() -> dt.date|None:
    ''' Pregunta a l'usuari una data. Verifica que es correcta i avisa si no ho és.
    Retorna una data o None si l'usuari no n'ha introduit cap (fa intro).
    '''
    try:
        while True:
            data = dt.datetime.strptime(input_type('Quin any vols?(d/m/y)'), '%d/%m/%y')

            if data < dt.datetime.today():
                raise Data_incorrecta
            
            return data
            
    except Data_incorrecta:
        print('La data es incorrecta')

    except ValueError:
        print('La data es incorrecta')

    except input_type_cancel·lat:
        return None
    
        


#------------------------------------------------------------------------
def obtin_data_hora() -> dt.datetime:
    ''' Pregunta a l'usuari una data en forma ddmmaa i una hora en forma hhmm.
    Verifica que es la i l'hora són correctes i avisa si no ho és.
    Retorna el datetime corresponent. Si polsem intro llança l'excepció 'input_type_cancel·lat'
    '''
    try:
        while True:
            data = obtin_data()

            hora = dt.datetime.strptime(input_type('Quin any vols?(h:m)'), '%H:%M')


            data_hora = dt.datetime.combine(data, hora)

            if data_hora < dt.datetime.now():
                raise Data_incorrecta
            
            return data
            
    except Data_incorrecta:
        print('La data es incorrecta')

    except ValueError:
        print('La data es incorrecta')

    except input_type_cancel·lat:
        return None




    
#==========================================================================================================
# Persistència de dades.
#==========================================================================================================
def grava_arxiu() -> None:
    '''Grava en arxiu.pkl la llista de pel·licules i la de cines'''
    with open('arxiu.pkl', 'wb') as fd:
        pickle.dump(pel_licules, fd)
        pickle.dump(cines, fd)

def llig_arxiu() -> None:
    ''' Si arxiu.pkl no existix el crea y grava en ell la llista de pel·licules i la de cines.
    Si arxiu.pkl existix el sobreescriu amb les llistes de pel·licules i de cines.
    '''
    global pel_licules
    global cines
    if not os.path.exists('arxiu.pkl'):
        grava_arxiu()
        return
    with open('arxiu.pkl', 'rb') as fd:
        pel_licules = pickle.load(fd)
        cines = pickle.load(fd)

