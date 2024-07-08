import sqlite3
from utilities import create_db, show


def cargar_platos(fichero):
    with open(fichero, 'r') as fi, sqlite3.connect('menu.db') as db:
        caquita = []
        cursor = db.cursor()
        for line in fi:
            platito = line.strip().split(",")
            cursor.execute("SELECT * FROM categorias WHERE nombre = ?", (platito[0],)) 
            result = cursor.fetchone()
            if not result:
                caquita.append((platito[0], platito[1]))
            else:
                cursor.execute("INSERT INTO platos VALUES (?, ?, ?)", (platito[1],platito[2], result[0][0]))
        if caquita == []:
            return True
        else:
            return caquita


if __name__ == "__main__":
    create_db("menu.db")
    print("BBDD original------------------------------------------")
    show("menu.db")

    filename = "menu.csv"
    print("Resultado devuelto por la función----------------------")
    print(cargar_platos(filename))

    print("BBDD final---------------------------------------------")
    show("menu.db")
