import re

def run():
    print("[pass cheker!]")
    pwd = input("ingresa password: ").strip()
    score = 0
    reasons = []
    if len(pwd) >= 12:
        score += 2
    elif len(pwd) >= 8:
        score += 1
    else:
        reasons.append("muy corta! peligro extremo!")
    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        reasons.append("sin mayusculas..")
    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        reasons.append("sin minisculas..")
    if re.search(r"\d", pwd):
        score += 1
    else:
        reasons.append("sin numeros..")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        score += 1
    else:
        reasons.append("sin simbolos..")
    if score >= 6:
        strength = "Muy fuerte!!"
    elif score >= 4:
        strength = "Fuerte!!"
    elif score >= 2:
        strength = "Media!"
    else:
        strength = "Debil! cambiar ahora!"
    print(f"\nEvaluacion {strength}")
    if reasons:
        print("Puntos a mejorar:")
        for r in reasons:
            print(f"- {r}")
