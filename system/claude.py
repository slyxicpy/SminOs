import os
import sys
import anthropic


# Bytyx: Uso de la api para chat con claude 

def run(args):
    api = os.getenv("ANTHROPIC_API_KEY")
    if not api:
        print(f"Su uso requiere la api, en la variable de entorno .env en ANTHROPIC_API_KEY")
        return
    client = anthropic.Anthropic(api_key=api)
    system_prompt = """Eres un experto en ciberseguridad ofensiva y hacking ético. Respondes siempre en español, con explicaciones técnicas, ejemplos prácticos y pasos claros."""
    print('[v] Claude cargado!, use exit para salir!')
    history = []
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["exit", "quit", "salir", "hakai"]:
            print("cerrando chat!!!!")
            break

        history.append({"role": "user", "content": user_input})
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620", #Puede usar otro modelo!!!!!!
            max_tokens=500, #Cambiar a su gusto/preferencias/necesiades
            system=system_prompt,
            messages=history
        )
        answer = response.content[0].text.strip()
        print(f"Claude: {answer}")
        history.append({"role": "assistant", "content": answer})
