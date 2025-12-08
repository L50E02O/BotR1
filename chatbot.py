"""
Clase principal que integra los patrones de diseño.
"""
from singleton import OpenAIClientSingleton
from facade import APIFacade


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

