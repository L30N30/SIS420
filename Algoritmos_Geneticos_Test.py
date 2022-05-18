
def run():
    poblacion = crear_poblacion(tamano_poblacion)  # Inicializar una poblacion
    print("Poblacion Inicial:\n%s" % (poblacion))  # Se muestra la poblacion inicial

    mejor_fitness = 1000
    # Se evoluciona la poblacion
    for i in range(100000):
        poblacion = seleccion_y_reproduccion(poblacion)
        poblacion = mutacion(poblacion)
        puntuados = [(calcular_fitness(ind), ind) for ind in poblacion]
        for indPun in puntuados:
            if indPun[0] < mejor_fitness:
                mejor_fitness = indPun[0]
            if indPun[0] == 0:
                break

    puntuados = [(calcular_fitness(ind), ind) for ind in poblacion]
    puntuados = [i[1] for i in sorted(puntuados)]
    for ind in puntuados:
        print(f"individuo: {ind} fitness: {calcular_fitness(ind)}")

    print("\nPoblacion Final que cuenta con una solucion:\n%s" % (poblacion))  # Se muestra la poblacion evolucionada
    print("\n\n")

    if mejor_fitness == 0:
        individuo = puntuados[0]
        print(f"El mejor fenotipo que resuelve la ecuacion es:{individuo[0]}, {individuo[1]}, {individuo[2]}")
        print(f"La solucion a la ecuacion X1 + X2 - X3 = 4 es {individuo[0]} + {individuo[1]} - {individuo[2]} = 4 ")
    else:
        print("El algoritmo no pudo encontrar una solucion")