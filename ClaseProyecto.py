class Proyecto:
    __idProyecto = str
    __titulo = str
    __palabrasClave = str
    __puntos = int

    def __init__(self, v1 = "asd",v2 = "asd",v3 = 0):
        self.__idProyecto = v1
        self.__titulo = v2
        self.__palabrasClave = v3
        self.__puntos = 0

    def GetID(self):
        return self.__idProyecto

    def GetPuntos(self):
        return self.__puntos

    def AlteraPuntosProyecto(self, v1):
        self.__puntos += v1

    def __gt__(self, other):
        retorna = False
        if type(other) == type(self):
            if self.__puntos > other.GetPuntos():
                retorna = True
        return retorna
