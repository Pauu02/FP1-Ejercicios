def hay_elementos(tupla, tipo):
    for elemento in tupla:
        if type(elemento) == tipo:
            return True
    return False


if "__main__" == __name__:
    tupla = (2, "hola", True, 5, False, "adios", (2, 5, 6))

    print(hay_elementos(tupla, int))
    print(hay_elementos(tupla, float))
    print(hay_elementos(tupla, str))
    print(hay_elementos(tupla, tuple))
    print(hay_elementos(tupla, bool))
