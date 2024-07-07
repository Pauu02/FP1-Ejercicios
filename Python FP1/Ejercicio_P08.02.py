#from auxiliar import show
def getkey(tupla):
    return tupla[1]

def clasificación(liga):
    lista = []
    for equipos, partidos in liga.items():
        puntos = partidos[0] * 3 + partidos[1] * 1
        tupla = (equipos, puntos)
        lista.append(tupla)
        lista.sort(reverse=True, key = getkey)
    return lista


if __name__ == "__main__":
    liga_petanca = {
        "Lobos grises": (4, 3, 1),
        "Damas de la noche": (3, 2, 3),
        "Los de aquí": (2, 3, 3),
        "Los de allí": (3, 1, 4),
        "Las del otro lado": (2, 3, 3)
    }
    print(clasificación(liga_petanca))
    #show(lst_clasificación)
