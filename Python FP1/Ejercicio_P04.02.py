def suma(tupla):
    suma = 0
    for elemento in tupla:
        suma += elemento
    return suma


if "__main__" == __name__:
    tupla = (5, 10, 2, 8, 3)
    print(suma(tupla))
