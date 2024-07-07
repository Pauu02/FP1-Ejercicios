def multisuma(multilista):
    suma = 0
    for elemento in multilista:
        if isinstance(elemento, int):
            suma += elemento
        elif isinstance(elemento, list):
            suma += multisuma(elemento)
    return suma


if __name__ == "__main__":
    lista_de_prueba = [
        35, 14,
        [
            [12, 34],
            14, 98,
        ],
        10, 12, 28,
        [
            56,
            [
                [10, 14],
                [11]
            ]
        ]
    ]
    print(multisuma(lista_de_prueba))
