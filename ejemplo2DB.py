import sqlite3

miConexion = sqlite3.connect("gestionProductos")

miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE productos (
        id integer PRIMARY KEY AUTOINCREMENT,
        nombre_articulo varchar(50),
        precio integer,
        seccion varchar(20)
    )
''')

productos = [
    ( "pelota", 20, "juguetería"),
    ( "pantalon", 20, "confección"),
    ( "destornillador", 20, "ferrretería"),
    ( "jarron", 20, "ceramica")
]

miCursor.executemany("INSERT INTO productos VALUES (NULL, ?, ?, ?)", productos)

#miCursor.execute("INSERT INTO productos VALUES ('AR05', 'Tren', 15, 'Juguetería')")

miConexion.commit()

miConexion.close