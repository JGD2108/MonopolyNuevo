from random import randint
from Listas.listaCircular import listaCircular
from Tablero import *
class Jugador():

    def __init__(self, name: str, balance:int,
                    current_position:int, in_jail: bool, 
                    doubles_counter:int,bankruptcy_status:bool):
        self.name = name
        self.balance = balance
        self.current_position = current_position
        self.in_jail = in_jail
        self.doubles_counter = doubles_counter 
        self.bankruptcy_status = bankruptcy_status 
        self.puedoJugar = None

    def roll_dice(self):
        '''
            Simula el tiro de dados por medio de un random y retorna 
            la cantidad de casillas que deberia avanzar el jugador
        '''
        #if dias_En_Carcel < 1:
        #   self.puedoJugar = true
        #else: 
        #   self.puedoJugar = false   
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        dice_amt = dice1 + dice2
        if dice1==dice2: 
            self.in_jail = False
        else:
            self.doubles_counter=0
        return dice_amt

    def move_player(self, dice_amt):
        """
        Mueve el jugador deacuerdo a lo indicado por el dado
        """
        posicion = self.current_position+dice_amt
        if posicion >39:
            self.current_position = posicion - self.current_position
        else:
            self.current_position = posicion

        return self.current_position

    def checkDouble(self):
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        if dice1==dice2: 
            self.in_jail = False
        else:
            self.in_jail = True


    def add_balance(self, amount):
        """
            Incrementa el capital del jugador
        """
        self.balance += amount
        return self.balance

    def reduce_balance(self, amount):
        if self.balance < amount:
            print("dinero insuficiente para esta accion")
            self.bankruptcy_status = True
        else:
            self.balance -= amount
  

        

 