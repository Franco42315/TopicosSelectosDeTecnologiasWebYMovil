import mysql.connector
from .db_connection import DBConnection

# Definimos la clase MySQLConnection que hereda de DBConnection
class MySQLConnection(DBConnection):
    # Método constructor que inicializa los atributos para la conexión
    def __init__(self, host, user, password, database):
        self.host = host             # Dirección del servidor MySQL
        self.user = user             # Usuario para la conexión
        self.password = password     # Contraseña del usuario
        self.database = database     # Base de datos a la que se conectará
        self.connection = None       # Inicializamos la variable de conexión

    # Implementación del método abstracto connect()
    def connect(self):
        # Utilizamos mysql.connector para realizar la conexión a la base de datos
        self.connection = mysql.connector.connect(
            host=self.host,          # Usamos los valores definidos en el constructor
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.connection       # Retornamos el objeto de conexión
    
    # Método para cerrar la conexión
    def close_connection(self):
        if self.connection:
            self.connection.close()  # Cerramos la conexión si está abierta
            print("Conexión cerrada.")
        else:
            print("No hay conexión activa para cerrar.")
