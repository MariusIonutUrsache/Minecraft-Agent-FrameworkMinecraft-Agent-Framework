from abc import ABC, abstractmethod

class AgenteBase(ABC):
    def __init__(self, name):
        """Inicializa el agente con un nombre."""
        self.name = name
        self.running = False

    @abstractmethod
    def start(self):
        """Método para iniciar el agente."""
        pass

    @abstractmethod
    def stop(self):
        """Método para detener el agente."""
        pass
