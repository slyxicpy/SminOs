import os
import sys
from openai import OpenAI

# Bytyx: Uso de la api OpenAi, para chatgpt en terminal

def run(args):
    api = os.getenv("OPENAI_API_KEY")
    if not api:
        print(f"Uso de OPENAI_API_KEY, debe definir la APIKEY en la variable .env")
        return

    client = OpenAI(api_key=api)
    system_prompt = """Eres una IA coqueta, simpática y juguetona. Respondes siempre en español, breve, clara y sexy, con un tono divertido y travieso"""

    print("[V] GPT cargado! usa exit para salir!")
    history = [{"role": "system", "content": system_prompt}]
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "salir", "hakai", "quit"]:
            print("Cerrando chat!")
            break
        history.append({"role": "user", "content": user_input})
        if len(history) > 20:
            history = history[:1] + history[-19:]

        response = client.chat.completions.create(
            model="gpt-4o-mini", # Puede cambiar!
            messages=history,
            max_tokens=500
        )
        answer = response.choices[0].message.content.strip()
        print(f"GPT: {answer}")
        history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    run(sys.argv[1:])
