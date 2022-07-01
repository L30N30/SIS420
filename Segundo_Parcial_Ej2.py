import os
import numpy as np
from matplotlib import pyplot
from scipy import optimize
from scipy.io import loadmat
import matplotlib.pyplot as plot
import random


'''
PREDECIR SI EL SALARIO DE LA PERSONA ES MAYOR A 50K DÓLARES
>50K 1, <=50K 0.

age: continuous.
workclass: Private 0, Self-emp-not-inc 5, Self-emp-inc 10, Federal-gov 15, Local-gov 20, State-gov 25, Without-pay 30, Never-worked 35, ? 40.
fnlwgt: continuous.
education: Bachelors 0, Some-college 5, 11th 10, HS-grad 15, Prof-school 20, Assoc-acdm 25, Assoc-voc 30, 9th 35, 7th-8th 40, 12th 45, Masters 50, 1st-4th 55, 10th 60, Doctorate 65, 5th-6th 70, Preschool 75.
education-num: continuous.
marital-status: Married-civ-spouse 0, Divorced 5, Never-married 10, Separated 15, Widowed 20, Married-spouse-absent 25, Married-AF-spouse 30.
occupation: Tech-support 0, Craft-repair 5, Other-service 10, Sales 15, Exec-managerial 20, Prof-specialty 25, Handlers-cleaners 30, Machine-op-inspct 35, Adm-clerical 40, Farming-fishing 45, Transport-moving 50, Priv-house-serv 55, Protective-serv 60, Armed-Forces 65, ? 70.
relationship: Wife 0, Own-child 10, Husband 15, Not-in-family 20, Other-relative 25, Unmarried 30.
race: White 0, Asian-Pac-Islander 1, Amer-Indian-Eskimo 2, Other 3, Black 4.
sex: Female 0, Male 1.
capital-gain: continuous.
capital-loss: continuous.
hours-per-week: continuous.
native-country: United-States 0, Cambodia 1, England 2, Puerto-Rico 3, Canada 4, Germany 5, Outlying-US(Guam-USVI-etc) 6, India 7, Japan 8, Greece 9, South 10, China 11, Cuba 12, Iran 13, Honduras 14, Philippines 15, Italy 16, Poland 17, Jamaica 18, Vietnam 19, Mexico 20, Portugal 21, Ireland 22, France 23, Dominican-Republic 24, Laos 25, Ecuador 26, Taiwan 27, Haiti 28, Columbia 29, Hungary 30, Guatemala 31, Nicaragua 32, Scotland 33, Thailand 34, Yugoslavia 35, El-Salvador 36, Trinadad&Tobago 37, Peru 38, Hong 39, Holand-Netherlands 40, ? 41.
'''


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def lr_cost_function(theta, x, y, lambda_):
    m = y.size

    if y.dtype == bool:
        y = y.astype(int)

    j = 0
    grad = np.zeros(theta.shape)

    h = sigmoid(x.dot(theta.T))

    temp = theta
    temp[0] = 0

    j = (1 / m) * np.sum(-y.dot(np.log(h)) - (1 - y).dot(np.log(1 - h))) + (lambda_ / (2 * m)) * np.sum(np.square(temp))

    grad = (1 / m) * (h - y).dot(x)
    grad = grad + (lambda_ / m) * temp

    return j, grad


def one_vs_all(x, y, num_labels, lambda_):
    m, n = x.shape

    all_theta = np.zeros((num_labels, n + 1))

    x = np.concatenate([np.ones((m, 1)), x], axis=1)

    for c in np.arange(num_labels):
        initial_theta = np.zeros(n + 1)
        options = {'maxiter': 50}
        res = optimize.minimize(lr_cost_function, initial_theta, (x, (y == c), lambda_), jac=True, method='CG', options=options)

        all_theta[c] = res.x

    return all_theta


def predict_one_vs_all(all_theta, x):
    m = x.shape[0];
    num_labels = all_theta.shape[0]

    p = np.zeros(m)

    x = np.concatenate([np.ones((m, 1)), x], axis=1)
    p = np.argmax(sigmoid(x.dot(all_theta.T)), axis=1)

    return p


def run():
    input_layer_size = 14
    num_labels = 2

    data = np.loadtxt('Adult/adult-train-corregido.csv', delimiter=',', skiprows=1)
    x = data[:, 0:input_layer_size]
    y = data[:, 14].ravel()
    m = y.size

    '''rand_indices = np.random.choice(m, 100, replace=False)
    sel = x[rand_indices, :]
    display_data(sel)
    plot.show()'''

    lambda_ = 0.001
    all_theta = one_vs_all(x, y, num_labels, lambda_)

    a = 'y'
    data_test = np.loadtxt('Adult/adult-test-corregido.csv', delimiter=',', skiprows=1)
    x_test = data_test[:, 0:input_layer_size]
    y_test = data_test[:, 14].ravel()
    while a == 'y':
        valor_inferior = random.randint(0, y_test.size-1)  # Max: 9999
        valor_superior = valor_inferior + 1

        predict = predict_one_vs_all(all_theta, x_test)
        print('Precision del conjunto de entrenamiento: {:.2f}%'.format(np.mean(predict == y_test) * 100))
        x_prueba = x_test[valor_inferior:valor_superior, :].copy()
        x_prueba = np.concatenate([np.ones((1, 1)), x_prueba], axis=1)
        p = np.argmax(sigmoid(x_prueba.dot(all_theta.T)), axis=1)

        print(f'Predicción aprendida: {p}')
        print(f'Etiqueta original: {y_test[valor_inferior:valor_superior]}')

        mensaje = ''
        if p == 1:
            mensaje = 'sí'
        else:
            mensaje = 'no'
        print(f'Basado en el aprendizaje, la persona {mensaje} gana más de 50k dólares anuales')

        plot.show()
        a = input('Y: ')


run()