from db.mysql_connection import MySQLConnection

# Definimos la clase DBFactory que maneja la creación de conexiones
class DBFactory:
    # Método estático que no requiere instancia de la clase para ser utilizado
    @staticmethod
    def get_connection(db_type, host, user, password, database):
        # Si el tipo de base de datos es 'mysql', retorna una instancia de MySQLConnection
        if db_type == 'mysql':
            return MySQLConnection(host, user, password, database)
        else:
            # Si no es MySQL, lanza una excepción indicando que no es compatible
            raise ValueError(f"Tipo de base de datos '{db_type}' no es compatible.")