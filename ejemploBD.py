import sqlite3

# CREAR CONEXION
miConexion = sqlite3.connect("PrimeraBase")

#CREAR CURSOR
miCursor = miConexion.cursor()

#CREAR TABLA
miCursor.execute("CREATE TABLE productos (nombre_articulo varchar(50), precio integer, seccion varchar(20))") #Crear tabla

#INSERTAR EN TABLA
miCursor.execute("INSERT INTO productos VALUES ('Balón', 15, 'Deportes')")

#LISTA DE PRODUCTOS
variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería")
]

#INSERTAR LISTA DE PRODUCTOS
miCursor.executemany("INSERT INTO productos VALUES (?, ?, ?)", variosProductos)

#CONSULTAR PRODUCTOS
miCursor.execute("SELECT * FROM productos")

#OBTENER LISTA DE PRODUCTOS
variosProductos = miCursor.fetchall()

#MOSTRAR PRODUCTOS
for producto in variosProductos:

    print(producto)

#CONFIRMAR CAMBIOS
miConexion.commit() 

#CERRAR CONEXION
miConexion.close()