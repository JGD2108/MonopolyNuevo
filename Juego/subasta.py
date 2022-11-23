#import linkedList_jugadores
from player import Jugador
from Cartas import Propiedades

class subasta:
    def __init__(self, jugador: Jugador, propiedad_subasta: Propiedades):
        self.jugador = jugador
        self.propiedad_subasta = propiedad_subasta
    
    def subastar(self):
        """
        Se hace un objeto tipo linkedList de los jugadores para que por medio del ciclo,
        vaya haciendo las mismas preguntas y añadiendo en una lista aparte los participantes que van,
        a jugar la subasta.
        """

        #lista_jugadores = linkedList_jugadores(jugadores))
        #p = lista_jugadores.head
        #for i in range(cant_jugadores):
        print(f"{self.jugador}, Su dinero actual es: {self.dinero}")
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
        print(f"{self.jugador}, Su dinero actual es: {self.dinero}")
        cant_propuesta = int(input("Ingrese la cantidad a proponer: "))
        while(cant_propuesta < self.dinero):
            print(f"Intente hacer una propuesta más baja, su dinero es {self.dinero}")
            cant_propuesta = int(input("Ingrese la cantidad a proponer: "))
        balance = self.check_if(cant_propuesta)
        return balance
            
    def check_if(self, cant_propuesta: int):
        while True:
            if (cant_propuesta == self.dinero):
                print("No puede quedar sin dinero")
                print(f"Intente hacer una propuesta más baja, su dinero es {self.dinero}")
                cant_propuesta = int(input("Ingrese la cantidad a proponer: "))
            else:
                disponible = self.dinero - cant_propuesta
                break
        return disponible
    
    def process(self):
        participantes = {}
        self.subastar(participantes)
        propuesta_mayor = max(participantes.keys(), key=lambda k: participantes[k])
        print(f"La mayor propuesta es {participantes[propuesta_mayor]}, de {propuesta_mayor}")

class acciones:
    def __init__(self, dinero: int, jugador: Jugador):
        self.dinero = dinero
        self.jugador = jugador

    def comprar(self, accion: subasta):
        while True:
            print("Desea comprar esta propiedad?")
            sw = int(input("1. si; 2. no"))
            if (sw == 1):
                #Método para comprar propiedad
                break
            elif (sw == 2):
                accion.process()
                break
            else:
                print("Eliga una opción válida")
    

