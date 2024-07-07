def maxima_semana(lista):
    temp_max = []
    for fila in lista:
        max = 0
        for tupla in fila:
            if tupla[0] > max:
                max = tupla[0]
        temp_max.append(max)
    return temp_max


if "__main__" == __name__:
    datos_semanales = [
    ((28, 18), (30, 19), (31, 20), (29, 18), (27, 17), (26, 16), (25, 15)),
    ((32, 21), (33, 22), (34, 23), (32, 20), (29, 18), (27, 17), (25, 15)),
    ((27, 16), (28, 17), (29, 18), (30, 19), (28, 18), (26, 17), (25, 16))
]

    print(maxima_semana(datos_semanales))
