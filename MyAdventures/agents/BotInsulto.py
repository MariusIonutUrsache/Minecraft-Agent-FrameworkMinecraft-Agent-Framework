import sys
import os
import time
import random
# Obtener la ruta absoluta del directorio actual (donde está Bot_Tnt.py)
current_dir = os.path.dirname(__file__)
# Navegar al directorio raíz del proyecto (un nivel hacia arriba)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
# Agregar el directorio raíz al PYTHONPATH si no está ya incluido
if project_root not in sys.path:
    sys.path.append(project_root)
from framework.AgenteBase import AgenteBase


class BotInsulto(AgenteBase):
    def __init__(self, mc):
        super().__init__("BotInsulto")
        self.mc = mc
        self.insultos = [
            "Eres noob",
            "Juegas como mi hermana pequena",
            "No espero nada de ti, y aun asi logras decepcionarme",
            "Das pena"
        ]

    def start(self):
        """Inicia el bot de insultos."""
        self.running = True
        print(f"[INFO] {self.name} iniciado.")
        while self.running:
            try:
                # Elegir un insulto aleatorio
                insulto = random.choice(self.insultos)
                mensaje = f"[InsultoBot] {insulto}"
                self.mc.postToChat(mensaje)
                print(f"[DEBUG] Enviando insulto: {mensaje}")
            except Exception as e:
                print(f"[ERROR] Error en {self.name}: {e}")
            time.sleep(10)

    def stop(self):
        """Detiene el bot de insultos."""
        self.running = False
        print(f"[INFO] {self.name} detenido.")
