import random
import time


# Crea una población del tamaño especificado
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
        if i % 2 == 0:
            hijo.append(individuo1[i])
        else:
            hijo.append(individuo2[i])
    return hijo


def sort_key(company):
    return company[1]


def run():
    quitar_duplicados = False  # Quita los duplicados de la población
    mantener_poblacion = False  # Repoblación al azar en caso de haber un número menor al especificado
    controlar_sobrepoblacion = True  # Mantiene el número de población menor o igual al especificado

    num_procreacion = 30  # Recomendado = 30, menor al número de individuos
    prob_mutacion = 0.1
    numero_empleados = 10  # Recomendado = 10
    numero_individuos = 1000  # Recomendado = 1000

    poblacion = crear_poblacion(numero_individuos, numero_empleados)
    individuos_fit = []

    for i in poblacion:
        individuos_fit.append([i, fitness(i)])
    individuos_fit.sort(key=sort_key)

    start = time.time()

    resuelto = False
    ciclos = 0

    while not resuelto:
        if individuos_fit[0][1] == 0:
            resuelto = True
        else:
            ciclos += 1
            poblacion = []
            cont = 0
            # Reiniciar la lista de individuos
            for i in individuos_fit:
                poblacion.append(i[0])

            # Quitar duplicados
            if quitar_duplicados:
                # print('Purgando duplicados...')
                result = []
                for i in poblacion:
                    if i not in result:
                        result.append(i)
                poblacion = []
                poblacion = result

            # Repoblación nueva
            if mantener_poblacion and (len(poblacion) < numero_individuos):
                # print('Repoblando...')
                while len(poblacion) < numero_individuos:
                    poblacion.append(crear_individuo(numero_empleados))

            # Procrear mejores individuos
            for i in range(num_procreacion):
                poblacion.append(procrear(poblacion[i], poblacion[i+1]))

            # Mutar individuos al azar
            for i in range(len(poblacion)):
                if random.randint(1, 100/(prob_mutacion*100)) == 1:
                    poblacion.append(mutar(poblacion[i], numero_empleados))
                    poblacion.pop(i)

            individuos_fit = []
            # Sacar el fitness de la nueva población y ordenarla
            for i in poblacion:
                individuos_fit.append([i, fitness(i)])
            individuos_fit.sort(key=sort_key)

            # Reducir la población al número de individuos original
            if controlar_sobrepoblacion:
                # print('Purgando sobrepoblación...')
                while len(individuos_fit) > numero_individuos:
                    individuos_fit.pop()

            # print(individuos_fit)
            # print(f'Número de población: {len(individuos_fit)}')

    end = time.time()
    tiempo = round(end-start, 3)

    return individuos_fit[0][0], tiempo, ciclos

    # print('====================')
    # print(individuos_fit[0][0])
    # print(f'Tiempo: {round(end-start, 3)} seg')
    # print(f'{ciclos} generaciones')


def testing_grounds(numero_pruebas):
    suma = 0
    minimo = 1000
    maximo = 0

    for i in range(numero_pruebas):
        individuo, tiempo, ciclos = run()

        if tiempo > maximo:
            maximo = float(tiempo)
        if tiempo < minimo:
            minimo = float(tiempo)

        suma += tiempo
        # print(f'Individuo: {individuo}')
        print(f'Tiempo {i+1}: {tiempo}')
        # print(f'Generaciones: {ciclos}')

    print('=========================')
    print(f'Tiempo promedio: {round(suma/numero_pruebas, 3)}')
    print(f'Tiempo mínimo: {minimo}')
    print(f'Tiempo máximo: {maximo}')


testing_grounds(100)
print('dan')