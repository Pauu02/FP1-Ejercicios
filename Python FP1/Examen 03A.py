import sqlite3
from utilities import create_db, show


def presentados(descripcion_examen):
    """Función para obterner los nombres de los estudiantes que participaron\
    en un examen en funcion de la descripción del examen"""
    id_exam = buscar_id_examen(descripcion_examen)
    if id_exam is not False:
        """Filtro para aquellos casos en la que la descripción\
        no corresponda a un examen"""
        tupla_nomb_nota = estudiante_id_nota(id_exam)
        return lista_participantes_examen(tupla_nomb_nota)
    return False


def buscar_id_examen(descripcion_examen):
    """Función para obtener el id del examen , filtrando aquellos examenes\
    sin descripción"""
    db = sqlite3.connect("examenes.db")
    cursor = db.cursor()
    comant = "SELECT id FROM examenes WHERE descripcion = ?;"
    cursor.execute(comant, (descripcion_examen,))
    id_exam = cursor.fetchone()
    if id_exam is None:
        return False
    return id_exam


def estudiante_id_nota(id_exam):
    """Función para obtener un tupla de listas donde dentro de esas listas\
    estan el id del estudiante y su nota"""
    db = sqlite3.connect("examenes.db")
    cursor = db.cursor()
    comant = "SELECT estudiante_id, nota FROM resultados\
    WHERE examen_id = ?;"
    cursor.execute(comant, (id_exam[0],))
    tupla_nomb_nota = cursor.fetchall()
    return tupla_nomb_nota


def lista_participantes_examen(tupla_nomb_nota):
    """Función para obtener una lista de los nombres de aquellos alumnos\
    que participaron en el examen """
    db = sqlite3.connect("examenes.db")
    cursor = db.cursor()
    list_nomb_exam = []
    for id_nombre, nota in tupla_nomb_nota:
        if nota is not None:
            """Filtro para no devolver aquellos estudiantes que no tienen\
            nota en el examen"""
            comant = "SELECT nombre FROM  estudiantes WHERE id = ?"
            cursor.execute(comant, (id_nombre,))
            nombre = cursor.fetchone()
            list_nomb_exam.append(nombre[0])
    return list_nomb_exam


if __name__ == "__main__":
    create_db("examenes.db")
    print("--- Base de Datos original ---")
    show("examenes.db")
    descr_examenes = ["Primer parcial", "Segundo parcial", "Tercer parcial"]
    for descr_examen in descr_examenes:
        print(f"--- Resultado para '{descr_examen}' ---")
        print(presentados(descr_examen))
