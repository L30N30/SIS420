import random
import math


distanciaMinima = (math.sqrt((10*10)+(10*10)))
largo = 10
tamano_poblacion = 100
valor_minimo_gen = 0
valor_maximo_gen = 100
precision = 30  # Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
probabilidad_mutacion = 0.2  # La probabilidad de que un individuo mute


def crear_individuo():
    creados = []
    individuo = []
    while len(individuo) < 10:
        gen = 10 * random.randint(0, 10)
        if gen not in creados:
            individuo.append(gen)
            creados.append(gen)
        gen = 0


def crear_poblacion(numero_individuos):
    poblacion = []
    while len(poblacion) < (numero_individuos+1):
        poblacion.append(crear_individuo())
    return poblacion


def distancia(gen1, pos1, gen2, pos2):
    return math.sqrt(((gen1-gen2)**2) + ((pos1-pos2)**2))


def calcular_fitness(individuo):
    fitness = 0
    copy = individuo[:]
    for i in range(0, 10):
        for j in range(0, 10):
            if copy[i] == copy[j]:
                continue
            if distancia(copy[i], (i*10), copy[j], (j*10)) < distanciaMinima:
                fitness += 10000
            else:
                fitness += distancia(copy[i], (i*10), copy[j], (j*10))
    return fitness


def run():
    poblacion = crear_poblacion(tamano_poblacion)
    print(poblacion)
    poblacion_medida = []

    for i in poblacion:
        poblacion_medida.append([i, calcular_fitness(i)])
    print(poblacion)


run()