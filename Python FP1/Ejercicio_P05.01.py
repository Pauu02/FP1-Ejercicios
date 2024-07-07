def tipos(elementos):
    tipos = []
    for elemento in elementos:
        tipos.append(f"{type(elemento).__name__}")
    return tipos

if "__main__" == __name__:
    elementos = [1, "Hola", 3.14, True, [1, 2, 3], (2, 3, 4)]
    print(tipos(elementos))
