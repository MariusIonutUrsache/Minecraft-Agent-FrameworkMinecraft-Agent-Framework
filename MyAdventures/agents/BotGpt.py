from framework.AgenteBase import AgenteBase
import os
import openai
import time
import sys
# Obtener la ruta absoluta del directorio actual (donde está el bot)
current_dir = os.path.dirname(__file__)
# Navegar al directorio raíz del proyecto (un nivel hacia arriba)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
# Agregar el directorio raíz al PYTHONPATH si no está ya incluido
if project_root not in sys.path:
    sys.path.append(project_root)

# Configurar la API de OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")

class BotGpt(AgenteBase):
    def __init__(self, mc):
        super().__init__("BotChat")
        self.mc = mc
        
    def procesar_mensaje(self, mensaje):
        """
        Procesa un mensaje con la API de OpenAI y devuelve la respuesta.
        """
        try:
            # Llamar a la API de OpenAI
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un asistente amigable dentro de Minecraft."},
                    {"role": "user", "content": mensaje}
                ]
            )
            # Extraer la respuesta generada por el modelo
            return response['choices'][0]['message']['content']
        except Exception as e:
            # Error 429: Es necesario añadir saldo para poder usar el API
            print(f"[ERROR] Error al llamar a la API de OpenAI: {e}")
            return "Lo siento, no puedo procesar tu mensaje en este momento."

    def start(self):
        """Inicia el agente y responde a los mensajes del chat."""
        self.running = True
        print(f"[INFO] {self.name} iniciado.")
        while self.running:
            try:
                # Obtener mensajes del chat    
                mensajes = self.mc.events.pollChatPosts()
                for mensaje in mensajes:
                    usuario = mensaje.entityId
                    texto = mensaje.message
                    print(f"[DEBUG] Mensaje recibido de {usuario}: {texto}")

                    # Generar respuesta usando la API de OpenAI
                    respuesta = self.procesar_mensaje(texto)
                    print(f"[DEBUG] Respuesta generada: {respuesta}")

                    # Enviar respuesta al chat de Minecraft
                    self.mc.postToChat(respuesta)

                time.sleep(1)  # Esperar 1 segundo antes de comprobar nuevos mensajes
            except Exception as e:
                print(f"[ERROR] Error en el bot {self.name}: {e}")

    def stop(self):
        """Detiene el agente."""
        self.running = False
        print(f"[INFO] {self.name} detenido.")