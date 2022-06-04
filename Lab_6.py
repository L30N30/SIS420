import random
import time


nombres = ['Alberto', 'José', 'María', 'Daniel', 'Benjamin', 'Pablo', 'Antonio', 'Debora', 'Ivana', 'Leonardo',
           'Danilo', 'Mateo', 'Elva', 'Isabel', 'Alejandro', 'Alejandra', 'Roberto', 'Dana', 'Sara', 'Monica',
           'Veronica', 'Wendy', 'Nicole', 'Dayana', 'Marco']


def sort_key(lista):
    return lista[1]


# Crea una lista aleatoria con nombres escogidos al azar
def asignar_puntajes(longitud):
    lista = []

    for i in range(longitud * 10):
        lista.append(random.choice(nombres))

    # print(lista)
    return lista


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


# Muta el individuo en una sola posición
def mutar(individuo, longitud):
    hijo_mutado = []
    pos_mutacion = random.randint(0, len(individuo)-1)

    for i in range(len(individuo)):
        if i == pos_mutacion:
            hijo_mutado.append(random.randint(1, longitud*10))
        else:
            hijo_mutado.append(individuo[i])

    return hijo_mutado


# Recibe dos individuos y los cruza en posiciones intercaladas
def procrear(individuo1, individuo2):
    hijo = []
    for i in range(len(individuo1)):
        if i % 2 == 0:
            hijo.append(individuo1[i])
        else:
            hijo.append(individuo2[i])
    return hijo


# Realiza la búsqueda
def run():
    # Lista de los puestos disponibles
    lista_puestos = ['Jefe', 'Sub Jefe', 'Manager', 'Ingeniero 1', 'Ingeniero 2',
                     'Administrador 1', 'Administrador 2', 'Secretario 1', 'Secretario 2', 'Secretario 3']

    quitar_duplicados = False  # Quita los duplicados de la población
    mantener_poblacion = False  # Repoblación al azar en caso de haber un número menor al especificado
    controlar_sobrepoblacion = True  # Mantiene el número de población menor o igual al especificado

    # Recomendado = 300, siempre menor al número de individuos (razón de 1/3 número de individuos)
    num_procreacion = 300
    prob_mutacion = 0.2  # Recomendado = 20%
    numero_empleados = int(len(lista_puestos))  # Recomendado = 10
    numero_individuos = 1000  # Recomendado = 1000

    lista_nombres = asignar_puntajes(numero_empleados)
    poblacion = crear_poblacion(numero_individuos, numero_empleados)
    individuos_fit = []

    for i in poblacion:
        individuos_fit.append([i, fitness(i)])
    individuos_fit.sort(key=sort_key)

    resuelto = False
    ciclos = 0

    start = time.time()

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
                if random.randint(0, int(100/(prob_mutacion*100) - 1)) == 0:
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

    # Imprime a los empleados contratados y sus puestos
    for i in range(numero_empleados):
        print(f'Puesto de {lista_puestos[i]}: {lista_nombres[i*10]}')
    end = time.time()
    tiempo = round(end - start, 3)

    print('====================')
    print(f'Individuo ideal: {individuos_fit[0][0]}')
    print(f'Tiempo: {tiempo} seg')
    print(f'{ciclos} generaciones')


run()