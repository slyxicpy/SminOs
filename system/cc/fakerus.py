from faker import Faker
import json

def run():
    print(f"[GenFake Usser!]")
    while True:
        gener = input(f"genero (male|female|any): ").strip().lower()
        if gener in ["male", "female", "any"]:
            break
        print("Ingrese el genero!")
    while True:
        try:
            count = int(input("cantidad? (1|500000): "))
            if 1 <= count <= 500000:
                break
            else:
                print("ingrese cantidad!")
        except ValueError:
            print("num invalido!")
    save = input(f"desea guardar? (s|n): ").strip().lower()
    file_type = None
    file_name = None
    if save == "s":
        file_type = input("formato (txt|json): ").strip().lower()
        file_name = input("nombre de archivo sin extension: ").strip()
    fake = Faker()
    results = []
    for _ in range(count):
       #profile = fake.profile(sex=gener if gener != "any" else None)
        sex_mapping = {"male": "M", "female": "F", "any": None}
        profile = fake.profile(sex=sex_mapping[gener])
        additional = {
            "username": fake.user_name(),
            "password": fake.password(length=12),
            "phone_number": fake.phone_number(),
            "cell_number": fake.msisdn()[:12],
            "address": fake.address().replace("\n", ", "),
            "country": fake.country(),
            "company": fake.company(),
            "job": fake.job(),
            "ipv4": fake.ipv4(),
            "credit_card": {
                "provider": fake.credit_card_provider(),
                "number": fake.credit_card_number(),
                "exp": fake.credit_card_expire(),
                "cvv": fake.credit_card_security_code()
            }
        }
        profile.update(additional)
        results.append(profile)
    for r in results[:10]:
        print("\n---------------")
        for k, v in r.items():
            print(f"{k}: {str(v)}")
    print(f"\nTotal generados: {len(results)}")
    if save == "s":
        if file_type == "txt":
            with open(f"{file_name}.txt", "w") as f:
                for r in results:
                    for k, v in r.items():
                        f.write(f"{k}: {v}\n")
                    f.write("\n> ---- <\n")
            print(f"guardado como {file_name}.txt")
        elif file_type == "json":
            with open(f"{file_name}.json", "w") as f:
                json.dump(results, f, indent=4)
            print(f"guardado en {file_name}.json")
        else:
            print("formato no valido!, no se guardo!")

if __name__ == "__main__":
    run()
