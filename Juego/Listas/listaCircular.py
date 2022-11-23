from Listas.Nodo import Nodo
class listaCircular:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self,data,coordenadas):
        P = Nodo(data,coordenadas)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P             
        self.ULT.next= self.PTR
    
    def Recorrido(self,amt:int):
        P = self.PTR

        #print(P.data, end="->")
        if amt>0:
            P = P.next
            cont=1
            while((P != self.PTR)and cont<amt):
                #print(P.data, end="->")
                P = P.next
                cont+=1
            return P.data
        elif amt==0:
            return P.data

    