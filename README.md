# BotR1 - Consultas a la API de R1

Proyecto simple en Python para hacer consultas a la API de R1 usando OpenAI. Básicamente envías un prompt y recibes una respuesta procesada.

## Requisitos

- Python 3.7 o superior
- Cuenta y credenciales de acceso a la API de R1 en https://openrouter.ai/settings/keys

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/L50E02O/BotApiR1.git
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
```

3. Activa el entorno virtual:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto con tu clave de API:

```
R1_api_Key=tu_clave_de_api_aqui
```

## Uso

Ejecuta el script principal:

```bash
python BotApi.py
```

El programa te pedirá:
1. El prompt del sistema (instrucciones para el modelo)
2. Tu pregunta o consulta

Después de cada respuesta, puedes elegir si quieres hacer otra consulta o salir.

## Estructura del Proyecto

- `BotApi.py` - Script principal, punto de entrada
- `singleton.py` - Patrón Singleton para el cliente de OpenAI
- `strategy.py` - Patrón Strategy para diferentes modelos
- `facade.py` - Patrón Facade para simplificar la API
- `chatbot.py` - Clase principal que integra todo
- `requirements.txt` - Dependencias del proyecto

## Patrones de Diseño

Este proyecto implementa tres patrones de diseño:
- Singleton (Creacional): Una sola instancia del cliente
- Facade (Estructural): Simplifica el uso de la API
- Strategy (Comportamental): Intercambia entre diferentes modelos

Más detalles en `PATRONES_DISENO.md`.

## Contribuciones

Las contribuciones son bienvenidas. Abre un issue o pull request si quieres proponer cambios.

## Licencia

MIT License - ver el archivo LICENSE para más detalles.
