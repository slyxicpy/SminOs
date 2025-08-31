import random
import string

def run():
    print("[pass gen!]")
    while True:
        try:
            length = int(input("longitud (min 6| max 128)"))
            if 6 <= length <= 128:
                break
            else:
                print("ingresa num valido!")
        except ValueError:
            print("numero invalido!")
    use_upper = input("mayusculas? (s|n): ").strip().lower() == 's'
    use_lower = input("minusculas? (s|n): ").strip().lower() == 's'
    use_digits = input("numeros? (s|n): ").strip().lower() == 's'
    use_symbols = input("simbolos? (s|n): ").strip().lower() == 's'
    charset = ""
    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation
    if not charset:
        print("selecciona al menos un tipo de character!")
        return
    password = ''.join(random.choice(charset) for _ in range(length))
    print(f"\nPassword generada!: {password}")
