import os
import numpy as np
from matplotlib import pyplot
from scipy import optimize
from scipy.io import loadmat


def run():
    data = np.loadtxt('fasion_mnist/fashion-mnist_train.csv', delimiter=',', skiprows=1)

    input_layer_size = 784
    num_labels = 10

    x = data[:, 1:input_layer_size]
    y = data[:, 0].ravel()
    print(x)


run()