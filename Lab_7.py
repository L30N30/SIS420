import os
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plot


'''
11 variables independientes, 1 etiqueta (Calidad)
---------------------------
PREDECIR: Calidad
---------------------------
BASADO EN:
1. Acides Fija
2. Acidez Volátil
3. Ácido Cítrico
4. Azúcar Residual
5. Cloros
6. Sin Dióxido de Azufre
7. Dióxido de azufre total
8. Densidad
9. pH
10. Sulfatos
11. Alcohol
'''


def costo_multiple(x, y, theta):
    m = y.shape[0]

    costo = 0
    costo = (1 / (2 * m)) * np.sum(np.square(np.dot(x, theta) - y))
    # print(costo)

    return costo


def gradiente_multiple(x, y, theta, alpha, num_itera):
    m = y.shape[0]

    theta = theta.copy()

    j_historial = []

    for i in range(num_itera):
        theta = theta - ((alpha / m) * (np.dot(x, theta) - y).dot(x))
        j_historial.append(costo_multiple(x, y, theta))

    return theta, j_historial


def normalizar_muestras(X):
    prom = np.mean(X, axis=0)
    des_est = np.std(X, axis=0)

    x_norm = (X - prom) / des_est

    return x_norm


def run():
    # Leer datos
    data = np.loadtxt('calidad_vino_rojo_dataset.txt', delimiter=';')
    x = data[:, :11]
    y = data[:, 11]
    m = y.size

    x_normalizado = normalizar_muestras(x)
    x = np.concatenate([np.ones((m, 1)), x_normalizado], axis=1)

    theta = np.zeros(12)

    num_iteraciones = 10000
    alpha = 0.0003

    theta, j_historial = gradiente_multiple(x, y, theta, alpha, num_iteraciones)

    pyplot.plot(np.arange(len(j_historial)), j_historial, lw=2)
    pyplot.xlabel('Numero de iteraciones')
    pyplot.ylabel('Costo')

    print(theta)
    plot.show()

    datos_prediccion = [1, 6.9, 0.48, 0.2, 1.9, 0.082, 9, 23, 0.99585, 3.39, 0.43, 9.05]
    print(f'Predicción de calidad: {round(np.dot(theta, datos_prediccion), 4)}')


run()