import unittest
import time
import threading
from agents.BotChat import BotChat
from unittest.mock import MagicMock, patch


class TestBotChat(unittest.TestCase):
    def setUp(self):
        """Configura el entorno antes de cada test."""
        self.mc = MagicMock()  # Crear un mock de Minecraft
        self.bot = BotChat(self.mc)  # Instanciar el bot con el mock

    def test_responder_pregunta_existente(self):
        """Prueba que el bot responda correctamente a una pregunta conocida."""
        pregunta = "hola"
        respuesta_esperada = "Bienvenido"

        respuesta_obtenida = self.bot.responder_pregunta(pregunta)

        self.assertEqual(respuesta_obtenida, respuesta_esperada)
        print(f"[TEST] Pregunta: '{pregunta}' → Respuesta: '{respuesta_obtenida}' (Correcto)")

    def test_responder_pregunta_no_existente(self):
        """Prueba que el bot devuelva una respuesta genérica si la pregunta no está en su base de datos."""
        pregunta = "cual es tu color favorito"
        respuesta_esperada = "Lo siento, no tengo una respuesta para eso. Intenta otra pregunta."

        respuesta_obtenida = self.bot.responder_pregunta(pregunta)

        self.assertEqual(respuesta_obtenida, respuesta_esperada)
        print(f"[TEST] Pregunta desconocida: '{pregunta}' → Respuesta: '{respuesta_obtenida}' (Correcto)")

    def test_enviar_respuesta_al_chat(self):
        """Prueba que el bot envíe la respuesta correcta al chat de Minecraft (ejecutado en un thread)."""
        pregunta = "bot hola"
        respuesta_esperada = "[BotChat]: Bienvenido"

        # Simular un mensaje en el chat
        mensaje_mock = MagicMock()
        mensaje_mock.message = pregunta
        self.mc.events.pollChatPosts.return_value = [mensaje_mock]

        # Ejecutar el bot en un hilo separado
        bot_thread = threading.Thread(target=self.bot.start, daemon=True)
        self.bot.running = True
        bot_thread.start()

        # Esperar un poco para que el bot procese el mensaje
        time.sleep(2)

        # Detener el bot y esperar a que el hilo termine
        self.bot.stop()
        bot_thread.join()

        # Verificar que se envió la respuesta correcta al chat
        self.mc.postToChat.assert_called_with(respuesta_esperada)
        print(f"[TEST] Mensaje enviado al chat: '{respuesta_esperada}' (Correcto)")

    def test_detener_bot(self):
        """Prueba que el bot se detenga correctamente."""
        self.bot.running = True
        self.bot.stop()

        self.assertFalse(self.bot.running)
        print("[TEST] BotChat detenido correctamente.")

    def tearDown(self):
        """Limpia después de cada test."""
        self.bot.stop()
        print("[TEST] Limpieza completada.")

if __name__ == "__main__":
    unittest.main()
