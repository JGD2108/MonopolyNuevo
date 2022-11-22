import abc
from player import Jugador
from random import randint, random

'''
@autor Jose Gomez
'''
class Cartas(abc.ABC):
    def __init__(self, precio:int, renta:int,nombre:str):
        self.precio = precio
        self.renta = renta
        self.dueño = "Bank"
        self.nombre = nombre
    @abc.abstractmethod
    def CambiarDueño():
        pass

class Propiedades(Cartas):
    @property
    def CambiarDueño(self):
        return self.dueño
    @CambiarDueño.setter
    def CambiarDueño(self,a):
        self.dueño = a

class Utilidades(Cartas):
    @property
    def CambiarDueño(self):
        return self.dueño
    @CambiarDueño.setter
    def CambiarDueño(self,a):
        self.dueño = a

"""
Tipos de cartas
1. Cobrar
2. Pagar
3. Avanzar
4. Ir a la carcel 
5. Carta salir de carcel
"""

class Cofre():
    def __init__(self, info:str, data:str,  tipo:str):
        self.data = data 
        self.tipo = tipo
        self.info = info
    def Avanzar(obj:Jugador, pos:int):
        obj.current_position = obj.current_position + pos
        return obj.current_position

    def GanarDinero(self, obj:Jugador):
        """
        Se le agrega al jugador cierta cantidad
        sumarle al atributo 
        """
        obj.add_balance(self.data)
        return obj
    def Pagar(self, obj:Jugador):
        """
        Se le resta al jugador cierta cantidad
        restarle al atributo
        """
        obj.reduce_balance(self.data)

class Fortuna():
     def __init__(self, info: str, data:str,tipo:str):
        self.data = data #Dato a operar
        self.tipo = tipo #Tipos
        self.info = info ## Texto carta
     def Avanzar(obj:Jugador, pos:int):
        obj.current_position = obj.current_position + pos
        return obj.current_position

     def GanarDinero(self, obj:Jugador):
        """
        Se le agrega al jugador cierta cantidad
        sumarle al atributo 
        """
        obj.add_balance(self.data)
        return obj
     def Pagar(self, obj:Jugador):
        """
        Se le resta al jugador cierta cantidad
        restarle al atributo
        """
        obj.reduce_balance(self.data)

class Robo():
    def __init__(self,info:str ):
        self.info = info
    
    def Dado_Tramposo(obj:Jugador):
        """
        Le suma cierta cantidad al dado de verdad
        """
        dice = randint(1,6)
        obj.dice_amt = obj.dice_amt+dice
        return obj.dice_amt
    
    def Robar(obj:Jugador, data):
        obj.balance+=data
        return obj.balance

    def Atrapar(obj:Jugador):
        prob = randint(1,4)
        if prob == 4:
            obj.in_jail= True
        else: 
            obj.in_jail = False
        return obj.in_jail





    






    