import sys
import os
import time
# Obtener la ruta absoluta del directorio actual (donde está el bot)
current_dir = os.path.dirname(__file__)
# Navegar al directorio raíz del proyecto (un nivel hacia arriba)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
# Agregar el directorio raíz al PYTHONPATH si no está ya incluido
if project_root not in sys.path:
    sys.path.append(project_root)

from framework.AgenteBase import AgenteBase
import mcpi.block as block


class BuilderBot(AgenteBase):
    def __init__(self, mc):
        super().__init__("BuilderBot")
        self.mc = mc

    def construir_torre(self, altura=5):
        """Construye una torre de piedra cerca del jugador."""
        try:
            # Obtener la posición del jugador
            pos = self.mc.player.getTilePos()
            x, y, z = pos.x + 2, pos.y, pos.z  # A 2 bloques del jugador
            print(f"[DEBUG] Construyendo torre en: x={x}, y={y}, z={z}, altura={altura}")

            # Construir la torre bloque por bloque
            for i in range(altura):
                self.mc.setBlock(x, y + i, z, block.STONE.id)  # Colocar piedra
                time.sleep(0.2)  # Pausa entre bloques para visualizar la construcción
            print("[INFO] Torre construida correctamente.")
        except Exception as e:
            print(f"[ERROR] {self.name} al construir la torre: {e}")

    def construir_pared(self, ancho=5, alto=3):
        """Construye una pared de piedra cerca del jugador."""
        try:
            # Obtener la posición del jugador
            pos = self.mc.player.getTilePos()
            x, y, z = pos.x + 2, pos.y, pos.z  # A 2 bloques del jugador
            print(f"[DEBUG] Construyendo pared en: x={x}, y={y}, z={z}, ancho={ancho}, alto={alto}")

            # Construir la pared
            for i in range(alto):  # Altura
                for j in range(ancho):  # Anchura
                    self.mc.setBlock(x + j, y + i, z, block.STONE.id)
                    time.sleep(0.1)  # Pausa para visualizar la construcción
            print("[INFO] Pared construida correctamente.")
        except Exception as e:
            print(f"[ERROR] {self.name} al construir la pared: {e}")

    def start(self):
        """Inicia el bot para construir estructuras en base a comandos del chat."""
        self.running = True
        print(f"[INFO] {self.name} iniciado.")
        while self.running:
            try:
                # Leer mensajes del chat
                mensajes = self.mc.events.pollChatPosts()
                for mensaje in mensajes:
                    texto = mensaje.message.lower()
                    if texto.startswith("builder torre"):  # Comando para construir una torre
                        altura = 5
                        try:
                            altura = int(texto.replace("builder torre", "").strip())  # Leer altura si se especifica
                        except ValueError:
                            pass  # Si no se especifica altura, usa 5 como predeterminado
                        self.construir_torre(altura)
                    elif texto.startswith("builder pared"):  # Comando para construir una pared
                        self.construir_pared()
                time.sleep(0.5)  # Pausa para evitar saturar el servidor
            except Exception as e:
                print(f"[ERROR] {self.name}: {e}")

    def stop(self):
        """Detiene el bot."""
        self.running = False
        print(f"[INFO] {self.name} detenido.")