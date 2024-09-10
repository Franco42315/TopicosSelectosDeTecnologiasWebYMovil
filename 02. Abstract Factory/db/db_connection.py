from abc import ABC, abstractmethod

# Interfaz para definir métodos de conexión, consulta y cierre de conexiones
class DBConnection(ABC):
    # Método abstracto para conectar a la base de datos
    # Este método debe ser implementado en las clases concretas que hereden de esta interfaz
    @abstractmethod
    def connect(self):
        pass

    # Método abstracto para ejecutar una consulta en la base de datos
    # Recibe un parámetro 'query' que debe ser la consulta SQL a ejecutar
    # Este método debe ser implementado en las clases concretas que hereden de esta interfaz
    @abstractmethod
    def execute_query(self, query):
        pass

    # Método abstracto para cerrar la conexión con la base de datos
    # Este método debe ser implementado en las clases concretas que hereden de esta interfaz
    @abstractmethod
    def close_connection(self):
        pass
