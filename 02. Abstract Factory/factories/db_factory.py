from abc import ABC, abstractmethod

# Clase abstracta para las fábricas de conexiones
# Define un contrato para crear instancias de conexiones a distintas bases de datos
class DBConnectionFactory(ABC):
    # Método abstracto que deberá implementar cada fábrica concreta
    # Se espera que cada subclase de esta fábrica proporcione su propia implementación
    # para crear una conexión a una base de datos específica
    @abstractmethod
    def create_connection(self):
        pass
