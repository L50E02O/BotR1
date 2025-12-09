"""
Bot API R1 - Punto de entrada principal.
"""
from chatbot import ChatBot
from strategy import DeepSeekR1Strategy


def main():
    """Función principal del programa."""
    strategy = DeepSeekR1Strategy()
    chatbot = ChatBot(strategy)
    
    print("=== Bot API R1 ===\n")
    
    out = False
    while not out:
        prompt = ""
        while not prompt.strip():
            prompt = input("Ingresa el prompt del sistema: ").strip()
            if not prompt:
                print("El prompt no puede estar vacío. Por favor ingresa un prompt válido.")
        
        question = ""
        while not question.strip():
            question = input("Ingresa tu pregunta: ").strip()
            if not question:
                print("La pregunta no puede estar vacía. Por favor ingresa una pregunta válida.")
        
        response = chatbot.get_answer(question, prompt)
        if response:
            print(f"\nRespuesta de {strategy.get_model_name()}: {response}\n")
        
        answ = ""
        while answ not in ["S", "N"]:
            answ = input("¿Quieres preguntar de nuevo? S/N: ").strip().upper()
            if answ not in ["S", "N"]:
                print("Entrada inválida. Por favor ingresa 'S' para continuar o 'N' para salir.")
        
        if answ == "N":
            out = True
    
    print("\nHasta luego!")


if __name__ == "__main__":
    main()
