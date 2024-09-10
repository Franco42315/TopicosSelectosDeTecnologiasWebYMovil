from factories.mysql_factory import MySQLConnectionFactory
from factories.postgresql_factory import PostgreSQLConnectionFactory
from factories.sqlite_factory import SQLiteConnectionFactory

if __name__ == "__main__":
    # Ejemplo con MySQL
    # Crear una instancia de la fábrica de conexiones MySQL con los parámetros de conexión
    mysql_factory = MySQLConnectionFactory(host="localhost", user="root", password="", database="prueba")
    # Usar la fábrica para crear una conexión
    db_connection = mysql_factory.create_connection()
    
    try:
        # Establecer la conexión a la base de datos MySQL
        db_connection.connect()
        print("Conexión a MySQL establecida.")
        # Ejecutar una consulta SQL y obtener los resultados
        result = db_connection.execute_query("SELECT * FROM clientes")
        print("Resultado de la consulta MySQL:", result)
    finally:
        # Cerrar la conexión a la base de datos MySQL
        db_connection.close_connection()

    # Ejemplo con PostgreSQL
    # Crear una instancia de la fábrica de conexiones PostgreSQL con los parámetros de conexión
    postgres_factory = PostgreSQLConnectionFactory(host="localhost", user="postgres", password="123456789", database="dbpostgresql")
    # Usar la fábrica para crear una conexión
    db_connection = postgres_factory.create_connection()

    try:
        # Establecer la conexión a la base de datos PostgreSQL
        db_connection.connect()
        print("Conexión a PostgreSQL establecida.")
        # Ejecutar una consulta SQL y obtener los resultados
        result = db_connection.execute_query("SELECT * FROM clientes")
        print("Resultado de la consulta PostgreSQL:", result)
    finally:
        # Cerrar la conexión a la base de datos PostgreSQL
        db_connection.close_connection()

    # Ejemplo con SQLite
    # Crear una instancia de la fábrica de conexiones SQLite con el archivo de base de datos
    sqlite_factory = SQLiteConnectionFactory(database="dbsqlite.db")
    # Usar la fábrica para crear una conexión
    db_connection = sqlite_factory.create_connection()

    try:
        # Establecer la conexión a la base de datos SQLite
        db_connection.connect()
        print("Conexión a SQLite establecida.")
        
        # Crear la tabla MiTabla si no existe
        db_connection.execute_query("""
            CREATE TABLE IF NOT EXISTS MiTabla (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                edad INTEGER
            );
        """)
        
        # Insertar tres registros en la tabla
        db_connection.execute_query("""
            INSERT INTO MiTabla (nombre, edad) VALUES ('Juan', 25);
        """)
        db_connection.execute_query("""
            INSERT INTO MiTabla (nombre, edad) VALUES ('Maria', 30);
        """)
        db_connection.execute_query("""
            INSERT INTO MiTabla (nombre, edad) VALUES ('Carlos', 28);
        """)

        print("Registros insertados en SQLite.")
        
        # Ejecutar una consulta para obtener todos los datos de la tabla MiTabla
        result = db_connection.execute_query("SELECT * FROM MiTabla")
        
        # Imprimir los resultados obtenidos
        print("Datos en MiTabla:", result)
        
    finally:
        # Cerrar la conexión a la base de datos SQLite
        db_connection.close_connection()
