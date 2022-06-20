import os
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error


'''
EXPECTATIVA MEDIA DE VIDA
1. Mortalidad Adulta
2. Muerte Infantil
3. Alcohol
4. Porcentaje de Gasto
5. Hepatitis B
6. Sarampión
7. BMI
8. Muertes Debajo de los 5
9. Polio
10. Gasto Total
11. Difteria
12. HIV/AIDS
13. GDP
14. Población
15. Delgadez 1-19 años
16. Delgadez 5-9 años
17. Composición del ingreso de los recursos
18. Enseñanza
'''


def run():
    data = np.loadtxt('expectativa_vida_dataset.txt', delimiter='\t')
    x = data[:, 1:19]
    y = data[:, 0]
    m = y.size
    # print(x)

    pf = PolynomialFeatures(degree=5)
    # print(x.shape)
    x = pf.fit_transform(x.reshape(-1, 18))
    # print(x.shape)

    regresion_lineal = LinearRegression()

    regresion_lineal.fit(x, y)

    print('theta = ' + str(regresion_lineal.coef_) + ', b = ' + str(regresion_lineal.intercept_))

    # Predecimos los valores y para los datos usados en el entrenamiento
    prediccion_entrenamiento = regresion_lineal.predict(x)
    m_error_cuad = mean_squared_error(y_true=y, y_pred=prediccion_entrenamiento)
    # La raíz cuadrada del MSE es el RMSE
    rmse = np.sqrt(m_error_cuad)
    print('Error Cuadrático Medio (MSE) = ' + str(m_error_cuad))
    print('Raíz del Error Cuadrático Medio (RMSE) = ' + str(rmse))
    # calculamos el coeficiente de determinación R2
    r2 = regresion_lineal.score(x, y)
    print('Coeficiente de Determinación R2 = ' + str(r2))

    # test = data[]


run()