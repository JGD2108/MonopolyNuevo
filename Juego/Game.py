import pygame, sys, time
from Botones import Button
from player import Jugador
from Labels import Label
from Listas.listaCircular import listaCircular

Luisa = Jugador('Luisa',1500,[],1,False,0,False)
Jorge = Jugador('Jorge',1500,[],1,False,0,False)

def count_bankrupt_players(players):
    counter = 0
    for player in players:
        if player.bankruptcy_status:
            counter += 1
    return counter



pygame.init()

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

background_juego = pygame.image.load("Juego/Recursos/tablero_monopolio.png").convert()
background_menu = pygame.image.load("Juego/Recursos/menu.png").convert()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Juego/Recursos/font.ttf", size)

#myFont = pygame.font.SysFont("Calibri", 30)

#Controlar FPS|
clock = pygame.time.Clock()


done = False
boton_trade = pygame.Rect(770, 507, 120, 25)
boton_auction = pygame.Rect(775, 570, 120, 25)
boton_menu = pygame.Rect(775, 636, 120, 25)
currentPlayer = None

labels = []
def turnSelect():
    valueJ = Jorge.roll_dice()
    valueL = Luisa.roll_dice()
    if valueJ> valueL:
        currentPlayer = Jorge
        Jorge.puedoJugar = True
        Luisa.puedoJugar = False
    else:
        currentPlayer = Luisa
        Jorge.puedoJugar = False
        Luisa.puedoJugar = True


def show_labels():
	for _ in labels:
		_.draw()

def trade():
    pass

def auction():
    pass

def changeTurn():
    if (currentPlayer == Luisa):
        currentPlayer = Jorge
        Jorge.puedoJugar = True
        Luisa.puedoJugar = False
    else:
        currentPlayer = Luisa
        Jorge.puedoJugar = False
        Luisa.puedoJugar = True

def roll():
    Luisa.roll_dice()  
    # text = Label(screen, "1", 781, 378, 60, "white") # out of loop
    # text.draw()
    # time.sleep(3)
    # into the loop
      # Label(LDICE, "1", 800, 450, 36)
        # show_labels()
def jugar():
    if (currentPlayer.puedoJugar):
        cuantoSeMueve=currentPlayer.roll_dice()
        currentPlayer.move_player(cuantoSeMueve)
        changeTurn()
    else:
        changeTurn()
        #currentPlayer.dias_En_Carcel -= 1 
        #Implementen lo del boton.
    
def play():
    turnSelect()
        
    
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_ROLL.checkForInput(PLAY_MOUSE_POS):
                    jugar()
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

        PLAY_BUTTON = Button(image=pygame.image.load("Juego/Recursos/Play Rect.png"), pos=(100, 350), 
                            text_input="PLAY", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Juego/Recursos/Play Rect.png"), pos=(100, 450), 
                            text_input="OPTIONS", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Juego/Recursos/Play Rect.png"), pos=(100, 550), 
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