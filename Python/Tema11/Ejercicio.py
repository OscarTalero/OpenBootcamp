import sqlite3


def main():

    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE alumnos (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL)")
    cursor.execute("INSERT INTO alumnos VALUES (1,'Peter','Parker')")
    cursor.execute("INSERT INTO alumnos VALUES (2,'Bruce','Wayne')")
    cursor.execute("INSERT INTO alumnos VALUES (3,'Jhon','Connors')")
    cursor.execute("INSERT INTO alumnos VALUES (4,'Bruce','Banner')")
    cursor.execute("INSERT INTO alumnos VALUES (5,'Obi Wan','Kenobi')")
    cursor.execute("INSERT INTO alumnos VALUES (6,'Natasha','Romanov')")
    cursor.execute("INSERT INTO alumnos VALUES (7,'Clark','Kent')")
    cursor.execute("INSERT INTO alumnos VALUES (8,'Charles','Xavier')")

    rows = cursor.execute('SELECT * FROM alumnos WHERE nombre == "Peter"')
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
