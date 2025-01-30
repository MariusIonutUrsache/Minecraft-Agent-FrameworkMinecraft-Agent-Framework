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


class BotChat(AgenteBase):
    def __init__(self, mc):
        super().__init__("BotChat")
        self.mc = mc
        self.respuestas = self.cargar_respuestas()
        print(f"[INFO] {self.name} inicializado correctamente.")

    def cargar_respuestas(self):
        """Define las preguntas y respuestas predefinidas."""
        return {
            "hola": "Bienvenido",
            "como estas": "Estoy bien, y tu?",
            "que es minecraft": "Minecraft es un juego de construccion y aventuras donde puedes explorar mundos infinitos.",
            "como consigo diamantes": "Los diamantes se encuentran entre las capas 5 y 12 del mundo. Usa un pico de hierro o superior.",
            "como domestico un lobo": "Usa un hueso para domesticarlo. Los huesos se obtienen de los esqueletos.",
            "que es el nether": "El Nether es una dimension infernal en Minecraft con enemigos y recursos unicos.",
            "como construyo un portal al nether": "Necesitas 10 bloques de obsidiana y un mechero para activarlo.",
            "como consigo comida": "Puedes cazar animales, cultivar trigo o pescar.",
            "como consigo esmeraldas": "Las esmeraldas se encuentran en las montanas o comerciando con aldeanos.",
            "comandos": "<hola>, <como estas>, <que es minecraft>, <como consigo diamantes>, <como domestico un lobo>, <que es el nether>, <como consigo comida>, <como consigo esmeraldas>, <como construyo un portal al nether>"
        }

    def responder_pregunta(self, mensaje):
        """Busca una respuesta en la lista predefinida."""
        for pregunta, respuesta in self.respuestas.items():
            if pregunta in mensaje.lower():  # Busca si la pregunta está contenida en el mensaje
                return respuesta
        return "Lo siento, no tengo una respuesta para eso. Intenta otra pregunta."

    def start(self):
        """Inicia el bot y escucha mensajes en el chat de Minecraft."""
        self.running = True
        print(f"[INFO] {self.name} iniciado.")
        while self.running:
            try:
                mensajes = self.mc.events.pollChatPosts()  # Obtener todos los mensajes del chat
                for mensaje in mensajes:
                    texto = mensaje.message.lower()
                    if texto.startswith("bot "):  # Prefijo para activar el bot
                        pregunta = texto.replace("bot ", "").strip()
                        print(f"[DEBUG] Pregunta recibida: {pregunta}")
                        respuesta = self.responder_pregunta(pregunta)
                        print(f"[DEBUG] Respuesta generada: {respuesta}")
                        self.mc.postToChat(f"[BotChat]: {respuesta}")
                time.sleep(0.5)  # Pausa para evitar saturar el servidor
            except Exception as e:
                print(f"[ERROR] {self.name}: {e}")

    def stop(self):
        """Detiene el bot."""
        self.running = False
        print(f"[INFO] {self.name} detenido.")