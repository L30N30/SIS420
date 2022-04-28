import sys
#sys.setrecursionlimit(100000)

espacio = ' '
numEspaciosTorres = 0
simboloTorre = 'I'
simboloDisco = '='

torre = 0
posicionDiscos = [[], [], []]


class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = None
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.heuristica = 0
        self.set_hijo(hijo)

    def setHeuristica(self, heuristica):
        self.heuristica = heuristica

    def getHeuristica(self):
        return self.heuristica

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


class NodoBI:
    def __init__(self, estado, padre = None, hijo = None, accion = None, costo = 0):
        self.estado = estado
        self.padre = padre
        self.hijo = None
        self.accion = accion
        self.costo = costo
        self.heuristica = 0
        self.set_hijo(hijo)

    def setHeuristica(self, heuristica):
        self.heuristica = heuristica

    def getHeuristica(self):
        return self.heuristica

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_datos(self, estado):
        self.estado = estado

    def get_datos(self):
      return self.estado

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_hijo(self, hijo):
        self.hijo = hijo
        if self.hijo is not None:
            for s in self.hijo:
                s.padre = self

    def get_hijo(self):
        return self.hijo

    def set_accion(self, accion):
        self.accion = accion

    def get_accion(self):
        return self.accion

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, nodo):
        if self.get_estado() == nodo.get_estado():
            return True
        else:
            return False

    def en_lista(self, nodo_lista):
        enlistado = False
        for n in nodo_lista:
            if self.equal(n):
                enlistado = True
        return enlistado

    def expandir(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, accion)
                for accion in problem.acciones(self.estado)]

    def obtenerCamino(self):
        #Retorna la lista de los nodos que conforman el camino desde el nodo inicio al nodo actual.
        nodo, camino_regreso = self, []
        while nodo:
            camino_regreso.append(nodo)
            nodo = nodo.padre
        return list(reversed(camino_regreso))

    def obtenerSolucion(self):
        #Retorna la secuencia de acciones desde el nodo inicio al nodo actual.
        return [nodo.accion for nodo in self.obtenerCamino()[1:]]

    def __str__(self):
        return str(self.get_estado())


def busqueda_estrella_hanoi(nodo_inicial, solucion, visitados, piezaAnterior):
    visitados.append(nodo_inicial.get_estado())

    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        # Tres reglas de movimiento
        # 1 No mover el mismo disco más de una vez seguida
        # 2 Cualquier disco puede moverse sobre otro tres veces mayor a él mismo regla aritmética
        # 3 Heurística

        nodo_estado = nodo_inicial.get_estado()[:][:]
        print(nodo_estado)
        #estadoNuevo = nodo_estado[:]

        listaHijos = []
        #listaHabilitados = []
        #piezaAnterior = 0
        menor = 0

        # Lista de piezas habilitadas para mover
        for i in range(3):
            #estadoNuevo = nodo_inicial.get_estado()[:][:]
            #cacheEstado = nodo_inicial.get_estado()[:][:]

            if len(nodo_estado[i]) > 0 and nodo_estado[i][-1] != piezaAnterior:
                adAnt = i - 1
                adPos = i + 1

                estadoNuevo = nodo_inicial.get_estado()[:][:]
                cacheEstado = nodo_inicial.get_estado()[:][:]

                print(f'{estadoNuevo} {cacheEstado}')

                if adAnt < 0: adAnt = 2
                if adPos > 2: adPos = 0

                estadoNuevo[adAnt].append(estadoNuevo[i][-1])
                cacheEstado[adPos].append(cacheEstado[i][-1])

                if len(estadoNuevo[i]) > 0: estadoNuevo[i].pop()
                if len(cacheEstado[i]) > 0: cacheEstado[i].pop()

                print(f'{estadoNuevo} {cacheEstado}')

                listaHijos.append(Nodo(estadoNuevo))
                listaHijos.append(Nodo(cacheEstado))
                listaHijos[-1].set_costo(nodo_inicial.get_costo()+1)
                listaHijos[-2].set_costo(nodo_inicial.get_costo()+1)

        nodo_inicial.set_hijo(listaHijos)

        heuristica = []

        for hijo_node in nodo_inicial.get_hijo():
            costo = heuristica_costo(hijo_node)
            hijo_node.setHeuristica(costo)
            heuristica.append(costo)
        #print(heuristica)
        heuristica.sort()

        for hijo_node in nodo_inicial.get_hijo():
            if hijo_node.getHeuristica == heuristica[0]:
                hijo_node.setHeuristica(heuristica_costo(hijo_node))
                recursiva = busqueda_estrella_hanoi(hijo_node, solucion, visitados, piezaAnterior)
                if recursiva is not None:
                    return recursiva
        return None


