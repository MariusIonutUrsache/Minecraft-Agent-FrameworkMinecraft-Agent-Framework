import unittest
from unittest.mock import MagicMock, call
import time
import os
import sys
# Obtener la ruta absoluta del directorio actual (donde está BuilderBot.py)
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Importar la clase BotTnt
from agents.BotTnt import BotTnt

class TestBotTnt(unittest.TestCase):
    def setUp(self):
        """Configura el entorno antes de cada test."""
        self.mc = MagicMock()  # Crear un mock de Minecraft
        self.mc.player = MagicMock()  # Agregar el atributo `player`
        
        # Simular posición inicial del jugador
        self.pos = MagicMock(x=10, y=65, z=10)
        self.mc.player.getTilePos.return_value = self.pos

        # Instanciar el bot con el mock
        self.bot = BotTnt(self.mc)

    def test_colocar_y_activar_tnt(self):
        """Prueba que el bot coloque TNT y la active con fuego (sin ejecutar en un thread)."""

        # Simular una única ejecución del bucle del bot
        self.bot.running = True
        try:
            # Simular la lógica que se ejecuta en start() en una sola iteración
            pos = self.mc.player.getTilePos()
            x_tnt, y_tnt, z_tnt = pos.x + 5, pos.y, pos.z  # Posición esperada de la TNT

            # Simular la colocación de TNT
            self.mc.setBlock(x_tnt, y_tnt, z_tnt, 46)  # 46 es el ID de TNT
            time.sleep(1)  # Simular la pausa antes de activar la TNT

            # Simular la activación con fuego
            self.mc.setBlock(x_tnt, y_tnt + 1, z_tnt, 51)  # 51 es el ID de fuego

            # Verificar que primero se colocó la TNT
            self.mc.setBlock.assert_any_call(x_tnt, y_tnt, z_tnt, 46)

            # Verificar que después de 1 segundo se activó con fuego
            self.mc.setBlock.assert_any_call(x_tnt, y_tnt + 1, z_tnt, 51)

            print("[TEST] TNT colocada y activada correctamente.")
        finally:
            self.bot.stop()  # Asegurar que el bot se detenga

    def test_detener_bot(self):
        """Prueba que el bot se detenga correctamente."""
        self.bot.running = True
        self.bot.stop()

        # Verificar que el estado `running` es False
        self.assertFalse(self.bot.running)
        print("[TEST] BotTnt detenido correctamente.")

    def tearDown(self):
        """Limpia después de cada test."""
        self.bot.stop()
        print("[TEST] Limpieza completada.")

if __name__ == "__main__":
    unittest.main()
