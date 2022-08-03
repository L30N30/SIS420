import random

# Proveedor = [[P1, [[p1, precio], [p2, precio]]]]
# Precios = [[p1, precio_venta], [p2, precio_venta]]


def sort_key(lista):
    return lista[1]


def crear_poblacion(tam, num_prod, prod_prov):
    pob = []
    val = []
    for i in range(tam):
        precio = []
        indiv_tag = []
        for j in range(num_prod):
            proveedor_random = random.randint(0, num_prod - 1)
            producto_random = random.randint(0, num_prod - 1)
            indiv_tag.append([proveedor_random, producto_random])
            precio.append(prod_prov[proveedor_random][1][producto_random][1])
        pob.append(precio)
        val.append(indiv_tag)
    return pob, val


def fitness(val, prod_prov, pob):
    fit = 0
    for i in val:
        prov = prod_prov[i[0]][0]  # P1 Id Proveedor
        prod = prod_prov[i[0]][1][i[1]][0]  # p1 Id producto
        prec = prod_prov[i[0]][1][i[1]][1]  # Precio según tienda
        for j in pob:
            if j[0] == prod:
                tem = (prec/j[1]) * 100
                if tem < 50:
                    fit += tem
    return fit


def mutar(individuo, tag, pos):
    pos = random.randint(0, 9)
    ind = []

    for i in range(10):
        if i == pos:
            ind.append(tag[pos][pos][pos][1])
        else:
            ind.append(individuo[i])

    return individuo


def procrear(individuo1, individuo2, tag, pos1, pos2):
    ind = []
    tg = []
    for i in range(len(individuo1)):
        if i < 4:
            ind.append(individuo1[i])
            tg.append(tag[pos1][i])
        else:
            ind.append(individuo2[i])
            tg.append(tag[pos2][i])
    tag.append(tg)
    return ind, tag


def procrear_tag(individuo1, tag, pos1, pos2):
    tg = []
    Tag = tag.copy()
    for i in range(len(individuo1)):
        if i < 4:
            tg.append(tag[pos1][i])
        else:
            tg.append(tag[pos2][i])
    Tag.append(tg)
    return Tag


def run():
    proveedores = []
    productos = []
    prod_prov = []
    num_prov = 10
    num_prod = 10
    tam_pob = 100

    prob_mutacion = 0.2
    procreacion = 20

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

    poblacion, tags = crear_poblacion(tam_pob, num_prod, prod_prov)
    individuos_fit = []
    tags_fit = []
    print(tags)

    for i in range(len(poblacion)):
        fit = fitness(tags[i], prod_prov, productos)
        individuos_fit.append([poblacion[i], fit])
        tags_fit.append([tags[i], fit])

    individuos_fit.sort(key=sort_key)
    tags_fit.sort(key=sort_key)

    while not resuelto:
        if individuos_fit[0][1] == 0:
            resuelto = True
        else:
            poblacion = []
            tags = []

            for i in individuos_fit:
                poblacion.append(i[0])
            for i in tags_fit:
                tags.append(i[0])

            for i in range(procreacion):
                poblacion.append(procrear(poblacion[i], poblacion[i+1], tags, i, i+1))
                tags = procrear_tag(poblacion[i], tags, i, i+1)

            '''for i in range(len(poblacion)):
                if random.randint(0, int(100/(prob_mutacion*100) - 1)) == 0:
                    #poblacion.append(mutar(poblacion[i], tags, i))
                    #tags.append(tags[i])
                    poblacion.pop(i)
                    tags.pop(i)'''

            individuos_fit = []
            tags_fit = []
            for i in range(len(poblacion)):
                fit = fitness(poblacion[i], prod_prov, productos)
                individuos_fit.append([poblacion[i], fit])
                tags_fit.append([tags[i], fit])
            individuos_fit.sort(key=sort_key)
            tags_fit.sort(key=sort_key)

    print(individuos_fit[0][0])
    print(tags_fit[0][0])
    print(tags_fit[0][1])


run()