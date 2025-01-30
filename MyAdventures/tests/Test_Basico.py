import sys
import os
import unittest
# Obtener la ruta absoluta del directorio actual (donde está Bot_Tnt.py)
current_dir = os.path.dirname(__file__)
# Navegar al directorio raíz del proyecto (un nivel hacia arriba)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
# Agregar el directorio raíz al PYTHONPATH si no está ya incluido
if project_root not in sys.path:
    sys.path.append(project_root)
from framework.AgenteBase import AgenteBase
import mcpi.minecraft as minecraft
import mcpi.block as block

class TestBasico(unittest.TestCase):
    def setUp(self):
        """Configura el entorno antes de cada test."""
        self.mc = minecraft.Minecraft.create()

    def test_hello_world(self):
        """Prueba enviar un mensaje 'Hola mundo'."""
        self.mc.postToChat("Hola mundo desde PYTHON")
        print("[TEST] Mensaje 'Hola mundo' enviado correctamente.")

    def test_place_block(self):
        """Prueba colocar un bloque de piedra frente al jugador."""
        pos = self.mc.player.getTilePos()
        self.mc.setBlock(pos.x + 1, pos.y, pos.z, block.STONE.id)
        print("[TEST] Bloque de piedra colocado correctamente frente al jugador.")

    def tearDown(self):
        """Limpia después de cada test."""
        print("[TEST] Limpieza completada.")

if __name__ == "__main__":
    unittest.main()
