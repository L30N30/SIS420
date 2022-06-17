import os
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plot


def run():
    # Leer datos
    data = np.loadtxt('calidad_vino_rojo_dataset.txt', delimiter=';')
    x = data[:, 1]
    y = data[:, 11]
    m = y.size
    print(x)

    print(np.mean(x))
    print(np.std(x))


run()