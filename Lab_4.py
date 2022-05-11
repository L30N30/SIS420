class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = None
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.set_hijo(hijo)

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_hijo(self, hijo):
        self.hijo = hijo
        if self.hijo is not None:
            for s in self.hijo:
                s.padre = self

    def get_hijo(self):
        return self.hijo

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_accion(self, accion):
        self.padre = accion

    def get_accion(self):
        return self.accion

    def set_acciones(self, acciones):
        self.acciones = acciones

    def get_acciones(self):
        return self.acciones

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, Nodo):
        if self.get_estado() == Nodo.get_estado():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_estado())


vacio = ''
pastor = 'P'
oveja = 'O'
lobo = 'L'
hierba = 'H'


def busca_solucion(estado_inicial, solucion, frente_rio):
    """nodo_inicial = Nodo(estado_inicial)
    nodos_frontera = []
    nodos_frontera.append(nodo_inicial)"""
    nodos_frontera = []
    nodos_visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)
    pastor_esta_frente = False

    nodo_actual = nodos_frontera.pop(0)
    # nodos_frontera.pop()
    estado_actual = nodo_actual.get_estado()

    if nodo_actual not in nodos_visitados:
        nodos_visitados.append(nodo_actual)

    if nodo_actual.get_estado() == solucion:
        print('osiiii')
        return nodo_actual
    else:
        lista_nodos_hijo = []

        if pastor_esta_frente:
            estado_actual[0][0] = pastor
            estado_actual[1][0] = vacio
            pastor_esta_frente = False
        else:
            estado_actual[0][0] = vacio
            estado_actual[1][0] = pastor
            pastor_esta_frente = True

        for i in range(1, len(estado_actual[0])):
            nuevo_estado = estado_actual[:]

            if nuevo_estado[0][i] != vacio and nuevo_estado[0][0] == vacio:
                nuevo_estado[0][i] = vacio
                nuevo_estado[1][i] = simbolo(i)
            elif nuevo_estado[1][i] != vacio and nuevo_estado[1][0] == vacio:
                nuevo_estado[1][i] = vacio
                nuevo_estado[0][i] = simbolo(i)

            lista_nodos_hijo.append(Nodo(nuevo_estado))

            if not lista_nodos_hijo[i - 1].en_lista(nodos_visitados) and not lista_nodos_hijo[i - 1].en_lista(
                    nodos_frontera):
                nodos_frontera.append(lista_nodos_hijo[i - 1])
            print(nuevo_estado[0])
            print(nuevo_estado[1])

        nodo_actual.set_hijo(lista_nodos_hijo)


def simbolo(posicion):
    match posicion:
        case 1:
            return oveja
        case 2:
            return lobo
        case 3:
            return hierba


def heuristica(estado):
    calidad = 0
    animales = []

    for i in estado[1]:
        if i != vacio:
            if i != pastor: animales.append(i)
            calidad += 1
    if len(animales) > 1:
        for i in range(0, len(animales)):
            match animales[i]:
                case 'O':
                    for j in range(i, len(animales)):
                        if j+1 < len(animales):
                            if animales[j+1] == lobo and estado[1][0] != pastor: calidad = 0
                            elif animales[j+1] == hierba and estado[1][0] != pastor: calidad = 0
                case "L":
                    for j in range(i, len(animales)):
                        if j + 1 < len(animales):
                            if animales[j + 1] == oveja and estado[1][0] != pastor: calidad = 0
                case 'H':
                    for j in range(i, len(animales)):
                        if j + 1 < len(animales):
                            if animales[j + 1] == oveja and estado[1][0] != pastor: calidad = 0
    return calidad


if __name__ == '__main__':
    Inicio = [['P', 'O', 'L', 'H'], ['', '', '', '']]
    Solucion = [['', '', '', ''], ['P', 'O', 'L', 'H']]

    NodoSolucion = busca_solucion(Inicio, Solucion, Inicio)
    nodo_actual = NodoSolucion
    resultado = []

    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(Inicio)
    resultado.reverse()

    for i in range(len(resultado)):
        print(resultado[i])
        print('=====================')