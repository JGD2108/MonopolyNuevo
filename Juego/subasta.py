#import linkedList_jugadores
from player import Jugador
from Cartas import Propiedades

class subasta:
    def __init__(self, jugadores: Jugador, propiedad_subasta: Propiedades):
        self.jugadores = jugadores
        self.propiedad_subasta = propiedad_subasta
    
    def subastar(self):
        
            print(f"{self.jugadores.name}, Su dinero actual es: {self.jugadores.balance}")
            print(f"La propiedad a subastar es: {self.propiedad_subasta}")
            print("Desea participar en la subasta?")
            while True:
                opc = int(input("1. Si; 2. no"))
                if (opc == 1):
                    propuesta = self.hacer_propuesta()
                #participantes[self.jugador] = propuesta
                #p = p.next  
                    break
                elif (opc == 2):
                #p = p.next
                    break
                else:
                    print("Digite una opción válida")
       
        
        #return participantes   

    def hacer_propuesta(self):
        cant_propuesta = int(input("Ingrese la cantidad a proponer: "))
        balance = self.check_if(cant_propuesta)
        self.jugadores.subasta = balance
        
            
    def check_if(self, cant_propuesta: int):
        while True:
            if (cant_propuesta >= self.jugadores.balance):
                print("No puede quedar sin dinero")
                print(f"Intente hacer una propuesta más baja, su dinero es {self.jugadores.balance}")
                cant_propuesta = int(input("Ingrese la cantidad a proponer: "))
            else:
                return cant_propuesta

    
    def process(self):
        participantes = {}
        propuesta_mayor = max(participantes.keys(), key=lambda k: participantes[k])
        print(f"La mayor propuesta es {participantes[propuesta_mayor]}, de {propuesta_mayor}")


    

