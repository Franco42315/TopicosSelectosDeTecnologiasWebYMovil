from factory.db_factory import DBFactory

# Punto de entrada de la aplicación
if __name__ == "__main__":
    # Definimos los datos de conexión para la base de datos MySQL
    host = "localhost"              # El servidor de la base de datos, en este caso localhost
    user = "root"                   # Usuario de MySQL (en XAMPP es 'root' por defecto)
    password = ""                   # Contraseña del usuario (vacía por defecto en XAMPP)
    database = "prueba"             # Nombre de la base de datos a la que nos conectaremos

    # Usamos la fábrica para obtener una conexión MySQL, pasándole el tipo de base de datos y las credenciales
    db_connection = DBFactory.get_connection('mysql', host, user, password, database)
    
    # Intentamos realizar la conexión a la base de datos
    try:
        # Conectamos a la base de datos y guardamos la conexión en la variable mydb
        mydb = db_connection.connect()
        print("Conexión exitosa:", mydb)  # Si la conexión es exitosa, mostramos el objeto de conexión
    except Exception as e:
        # Si ocurre un error, mostramos el mensaje de error
        print("Error al conectar a la base de datos:", str(e))
        
    # Finalmente, cerramos la conexión
    try:
        db_connection.close_connection()  # Cerramos la conexión a la base de datos
    except Exception as e:
        print("Error al cerrar la conexión:", str(e))