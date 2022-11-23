import sys, time
from Botones import Button
import pygame
from Tablero import Tablero,chestList,fortList
from player import Jugador
from Labels import Label
from Cartas import *
from Listas.listaCircular import listaCircular

Board = listaCircular()
tablero = Tablero(Board)
tablero.getBoard()

class Game:
    def __init__(self) -> None:
        self.currentPlayer: Jugador= None
    def turnSelect(self):
        valueJ = Jorge.roll_dice()
        valueL = Luisa.roll_dice()
        while True:
            if valueJ==valueL:
                valueJ = Jorge.roll_dice()
                valueL = Luisa.roll_dice()
            if valueJ> valueL and valueJ!=valueL:
                self.currentPlayer = Jorge
                self.currentPlayer.puedoJugar = True
                Luisa.puedoJugar = False
                break
            else:
                self.currentPlayer = Luisa
                Jorge.puedoJugar = False
                self.currentPlayer.puedoJugar = True
                break
        return self.currentPlayer
        
    def check_pos(self, board:Tablero):
  
        brd_property = board.Board.Recorrido(self.currentPlayer.current_position)
        print(self.currentPlayer.current_position)

        
        if(isinstance(brd_property, Propiedades)):
            ## input comprar o subastar
            ## si comprar, resta balance, añade a lista, Propiedad.CambiarDueño= self.current_player
            ## brd_property.CambiarDueño = self.current_player
            ## si va subastar: print("Unda el boton subasta")
            print("Estas en una propiedad")

        elif(brd_property==chestList):
            print("Estas en un  cofre")
        elif(brd_property==fortList):
            print("Estas en una fortuna")
        else:
            print("wiuwiuwiuww")
    def jugar(self):
        if (self.currentPlayer.puedoJugar):
            cuantoSeMueve=self.currentPlayer.roll_dice()
            self.currentPlayer.move_player(cuantoSeMueve)
            ##verificar donde cae
            self.check_pos(self,tablero)
            Game.changeTurn(Game)
            pygame.display.update()
        else:
            Game.changeTurn(Game)
            pygame.display.update()
            #currentPlayer.dias_En_Carcel -= 1 
            #Implementen lo del boton.
    def changeTurn(self):
        if (self.currentPlayer == Luisa):
            self.currentPlayer = Jorge
            self.currentPlayer.puedoJugar = True
            Luisa.puedoJugar = False
        else:
            self.currentPlayer = Luisa
            Jorge.puedoJugar = False
            Luisa.puedoJugar = True
        return self.currentPlayer, Jorge, Luisa
        

Luisa = Jugador('Luisa',1500,[],1,False,0,False,[])
Jorge = Jugador('Jorge',1500,[],1,False,0,False,[])

def count_bankrupt_players(players):
    counter = 0
    for player in players:
        if player.bankruptcy_status:
            counter += 1
    return counter

#Definir colores
BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
GREEN   = (  0, 255,   0)
RED     = (255,   0,   0)
BLUE    = (  0,   0, 255)


size = (945, 710)
#Crear ventana
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Menu")

background_juego = pygame.image.load("Recursos/tablero_monopolio.png").convert()
background_menu = pygame.image.load("Recursos/menu.png").convert()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Recursos/font.ttf", size)

#myFont = pygame.font.SysFont("Calibri", 30)

#Controlar FPS|
clock = pygame.time.Clock()


done = False
boton_trade = pygame.Rect(770, 507, 120, 25)
boton_auction = pygame.Rect(775, 570, 120, 25)
boton_menu = pygame.Rect(775, 636, 120, 25)
currentPlayer:Jugador= None

labels = []
def show_labels():
	for _ in labels:
		_.draw()

def trade():
    pass

def auction():
    try:
        auc = int(input("Digita un numero: "))
    except ValueError:
        print("DIGITA UN NUMERO VALIDO")
    
def play():
    Game.turnSelect(Game)
    
    while True:
        pygame.display.set_caption("Play")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        #LDICE = pygame.display.set_mode((945, 710))

        screen.blit(background_juego, (0, 0))

        PLAY_BACK = Button(image=None, pos=(820, 680), 
                            text_input="MENU", font=get_font(20), base_color="White", hovering_color="Green")
        
        PLAY_ROLL = Button(image=None, pos=(890, 450), 
                            text_input="ROLL", font=get_font(10), base_color="White", hovering_color="Green")
        
        PLAY_TRADE = Button(image=None, pos=(820, 500), 
                             text_input="TRADE", font=get_font(20), base_color="White", hovering_color="Green")
        
        PLAY_AUCTION = Button(image=None, pos=(820, 590), 
                             text_input="AUCTION", font=get_font(20), base_color="White", hovering_color="Green")

        #text = Label(LDICE, "1", 781, 378, 60, "white") # out of loop
        #show_labels()
        #text.draw() # into the loop
        

        for button in [PLAY_BACK, PLAY_ROLL, PLAY_TRADE, PLAY_AUCTION]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)

        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_ROLL.checkForInput(PLAY_MOUSE_POS):
                    Game.jugar(Game)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_AUCTION.checkForInput(PLAY_MOUSE_POS):
                    auction()
        pygame.display.update()
                    

def options():
    while True:
        pygame.display.set_caption("Options")
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("Black")

        OPTIONS_TEXT = get_font(20).render("How many players are playing?", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(480, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(900, 690), 
                            text_input="MENU", font=get_font(20), base_color="white", hovering_color="Green")


        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        pygame.display.set_caption("Menu")
        screen.blit(background_menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("Recursos/Play Rect.png"), pos=(100, 350), 
                            text_input="PLAY", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Recursos/Play Rect.png"), pos=(100, 450), 
                            text_input="OPTIONS", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Recursos/Play Rect.png"), pos=(100, 550), 
                            text_input="QUIT", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()