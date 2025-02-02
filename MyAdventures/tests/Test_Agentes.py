import unittest
from framework.AgenteBase import AgenteBase


class TestAgenteBase(unittest.TestCase):
    def test_cannot_instantiate_abstract_class(self):
        """Prueba que no se puede instanciar AgenteBase directamente."""
        with self.assertRaises(TypeError):
            agente = AgenteBase("TestAgent")
        print("[TEST] No se puede instanciar la clase abstracta AgenteBase.")

    def test_subclass_implementation(self):
        """Prueba que una subclase puede implementar AgenteBase correctamente."""
        # Crear una subclase concreta para probar
        class TestAgent(AgenteBase):
            def start(self):
                self.running = True

            def stop(self):
                self.running = False

        # Instanciar la subclase concreta
        agente = TestAgent("TestAgent")
        self.assertEqual(agente.name, "TestAgent")
        self.assertFalse(agente.running)

        # Probar los métodos start y stop
        agente.start()
        self.assertTrue(agente.running)

        agente.stop()
        self.assertFalse(agente.running)
        print("[TEST] Subclase de AgenteBase implementada correctamente.")

if __name__ == "__main__":
    unittest.main()
