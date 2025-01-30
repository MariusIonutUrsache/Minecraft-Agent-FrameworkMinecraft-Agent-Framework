from framework.Framework import Framework
from agents.BotChat import BotChat
from agents.BotInsulto import BotInsulto
from agents.BotTnt import BotTnt
from agents.BuilderBot import BuilderBot
from agents.StatsBot import StatsBot
from agents.BotGpt import BotGpt
import mcpi.minecraft as minecraft
import sys
import os


# Configurar el proyecto para que las importaciones funcionen correctamente
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '.'))
if project_root not in sys.path:
    sys.path.append(project_root)

def menu():
    """Muestra un menu interactivo para seleccionar bots."""
    print("\nSelecciona los bots que deseas ejecutar (separados por comas):")
    print("1 - BotChat")
    print("2 - BotInsulto")
    print("3 - BotTnt")
    print("4 - BuilderBot")
    print("5 - StatsBot")
    print("6 - BotGpt")
    print("7 - Detener todos los bots")
    print("8 - Salir")
    return input("Tu selección: ")

if __name__ == "__main__":
    mc = minecraft.Minecraft.create()

    # Inicializar framework
    framework = Framework()

    # Crear los bots disponibles
    bots = {
        "1": BotChat(mc),
        "2": BotInsulto(mc),
        "3": BotTnt(mc),
        "4": BuilderBot(mc),
        "5": StatsBot(mc),
        "6": BotGpt(mc)
    }

    while True:
        seleccion = menu().split(",")

        if "8" in seleccion:
            print("[INFO] Saliendo del programa.")
            break

        if "7" in seleccion:
            print("[INFO] Deteniendo todos los bots...")
            framework.stop()
            framework = Framework()  # Reiniciar el framework para limpiar los registros
            continue

        # Registrar y ejecutar los bots seleccionados
        for opcion in seleccion:
            bot = bots.get(opcion.strip())
            if bot:
                framework.register_agent(bot)
            else:
                print(f"[WARNING] Opcion invalida: {opcion}")

        # Iniciar los bots seleccionados
        try:
            framework.start()
        except KeyboardInterrupt:
            print("[INFO] Deteniendo bots por interrupcion del usuario.")
            framework.stop()
