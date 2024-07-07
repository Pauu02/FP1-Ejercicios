from auxiliar import *

def valor_pixel(imagen):
    pmax = 0
    for fila in imagen:
        for elemento in fila:
            if elemento > pmax and elemento < 255:
                pmax = elemento
    return pmax

def saturated(imagen):
    new_imagen = []
    pmax = valor_pixel(imagen)
    delta = pmax -255

    for m in range(len(imagen)):
        for n in range(len(imagen[0])):
            new_imagen[m][n] = imagen[m][n] + delta
            if new_imagen[m][n] > 255:
                new_imagen[m][n] = 255
            new_imagen.append(new_imagen[m][n])
    return new_imagen


if __name__ == "__main__":
    """Código para ejecutar la función solicitada."""

    # Cargamos una imagen de ejemplo.
    # Puede cargar otra imagen cambiando get_eii_img() por get_ball_img(size)
    # donde size es un número entero positivo

    imagen = get_eii_img()

    # Mostramos la imagen original y la resultante del proceso de saturación.
    # cambiando show(imagen) por show(imagen, True) no se muestran los números.
    # (igual show(result, True))

    show(imagen)
    result = saturated(imagen)
    print("-" * (5 * len(imagen[0])))
    show(result)
