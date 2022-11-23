import abc
from player import Jugador
from random import randint

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
        obj.move_player(pos)
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
    def proceso(self,obj:Jugador):
        if self.tipo=="1":
            Cofre.GanarDinero(self,obj)
        elif self.tipo== "2":
            Cofre.Pagar(self,obj)
        elif self.tipo=="3":
            Cofre.Avanzar(obj,self.data)
        elif self.tipo=="4":
            if self.data == '"Go to Jail"':
                obj.in_jail = True
            else: 
                obj.cards_owned.append("out of jail")


class Fortuna():
     def __init__(self, info: str, data:str,tipo:str):
        self.data = data #Dato a operar
        self.tipo = tipo #Tipos
        self.info = info ## Texto carta
     def Avanzar(pos:int,obj:Jugador):
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
     def proceso(self,obj:Jugador):
        if self.tipo=="1":
            Fortuna.GanarDinero(self,obj)
        elif self.tipo== "2":
            Fortuna.Pagar(self,obj)
        elif self.tipo=="3":
            Fortuna.Avanzar(self.data, obj)
        elif self.tipo=="4":
            if self.data == '"Go to Jail"':
                obj.in_jail = True
            else: 
                obj.cards_owned.append("out of jail")

class Robo():
    def __init__(self,info:str,data:str):
        self.info = info
        self.data = data
    
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





    






    