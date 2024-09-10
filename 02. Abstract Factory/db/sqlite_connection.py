import sqlite3
from .db_connection import DBConnection

# Implementación para la conexión y consulta en SQLite
class SQLiteConnection(DBConnection):
    # Constructor que recibe el nombre de la base de datos como parámetro
    def __init__(self, database):
        # Asigna el nombre de la base de datos al atributo 'database'
        self.database = database
        self.connection = None  # Inicialmente, no hay conexión establecida

    # Método para establecer la conexión con la base de datos SQLite
    def connect(self):
        # Utiliza la función 'connect' de sqlite3 para establecer la conexión a la base de datos
        self.connection = sqlite3.connect(self.database)
        return self.connection  # Retorna la conexión establecida

    # Método para ejecutar una consulta SQL en la base de datos
    # Recibe un parámetro 'query', que es la consulta SQL a ejecutar
    def execute_query(self, query):
        cursor = self.connection.cursor()  # Crea un cursor para ejecutar la consulta
        cursor.execute(query)  # Ejecuta la consulta SQL
        result = cursor.fetchall()  # Obtiene todos los resultados de la consulta
        return result  # Retorna los resultados

    # Método para cerrar la conexión con la base de datos SQLite
    def close_connection(self):
        if self.connection:
            self.connection.close()  # Cierra la conexión si está activa
            print("Conexión SQLite cerrada.")  # Imprime un mensaje indicando que la conexión ha sido cerrada
