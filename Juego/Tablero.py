import pandas as pd
from Cartas import Fortuna, Cofre, Propiedades
from Listas.listaCircular import listaCircular
file = "Cofre.xlsx"
Sheet = "Libro1"
File2 = "Fortuna.xlsx"
sheet = 'Hoja1'
File3 = "Propiedades.xlsx"


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
def getBoard():
    getLists(chestList, fortList, propiedades)
    Board =listaCircular()

    Board.AddNode("go")
    Board.AddNode(propiedades[0])
    Board.AddNode(chestList)
    Board.AddNode(propiedades[1])
    Board.AddNode(propiedades[2])
    Board.AddNode("")
    Board.AddNode(propiedades[3])
    Board.AddNode(fortList)
    Board.AddNode(propiedades[4])
    Board.AddNode(propiedades[5])
    Board.AddNode("jail")
    Board.AddNode(propiedades[6])
    Board.AddNode(chestList)
    Board.AddNode(propiedades[7])
    Board.AddNode(propiedades[8])
    Board.AddNode("")
    Board.AddNode(propiedades[9])
    Board.AddNode(fortList)
    Board.AddNode(propiedades[10])
    Board.AddNode(propiedades[11])
    Board.AddNode("Parada libre")
    Board.AddNode(propiedades[12])
    Board.AddNode(chestList)
    Board.AddNode(propiedades[13])
    Board.AddNode(propiedades[14])
    Board.AddNode("")
    Board.AddNode(propiedades[15])
    Board.AddNode(propiedades[16])
    Board.AddNode(fortList)
    Board.AddNode(propiedades[17])
    Board.AddNode("Go to jail")
    Board.AddNode(propiedades[18])
    Board.AddNode(propiedades[19])
    Board.AddNode(chestList)
    Board.AddNode(propiedades[20])
    Board.AddNode("")
    Board.AddNode(propiedades[21])
    Board.AddNode(propiedades[22])
    Board.AddNode(fortList)
    Board.AddNode(propiedades[23])


    return Board
