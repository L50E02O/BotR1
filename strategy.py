"""
Patrón Strategy: Define estrategias intercambiables para diferentes modelos de IA.
"""
from abc import ABC, abstractmethod


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

