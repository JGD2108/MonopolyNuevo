import pandas as pd
from Cartas import Fortuna, Cofre, Propiedades, Robo
from Listas.listaCircular import listaCircular
file = "Cofre.xlsx"
Sheet = "Libro1"
File2 = "Fortuna.xlsx"
sheet = 'Hoja1'
File3 = "Propiedades.xlsx"
File4 = "Robar.xlsx"

class Tablero:
    def __init__(self,Board:listaCircular) -> None:
        self.Board = Board
    def getBoard(self):
        getLists(chestList, fortList, propiedades,robar)
        self.Board.AddNode("Go", [662,665])
        self.Board.AddNode(propiedades[0],[586,665])
        self.Board.AddNode(chestList,[530,665])
        self.Board.AddNode(propiedades[1],[473,665])
        self.Board.AddNode(propiedades[2],[414,665])
        self.Board.AddNode(robar,[357,665])
        self.Board.AddNode(propiedades[3],[297,665])
        self.Board.AddNode(fortList,[244,665])
        self.Board.AddNode(propiedades[4],[183,665])
        self.Board.AddNode(propiedades[5],[128,665])
        self.Board.AddNode("jail",[52,665])
        self.Board.AddNode(propiedades[6],[52,586])
        self.Board.AddNode(chestList,[52,529])
        self.Board.AddNode(propiedades[7],[52,474])
        self.Board.AddNode(propiedades[8],[52,421])
        self.Board.AddNode(robar,[52,361])
        self.Board.AddNode(propiedades[9],[52,301])
        self.Board.AddNode(fortList,[52,244])
        self.Board.AddNode(propiedades[10],[52,188])
        self.Board.AddNode(propiedades[11],[52,132])
        self.Board.AddNode("Parada libre",[52,48])
        self.Board.AddNode(propiedades[12],[126,48])
        self.Board.AddNode(chestList,[182,48])
        self.Board.AddNode(propiedades[13],[242,48])
        self.Board.AddNode(propiedades[14],[296,48])
        self.Board.AddNode(robar,[359,48])
        self.Board.AddNode(propiedades[15],[414,48])
        self.Board.AddNode(propiedades[16],[472,48])
        self.Board.AddNode(fortList,[529,48])
        self.Board.AddNode(propiedades[17],[586,48])
        self.Board.AddNode("Go to jail",[662,48])
        self.Board.AddNode(propiedades[18],[662,131])
        self.Board.AddNode(propiedades[19],[662,188])
        self.Board.AddNode(chestList,[662, 244])
        self.Board.AddNode(propiedades[20],[662,300])
        self.Board.AddNode(robar,[662,359])
        self.Board.AddNode(propiedades[21],[662,419])
        self.Board.AddNode(propiedades[22],[662,476])#wiwiwiwi
        self.Board.AddNode(fortList,[662,532])#hola hola 
        self.Board.AddNode(propiedades[23],[662,588])
        return self.Board

def getRows(excel_file, sheet_name, start_row = 1):
    excel_data = pd.read_excel(excel_file, sheet_name = sheet_name, header=None)
    size = excel_data.shape
    row_num = size[0]
    datax = []
    for i in range(start_row, row_num):
        data = excel_data.iloc[i].values.tolist()
        datax.append(data)
    return datax
chestList = []
fortList = []
propiedades = []
robar = []
def getLists(a:list, b:list, c:list, d:list):
    data = getRows(file, Sheet)
    for row in data:
        chest = Cofre(row[0],row[2], row[1])
        a.append(chest)
    data1 = getRows(File2,sheet)
    for row in data1:
        fort = Fortuna(row[0], row[2], row[1])
        b.append(fort)
    data2 = getRows(File3, sheet)
    for row in data2:
        carta = Propiedades(row[1],row[2],row[0])
        c.append(carta)
    data3= getRows(File4,sheet)
    for row in data3:
        robar = Robo(row[0],row[1])
        d.append(robar)
    return a,b,c,d

