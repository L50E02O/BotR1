"""
Bot API R1 - Punto de entrada principal.
"""
from chatbot import ChatBot
from strategy import DeepSeekR1Strategy


def main():
    """
    Run the interactive command-line chat loop that prompts for a system prompt and user questions.
    
    Creates a DeepSeekR1Strategy and a ChatBot, then repeatedly:
    - asks the user for a non-empty system prompt,
    - asks the user for a non-empty question,
    - queries the chatbot for a response and prints it,
    - asks whether to continue and exits when the user chooses not to.
    
    The function prints a header at start and a farewell message ("Hasta luego!") on exit.
    """
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
            print(f"\nRespuesta de ChatGPT: {response}\n")
        
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