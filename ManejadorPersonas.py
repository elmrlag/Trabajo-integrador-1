import csv
from ClasePersona import Persona

class ManejadorPersonas:
    __lista = []

    def __init__(self):
        titulo = True
        archivo1 = open("integrantesProyectos.csv")
        reader = csv.reader(archivo1, delimiter=";")
        for fila in reader:
            if titulo == False:
                v1 = fila[0]
                v2 = fila[1]
                v3 = fila[2]
                v4 = fila[3]
                v5 = fila[4]
                UnaPersona = Persona(v1, v2, v3, v4, v5)
                self.__lista.append(UnaPersona)
            if titulo == True:
                titulo = False
        archivo1.close()

    def __len__(self):
        lista = list()
        lista = self.__lista
        return len(lista)

    def GetID(self, v1):
        return self.__lista[v1].GetID()

    def GetRol(self, v1):
        return  self.__lista[v1].GetRol()

    def GetCategoria(self, v1):
        return  self.__lista[v1].GetCategoria()