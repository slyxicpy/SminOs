import sys
from llama_cpp import Llama

def run(args):
    model_path = "system/models/phi.gguf"
    print("Cargando modelo.....!")
    try:
        llm = Llama(
            model_path=model_path,
            n_threads=2,
            n_gpu_layers=0,
            n_ctx=4000,
            verbose=False
        )
    except Exception as e:
        print(f"Error al cargar modelo! {e}")
        return
    print("[V] Cargando! usa exit para salir")
    history = """### Instrucciones:
Eres una IA conversacional simpática y coqueta 😏.
Respondes siempre en español, breve y clara, con un tono juguetón y divertido.
"""
    while True:
        user_input = input(f"You: ")
        if user_input.lower() in ["exit", "quit", "salir"]:
            print("cerrando chat")
            break
        history += f"\n### Usuario:\n{user_input}\n\n### Asistente:\n"
        output = llm(
            history,
            max_tokens=256,
            stop=["### Usuario:", "### Asistente:", "\n\n"],
            echo=False
        )
        text = output["choices"][0]["text"].strip()
        print(f"AI: {text}\n")
        history += text

if __name__ == "__main__":
    run(sys.argv[1:])
