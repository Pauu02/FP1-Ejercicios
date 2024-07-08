import sqlite3
from utilities import create_db, show


def nota_final(tupla_exam_nota):
    """Función para obtener la nota final del estudiante"""
    db = sqlite3.connect("examenes.db")
    cursor = db.cursor()
    nota_final = 0
    for examen_id, nota in tupla_exam_nota:
        if nota is not None:
            """Filtro para no devolver aquellos estudiantes que no tienen\
            nota en el examen"""
            nota_final = nota_final + nota * peso_examen(examen_id)
    return nota_final

def estudiante_id_nota(id_estudiante):
    """Función para obtener un tupla de listas donde dentro de esas listas\
    estan el examen del estudiante y su nota"""
    db = sqlite3.connect("examenes.db")
    cursor = db.cursor()
    comant = "SELECT examen_id, nota FROM resultados\
    WHERE estudiante_id = ?;"
    cursor.execute(comant, (id_estudiante,))
    tupla_examen_nota = cursor.fetchall()
    return tupla_examen_nota

def id_estudiante(nombre):
    """Función para obterner la id del estudiante dado su nombre""" 
    with sqlite3.connect('examenes.db') as db:
        cursor = db.cursor()
        comant = "SELECT id FROM estudiantes WHERE nombre = ?;"
    cursor.execute(comant, (nombre,))
    id_estudiante = cursor.fetchone()
    if id_estudiante is None:
        return False
    return id_estudiante

def peso_examen(id_examen):
    """Función para obterner la id del estudiante dado su nombre""" 
    with sqlite3.connect('examenes.db') as db:
        cursor = db.cursor()
        comant = "SELECT peso FROM examenes WHERE id = ?;"
    cursor.execute(comant, (id_examen))
    peso_examen = cursor.fetchone()
    if peso_examen is None:
        return False
    return peso_examen


if __name__ == "__main__":
    create_db("examenes.db")
    print("BBDD original------------------------------------------")
    show("examenes.db")

    print("Resultado devuelto por la función----------------------")
    estudiante = "Pedro Bénitez Gómez"
    print(nota_final(estudiante))
