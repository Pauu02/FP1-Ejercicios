def cuantos_hay(tupla, tipo):
    cont = 0
    for elemento in tupla:
        if type(elemento) == tipo:
            cont += 1
    return cont


if "__main__" == __name__:
    tupla = (2, "hola", True, 5, False, "adios", (2, 5, 6))

    print(cuantos_hay(tupla, int))
    print(cuantos_hay(tupla, str))
    print(cuantos_hay(tupla, tuple))
    print(cuantos_hay(tupla, bool))
    print(cuantos_hay(tupla, float))
