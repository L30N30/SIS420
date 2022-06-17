import os
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plot


# Acides Fija, Acidez Volátil, Ácido Cítrico, Azúcar Residual, Cloros, Sin Dióxido de Azufre
# Dióxido de azufre total, Densidad, pH, Sulfatos, Alcohol, Calidad

# 11 variables independientes, 1 etiqueta (Calidad)


def costo_multiple(X, y, theta):
    # Inicializa algunos valores utiles
    m = y.shape[0]  # numero de ejemplos de entrenamiento
    J = 0
    h = np.dot(X, theta)
    J = (1 / (2 * m)) * np.sum(np.square(np.dot(X, theta) - y))
    print(J)

    return J


def gradiente_multiple(X, y, theta, alpha, num_itera):
    # Inicializa algunos valores
    m = y.shape[0]

    # realiza una copia de theta, el cual será acutalizada por el descenso por el gradiente
    theta = theta.copy()

    j_historial = []

    for i in range(num_itera):
        theta = theta - (alpha / m) * (np.dot(X, theta) - y).dot(X)
        j_historial.append(costo_multiple(X, y, theta))

    return theta, j_historial


def normalizar_muestras(X):
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    x_norm = (X - mu) / sigma

    return x_norm #, mu, sigma


def run():
    # Leer datos
    data = np.loadtxt('calidad_vino_rojo_dataset.txt', delimiter=';')
    # x0, x1, x2, x3, x4 = data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 4]
    # x5, x6, x7, x8, x9, x10 = data[:, 5], data[:, 6], data[:, 7], data[:, 8], data[:, 9], data[:, 10]
    x = data[:, :11]
    y = data[:, 11]
    m = y.size

    '''x0 = np.stack([np.ones(m), x0], axis=1)
    x1 = np.stack([np.ones(m), x1], axis=1)
    x2 = np.stack([np.ones(m), x2], axis=1)
    x3 = np.stack([np.ones(m), x3], axis=1)
    x4 = np.stack([np.ones(m), x4], axis=1)
    x5 = np.stack([np.ones(m), x5], axis=1)
    x6 = np.stack([np.ones(m), x6], axis=1)
    x7 = np.stack([np.ones(m), x7], axis=1)
    x8 = np.stack([np.ones(m), x8], axis=1)
    x9 = np.stack([np.ones(m), x9], axis=1)
    x10 = np.stack([np.ones(m), x10], axis=1)'''

    # stack_x = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

    # theta = np.zeros(len(stack_x) + 1)
    # print(theta)

    x_normalizado = normalizar_muestras(x)
    # print(x_normalizado)

    x = np.concatenate([np.ones((m, 1)), x_normalizado], axis=1)

    theta = np.zeros(12)

    num_iteraciones = 10000
    alpha = 0.0003

    theta, j_historial = gradiente_multiple(x, y, theta, alpha, num_iteraciones)

    pyplot.plot(np.arange(len(j_historial)), j_historial, lw=2)
    pyplot.xlabel('Numero de iteraciones')
    pyplot.ylabel('Costo J')

    print(theta)
    plot.show()


run()