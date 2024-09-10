from db.postgresql_connection import PostgreSQLConnection
from .db_factory import DBConnectionFactory

# Fábrica concreta para crear conexiones PostgreSQL
class PostgreSQLConnectionFactory(DBConnectionFactory):
    # Constructor que recibe los parámetros necesarios para establecer la conexión a PostgreSQL
    def __init__(self, host, user, password, database):
        # Asigna los valores de conexión a los atributos de la clase
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # Implementación del método 'create_connection' definido en la clase abstracta
    # Este método devuelve una instancia de PostgreSQLConnection configurada con los valores proporcionados
    def create_connection(self):
        return PostgreSQLConnection(self.host, self.user, self.password, self.database)
