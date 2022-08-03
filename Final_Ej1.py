import random


def sort_key(lista):
    return lista[1]


def run():
    proveedores = []
    productos = []
    prod_prov = []
    num_prov = 10
    num_prod = 10

    resuelto = False

    # [P1, [[p1, precio], [p2, precio]]]

    for i in range(num_prov):
        msg = 'P' + str(i + 1)
        proveedores.append(msg)

    for i in range(num_prod):
        msg = 'p' + str(i + 1)
        item = [msg, random.randint(50, 100)]
        productos.append(item)

    for i in proveedores:
        precios = []
        for j in productos:
            precios.append([j[0], random.randint(1, 70)])
        prod_prov.append([i, precios])

    individuos_fit = []
    print(prod_prov)
    # while not resuelto:


run()