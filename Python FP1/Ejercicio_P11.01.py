# Escriba aquí la función solicitada
def marcas(autos):
    fe = open(autos, 'r')
    line = fe.readline()
    marcas_coches = []

    while line != '':
        line = line.split(',')
        word = line[1]
        if word not in marcas_coches:
            marcas_coches.append(word)
        line = fe.readline()
    return sorted(marcas_coches)

    fe.close()


if __name__ == "__main__":
    lista_de_marcas = marcas("data.csv")
    print(lista_de_marcas)
