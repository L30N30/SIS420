import random
import time


def crear_poblacion(numero, longitud):
    pob = []
    for i in range(numero):
        pob.append(crear_individuo(longitud))
    return pob


# Crea individuos con valores al azar entre 0 y diez veces la longitud
def crear_individuo(longitud):
    indiv = []
    for i in range(longitud):
        # num = random.randint(((i*10)-10), (i*10))
        indiv.append(random.randint(1, (longitud*10)))
    return indiv


# Incrementa el valor de fitness mientras más sea la diferencia entre el puntaje de un individuo y su puesto
def fitness(individuo):
    fit = 0
    for i in range(len(individuo)):
        inf = (i * 10) + 1
        sup = (i * 10) + 10
        fit += abs(sup - individuo[i])
    return fit


def mutar(individuo, longitud):
    hijo_mutado = []
    pos_mutacion = random.randint(0, len(individuo)-1)

    for i in range(len(individuo)):
        if i == pos_mutacion:
            hijo_mutado.append(random.randint(1, longitud*10))
        else:
            hijo_mutado.append(individuo[i])

    return hijo_mutado


def procrear(individuo1, individuo2):
    hijo = []
    for i in range(len(individuo1)):
        if i%2 == 0:
            hijo.append(individuo1[i])
        else:
            hijo.append(individuo2[i])
    return hijo


def sort_key(company):
    return company[1]


def run():
    num_procreacion = 30
    prob_mutacion = 0.1
    numero_empleados = 10
    numero_individuos = 100

    individuos = crear_poblacion(numero_individuos, numero_empleados)
    individuos_fit = []

    for i in individuos:
        individuos_fit.append([i, fitness(i)])
    individuos_fit.sort(key=sort_key)

    start = time.time()

    resuelto = False

    while not resuelto:
        if individuos_fit[0][1] == 0:
            resuelto = True
        else:
            individuos = []
            cont = 0
            # Reiniciar la lista de individuos
            for i in individuos_fit:
                individuos.append(i[0])

            # Procrear mejores individuos
            for i in range(num_procreacion):
                individuos.append(procrear(individuos[i], individuos[i+1]))

            # Mutar individuos al azar
            for i in range(len(individuos)):
                if random.randint(0, (prob_mutacion*100)) == 0:
                    individuos.append(mutar(individuos[i], numero_empleados))
                    individuos.pop(i)

            individuos_fit = []
            # Sacar el fitness de la nueva población y ordenarla
            for i in individuos:
                individuos_fit.append([i, fitness(i)])
            individuos_fit.sort(key=sort_key)

            # Reducir la población al número de individuos original
            while len(individuos_fit) > numero_individuos:
                individuos_fit.pop()
            print(individuos_fit)

    end = time.time()

    print(individuos_fit[0][0])
    print(end - start)

run()