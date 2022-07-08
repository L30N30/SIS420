import numpy as np
from matplotlib import pyplot
from scipy import optimize
import matplotlib.pyplot as plot
import random


def normalizar_muestras(X):
    prom = np.mean(X, axis=0)
    des_est = np.std(X, axis=0)

    x_norm = (X - prom) / des_est

    return x_norm


def display_data(x, example_width=None, figsize=(28, 28)):
    if x.ndim == 2:
        m, n = x.shape
    elif x.ndim == 1:
        n = x.size
        m = 1
        x = x[None]
    else:
        raise IndexError('La entrada X debe ser 1 o 2 dimensinal.')

    example_width = example_width or int(np.round(np.sqrt(n)))
    example_height = n / example_width

    display_rows = int(np.floor(np.sqrt(m)))
    display_cols = int(np.ceil(m / display_rows))

    fig, ax_array = pyplot.subplots(display_rows, display_cols, figsize=figsize)
    fig.subplots_adjust(wspace=0.025, hspace=0.025)

    ax_array = [ax_array] if m == 1 else ax_array.ravel()

    for i, ax in enumerate(ax_array):
        ax.imshow(x[i].reshape(example_width, example_width, order='F'),
                  cmap='Greys', extent=[0, 1, 0, 1])
        ax.axis('off')


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
    input_layer_size = 784  # Número de pixeles
    num_labels = 10  # 0 - 9

    data_train = np.loadtxt('fashion_mnist/fashion-mnist_train.csv', delimiter=',', skiprows=1)
    x_train = data_train[:, 1:input_layer_size+1]
    y_train = data_train[:, 0].ravel()
    y_train[(y_train == 10)] = 0

    data_test = np.loadtxt('fashion_mnist/fashion-mnist_test.csv', delimiter=',', skiprows=1)
    x_test = data_test[:, 1:input_layer_size + 1]
    y_test = data_test[:, 0].ravel()
    y_test[(y_test == 10)] = 0

    m1 = y_train.size + y_test.size
    porcentaje = round(m1 * 0.8)

    x = np.concatenate([x_train, x_test], axis=0)
    # x = normalizar_muestras(x)
    x_train = x[:porcentaje]
    x_test = x[porcentaje:]

    y = np.concatenate([y_train, y_test], axis=0)
    # y = normalizar_muestras(y)
    y_train = y[:porcentaje]
    y_test = y[porcentaje:]

    lambda_ = 0.1
    all_theta = one_vs_all(x_train, y_train, num_labels, lambda_)

    a = 'y'
    while a == 'y':
        valor_inferior = random.randint(0, 999)
        valor_superior = valor_inferior + 1

        predict = predict_one_vs_all(all_theta, x_test)
        print('Precision del conjunto de entrenamiento: {:.2f}%'.format(np.mean(predict == y_test) * 100))

        x_prueba = x_test[valor_inferior:valor_superior, :].copy()
        x_prueba = np.concatenate([np.ones((1, 1)), x_prueba], axis=1)
        p = np.argmax(sigmoid(x_prueba.dot(all_theta.T)), axis=1)

        print(f'Predicción aprendida: {p}')
        display_data(x_test[valor_inferior:valor_superior, :])
        print(f'Etiqueta original: {y_test[valor_inferior:valor_superior]}')

        plot.show()
        a = input('Y: ')


run()