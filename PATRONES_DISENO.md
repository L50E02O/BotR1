# Patrones de Diseño en BotR1

Este documento explica los tres tipos principales de patrones de diseño y cómo se han aplicado en el proyecto BotR1.

---

## Tipos de Patrones de Diseño

Los patrones de diseño se clasifican en tres categorías principales según su propósito:

### 1. **Patrones Creacionales (Creational Patterns)**
Se encargan de la **creación de objetos**, proporcionando mecanismos flexibles para instanciar clases. Ayudan a desacoplar el código de la creación específica de objetos.

**Ejemplos comunes:**
- Singleton
- Factory Method / Abstract Factory
- Builder
- Prototype

### 2. **Patrones Estructurales (Structural Patterns)**
Se enfocan en la **composición de clases y objetos** para formar estructuras más grandes. Facilitan la organización y las relaciones entre componentes.

**Ejemplos comunes:**
- Adapter
- Decorator
- Facade
- Proxy

### 3. **Patrones Comportamentales (Behavioral Patterns)**
Gestionan la **comunicación y responsabilidades** entre objetos. Definen cómo los objetos interactúan y distribuyen tareas.

**Ejemplos comunes:**
- Strategy
- Observer
- Command
- Template Method

---

## Patrones Implementados en BotR1

Este proyecto implementa un patrón de cada tipo para demostrar su aplicación práctica:

---

## 1. Patrón Singleton (Creacional)

### ¿Qué es?
El patrón **Singleton** asegura que una clase tenga **solo una instancia** y proporciona un punto de acceso global a ella.

### ¿Por qué es útil?
- **Ahorro de recursos**: Evita crear múltiples conexiones a APIs o bases de datos
- **Consistencia**: Garantiza que todos los componentes usen la misma instancia
- **Control centralizado**: Facilita la gestión de configuración y estado

### Implementación en BotR1

Archivo: `singleton.py`

```python
class OpenAIClientSingleton:
    """Patrón Singleton para el cliente de OpenAI."""
    
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAIClientSingleton, cls).__new__(cls)
            load_dotenv()
            secret_key = os.getenv("R1_api_Key")
            cls._client = openai.OpenAI(
                api_key=secret_key,
                base_url="https://openrouter.ai/api/v1"
            )
        return cls._instance

    def get_client(self):
        """Retorna la instancia única del cliente."""
        return self._client
```

### Cómo se usa:
```python
from singleton import OpenAIClientSingleton

client = OpenAIClientSingleton().get_client()
```

### Beneficios en este proyecto:
- Evita crear múltiples clientes de OpenAI innecesariamente
- Centraliza la configuración de la API
- Reduce el consumo de recursos

---

## 2. Patrón Facade (Estructural)

### ¿Qué es?
El patrón **Facade** proporciona una interfaz simplificada a un subsistema complejo. Oculta la complejidad de múltiples clases y proporciona una interfaz más fácil de usar.

### ¿Por qué es útil?
- **Simplicidad**: Oculta la complejidad del subsistema
- **Facilidad de uso**: Proporciona una interfaz más simple y clara
- **Desacoplamiento**: Reduce las dependencias entre el cliente y el subsistema

### Implementación en BotR1

Archivo: `facade.py`

```python
class APIFacade:
    """Facade que simplifica el uso de la API de OpenAI."""
    
    @staticmethod
    def build_conversation(system_prompt, user_message):
        """Construye la estructura de conversación de forma simple."""
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    
    @staticmethod
    def format_response(response):
        """Extrae y formatea la respuesta de la API."""
        if response and response.choices:
            return response.choices[0].message.content.strip()
        return None
    
    @staticmethod
    def create_request(client, model, conversation):
        """Crea una petición a la API de forma simplificada."""
        return client.chat.completions.create(
            model=model,
            messages=conversation
        )
```

### Cómo se usa:
```python
from facade import APIFacade

facade = APIFacade()
conversation = facade.build_conversation("Eres un asistente", "Hola")
response = facade.create_request(client, "model-name", conversation)
formatted = facade.format_response(response)
```

### Beneficios en este proyecto:
- Simplifica el uso de la API de OpenAI
- Oculta la complejidad de construir conversaciones y formatear respuestas
- Facilita el mantenimiento al centralizar la lógica de la API

---

## 3. Patrón Strategy (Comportamental)

