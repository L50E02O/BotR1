"""
Patrón Strategy: Define estrategias intercambiables para diferentes modelos de IA.
"""
from abc import ABC, abstractmethod


class ModelStrategy(ABC):
    """Interfaz base para estrategias de modelos."""
    
    @abstractmethod
    def get_model_name(self):
        """
        Provide the model's canonical identifier.
        
        Returns:
            model_name (str): The model's identifier string (e.g., "openai/gpt-4").
        """
        pass

    @abstractmethod
    def process_response(self, response):
        """
        Process a raw model response and return the strategy-specific textual output.
        
        Parameters:
            response: The model response object expected to contain a `choices` sequence with message content (e.g., `response.choices[0].message.content`).
        
        Returns:
            processed_text (str): The text produced by applying the strategy's processing to the response.
        """
        pass


class DeepSeekR1Strategy(ModelStrategy):
    """Estrategia para el modelo DeepSeek R1."""
    
    def get_model_name(self):
        """
        Identifier for the DeepSeek R1 model.
        
        Returns:
            str: The model identifier "deepseek/deepseek-r1:free".
        """
        return "deepseek/deepseek-r1:free"
    
    def process_response(self, response):
        """
        Extract the first choice's message content from a model response and trim surrounding whitespace.
        
        Parameters:
            response: An API response object expected to contain a `choices` sequence where `choices[0].message.content` is the text content.
        
        Returns:
            str: The first choice's message content with leading and trailing whitespace removed.
        """
        return response.choices[0].message.content.strip()


class GPT4Strategy(ModelStrategy):
    """Estrategia para el modelo GPT-4."""
    
    def get_model_name(self):
        """
        Provide the strategy's model identifier for GPT-4.
        
        Returns:
            model_name (str): The model identifier "openai/gpt-4".
        """
        return "openai/gpt-4"
    
    def process_response(self, response):
        """
        Format and return the primary message content from a GPT-4 model response with a GPT-4 header.
        
        Parameters:
            response: An API response object expected to contain `choices[0].message.content`. The function extracts and trims that content.
        
        Returns:
            formatted (str): A string beginning with "[GPT-4 Response]\n" followed by the trimmed message content.
        """
        content = response.choices[0].message.content.strip()
        return f"[GPT-4 Response]\n{content}"
