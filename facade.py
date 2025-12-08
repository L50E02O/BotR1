"""
Patrón Facade: Simplifica la interfaz compleja de la API de OpenAI.
"""
from typing import List, Dict


class APIFacade:
    """
    Facade que simplifica el uso de la API de OpenAI.
    Oculta la complejidad de construir conversaciones y manejar respuestas.
    """
    
    @staticmethod
    def build_conversation(system_prompt, user_message):
        """
        Construye la estructura de conversación de forma simple.
        
        Args:
            system_prompt: Prompt del sistema
            user_message: Mensaje del usuario
        
        Returns:
            Lista de mensajes formateada para la API
        """
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    
    @staticmethod
    def format_response(response):
        """
        Extrae y formatea la respuesta de la API.
        
        Args:
            response: Respuesta de la API de OpenAI
        
        Returns:
            Contenido de la respuesta formateado
        """
        if response and response.choices:
            return response.choices[0].message.content.strip()
        return None
    
    @staticmethod
    def create_request(client, model, conversation):
        """
        Crea una petición a la API de forma simplificada.
        
        Args:
            client: Cliente de OpenAI
            model: Nombre del modelo
            conversation: Lista de mensajes
        
        Returns:
            Respuesta de la API
        """
        return client.chat.completions.create(
            model=model,
            messages=conversation
        )

