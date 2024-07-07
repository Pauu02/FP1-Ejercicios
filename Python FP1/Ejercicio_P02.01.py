def inicial_o_final(primer_texto, segundo_texto):
    if primer_texto[0] == segundo_texto[0] or primer_texto[-1] == segundo_texto[-1]:
        return True
    return False


if "__main__" == __name__:

    texto1 = "Casa"
    texto2 = "Caso"
    texto3 = "Pasa"
    texto4 = "Cosa"
    print(inicial_o_final(texto1, texto2))
    print(inicial_o_final(texto1, texto3))
    print(inicial_o_final(texto1, texto4))
    print(inicial_o_final(texto2, texto3))
