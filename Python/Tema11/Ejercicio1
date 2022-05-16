import sqlite3


def main():

    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    rows = cursor.execute('SELECT * FROM alumnos WHERE nombre == "Peter"')
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
