import math
import os
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plot
from scipy import optimize


'''
DETERMINA SI LA ESPECIE ES BREAM
1. Peso
2. Longitud 1
3. Longitud 2
4. Longitud 3
5. Altura
6. Ancho
'''


def costFunction(theta, X, y):
    # Inicializar algunos valores utiles
    m = y.size  # numero de ejemplos de entrenamiento

    J = 0
    grad = np.zeros(theta.shape)

    h = sigmoid(X.dot(theta.T))

    J = (1 / m) * np.sum(-y.dot(np.log(h)) - (1 - y).dot(np.log(1 - h)))
    grad = (1 / m) * (h - y).dot(X)

    return J, grad


def costo(theta, x, y):
    m = y.size

    j = 0
    h = sigmoid(x.dot(theta.T))
    j = (1 / m) * np.sum(-y.dot(np.log(h)) - (1 - y).dot(np.log(1 - h)))

    return j


def sigmoid(z):
    z = np.array(z)
    g = np.zeros(z.shape)
    g = 1 / (1 + np.exp(-z))

    return g


def sig(val):
    return 1 / (1 + (math.e ** (-val)))


def descenso_gradiente(theta, x, y, alpha, num_itera):
    m = y.shape[0]

    theta = theta.copy()
    j_historial = []

    for i in range(num_itera):
        h = sigmoid(x.dot(theta.T))
        theta = theta - (alpha / m) * (h - y).dot(x)

        j_historial.append(costo(theta, x, y))

    return theta, j_historial


def predecir(theta, x):
    m = x.shape[0]

    p = np.zeros(m)

    p = np.round(sigmoid(x.dot(theta.T)))
    return p


def run():
    data = np.loadtxt('pescados_dataset.txt', delimiter='\t')
    x = data[:, 0:6]
    y = data[:, 6]
    m = y.size

    x = np.concatenate([np.ones((m, 1)), x], axis=1)

    alpha = 0.00003
    num_itera = 1000

    theta = np.zeros(7)
    theta, j_historial = descenso_gradiente(theta, x, y, alpha, num_itera)

    options = {'maxiter': 1000}

    initial_theta = np.zeros(7)
    res = optimize.minimize(costFunction, initial_theta, (x, y), jac=True, method='TNC', options=options)
    cost = res.fun
    theta = res.x

    pyplot.plot(np.arange(len(j_historial)), j_historial, lw=2)
    pyplot.xlabel('Numero de iteraciones')
    pyplot.ylabel('Costo J')

    plot.show()

    x_prediccion = [1, 100, 16.2, 18, 19.2, 5.2224, 3.3216]
    esBream = round(100 * sig(np.dot(x_prediccion, theta)), 2)
    print(esBream)


run()