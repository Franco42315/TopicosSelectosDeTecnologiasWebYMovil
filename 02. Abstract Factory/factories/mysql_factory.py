from db.mysql_connection import MySQLConnection
from .db_factory import DBConnectionFactory

# Fábrica concreta para crear conexiones MySQL
class MySQLConnectionFactory(DBConnectionFactory):
    # Constructor que recibe los parámetros necesarios para establecer la conexión a MySQL
    def __init__(self, host, user, password, database):
        # Asigna los valores de conexión a los atributos de la clase
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # Implementación del método 'create_connection' definido en la clase abstracta
    # Este método devuelve una instancia de MySQLConnection configurada con los valores proporcionados
    def create_connection(self):
        return MySQLConnection(self.host, self.user, self.password, self.database)
