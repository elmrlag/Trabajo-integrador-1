import csv
from ClaseProyecto import Proyecto

class ManejadorProyectos:
    __lista = []

    def __init__(self):
        titulo = True
        archivo2 = open("Proyectos.csv")
        reader = csv.reader(archivo2, delimiter=";")
        for fila in reader:
            if titulo == False:
                v1 = fila[0]
                v2 = fila[1]
                v3 = fila[2]
                UnProyecto = Proyecto(v1, v2, v3)
                self.__lista.append(UnProyecto)
            if titulo == True:
                titulo = False
        archivo2.close()

    def __len__(self):
        lista = list()
        lista = self.__lista
        return len(lista)

    def GetID(self, v1):
        return self.__lista[v1].GetID()

    def AlteraPuntos(self, v1, v2):
        self.__lista[v1].AlteraPuntosProyecto(v2)

    def Ordena(self, v1):
        if self.__lista[v1] > self.__lista[v1 - 1]:
            aux = self.__lista[v1]
            self.__lista[v1] = self.__lista[v1 - 1]
            self.__lista[v1 - 1] = aux
            return (True)

    def MuestraPuntos(self, v1):
        return (self.__lista[v1].GetPuntos())
