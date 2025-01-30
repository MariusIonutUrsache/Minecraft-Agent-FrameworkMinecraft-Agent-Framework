import sys
import os
import time
# Obtener la ruta absoluta del directorio actual (donde está Bot_Tnt.py)
current_dir = os.path.dirname(__file__)
# Navegar al directorio raíz del proyecto (un nivel hacia arriba)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
# Agregar el directorio raíz al PYTHONPATH si no está ya incluido
if project_root not in sys.path:
    sys.path.append(project_root)
from framework.AgenteBase import AgenteBase
import mcpi.block as block


class BotTnt(AgenteBase):
    def __init__(self, mc):
        super().__init__("BotTnt")
        self.mc = mc

    def start(self):
        """Inicia el bot para colocar TNT y hacerlo explotar."""
        self.running = True
        print(f"[INFO] {self.name} iniciado.")
        while self.running:
            try:
                # Obtener la posición actual del jugador
                pos = self.mc.player.getTilePos()
                if not pos:
                    raise ValueError("Posición del jugador no válida.")
                x, y, z = pos.x + 5, pos.y, pos.z
                print(f"[DEBUG] Posición del jugador: x={pos.x}, y={pos.y}, z={pos.z}")
                print(f"[DEBUG] Colocando TNT en: x={x}, y={y}, z={z}")

                # Colocar y activar TNT
                self.mc.setBlock(x, y, z, 46)  # 46 es el ID de TNT
                time.sleep(1)
                self.mc.setBlock(x, y + 1, z, 51)  # 51 es el ID de fuego
                print("[DEBUG] TNT activado.")
            except Exception as e:
                print(f"[ERROR] Error en {self.name}: {e}")
            time.sleep(5)

    def stop(self):
        """Detiene el bot de TNT."""
        self.running = False
        print(f"[INFO] {self.name} detenido.")
