from utilities import show


def save(sighting, filename):
    índices_avistamientos = sighting[0]
    lista_avistamientos = sighting[1]
    f = open(filename, 'w')

    for nombre in sorted(índices_avistamientos.keys()):
        indices = índices_avistamientos[nombre]
        f.write(f"{nombre};")
        for indice in indices:
            fecha, hora = lista_avistamientos[indice]
            f.write(f"('{fecha}', '{hora}')")
            if indice != indices[-1]:
                f.write(';')
        f.write('\n')

    f.close()


if __name__ == "__main__":
    sighting = (
        {  # Diccionario {individuos:índices de avistamiento}
            'Whale_A': [0, 4, 5, 6, 7, 8, 10, 11],
            'Whale_B': [0, 1, 2, 3, 6, 7, 11, 12, 13, 19],
            'Whale_C': [2, 4, 12, 13, 15],
            'Whale_D': [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18]
        },
        [  # Lista de avistamientos
            ('01/02/2023', '11:39:15'), ('02/03/2023', '13:22:49'),
            ('23/02/2023', '07:11:45'), ('25/05/2023', '19:58:26'),
            ('19/09/2023', '04:28:23'), ('06/01/2023', '20:41:07'),
            ('07/12/2023', '23:09:13'), ('26/03/2023', '23:55:33'),
            ('16/01/2023', '09:34:55'), ('02/03/2023', '22:16:08'),
            ('23/01/2023', '05:12:49'), ('12/01/2023', '01:26:06'),
            ('19/09/2023', '01:19:35'), ('17/05/2023', '12:54:00'),
            ('16/06/2023', '17:43:15'), ('02/06/2023', '18:08:12'),
            ('17/10/2023', '05:24:34'), ('09/09/2023', '02:48:02'),
            ('13/02/2023', '18:07:13'), ('08/12/2023', '07:46:47')
        ]
    )

    filename = "sighting_data.csv"
    save(sighting, filename)
    show(filename)
