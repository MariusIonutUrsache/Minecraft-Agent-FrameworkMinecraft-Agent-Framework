import unittest
import mcpi.block as block
from unittest.mock import MagicMock, call
from agents.BuilderBot import BuilderBot


class TestBuilderBot(unittest.TestCase):
    def setUp(self):
        """Configura el entorno antes de cada test."""
        self.mc = MagicMock()  # Crear un mock de Minecraft
        self.mc.player = MagicMock()  # Añadir el atributo `player`
        self.builder_bot = BuilderBot(self.mc)  # Instanciar el BuilderBot con el mock

    def test_construir_torre(self):
        """Prueba que el bot construya una torre correctamente."""
        # Simular la posición del jugador
        pos = MagicMock(x=0, y=5, z=0)
        self.mc.player.getTilePos.return_value = pos

        # Llamar a la función para construir la torre
        self.builder_bot.construir_torre(altura=3)

        # Verificar que se colocaron los bloques en las posiciones correctas
        llamadas_esperadas = [
            call(2, 5, 0, block.STONE.id),
            call(2, 6, 0, block.STONE.id),
            call(2, 7, 0, block.STONE.id),
        ]
        self.mc.setBlock.assert_has_calls(llamadas_esperadas, any_order=False)
        print("[TEST] Torre construida correctamente.")

    def test_construir_pared(self):
        """Prueba que el bot construya una pared correctamente."""
        # Simular la posición del jugador
        pos = MagicMock(x=0, y=5, z=0)
        self.mc.player.getTilePos.return_value = pos

        # Llamar a la función para construir la pared
        self.builder_bot.construir_pared(ancho=3, alto=2)

        # Verificar que se colocaron los bloques en las posiciones correctas
        llamadas_esperadas = [
            call(2, 5, 0, block.STONE.id),
            call(3, 5, 0, block.STONE.id),
            call(4, 5, 0, block.STONE.id),
            call(2, 6, 0, block.STONE.id),
            call(3, 6, 0, block.STONE.id),
            call(4, 6, 0, block.STONE.id),
        ]
        self.mc.setBlock.assert_has_calls(llamadas_esperadas, any_order=False)
        print("[TEST] Pared construida correctamente.")

    def tearDown(self):
        """Limpia después de cada test."""
        print("[TEST] Limpieza completada.")


if __name__ == "__main__":
    unittest.main()
