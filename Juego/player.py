from random import randint
from Listas.listaCircular import listaCircular
from Cartas import *
class Jugador():

    def __init__(self, name: str, balance:int, cards_owned:list,
                    current_position:int, in_jail: bool, 
                    doubles_counter:int,bankruptcy_status:bool, efectos:list):
        self.name = name
        self.balance = balance
        self.cards_owned = cards_owned
        self.current_position = current_position
        self.in_jail = in_jail
        self.doubles_counter = doubles_counter 
        self.bankruptcy_status = bankruptcy_status 
        self.puedoJugar = None
        self.efectos = efectos

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
            self.doubles_counter+=1
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
    def add_balance(self, amount):
        """
            Incrementa el capital del jugador
        """
        self.balance += amount
        return self.balance

    def reduce_balance(self, amount):
        if self.balance < amount:
            print("dinero insuficiente para esta accion")
            bankrupt = self.check_if_bankrupt(amount)
            if not bankrupt:
                print("vende alguna de tus propiedades")
        else:
            self.balance -= amount

    def check_pos(self, board):
  
        brd_property = board.Recorrido(self.current_pos)

        '''
            serie de condicionales que comprueban la posicion
        '''

    def check_if_bankrupt(self, amt_owed):
        pass
## verificar que casilla es en la que estamos
    def checkBoard(self, a:listaCircular):
        if self.current_position==0:
            self.add_balance(200)
        elif self.current_position==1:
            ## deseas comprar?
            pass
        elif self.current_position==2 or self.current_position==12 or self.current_position==22 or self.current_position==33:
            Cofre.proceso(Cofre,self)
        elif self.current_position==7 or self.current_position==17 or self.current_position==28 or self.current_position==38:
            Fortuna.proceso(Fortuna,self)
            
        

