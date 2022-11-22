import pandas as pd
from Cartas import Fortuna, Cofre, Propiedades
from Listas.listaCircular import listaCircular
file = "Cofre.xlsx"
Sheet = "Libro1"
File2 = "Fortuna.xlsx"
sheet = 'Hoja1'
File3 = "Propiedades.xlsx"

class Tablero:
    def __init__(self,Board:listaCircular) -> None:
        self.Board = Board
    def getBoard(self):
        getLists(chestList, fortList, propiedades)
        self.Board.AddNode("Go")
        self.Board.AddNode(propiedades[0])
        self.Board.AddNode(chestList)
        self.Board.AddNode(propiedades[1])
        self.Board.AddNode(propiedades[2])
        self.Board.AddNode("")
        self.Board.AddNode(propiedades[3])
        self.Board.AddNode(fortList)
        self.Board.AddNode(propiedades[4])
        self.Board.AddNode(propiedades[5])
        self.Board.AddNode("jail")
        self.Board.AddNode(propiedades[6])
        self.Board.AddNode(chestList)
        self.Board.AddNode(propiedades[7])
        self.Board.AddNode(propiedades[8])
        self.Board.AddNode("")
        self.Board.AddNode(propiedades[9])
        self.Board.AddNode(fortList)
        self.Board.AddNode(propiedades[10])
        self.Board.AddNode(propiedades[11])
        self.Board.AddNode("Parada libre")
        self.Board.AddNode(propiedades[12])
        self.Board.AddNode(chestList)
        self.Board.AddNode(propiedades[13])
        self.Board.AddNode(propiedades[14])
        self.Board.AddNode("")
        self.Board.AddNode(propiedades[15])
        self.Board.AddNode(propiedades[16])
        self.Board.AddNode(fortList)
        self.Board.AddNode(propiedades[17])
        self.Board.AddNode("Go to jail")
        self.Board.AddNode(propiedades[18])
        self.Board.AddNode(propiedades[19])
        self.Board.AddNode(chestList)
        self.Board.AddNode(propiedades[20])
        self.Board.AddNode("")
        self.Board.AddNode(propiedades[21])
        self.Board.AddNode(propiedades[22])
        self.Board.AddNode(fortList)
        self.Board.AddNode(propiedades[23])
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
def getLists(a:list, b:list, c:list):
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
    return a,b,c

