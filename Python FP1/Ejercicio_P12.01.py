import sqlite3
from utilities import create_db, show


def cargar_platos(fichero):
    db = sqlite3.connect("menu.db")
    cursor = db.cursor()
    with open(fichero, 'r') as fr:
        lineas = fr.readlines()

    cat_incorrectas = []
    cat_correctas = []

    for linea in lineas:
        categoria, plato, precio = linea.strip().split(';')

        try:
            cursor.execute("INSERT INTO platos(nombre, precio, \
            categoria_id) VALUES(?, ?, (SELECT id FROM categorias WHERE\
            nombre = ?))", (plato, precio, categoria))
        except sqlite3.IntegrityError:
            cat_incorrectas.append((categoria, plato))
        else:
            cat_correctas.append((categoria, plato, precio))

    db.commit()
    db.close()
    if cat_incorrectas:
        return cat_incorrectas
    else:
        return True


if __name__ == "__main__":
    create_db("menu.db")
    print("BBDD original------------------------------------------")
    show("menu.db")

    filename = "menu.csv"
    print("Resultado devuelto por la función----------------------")
    print(cargar_platos(filename))

    print("BBDD final---------------------------------------------")
    show("menu.db")
