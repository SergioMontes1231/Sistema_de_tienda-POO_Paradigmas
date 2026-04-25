import sqlite3
import os


def get_connection():
    DB_PATH = os.path.join( "..", "database", "tienda.db")
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def crear_tablas():
    conn = get_connection()
    cursor = conn.cursor()

    #====== Producto ======

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventario(
            id_producto INTEGER PRIMARY KEY
            AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT,
            codigo_barras  INTEGER UNIQUE,
            precio_compra REAL,
            precio_venta REAL,
            stock REAL NOT NULL
            )
        """) 

    #===== Cliente =======
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente(
            id_cliente INTEGER PRIMARY KEY 
            AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            puntos INTEGER DEFAULT 0
            )"""
        )

    conn.commit()
    conn.close()

if __name__ == '__main__':
    get_connection()
    crear_tablas()
