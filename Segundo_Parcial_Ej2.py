# import os
import numpy as np
from matplotlib import pyplot
# from scipy import optimize
from scipy.io import loadmat
import utils


'''
ENCONTRAR SI EL INGRESO ES MAYOR A 50K O NO
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


def predict(theta_1, theta_2, x):
    """
    Predict the label of an input given a trained neural network.

    Parameters
    ----------
    theta_1 : array_like
        Weights for the first layer in the neural network.
        It has shape (2nd hidden layer size x input size)

    theta_2: array_like
        Weights for the second layer in the neural network.
        It has shape (output layer size x 2nd hidden layer size)

    x : array_like
        The image inputs having shape (number of examples x image dimensions).

    Return
    ------
    p : array_like
        Predictions vector containing the predicted label for each example.
        It has a length equal to the number of examples.

    Hint
    ----
    This code can be done all vectorized using the numpy argmax function.
    In particular, the argmax function returns the index of the  max element,
    for more information see '?np.argmax' or search online. If your examples
    are in rows, then, you can use np.argmax(A, axis=1) to obtain the index
    of the max for each row.

    """
    # Asegurar que la entrada tenga dos dimensiones
    if x.ndim == 1:
        x = x[None]  # Promover a dos dimensiones

    # Variables útiles
    m = x.shape[0]
    num_labels = theta_2.shape[0]

    p = np.zeros(x.shape[0])

    x = np.concatenate([np.ones((m, 1)), x], axis=1)

    a2 = utils.sigmoid(x.dot(theta_1.T))
    a2 = np.concatenate([np.ones((a2.shape[0], 1)), a2], axis=1)

    p = np.argmax(utils.sigmoid(a2.dot(theta_2.T)), axis=1)

    return p


def run():

    data = np.loadtxt('Adult/adult-train-corregido.csv', delimiter=',', skiprows=1)
    x = data[:, 0:14]
    y = data[:, 14].ravel()

    '''# Se convierte la etiqueta 10 a 0
    y[y == 10] = 0
    m = y.size

    # se permutan los ejemplos, para ser usados para visualizar ina imagen a la vez
    indices = np.random.permutation(m)

    # Selecciona 100 puntos al azar de datos para visualizar
    rand_indices = np.random.choice(m, 100, replace=False)
    sel = x[rand_indices, :]

    # sel = x[0,:]
    utils.displayData(sel)

    # Configura los parámetros que se requieren
    input_layer_size = 400  # Entrada Imagen de dígitos de 20x20
    hidden_layer_size = 25  # 25 unidades ocultas
    num_labels = 10  # 10 etiquetas, del 1 al 10 (se remaps el numero 10 con el valor de 0)

    # Carga el archivo .mat, que devuelve un diccionario
    weights = loadmat('ex3weights.mat')

    # Obtiene el modelo de pesos del diccionario
    # theta_1 has size 25 x 401
    # theta_2 has size 10 x 26
    theta_1, theta_2 = weights['Theta1'], weights['Theta2']

    # Intercambia la primera y la última columna de theta_2, debido al legado de la indexación de MATLAB,
    # Desde que el archivo de peso ex3weights.mat se guardó según la indexación de MATLAB
    theta_2 = np.roll(theta_2, 1, axis=0)

    pred = predict(theta_1, theta_2, x)
    print('Precisión del conjunto de entrenamiento: {:.3f}%'.format(np.mean(pred == y) * 100))

    if indices.size > 0:
        i, indices = indices[0], indices[1:]
        utils.displayData(x[i, :], figsize=(4, 4))
        pred = predict(theta_1, theta_2, x[i, :])
        print('Predicción de la red neuronal: {}'.format(*pred))
    else:
        print('No hay mas imágenes para mostrar!')

    pyplot.show()'''


run()