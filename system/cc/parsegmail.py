import itertools
import json

def gen_als(email: str, count: int):
    if "@" not in email:
        print("correo no valido!")
        return []
    user, domain = email.split("@")
    dot_positions = list(range(1, len(user)))
    all_variants = set()
    for n_dots in range(0, len(dot_positions)+1):
        for positions in itertools.combinations(dot_positions, n_dots):
            alias = ""
            for i, c in enumerate(user):
                alias += c
                if i in positions:
                    alias += "."
            all_variants.add(f"{alias}@{domain}")
    for i in range(1, min(10, count+1)):
        all_variants.add(f"{user}+{i}@{domain}")
    all_variants = list(all_variants)[:count]
    return all_variants

def run():
    email = input("digita el correo: ").strip()
    while True:
        try:
            count = int(input("cuantos a generar ?: "))
            if 1 <= count <= 5000000:
                break
            else:
                print("ingresa numero 1-500k")
        except ValueError:
            print("numero invalido!!!!!!!!!")
    results = gen_als(email, count)
    print(f"\nGeneradas {len(results)} variaciones:")
    for r in results[:50]:
        print(r)
    if len(results) > 50:
        print(f"... y {len(results)-50} mas!")
    save = input(f"quieres guardar? (s|n): ").strip().lower()
    if save == "s":
        tipo = input(f"formato? (txt|json): ").strip().lower()
        filename = input(f"nombre del archivo(sin extension!): ").strip()
        if tipo == "txt":
            with open(f"{filename}.txt", "w") as f:
                for r in results:
                    f.write(r + "\n")
            print(f"guardado como {filename}.txt")
        elif tipo == "json":
            with open(f"{filename}.json", "w") as f:
                json.dump(results, f, indent=4)
            print(f"guardado como {filename}.json")
        else:
            print("formato no disponible!, no se guardo!")

if __name__ == "___main__":
    run()
