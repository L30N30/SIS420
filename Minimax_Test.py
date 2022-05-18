import copy
import random

equis = 'X'
circulo = 'O'

""" Estructura de aplicación
    FUNCIONES:  dibujar, pasos disponibles
    HEURÍSTICA: Menor mientras hayan opciones de ganar y si hay una jugada ganadora posible."""


def isBreakRow(dimension, actual):
    # Devuelve verdadero o falso dependiendo si se trata de una nueva fila
    if actual%dimension == 0: return True
    else: return False


def estadoJuego(tabla, dimension, bloqueados):
    revisados = []

    for i in range(1, len(tabla)):
        if tabla[i] == equis and i not in revisados:
            # Revisión horizontal
            isRevisando = True
            revision = 1
            cont = i + 1
            while isRevisando:
                if tabla[cont] == equis and not isBreakRow(dimension, (cont-1)):
                    revision += 1
                    revisados.append(cont)
                    cont += 1
                else:
                    isRevisando = False
            if revision >= 3:
                print(f'{equis} gana!')


def crearTabla(dimension):
    tabla = []

    for i in range(0, (dimension * dimension) + 1):
        tabla.append(i)

    return tabla


def run():
    bloqueados = [0, 5]
    jugando = False
    dimension = 0

    turno = ''
    jugador = ''
    ai = ''

    #   Introducción de las dimensiones del tablero.
    while dimension < 3:
        dimension = int(input('Dimensión del tablero (mayor a 2): '))

    tabla = crearTabla(dimension)
    print(tabla)

    #   Selección de pieza del jugador.
    while not jugador == equis or jugador == circulo:
        print('Selecciona tu pieza:')
        jugador = input().upper()

    # Asigna la pieza del AI basado en la selección del jugador
    if jugador == equis: ai = circulo
    else: ai = equis

    # Decide el turno del que empieza el juego al azar
    if random.randint(0, 1) == 0:
        turno = jugador
        print('El jugador empieza.')
    else:
        turno = ai
        print('La computadora empieza.')

    #jugando = True
    estadoJuego([0, equis, equis, 3, equis, equis, equis, 7, 8, 9], dimension, bloqueados)

    while jugando:
        print('')


run()