import threading

class Framework:
    def __init__(self):
        """Inicializa el framework con una lista de agentes."""
        self.agents = []

    def register_agent(self, agent):
        """Registra un agente en el framework."""
        self.agents.append(agent)
        print(f"[INFO] Agente {agent.name} registrado correctamente.")

    def start(self):
        """Inicia todos los agentes registrados en hilos separados."""
        print("[INFO] Iniciando agentes...")
        self.threads = []
        for agent in self.agents:
            thread = threading.Thread(target=agent.start)
            thread.daemon = True
            self.threads.append(thread)
            thread.start()
            print(f"[INFO] {agent.name} iniciado en un hilo.")

    def stop(self):
        """Detiene todos los agentes registrados."""
        print("[INFO] Deteniendo agentes...")
        for agent in self.agents:
            agent.stop()
        for thread in self.threads:
            thread.join(timeout=1)
        print("[INFO] Todos los agentes detenidos.")
