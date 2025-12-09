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
        """
        Ensure a single OpenAIClientSingleton instance exists and initialize the shared OpenAI client on first creation.
        
        On first instantiation, this method loads environment variables from a .env file, reads the `R1_api_Key` environment variable, and creates a shared OpenAI client assigned to `cls._client` with `base_url` set to "https://openrouter.ai/api/v1". Initialization is performed in a thread-safe manner to guarantee a single instance across threads.
        
        Returns:
            OpenAIClientSingleton: The singleton instance.
        """
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
        """
        Retrieve the shared OpenAI client instance.
        
        Returns:
            openai.OpenAI or None: The singleton OpenAI client stored by the class, or `None` if it has not been initialized.
        """
        return self._client
