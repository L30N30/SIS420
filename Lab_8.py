import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

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
    print('Datos Adquiridos')

    pf = PolynomialFeatures(degree=3)
    x = pf.fit_transform(x.reshape(-1, 18))

    regresion_lineal = LinearRegression()
    regresion_lineal.fit(x, y)

    print('Calculando predicción')

    x_prediccion = np.array([263, 62, 0.01, 71.2796, 65, 1154, 19.1, 83, 6, 8.16, 65, 0.1, 584.2592, 33736494, 17.2, 17.3, 0.479, 10.1])
    x_prediccion = pf.fit_transform(x_prediccion.reshape(-1, 18))
    prediccion = regresion_lineal.predict(x_prediccion)
    print(prediccion)


run()