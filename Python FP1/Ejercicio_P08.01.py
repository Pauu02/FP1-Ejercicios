#from auxiliar import show

def puntuación(liga):
    for equipos, valores in liga.items():
        puntos = 0
        puntos = valores[0] * 3 + valores[1] * 1
        liga[equipos] = (valores, puntos)
    return liga 


if __name__ == "__main__":
    liga_petanca = {
        "Lobos grises": (4, 3, 1),
        "Damas de la noche": (3, 2, 3),
        "Los de aquí": (2, 3, 3),
        "Los de allí": (3, 1, 4),
        "Las del otro lado": (2, 3, 3)
    }
    print(puntuación(liga_petanca))
    #show(liga_petanca)