def heuristica_costo(hijo):
    costoHeuristica = 0
    heuristica = 0
    #estadoHijo = hijo.get_estado()[:]

    for i in range(3):
        estadoHijo = hijo.get_estado()[:]
        if len(estadoHijo[i]) > 1 and estadoHijo[i][-1] > estadoHijo[i][-2]:
            heuristica += (estadoHijo[i][-1] + estadoHijo[i][-2]) * 2
        elif len(estadoHijo[i]) > 1 and estadoHijo[i][-1] < estadoHijo[i][-2]:
            sumAritmetica = 0
            cont = 1
            isRegla2 = False
            while estadoHijo[i][-2] >= sumAritmetica:
                sumAritmetica = (2 * cont) - 1
                if sumAritmetica == (estadoHijo[i][-2] - estadoHijo[i][-1]):
                    isRegla2 = True
                cont += 1
            if not isRegla2:
                heuristica += estadoHijo[i][-1] + estadoHijo[i][-2]
        # if not hijo.get_estado() in visitados:
        costoHeuristica = hijo.get_costo() + heuristica
        #hijo.setHeuristica(costoHeuristica)
    return costoHeuristica


def generar_fichas(numFichas):
    for i in range(1, numFichas + 1):
        posicionDiscos[0].append(i)
    posicionDiscos[0].reverse()
    return (numFichas * 2) + 1


def disco(tamano):
    ficha = ((tamano*2)+1)*simboloDisco
    return ficha


def dibujar(posicionDiscos):
    trazoTorre_1 = []
    trazoTorre_2 = []
    trazoTorre_3 = []

    # Torre 1
    dif = 0
    i = 0
    while i < torre:
        if len(posicionDiscos[0]) > 0 and dif < len(posicionDiscos[0]):
            ficha = ''
            ficha += ((numEspaciosTorres*2) - posicionDiscos[0][i-dif])*espacio
            ficha += disco(posicionDiscos[0][i-dif])
            ficha += ((numEspaciosTorres*2) - posicionDiscos[0][i-dif])*espacio
            trazoTorre_1.append(ficha)
            trazoTorre_1.append(f'{espacio*(numEspaciosTorres*2)}{simboloTorre}{espacio*(numEspaciosTorres*2)}')
            i += 2
            dif += 1
        else:
            trazoTorre_1.append(f'{espacio*(numEspaciosTorres*2)}{simboloTorre}{espacio*(numEspaciosTorres*2)}')
            i += 1

    # Torre 2
    dif = 0
    i = 0
    while i < torre:
        if len(posicionDiscos[1]) > 0 and dif < len(posicionDiscos[1]):
            ficha = ''
            ficha += ((numEspaciosTorres * 2) - posicionDiscos[1][i - dif]) * espacio
            ficha += disco(posicionDiscos[1][i - dif])
            ficha += ((numEspaciosTorres * 2) - posicionDiscos[1][i - dif]) * espacio
            trazoTorre_2.append(ficha)
            trazoTorre_2.append(f'{espacio * (numEspaciosTorres * 2)}{simboloTorre}{espacio * (numEspaciosTorres * 2)}')
            i += 2
            dif += 1
        else:
            trazoTorre_2.append(f'{espacio * (numEspaciosTorres * 2)}{simboloTorre}{espacio * (numEspaciosTorres * 2)}')
            i += 1

    # Torre 3
    dif = 0
    i = 0
    while i < torre:
        if len(posicionDiscos[2]) > 0 and dif < len(posicionDiscos[2]):
            ficha = ''
            ficha += ((numEspaciosTorres * 2) - posicionDiscos[2][i - dif]) * espacio
            ficha += disco(posicionDiscos[2][i - dif])
            ficha += ((numEspaciosTorres * 2) - posicionDiscos[2][i - dif]) * espacio
            trazoTorre_3.append(ficha)
            trazoTorre_3.append(f'{espacio * (numEspaciosTorres * 2)}{simboloTorre}{espacio * (numEspaciosTorres * 2)}')
            i += 2
            dif += 1
        else:
            trazoTorre_3.append(f'{espacio * (numEspaciosTorres * 2)}{simboloTorre}{espacio * (numEspaciosTorres * 2)}')
            i += 1

    trazoTorre_1.reverse()
    trazoTorre_2.reverse()
    trazoTorre_3.reverse()
    for i in range(len(trazoTorre_1)):
        print(f'{trazoTorre_1[i]}{trazoTorre_2[i]}{trazoTorre_3[i]}')


if __name__ == '__main__':
    numUsuario = 0

    while numUsuario < 3:
        numUsuario = int(input('Ingrese el número de fichas: '))

    torre += generar_fichas(numUsuario)
    numEspaciosTorres = len(posicionDiscos[0])
    posicionDiscosSolucion = [[], [], posicionDiscos[0]]
    #dibujar(posicionDiscos)

    nodosVisitados = []
    nodoInicial = Nodo(posicionDiscos)
    nodoInicial.set_costo(0)
    nodosVisitados.append(nodoInicial)

    # Formula aritmetica: 1+(2)(n−1) = 2n-1
    #heuristica_costo(nodoInicial)
    nodoSolucion = busqueda_estrella_hanoi(nodoInicial, posicionDiscosSolucion, nodosVisitados, 0)

    pasos = []
    padre = nodoSolucion
    while padre.get_padre() is not None:
        pasos.append(padre.get_estado())
        padre = padre.get_padre()
    pasos.append(nodoInicial)
    pasos.reverse()
    for nodo in pasos:
        dibujar(nodo.get_estado())