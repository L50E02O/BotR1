from dotenv import load_dotenv
import openai
import os

load_dotenv()
secret_key = os.getenv("R1_api_Key")
Client = openai.OpenAI(api_key=secret_key, base_url="https://openrouter.ai/api/v1")

def chatGPT_answer(question_and_answers, prompt):
    conversation = [
        {
            "role": "system",
            "content": prompt,
        },
        {"role": "user", "content": question_and_answers},
    ]
    try:
        response = Client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=conversation,
        )
        reply = response.choices[0].message.content.strip()
        return reply

    except Exception as e:
        print(f"API error: {e}")
        return None

def main():
    out = False
    while not out:
        prompt = ""
        while not prompt.strip():
            prompt = input("Enter the system prompt: ").strip()
            if not prompt:
                print("Prompt cannot be empty. Please enter a valid prompt.")

        question_and_answers = ""
        while not question_and_answers.strip():
            question_and_answers = input("Enter your question: ").strip()
            if not question_and_answers:
                print("Question cannot be empty. Please enter a valid question.")
    
        # Call chatGPT_answer and print the response
        response = chatGPT_answer(question_and_answers, prompt)
        if response:
            print(f"ChatGPT response: {response}")
        
        answ = ""
        while answ not in ["S", "N"]:
            answ = input("Wanna ask again? S/N: ").strip().upper()
            if answ not in ["S", "N"]:
                print("Invalid input. Please enter 'S' to continue or 'N' to exit.")
        
        if answ == "N":
            out = True

if __name__ == "__main__":
    main()