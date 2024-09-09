from abc import ABC, abstractmethod

# Definimos una clase abstracta llamada DBConnection, que servirá como plantilla
class DBConnection(ABC):
    # Definimos un método abstracto que obliga a las clases hijas a implementarlo
    @abstractmethod
    def connect(self):
        # Este método debe ser implementado por las subclases
        pass
    
    # Método abstracto para cerrar la conexión
    @abstractmethod
    def close_connection(self):
        pass