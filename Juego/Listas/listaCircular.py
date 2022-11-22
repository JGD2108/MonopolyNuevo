from Listas.Nodo import Nodo
class listaCircular:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self,data):
        P = Nodo(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P             
        self.ULT.next= self.PTR
    
    def Recorrido(self,amt:int):
        P = self.PTR
        print(P.data, end="->")
        P = P.next
        
        while((P != self.PTR)and amt>0):
            print(P.data, end="->")
            P = P.next
            amt=amt-1

        if (P == self.PTR):
            print(P.data)

    def __repr__(self):
        respuesta = ""
        P = self.PTR
        respuesta = respuesta + str(P.data) + "->"
        P = P.next
        while(P != self.PTR):
            respuesta = respuesta + str(P.data) + "->"
            P = P.next
        respuesta = respuesta +  str(P.data) 
        return respuesta

