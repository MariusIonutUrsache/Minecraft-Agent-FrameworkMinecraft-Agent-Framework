# Minecraft Agent Framework

Este proyecto implementa un framework en Python que permite la creación de agentes (bots) para interactuar dentro de un servidor de Minecraft ejecutado en `localhost`. Utiliza la librería `mcpi` para la interacción con Minecraft y soporta múltiples agentes con diferentes funcionalidades.

# Autores del Proyecto:

- Marius Ionut Ursache
- Àlex Casanova Margalef

## Instalación

### 1️⃣ Requisitos Previos
1. Python 3.10 o superior.
2. Servidor de Minecraft con el plugin **RaspberryJuice**.
3. API Key de OpenAI (Opcional, solo para `BotGpt`).

### 2️⃣ Pasos para la Instalación
1. Clonar el Repositorio:
   ```bash
   git clone https://github.com/MariusIonutUrsache/Minecraft-Agent-Framework
   
2. Instalar Dependencias:

    ```bash
    pip install mcpi
    pip install openai

3. Configurar la Variable de Entorno OPENAI_API_KEY (Opcional):**

- Windows CMD:
    ```bash
    set OPENAI_API_KEY="tu-clave-api"
- Windows PowerShell:

    ```bash
    $env:OPENAI_API_KEY="tu-clave-api"
- Linux/macOS:
    ```bash
    export OPENAI_API_KEY="tu-clave-api"
    
4. Ejecutar Minecraft (Versión 1.12):

5. Configura un servidor en localhost.

6. Ejecuta StartServer.sh para iniciar el servidor.

7. Iniciar el Framework:
    ```bash
    python main.py

### 3️⃣ Creación de Agentes
1. Crear un Nuevo Agente
Crea un archivo en el directorio agents/, por ejemplo: BotSaludo.py.
Hereda de la clase AgenteBase e implementa los métodos start() y stop().
- Ejemplo de un agente:
    ```python
    from framework.AgenteBase import AgenteBase

    class BotSaludo(AgenteBase):
        def __init__(self, mc):
            super().__init__("BotSaludo")
            self.mc = mc

        def start(self):
            self.running = True
            while self.running:
                self.mc.postToChat("¡Hola a todos!")
        
        def stop(self):
            self.running = False

2. Registrar el Agente
- Abre main.py y registra el agente en el framework:

    ```python

    from agents.BotSaludo import BotSaludo
    bot_saludo = BotSaludo(mc)
    framework.register_agent(bot_saludo)

### 4️⃣ Tests y Cobertura de Código
Este proyecto incluye pruebas unitarias que verifican el funcionamiento de los agentes y el framework. Para ejecutarlas:

- Instalar Coverage:
    ```bash
    pip install coverage
- Ejecutar Tests:
    ```bash
    coverage run -m unittest discover -s tests
- Generar Informe HTML de Cobertura:
    ```bash
    coverage html
    start htmlcov/index.html  # En Windows
    open htmlcov/index.html   # En macOS
    xdg-open htmlcov/index.html  # En Linux

FIN