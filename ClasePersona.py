class Persona:
    __idProyecto = str
    __apellidoNombre = str
    __dni = int
    __categoriaInvestigacion = str
    __rol = str

    def __init__(self,v1 = 123,v2 = "asd",v3 = 32323,v4 = "II",v5 = "investigador"):
        self.__idProyecto = v1
        self.__apellidoNombre = v2
        self.__dni = v3
        self.__categoriaInvestigacion = v4
        self.__rol = v5

    def GetID(self):
        return self.__idProyecto

    def GetRol(self):
        return self.__rol

    def GetCategoria(self):
        return  self.__categoriaInvestigacion