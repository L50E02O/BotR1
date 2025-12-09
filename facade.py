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
        Constructs a two-message conversation payload with system and user roles.
        
        Parameters:
            system_prompt (str): The system-level prompt that sets behavior or context.
            user_message (str): The user's message to include in the conversation.
        
        Returns:
            list: A list of two dicts formatted for the chat API: 
                  [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_message}].
        """
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    
    @staticmethod
    def format_response(response):
        """
        Extracts and return the trimmed content of the first message choice from an OpenAI chat response.
        
        Parameters:
            response: OpenAI chat response object expected to have a `choices` sequence where each choice contains a `message` with `content`.
        
        Returns:
            str: The first choice's message content with leading and trailing whitespace removed, or `None` if the response or its choices are missing.
        """
        if response and response.choices:
            return response.choices[0].message.content.strip()
        return None
    
    @staticmethod
    def create_request(client, model, conversation):
        """
        Constructs and sends a chat completion request to the OpenAI API.
        
        Parameters:
            model (str): Model name to use for the completion.
            conversation (list): List of message objects (dicts) formatted for the API.
        
        Returns:
            The API response object returned by the client's chat completion creation call.
        """
        return client.chat.completions.create(
            model=model,
            messages=conversation
        )
