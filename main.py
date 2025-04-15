import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))


def chatbot(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error connecting to Gemini: {str(e)}"


def main():
    print("Welcome to the Chatbot! Type 'exit' to quit.")

    historical = []

    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() == "exit":
            print("Goodbye!")
            break

        historical.append(f"User: {user_input}")
        prompt = "\n".join(historical)
        response = chatbot(prompt)
        historical.append(f"Bot: {response}")

        print(f"\nBot: {response}")


if __name__ == "__main__":
    main()
