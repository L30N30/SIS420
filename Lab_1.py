# Librerías necesarias
import time
import random

# Símbolos
vacio = '*'
robot = 'R'
robotPlaga = 'r'
cuervo = 'C'
insecto = 'I'
hierba = 'H'
reaccion = 'X'
ninguna = 'ninguna'

# Matriz inicial 4x4
matriz = [[robot, vacio, vacio, vacio],
          [vacio, vacio, vacio, vacio],
          [vacio, vacio, vacio, vacio],
          [vacio, vacio, vacio, vacio]]

# Posición robot
posRobot = [0, 0]

# Reglas de acción-reacción
PROTOCOLOS = {
    'C': 'humo',
    'I': 'fumigación',
    'H': 'extirpación'}


# Clase Agente Reactivo
class robotReactivoSimple:
    def __init__(self, protocolo):
        self.protocolo = protocolo

    def reaccionar(self, percepcion):
        if not percepcion:
            return ninguna
        if percepcion in self.protocolo.keys():
            return self.protocolo[percepcion]
        return ninguna


# Inicializador del programa
def start():
    # Descripción del programa
    print('El agente debe corresponder con un robot que espanta aves, insectos u otro tipo de plagas en un sembradío.')
    print('Debe recorrer el sembradio por cuadrantes y aplicar un tipo de accion para eliminar la amenaza de los cultivos, el agente deberá funciona indeterminadamente.')
    print('')
    print('----------------------------------')
    print('SIMBOLOGÍA')
    print('')
    print(f'Cuadrante vacío:    {vacio}')
    print(f'Robot/Agente:    {robot}')
    print(f'Robot/Agente sobre una plaga:    {robotPlaga}')
    print(f'Plagas:    {cuervo}/{hierba}/{insecto}')
    print(f'Cuadrante con plagas eliminadas:    {reaccion}')
    print('----------------------------------')

    # Reglas
    print('REGLAS')
    print('')
    print('Humo espanta a: Cuervo')
    print('Fumigación elimina: Insectos')
    print('Extirpación elimina a: Hierbas')
    print('----------------------------------')
    print('')

    # Tamaño mínimo del sembradío: 4x4
    print('Introduzca las dimensiones del sembradío (mayor o igual a 4x4)')

    filas = 1
    columnas = 1

    while columnas < 4:
        columnas = int(input('Numero de columnas: '))
    while filas < 4:
        filas = int(input('Numero de filas: '))

    # Ajuste de matriz (sembradío)
    if filas > 4:
        for i in range(4, filas):
            tempFila = [vacio]
            for j in range(1,4):
                tempFila.append(vacio)
            matriz.append(tempFila)

    if columnas > 4:
        for i in range(0, filas):
            for j in range(4, columnas):
                matriz[i].append(vacio)

    generar_plagas(columnas, filas)
    dibujar_sembradio(columnas, filas, 'Matriz generada...')
    # Iniciar Agente
    correrRobot(columnas, filas)


# Generación de plagas en el sembradío al azar usando probabilidades relativas a las dimensiones
def generar_plagas(columna, fila):
    print('Generando plagas...')
    time.sleep(1)

    prob = 0
    if columna > fila:
        prob = fila
    else:
        prob = columna
    # prob = int((columna*fila)/8)

    for i in range(0,fila):
        for j in range(0,columna):
            if azar(prob) == 1:
                if matriz[i][j] == vacio:
                    if i != 0 or j != 0:
                        matriz[i][j] = plaga()


# Dibujar el sembradío en la consola
def dibujar_sembradio(columna, fila, mensaje):
    for i in range(0, fila):
        for j in range(0, columna):
            print(f'{matriz[i][j]}  ', end='')
        print('')

    print(mensaje)
    print('')


# Generación al azar de un tipo de plaga
def plaga():
    select = 0
    select = random.randint(1,3)

    match select:
        case 1:
            return cuervo
        case 2:
            return insecto
        case 3:
            return hierba


# Booleano de probabilidad
def azar(prob):
    if random.randint(1,prob) == 1:
        return 1


# Mueve el robot celda por celda, evaluando los parámetros gráficos y plagas en cada ciclo
def moverAgente(columna, fila, agente):
    log = ''

    if posRobot[0] == fila-1 and posRobot[1] == columna-1:
        matriz[posRobot[0]][posRobot[1]] = vacio
        posRobot[0] = 0
        posRobot[1] = 0
        for i in range(0, fila):
            for j in range(0, columna):
                matriz[i][j] = vacio
        print('Todas las plagas han sido eliminadas.')
        time.sleep(2)
        matriz[0][0] = robot
        print('Reiniciando sembradío...')
        dibujar_sembradio(columna,fila,'')
        time.sleep(1.5)
        generar_plagas(columna, fila)

    else:
        if posRobot[1] < columna-1:
            if matriz[posRobot[0]][posRobot[1]] == robotPlaga:
                matriz[posRobot[0]][posRobot[1]] = reaccion
            else:
                matriz[posRobot[0]][posRobot[1]] = vacio
            posRobot[1] += 1

            if agente.reaccionar(matriz[posRobot[0]][posRobot[1]]) != ninguna:
                log = f'El robot ha utilizado {agente.reaccionar(matriz[posRobot[0]][posRobot[1]])} para eliminar: {plagaString(matriz[posRobot[0]][posRobot[1]])}'
            evaluarCelda(agente)
        else:
            if matriz[posRobot[0]][posRobot[1]] == robotPlaga:
                matriz[posRobot[0]][posRobot[1]] = reaccion
            else:
                matriz[posRobot[0]][posRobot[1]] = vacio

            posRobot[0] += 1
            posRobot[1] = 0

            if agente.reaccionar(matriz[posRobot[0]][posRobot[1]]) != ninguna:
                log = f'El robot ha utilizado {agente.reaccionar(matriz[posRobot[0]][posRobot[1]])} para eliminar: {plagaString(matriz[posRobot[0]][posRobot[1]])}'
            evaluarCelda(agente)

    dibujar_sembradio(columna, fila, log)


# Devuelve el nombre de cada plaga basado en la percepción de cada una
def plagaString(codigo):
    match codigo:
        case 'C':
            return 'Cuervo'
        case 'I':
            return 'Insecto'
        case 'H':
            return 'Hierbas'


# Maneja la simbología de acción-reacción cuando una plaga es detectada
def evaluarCelda(agente):
    if agente.reaccionar(matriz[posRobot[0]][posRobot[1]]) != ninguna:
        matriz[posRobot[0]][posRobot[1]] = robotPlaga
    else:
        matriz[posRobot[0]][posRobot[1]] = robot


# Ciclo infinito que corre el programa con el agente inicializado
def correrRobot(columnas, filas):
    agenteRobot = robotReactivoSimple(PROTOCOLOS)

    while True:
        time.sleep(0.8)
        moverAgente(columnas, filas, agenteRobot)


# Iniciar programa
start()