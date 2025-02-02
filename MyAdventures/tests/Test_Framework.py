import unittest
from framework.AgenteBase import AgenteBase
from framework.Framework import Framework
from unittest.mock import MagicMock


class Test_Framework(unittest.TestCase):
    def setUp(self):
        """Configura el entorno antes de cada test."""
        self.framework = Framework()
        # Crear mocks para agentes
        self.agent1 = MagicMock(spec=AgenteBase)
        self.agent1.name = "Agent1"
        self.agent2 = MagicMock(spec=AgenteBase)
        self.agent2.name = "Agent2"

    def test_register_agent(self):
        """Prueba registrar agentes en el framework."""
        self.framework.register_agent(self.agent1)
        self.framework.register_agent(self.agent2)
        self.assertIn(self.agent1, self.framework.agents)
        self.assertIn(self.agent2, self.framework.agents)
        print("[TEST] Registro de agentes probado correctamente.")

    def test_start_agents(self):
        """Prueba iniciar todos los agentes en hilos separados."""
        self.framework.register_agent(self.agent1)
        self.framework.register_agent(self.agent2)

        self.framework.start()

        # Verificar que se haya llamado al método start de cada agente
        self.agent1.start.assert_called_once()
        self.agent2.start.assert_called_once()
        print("[TEST] Inicio de agentes probado correctamente.")

    def test_stop_agents(self):
        """Prueba detener todos los agentes."""
        self.framework.register_agent(self.agent1)
        self.framework.register_agent(self.agent2)

        self.framework.start()
        self.framework.stop()

        # Verificar que se haya llamado al método stop de cada agente
        self.agent1.stop.assert_called_once()
        self.agent2.stop.assert_called_once()
        print("[TEST] Detención de agentes probada correctamente.")

if __name__ == "__main__":
    unittest.main()
