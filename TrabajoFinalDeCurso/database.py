import sqlite3
from datetime import datetime

class ClientDB:
    #Manejo base de datos de clientes

    def __init__(self):
        self.conn = sqlite3.connect("clientes.db")
        self.create_table()

    def create_table(self):
        """crear tabla clientes"""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT,
                telefono TEXT,
                fecha TEXT)""")
        self.conn.commit()

    def add_client(self, nombre, email, telefono):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        self.conn.execute("""
            INSERT INTO clientes(nombre,email,telefono,fecha)
            VALUES(?,?,?,?)""", (nombre, email, telefono, fecha))

        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT * FROM clientes")
        return cursor.fetchall()

    def delete_client(self, client_id):
        self.conn.execute("DELETE FROM clientes WHERE id=?", (client_id,))
        self.conn.commit()