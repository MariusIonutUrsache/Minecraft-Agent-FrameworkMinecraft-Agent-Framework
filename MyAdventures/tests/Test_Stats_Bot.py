import sys
import os
import unittest
from unittest.mock import MagicMock
import time
import math

# Obtener la ruta absoluta del directorio actual (donde está el test)
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from agents.StatsBot import StatsBot  # Importar el bot a probar
import mcpi.minecraft as minecraft

class TestStatsBot(unittest.TestCase):
    def setUp(self):
        """Configura el entorno antes de cada test."""
        # Crear un mock para el servidor de Minecraft
        self.mc = MagicMock(spec=minecraft.Minecraft)
        self.mc.player = MagicMock()  # Agregar el atributo player al mock
        
        # Configurar posición inicial del jugador
        initial_pos = MagicMock()
        initial_pos.x, initial_pos.y, initial_pos.z = 0, 64, 0
        self.mc.player.getTilePos.return_value = initial_pos

        # Instanciar el StatsBot con el mock
        self.stats_bot = StatsBot(self.mc)

        # Guardar la posición inicial para verificar distancia
        self.stats_bot.last_position = initial_pos

    def test_actualizar_estadisticas(self):
        """Prueba que las estadísticas del bot se actualicen correctamente."""
        # Configurar nueva posición del jugador
        new_pos = MagicMock()
        new_pos.x, new_pos.y, new_pos.z = 3, 65, 4
        self.mc.player.getTilePos.return_value = new_pos

        # Llamar al método de actualización
        self.stats_bot.actualizar_estadisticas()

        # Verificar que las estadísticas se actualizan correctamente
        self.assertAlmostEqual(self.stats_bot.distance_traveled, 5.0, delta=0.1)  # Distancia recorrida
        self.assertEqual(self.stats_bot.max_height, 65)  # Altura máxima alcanzada
        self.assertEqual(self.stats_bot.blocks_descended, 0)  # Ningún bloque descendido
        self.assertEqual(self.stats_bot.jump_count, 1)  # Un salto registrado

    def test_enviar_estadisticas(self):
        """Prueba que las estadísticas se envíen correctamente al chat."""
        # Actualizar estadísticas para configurar datos
        self.stats_bot.max_height = 70
        self.stats_bot.distance_traveled = 12.5

        # Llamar al método para enviar estadísticas
        self.stats_bot.enviar_estadisticas()

        # Verificar que los mensajes fueron enviados al chat
        self.mc.postToChat.assert_any_call("[StatsBot]: Altura maxima alcanzada -> 70 bloques")
        self.mc.postToChat.assert_any_call("[StatsBot]: Distancia recorrida -> 12.50 bloques")

    def test_obtener_ping(self):
        """Prueba que el ping del servidor sea razonable."""
        ping = self.stats_bot.obtener_ping()
        self.assertTrue(50 <= ping <= 100, "El ping debe estar entre 50 y 100 ms.")

    def tearDown(self):
        """Limpia después de cada test."""
        self.stats_bot.stop()
        print("[TEST] Limpieza completada.")

if __name__ == "__main__":
    unittest.main()
