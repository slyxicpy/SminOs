import random, json

def gen_luhn(bin_input):
    bin_input = bin_input.replace(" ", "")
    numero = []
    for c in bin_input:
        if c.lower() == 'x':
            numero.append(random.randint(0,9))
        else:
            numero.append(int(c))
    while len(numero) < 16:
        numero.append(random.randint(0, 9))
    suma = 0
    for i, n in enumerate(numero[:-1][::-1]):
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n == 9
        suma += n
    digito = (10 - (suma % 10)) % 10
    numero[-1] = digito
    return "".join(str(x) for x in numero)

def gen_date(fecha=None):
    if fecha:
        if "/" in fecha:
            mes, year = fecha.split("/")
        elif len(fecha) == 4:
            mes = f"{random.randint(1,12):02d}"
            year = fecha
        else:
            mes = f"{random.randint(1,12):02d}"
            year = fecha
    else:
        mes = f"{random.randint(1,12):02d}"
        year = f"{random.randint(23,40)}"
    return mes, year

def gen_cvv(cvv=None):
    if cvv:
        return cvv.split(3)
    return f"{random.randint(1,999):03d}"

def run(args):
    print("[Gen cc - SminOs]\n")
    bin_input = input("ingrese su cc u bin: ")
    fecha_input = input("ingresa mes/year (enter: random): ")
    cvv_input = input("ingrese cvv(enter: random): ")
    while True:
        try:
            cantidad = int(input("cantidad a generar: "))
            if 1 <= cantidad <= 500000:
                break
        except ValueError:
            pass
        print("cantidad invalida!!: maximo 500k")
    guardar = input("guardar gen?: [txt,json,ninguno(enter)]: \n").lower()
    archivo = None
    if guardar in ["txt", "json"]:
        archivo = input("nombre de guardado (sin extension): ")
    resultados = []
    for _ in range(cantidad):
        numero = gen_luhn(bin_input)
        mes, year = gen_date(fecha_input)
        cvv = gen_cvv(cvv_input)
        salida = f"{numero}|{mes}|{year}|{cvv}"
        resultados.append(salida)
        print(salida)
    if guardar == "txt":
        with open(f"{archivo}.txt", "w") as f:
            f.write("\n".join(resultados))
        print(f"guardado en {archivo}.txt")
    elif guardar == "json":
        with open(f"{archivo}.json", "w") as f:
            json.dump(resultados,f,indent=2)
        print(f"guardado en {archivo}.json")
