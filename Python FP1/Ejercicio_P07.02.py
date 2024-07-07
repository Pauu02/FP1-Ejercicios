def mes_mas_lluvioso(lluvias):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    indice = -1
    max = 0
    for lluvia in lluvias:
        if lluvia > max:
            max = lluvia
            indice += 1
    return meses[indice]


if __name__ == "__main__":
    lluvias = [12.8, 10.5, 6.7, 5.3, 3.4, 2.8, 1.5, 0.5, 0.7, 2.0, 6.8, 10.3]
    print("El mes más lluvioso fue:", mes_mas_lluvioso(lluvias))
