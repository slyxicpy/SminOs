import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/119.0.0.0 Safari/537.36"
}

def chkbin(bin_input):
    bin_input = bin_input[:6]
    urls = [
        f"https://bincheck.io/details/{bin_input}"
       #f"https://bincheck.app/{bin_input}",
       #f"https://binlist.net/{bin_input}",
       #f"https://www.bincodes.com/bin/{bin_input}",
       #f"https://www.getodata.com/tools/bin-card-checker?bin={bin_input}"
    ]
    bin_input = bin_input[:6]  # solo primeros 6 dígitos
    url = f"https://bincheck.io/details/{bin_input}"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        info = {}
        # Buscar todas las filas de la tabla principal
        tabla = soup.find("table")
        if tabla:
            for fila in tabla.find_all("tr"):
                columnas = fila.find_all("td")
                if len(columnas) == 2:
                    etiqueta = columnas[0].get_text(strip=True)
                    valor = columnas[1].get_text(strip=True)
                    info[etiqueta] = valor

        if info:
            return info
        return {"error": "No se encontró información del BIN"}
    except Exception as e:
        return {"error": f"Error al obtener info del BIN: {e}"}
