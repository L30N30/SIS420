import sys
import copy

sys.setrecursionlimit(100000)

espacio = ' '
numEspaciosTorres = 0
simboloTorre = 'I'
simboloDisco = '='

torre = 0
posicionDiscos = [[], [], []]


class Nodo:
    def __init__(self, estado, padre = None, hijo = None, accion = None, costo = 0):
        self.estado = estado
        self.padre = padre
        self.hijo = None
        self.accion = accion
        self.costo = costo
        self.heuristica = 0
        self.accion_anterior = 0
        self.set_hijo(hijo)

    def set_accion_anterior(self, accion):
        self.accion_anterior = accion

    def get_accion_anterior(self):
        return self.accion_anterior

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


def busqueda_estrella_hanoi(nodo_inicial, solucion, visitados, pieza_anterior):
    visitados.append(nodo_inicial.get_estado())
    print(nodo_inicial.get_estado())

    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        # Tres reglas de movimiento
        # 1 No mover el mismo disco más de una vez seguida
        # 2 Cualquier disco puede moverse sobre otro tres veces mayor a él mismo regla aritmética
        # 3 Heurística

        # Revisar si el nodo padre tiene registrado un paso anterior para no repetirlo


        nodo_estado = copy.deepcopy(nodo_inicial.get_estado()[:])
        #print(nodo_estado)

        lista_hijos = []
        nueva_pieza_anterior = []

        # Mueve todas las piezas
        for i in range(3):
            if len(nodo_estado[i]) > 0 and nodo_estado[i][-1] not in pieza_anterior:
                ad_ant = i - 1
                ad_pos = i + 1

                if ad_ant < 0: ad_ant = 2
                if ad_pos > 2: ad_pos = 0

                estado_anterior = copy.deepcopy(nodo_estado)
                estado_posterior = copy.deepcopy(nodo_estado)

                anterior = copy.deepcopy(estado_anterior[i][-1])
                posterior = copy.deepcopy(estado_posterior[i][-1])

                estado_anterior[ad_ant].append(anterior)
                estado_anterior[i].pop()
                estado_posterior[ad_pos].append(posterior)
                estado_posterior[i].pop()

                lista_hijos.append(Nodo(estado_anterior))
                lista_hijos.append(Nodo(estado_posterior))

                nueva_pieza_anterior.append(anterior)

        nodo_inicial.set_hijo(lista_hijos)

        heuristica = []

        for hijo_nodo in nodo_inicial.get_hijo():
            cache_heuristica = heuristica_costo(hijo_nodo)
            heuristica.append(cache_heuristica)
            hijo_nodo.setHeuristica(cache_heuristica)

        heuristica.sort()

        for i in range(len(heuristica)):
            for hijo_node in nodo_inicial.get_hijo():
                if hijo_node.getHeuristica() == heuristica[i] and not hijo_node.get_estado() in visitados:
                    recursiva = busqueda_estrella_hanoi(hijo_node, solucion, visitados, nueva_pieza_anterior)
                    if recursiva is not None:
                        return recursiva
        return None


def generar_fichas(numFichas):
    for i in range(1, numFichas + 1):
        posicionDiscos[0].append(i)
    posicionDiscos[0].reverse()
    return (numFichas * 2) + 1


def heuristica_costo(hijo):
    costo_heuristica = 0
    heuristica = 0

    for i in range(3):
        estadoHijo = copy.deepcopy(hijo.get_estado())
        if len(estadoHijo[i]) > 1 and estadoHijo[i][-1] > estadoHijo[i][-2]:
            heuristica += (estadoHijo[i][-1] + estadoHijo[i][-2]) * 100
        elif len(estadoHijo[i]) > 1 and estadoHijo[i][-1] < estadoHijo[i][-2]:
            sumAritmetica = 0
            diferencia = estadoHijo[i][-2] - estadoHijo[i][-1]
            cont = 1
            isRegla2 = False
            while diferencia >= sumAritmetica:
                sumAritmetica = (2 * cont) - 1
                if sumAritmetica == diferencia:
                    isRegla2 = True
                cont += 1
            if not isRegla2:
                heuristica += (estadoHijo[i][-1] + estadoHijo[i][-2]) * 100
        costo_heuristica = hijo.get_costo() + heuristica
    for i in range(3):
        if len(estadoHijo[i]) > 0:
            for pieza in estadoHijo[i]:
                costo_heuristica += pieza * posicion_costo(i)
    return costo_heuristica


def posicion_costo(parametro):
    match parametro:
        case 0:
            return 3
        case 1:
            return 2
        case 2:
            return 1


def dibujar(posicion_discos):
    trazoTorre_1 = []
    trazoTorre_2 = []
    trazoTorre_3 = []

    # Torre 1
    dif = 0
    i = 0
    while i < torre:
        if len(posicion_discos[0]) > 0 and dif < len(posicion_discos[0]):
            ficha = ''
            ficha += ((numEspaciosTorres*2) - posicion_discos[0][i - dif]) * espacio
            ficha += disco(posicion_discos[0][i - dif])
            ficha += ((numEspaciosTorres*2) - posicion_discos[0][i - dif]) * espacio
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
        if len(posicion_discos[1]) > 0 and dif < len(posicion_discos[1]):
            ficha = ''
            ficha += ((numEspaciosTorres * 2) - posicion_discos[1][i - dif]) * espacio
            ficha += disco(posicion_discos[1][i - dif])
            ficha += ((numEspaciosTorres * 2) - posicion_discos[1][i - dif]) * espacio
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
        if len(posicion_discos[2]) > 0 and dif < len(posicion_discos[2]):
            ficha = ''
            ficha += ((numEspaciosTorres * 2) - posicion_discos[2][i - dif]) * espacio
            ficha += disco(posicion_discos[2][i - dif])
            ficha += ((numEspaciosTorres * 2) - posicion_discos[2][i - dif]) * espacio
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


def disco(tamano):
    ficha = ((tamano*2)+1)*simboloDisco
    return ficha


if __name__ == '__main__':
    numUsuario = 0

    while numUsuario < 3:
        numUsuario = int(input('Ingrese el número de fichas: '))

    torre += generar_fichas(numUsuario)
    numEspaciosTorres = len(posicionDiscos[0])
    posicionDiscosSolucion = [[], [], posicionDiscos[0]]
    dibujar(posicionDiscos)

    nodosVisitados = []
    nodoInicial = Nodo(posicionDiscos)
    nodoInicial.set_costo(0)
    nodosVisitados.append(nodoInicial)

    # Formula aritmetica: 1+(2)(n−1) = 2n-1
    nodoSolucion = busqueda_estrella_hanoi(nodoInicial, posicionDiscosSolucion, nodosVisitados, [0])

    pasos = []
    padre = nodoSolucion
    num_pasos = 0
    while padre.get_padre() is not None:
        paso = padre.get_estado()
        pasos.append(paso)
        padre = padre.get_padre()
        num_pasos += 1
    pasos.append(nodoInicial)
    pasos.reverse()
    for i in range(0, len(pasos)):
        print(pasos[i])
        #dibujar(paso)
    print(f'Pasos empleados: {num_pasos}')