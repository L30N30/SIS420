import random
import math
import copy


distanciaMinima = (math.sqrt((10*10)+(10*10)))
largo = 10
tamano_poblacion = 100
valor_minimo_gen = 0
valor_maximo_gen = 10
precision = 30
probabilidad_mutacion = 0.2  # La probabilidad de que un individuo mute


def crear_individuo():
    creados = []
    individuo = []
    while len(individuo) < 10:
        gen = 10 * random.randint(valor_minimo_gen, valor_maximo_gen)
        if gen not in creados:
            individuo.append(gen)
            creados.append(gen)
        gen = 0
    return individuo


def crear_poblacion(numero_individuos):
    poblacion = []
    while len(poblacion) <= numero_individuos:
        poblacion.append(crear_individuo())
    return poblacion


def distancia(gen1, pos1, gen2, pos2):
    return math.sqrt(((gen1-gen2)**2) + ((pos1-pos2)**2))


def procrear(individuo1, individuo2):
    pos11 = random.randint(0, 9)
    pos12 = int(pos11)

    while pos12 == pos11:
        pos12 = random.randint(0, 9)

    pos21 = -1
    pos22 = -1

    for i in individuo2:
        if individuo1[pos11] == i:
            pos21 = int(i.__pos__())
        elif individuo1[pos12] == i:
            pos22 = int(i.__pos__())

    hijo = []
    for i in individuo1:
        if i.__pos__() == pos11:
            hijo.append(individuo2[pos22])
        elif i.__pos__() == pos12:
            hijo.append(individuo2[pos21])
        else:
            hijo.append(i)
    return hijo


def mutar_individuo(individuo):
    if random.randint(0, probabilidad_mutacion*100) == 0:
        posInf = random.randint(0, 4)
        posPos = random.randint(5, 9)
        anterior = individuo[posInf]
        individuo[posInf] = individuo[posPos]
        individuo[posPos] = anterior
    return individuo


def calcular_fitness(individuo):
    fitness = 0
    copy = individuo[:]
    for i in range(0, 10):
        for j in range(0, 10):
            if copy[i] == copy[j]:
                continue
            if distancia(copy[i], (i*10), copy[j], (j*10)) < distanciaMinima:
                fitness += 10
            elif distancia(copy[i], (i*10), copy[j], (j*10)) <= 100:
                fitness += 1
            if distancia(copy[i], (i*10), copy[j], (j*10)) >= 100:
                if fitness >= 5:
                    fitness -= 5
    return abs(fitness)


def takeSecond(elem):
    return elem[1]


def run():
    poblacion = crear_poblacion(tamano_poblacion)
    poblacion_medida = []

    for i in poblacion:
        poblacion_medida.append([i, calcular_fitness(i)])
    poblacion_medida.sort(key=takeSecond)
    print(poblacion_medida)

    resuelto = False
    solucion = None
    fit = 0
    while not resuelto:
        if poblacion_medida[0][1] == 0:
            solucion = poblacion_medida[0][0]
            fit = poblacion_medida[0][1]
            resuelto = True
        else:
            poblacion_nueva = []
            # Mutación
            for i in range(0, len(poblacion_medida)):
                poblacion_nueva.append([mutar_individuo(poblacion_medida[i][0]), calcular_fitness(poblacion_medida[i][0])])
            poblacion_nueva.sort(key=takeSecond)

            # Procrear
            #for i in range(0, precision):
                #hijo = procrear(poblacion_nueva[i][0], poblacion_nueva[i+1][0])
                #poblacion_nueva.append([hijo, calcular_fitness(hijo)])
            #poblacion_nueva.sort(key=takeSecond)

            # Eliminar el exceso en la población
            while len(poblacion_nueva) > tamano_poblacion:
                poblacion_nueva.pop()

            poblacion_nueva.sort(key=takeSecond)
            poblacion_medida = copy.deepcopy(poblacion_nueva)
            print(poblacion_medida)
    print(solucion)
    print(fit)

run()