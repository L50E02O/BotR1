"""
Patrón Singleton: Asegura una única instancia del cliente de OpenAI.
"""
from dotenv import load_dotenv
import openai
import os
import threading

class OpenAIClientSingleton:
    """Patrón Singleton para el cliente de OpenAI."""
    
    _instance = None
    _client = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
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

