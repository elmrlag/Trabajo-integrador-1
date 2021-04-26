from ManejadorPersonas import ManejadorPersonas
from ManejadorProyectos import ManejadorProyectos

def CalcularPuntosxProyecto():
    print("Se iniciar cálculo")
    i = 0

    while i < LargoMProyectos:
        print(f"---------- Proyecto {i} ----------")
        IdProyecto = MProyectos.GetID(i)
        j = 0
        Integrantes = 0

        CategorDirSolicitado = False
        DirectorEncontrado = False

        CategorCodirSolicitado = False
        CodirectorEncontrado = False

        while j < LargoMPersonas:
            if MPersonas.GetID(j) == IdProyecto:
                Integrantes += 1

                #Busca director
                if MPersonas.GetRol(j) == "director":
                    DirectorEncontrado = True
                    print("CATEGORIAS DE DIRECTOR", MPersonas.GetCategoria(j))
                    if MPersonas.GetCategoria(j) == "I" or MPersonas.GetCategoria(j) == "II":
                        CategorDirSolicitado = True

                #Busca codirector
                if MPersonas.GetRol(j) == "codirector":
                    CodirectorEncontrado = True
                    print("CATEGORIAS DE CODIRECTOR", MPersonas.GetCategoria(j))
                    if MPersonas.GetCategoria(j) == "I" or MPersonas.GetCategoria(j) == "II" or MPersonas.GetCategoria(j) == "III":
                        CategorCodirSolicitado = True

            j += 1

        #Categoria codirector
        if CodirectorEncontrado == True:
            if CategorCodirSolicitado == False:
                MProyectos.AlteraPuntos(i,-5)
                print("El codirector debe ser de categoria I, II o III (Se restan 5 puntos)")
            else:
                MProyectos.AlteraPuntos(i,10)
                print("El codirector cumple con los requisitos")
        else:
            print("El proyecto debe tener un codirector (Se restan 10 puntos)")
            MProyectos.AlteraPuntos(i,-10)

        #Categoria director
        if DirectorEncontrado == True:
            if CategorDirSolicitado == False:
                MProyectos.AlteraPuntos(i,-5)
                print("El director debe ser de categoria I o II (Se restan 5 puntos)")
            else:
                MProyectos.AlteraPuntos(i,10)
                print("El director cumple con el requisito")
        else:
            print("El proyecto debe tener un director (Se restan 10 puntos)")
            MProyectos.AlteraPuntos(i,-10)

        #Cantidad de integrantes
        if Integrantes >= 3:
            MProyectos.AlteraPuntos(i,10)
            print("El proyecto cumple el requisito de 3 integrantes como mínimo")
        else:
            MProyectos.AlteraPuntos(i,-20)
            print("El proyecto debe tener como mínimo 3 integrantes (Se restan 20 puntos)")

        print(f"Lo puntos son de {MProyectos.MuestraPuntos(i)}")
        print("------------------------------")
        i += 1

def OrdenarProyectosxPuntos():
    intercambios = True
    numPasada = i = LargoMProyectos - 1
    while numPasada > 0 and intercambios:
        intercambios = False
        while i > 0:
            intercambios = MProyectos.Ordena(i)
            i -= 1
        numPasada = numPasada - 1

    i = 0
    while i < LargoMProyectos:
        print(MProyectos.MuestraPuntos(i))
        i += 1


if __name__ == '__main__':
    MProyectos = ManejadorProyectos()
    MPersonas = ManejadorPersonas()

    LargoMProyectos = len(MProyectos)
    LargoMPersonas = len(MPersonas)

    print("Procedemos a calcular los puntos por proyecto")
    CalcularPuntosxProyecto()
    OrdenarProyectosxPuntos()