"""
Clase principal que integra los patrones de diseño.
"""
from singleton import OpenAIClientSingleton
from facade import APIFacade


class ChatBot:
    """Clase principal que integra Singleton, Strategy y Facade."""
    
    def __init__(self, model_strategy):
        """
        Initialize the ChatBot with a model selection strategy and prepare API integration.
        
        Parameters:
            model_strategy: Strategy object that provides the model name and response processing methods; used to select and handle the underlying language model.
        
        Attributes set:
            client: OpenAI API client obtained from the OpenAIClientSingleton.
            model_strategy: The provided strategy instance.
            facade: APIFacade instance used to build conversations and requests.
        """
        self.client = OpenAIClientSingleton().get_client()
        self.model_strategy = model_strategy
        self.facade = APIFacade()
    
    def get_answer(self, question, system_prompt):
        """
        Send the given system prompt and user question to the configured model and return the strategy-processed response.
        
        Parameters:
            question (str): The user's question to be answered by the model.
            system_prompt (str): High-level system instruction or context for the model.
        
        Returns:
            The processed response produced by the model strategy, or `None` if an error occurs.
        """
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