### ¿Qué es?
El patrón **Strategy** define una familia de algoritmos, los encapsula y los hace intercambiables. Permite que el algoritmo varíe independientemente de los clientes que lo usan.

### ¿Por qué es útil?
- **Intercambiabilidad**: Cambiar el comportamiento en tiempo de ejecución
- **Extensibilidad**: Agregar nuevas estrategias sin modificar código existente
- **Principio Abierto/Cerrado**: Abierto para extensión, cerrado para modificación

### Implementación en BotR1

Archivo: `strategy.py`

```python
class ModelStrategy(ABC):
    """Interfaz base para estrategias de modelos."""
    
    @abstractmethod
    def get_model_name(self):
        """Retorna el nombre del modelo."""
        pass

    @abstractmethod
    def process_response(self, response):
        """Procesa la respuesta del modelo."""
        pass

class DeepSeekR1Strategy(ModelStrategy):
    """Estrategia para el modelo DeepSeek R1."""
    
    def get_model_name(self):
        return "deepseek/deepseek-r1:free"
    
    def process_response(self, response):
        return response.choices[0].message.content.strip()

class GPT4Strategy(ModelStrategy):
    """Estrategia para el modelo GPT-4."""
    
    def get_model_name(self):
        return "openai/gpt-4"
    
    def process_response(self, response):
        content = response.choices[0].message.content.strip()
        return f"[GPT-4 Response]\n{content}"
```

### Cómo se usa:
```python
from strategy import DeepSeekR1Strategy, GPT4Strategy
from chatbot import ChatBot

strategy = DeepSeekR1Strategy()  # o GPT4Strategy()
chatbot = ChatBot(strategy, processor_type="standard")
```

### Beneficios en este proyecto:
- Fácil cambiar entre diferentes modelos de IA
- Cada modelo puede tener su propia lógica de procesamiento
- Agregar nuevos modelos es simple (crear nueva clase Strategy)

---

## Integración de los Patrones

La clase `ChatBot` integra los tres patrones de forma cohesiva:

Archivo: `chatbot.py`

```python
class ChatBot:
    """Clase principal que integra Singleton, Strategy y Facade."""
    
    def __init__(self, model_strategy):
        self.client = OpenAIClientSingleton().get_client()
        self.model_strategy = model_strategy
        self.facade = APIFacade()
    
    def get_answer(self, question, system_prompt):
        """Obtiene una respuesta del modelo de IA."""
        try:
            conversation = self.facade.build_conversation(system_prompt, question)
            
            response = self.facade.create_request(
                self.client,
                self.model_strategy.get_model_name(),
                conversation
            )
            
            return self.model_strategy.process_response(response)
            
        except Exception as e:
            print(f"API error: {e}")
            return None
```

---

## Resumen Comparativo

| Patrón | Tipo | Propósito | Beneficio Principal |
|--------|------|-----------|---------------------|
| **Singleton** | Creacional | Una sola instancia | Ahorro de recursos y consistencia |
| **Facade** | Estructural | Simplificar interfaz compleja | Facilidad de uso y simplicidad |
| **Strategy** | Comportamental | Algoritmos intercambiables | Cambio de comportamiento dinámico |

---

## Ventajas de Usar Patrones de Diseño

1. **Código más mantenible**: Estructura clara y organizada
2. **Reutilización**: Componentes que pueden usarse en diferentes contextos
3. **Escalabilidad**: Fácil agregar nuevas funcionalidades
4. **Testabilidad**: Componentes desacoplados son más fáciles de probar
5. **Legibilidad**: Código más fácil de entender para otros desarrolladores

---

## Notas Finales

Los patrones de diseño son herramientas, no reglas estrictas. Deben usarse cuando aportan valor real al proyecto. En BotR1, estos patrones:

- Mejoran la organización del código
- Facilitan futuras extensiones (nuevos modelos, procesadores)
- Hacen el código más profesional y mantenible
- Sirven como ejemplo educativo de implementación práctica

---

## Estructura del Proyecto

El proyecto está organizado en archivos separados por responsabilidad:

- `singleton.py`: Implementación del patrón Singleton
- `strategy.py`: Implementación del patrón Strategy
- `facade.py`: Implementación del patrón Facade
- `chatbot.py`: Clase principal que integra los patrones
- `BotApi.py`: Punto de entrada principal del programa

---

**Autor**: BotR1 Project  
**Fecha**: 2025  
**Licencia**: MIT