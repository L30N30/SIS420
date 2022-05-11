import timeit

numeroCiclos = 0
numeroIteraciones = 0

class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = None
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.accionAnterior = -1
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

    def setAccionAnterior(self, accion):
        self.accionAnterior = accion

    def getAccionAnterior(self):
        if self.accionAnterior != None:
            return self.accionAnterior
        else:
            return None

    def __str__(self):
        return str(self.get_estado())


def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)

        if nodo_actual.get_estado() == solucion:
            # Solución encontrada
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()

            # Lista de objetos Nodo
            lista_hijos = []
            dif = 0

            # Ciclo que cambia basado en la cantidad de elementos del vector
            for i in range(len(estado_nodo) - 1):
                if nodo_actual.getAccionAnterior() == i:
                    dif += 1
                    continue
                hijo = nodo_actual.get_estado()[:]
                anterior = hijo[i]
                hijo[i] = hijo[i+1]
                hijo[i+1] = anterior
                print(hijo)
                lista_hijos.append(Nodo(hijo))
                lista_hijos[i-dif].setAccionAnterior(i)

                if not lista_hijos[i-dif].en_lista(nodos_visitados) and not lista_hijos[i-dif].en_lista(nodos_frontera):
                    nodos_frontera.append(lista_hijos[i-dif])

            print('============')
            nodo_actual.set_hijo(lista_hijos)


if __name__ == "__main__":
    # El programa funciona con listas de cualquier tamaño (mayor a 1) siempre y cuando tengan los mismos elementos
    estado_inicial = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # Marca el tiempo transcurrido antes de comenzar la búsqueda
    inicioReloj = timeit.default_timer()

    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)

    # Marca el tiempo transcurrido una vez se finaliza la búsqueda
    finalReloj = timeit.default_timer()

    # Mostrar resultado
    numPasos = 0
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
        numPasos += 1
    resultado.append(estado_inicial)
    resultado.reverse()
    #for i  in range(len(resultado)):
        #print(resultado[i])
    print(resultado)
    print(f'Número de pasos: {numPasos}')
    print(f'Tiempo empleado: {round(finalReloj - inicioReloj,5)} segundos')