import copy
import random

equis = 'X'
circulo = 'O'

""" Estructura de aplicación
    FUNCIONES:  dibujar, pasos disponibles
    HEURÍSTICA: Menor mientras hayan opciones de ganar y si hay una jugada ganadora posible."""

def estadoJuego(tabla, dimension):
    piezaEquis = []
    piezaCirculo = []

    for i in range(1, len(tabla)):
        if tabla[i] == equis:
            piezaEquis.append([tabla[i], i])
        elif tabla[i] == circulo:
            piezaCirculo.append([tabla[i], i])

    if len(piezaEquis) > 2:
        print('Flag 1')


def crearTabla(dimension):
    tabla = []

    for i in range(0, (dimension * dimension) + 1):
        tabla.append(i)

    return tabla


def run():
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

    if jugador == equis:
        ai = circulo
    else:
        ai = equis

    if random.randint(0, 1) == 0:
        turno = jugador
    else:
        turno = ai

    #jugando = True
    estadoJuego(tabla)

    while jugando:
        print('')


run()