import sys
import os
import time
import math
# Obtener la ruta absoluta del directorio actual (donde está StatsBot.py)
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)
from framework.AgenteBase import AgenteBase


class StatsBot(AgenteBase):
    def __init__(self, mc):
        super().__init__("StatsBot")
        self.mc = mc
        self.start_time = time.time()  # Tiempo en que se inicia el bot
        self.last_position = None
        self.distance_traveled = 0.0
        self.max_height = 0  # Altura maxima alcanzada
        self.blocks_descended = 0  # Bloques descendidos
        self.jump_count = 0  # Veces que el jugador ha saltado
        print(f"[INFO] {self.name} inicializado correctamente.")

    def start(self):
        """Inicia el bot para monitorear estadísticas del jugador."""
        self.running = True
        print(f"[INFO] {self.name} iniciado.")
        while self.running:
            try:
                mensajes = self.mc.events.pollChatPosts()  # Leer mensajes del chat
                for mensaje in mensajes:
                    texto = mensaje.message.lower()
                    if texto.startswith("statsbot"):  # Comando para activar el StatsBot
                        print("[DEBUG] Comando StatsBot recibido.")
                        self.enviar_estadisticas()
                self.actualizar_estadisticas()  # Actualizar estadísticas de posición
                time.sleep(1)  # Pausa para evitar saturar el servidor
            except Exception as e:
                print(f"[ERROR] {self.name}: {e}")

    def enviar_estadisticas(self):
        """Envía las estadísticas del jugador al chat."""
        try:
            # Obtener posición actual del jugador
            pos = self.mc.player.getTilePos()
            tiempo_jugado = int(time.time() - self.start_time)  # Tiempo de juego en segundos
            horas, resto = divmod(tiempo_jugado, 3600)
            minutos, segundos = divmod(resto, 60)

            # Enviar estadísticas al chat
            self.mc.postToChat(f"[StatsBot]: Posicion actual -> x: {pos.x}, y: {pos.y}, z: {pos.z}")
            self.mc.postToChat(f"[StatsBot]: Tiempo de juego -> {horas}h {minutos}m {segundos}s")
            self.mc.postToChat(f"[StatsBot]: Distancia recorrida -> {self.distance_traveled:.2f} bloques")
            self.mc.postToChat(f"[StatsBot]: Altura maxima alcanzada -> {self.max_height} bloques")
            self.mc.postToChat(f"[StatsBot]: Bloques descendidos -> {self.blocks_descended}")
            self.mc.postToChat(f"[StatsBot]: Veces que has saltado -> {self.jump_count}")
            self.mc.postToChat(f"[StatsBot]: Ping del servidor -> {self.obtener_ping()} ms")
        except Exception as e:
            print(f"[ERROR] Error al enviar estadísticas: {e}")

    def actualizar_estadisticas(self):
        """Actualiza las estadísticas del jugador basadas en su posición."""
        try:
            pos = self.mc.player.getTilePos()
            if self.last_position:
                # Calcular distancia recorrida
                dx = pos.x - self.last_position.x
                dy = pos.y - self.last_position.y
                dz = pos.z - self.last_position.z
                distancia = math.sqrt(dx**2 + dy**2 + dz**2)
                self.distance_traveled += distancia

                # Verificar altura máxima
                if pos.y > self.max_height:
                    self.max_height = pos.y

                # Contar bloques descendidos
                if pos.y < self.last_position.y:
                    self.blocks_descended += self.last_position.y - pos.y

                # Contar saltos
                if pos.y > self.last_position.y:
                    self.jump_count += 1

            self.last_position = pos
        except Exception as e:
            print(f"[ERROR] Error al actualizar estadísticas: {e}")

    def obtener_ping(self):
        """Simula un cálculo de ping del servidor (puedes modificarlo según el sistema que uses)."""
        try:
            # Aquí se puede agregar lógica para obtener el ping real del servidor.
            # Por ahora, simulamos un ping aleatorio entre 50 y 100 ms.
            import random
            return random.randint(50, 100)
        except Exception as e:
            print(f"[ERROR] Error al calcular ping: {e}")
            return "N/A"

    def stop(self):
        """Detiene el bot."""
        self.running = False
        print(f"[INFO] {self.name} detenido.")
