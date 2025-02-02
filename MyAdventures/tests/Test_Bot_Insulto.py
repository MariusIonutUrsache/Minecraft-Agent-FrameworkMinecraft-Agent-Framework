import unittest
from unittest.mock import MagicMock, patch
import time
import os
import sys
import threading
# Obtener la ruta absoluta del directorio actual (donde está BuilderBot.py)
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Importar la clase BotInsulto
from agents.BotInsulto import BotInsulto

class TestBotInsulto(unittest.TestCase):
    def setUp(self):
        """Configura el entorno antes de cada test."""
        self.mc = MagicMock()  # Crear un mock de Minecraft
        self.bot = BotInsulto(self.mc)  # Instanciar el bot con el mock

    @patch("random.choice", return_value="Eres noob")  # Simular elección de insulto
    def test_enviar_insulto(self, mock_choice):
        """Prueba que el bot envíe al menos un insulto en el chat antes de detenerse."""
        
        # Ejecutar el bot en un hilo separado para evitar el bloqueo
        bot_thread = threading.Thread(target=self.bot.start, daemon=True)
        self.bot.running = True
        bot_thread.start()

        # Esperar un poco para que el bot envíe al menos un insulto
        time.sleep(2)

        # Detener el bot después de la prueba
        self.bot.stop()
        bot_thread.join()

        # Verificar que el insulto fue enviado al chat
        self.mc.postToChat.assert_called_with("[InsultoBot] Eres noob")
        print("[TEST] Insulto enviado correctamente.")

    def test_detener_bot(self):
        """Prueba que el bot se detenga correctamente."""
        self.bot.running = True
        self.bot.stop()
        
        # Verificar que el estado `running` es False
        self.assertFalse(self.bot.running)
        print("[TEST] BotInsulto detenido correctamente.")

    def tearDown(self):
        """Limpia después de cada test."""
        self.bot.stop()
        print("[TEST] Limpieza completada.")

if __name__ == "__main__":
    unittest.main()
