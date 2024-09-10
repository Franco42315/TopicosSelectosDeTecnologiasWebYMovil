import mysql.connector
from .db_connection import DBConnection

# Implementación para la conexión y consulta en MySQL/MariaDB
class MySQLConnection(DBConnection):
    # Constructor que recibe los parámetros necesarios para establecer la conexión a MySQL
    def __init__(self, host, user, password, database):
        # Asigna los valores de conexión a los atributos de la clase
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None  # Inicialmente, no hay conexión establecida

    # Método para establecer la conexión con la base de datos MySQL
    def connect(self):
        # Utiliza la librería mysql.connector para conectarse a la base de datos
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.connection  # Retorna la conexión establecida

    # Método para ejecutar una consulta SQL en la base de datos
    # Recibe un parámetro 'query', que es la consulta SQL a ejecutar
    def execute_query(self, query):
        cursor = self.connection.cursor()  # Crea un cursor para ejecutar la consulta
        cursor.execute(query)  # Ejecuta la consulta SQL
        result = cursor.fetchall()  # Obtiene todos los resultados de la consulta
        return result  # Retorna los resultados

    # Método para cerrar la conexión con la base de datos MySQL
    def close_connection(self):
        if self.connection:
            self.connection.close()  # Cierra la conexión si está activa
            print("Conexión MySQL cerrada.")  # Imprime un mensaje indicando que la conexión ha sido cerrada
