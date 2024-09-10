from db.sqlite_connection import SQLiteConnection
from .db_factory import DBConnectionFactory

# Fábrica concreta para crear conexiones SQLite
class SQLiteConnectionFactory(DBConnectionFactory):
    # Constructor que recibe el nombre del archivo de la base de datos SQLite
    def __init__(self, database):
        # Asigna el nombre del archivo de la base de datos al atributo 'database'
        self.database = database

    # Implementación del método 'create_connection' definido en la clase abstracta
    # Este método devuelve una instancia de SQLiteConnection configurada con el valor proporcionado
    def create_connection(self):
        return SQLiteConnection(self.database)
