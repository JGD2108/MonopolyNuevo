class Nodo:
    def __init__(self, data,coordenadas):
        self.data = data
        self.coordenadas = coordenadas
        self.next = None
    
    def __repr__(self):
        return str(self.data)