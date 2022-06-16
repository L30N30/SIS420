import os
import numpy as np
from matplotlib import pyplot


# Acides Fija, Acidez Volátil, Ácido Cítrico, Azúcar Residual, Cloros, Sin Dióxido de Azufre
# Dióxido de azufre total, Densidad, pH, Sulfatos, Alcohol, Calidad

# 11 variables independientes, 1 etiqueta (Calidad)


# Leer datos
data = np.loadtxt('calidad_vino_rojo_dataset.txt', delimiter=';')
x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, y = data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 4], data[:, 5], data[:, 6], data[:, 7], data[:, 8], data[:, 9], data[:, 10], data[:, 11]
m = y.size

x0 = np.stack([np.ones(m), x0], axis=1)
x1 = np.stack([np.ones(m), x1], axis=1)
x2 = np.stack([np.ones(m), x2], axis=1)
x3 = np.stack([np.ones(m), x3], axis=1)
x4 = np.stack([np.ones(m), x4], axis=1)
x5 = np.stack([np.ones(m), x5], axis=1)
x6 = np.stack([np.ones(m), x6], axis=1)
x7 = np.stack([np.ones(m), x7], axis=1)
x8 = np.stack([np.ones(m), x8], axis=1)
x9 = np.stack([np.ones(m), x9], axis=1)
x10 = np.stack([np.ones(m), x10], axis=1)