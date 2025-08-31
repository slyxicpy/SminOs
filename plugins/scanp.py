from socket import *
import requests

def modos(modo):
    if modo == '-full':
        return list(range(1, 65536))
    elif modo == '-db':
        return [3306, 5432, 1521, 1433, 5000, 27017, 6379, 9042, 9200, 4984, 16000, 8091, 8086, 9042, 26257, 4000, 9000, 3306, 5433, 8812, 7687, 8529, 14240, 8080, 19530, 6333, 8000]
    elif modo == '-web':
        return [80, 443, 8080, 8443, 8000, 3000, 5000]
    elif modo == '-email':
        return [25, 110, 143, 465, 587, 993, 995]
    elif modo == '-ftp':
        return [20, 21, 989, 990]
    elif modo == '-vpn':
        return [1194, 1701, 1723, 500, 4500]
    elif modo == '-iot':
        return [23, 81, 554, 8001, 88, 161, 37777]
    elif modo == '-leak':
        return [9200, 27017, 6379, 5984, 15672, 5000]
    elif modo == '-geo':
        return None
    else:
        return []

def geo(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        respuesta = requests.get(url, timeout=30).json()
        if respuesta["status"] == "succes":
            return {
                "IP": respuesta["query"],
                "País": respuesta["country"],
                "Región": respuesta["regionName"],
                "Ciudad": respuesta["city"],
                "Latitud": respuesta["lat"],
                "Longitud": respuesta["lon"],
                "ISP": respuesta["isp"],
                "Organización": respuesta["org"]
                }
        else:
            return {"error": "No pude hacer geo! hacia la ip"}
    except Exception as e:
        return {"error": str(e)}
        
def nombre_servicio(puerto):
    try:
        return getservbyport(puerto)
    except:
        return "desconocido"

def conScan(tgHost, tgPort):
    try:
        const = socket(AF_INET, SOCK_STREAM)
        const.connect((tgHost, tgPort))
        print(f"\033[32m[+] {tgPort} abierto ({nombre_servicio(tgPort)})\033[0m")
        const.close()
    except:
        print(f"\033[31m[-] {tgPort} cerrado\033[0m")

def portScan(tgHost, tgPorts):
    try:
        tgip = gethostbyname(tgHost)
    except Exception as e:
        print(f"\033[31m[-] no pude resolver el host: {tgHost} ({e})\033[0m")
        return
    try:
        tgname = gethostbyaddr(tgip)
        print(f'\n\033[36m[+]resultado de escaneo de: {tgname[0]} ({tgip})\033[0m')
    except:
        print(f'\n\033[36m[+]resultado de scan de: {tgip}\033[0m')
    setdefaulttimeout(1)
    for port in tgPorts:
        print(f"\033[34mEscanenando puerto: {port}\033[0m")
        conScan(tgHost, int(port))

def run(args):
    if not args:
        print("""typea: scanp <ip|dominio> -modo
Modos: -full|-db|-web|-geo|-email|-ftp|-vpn|-iot|-leak|-geo
ejemplo: scanp hentaila.com -geo |  scanp 198.194.11.187 -vpn
        """)
        return
    objetivo = args[0]
    modo = args[1] if len(args) > 1 else None
    if modo == "-geo":
        resultado = geo(objetivo)
        print("\n\033[36m[+]info geo:\033[0m")
        for clave, valor in resultado,items():
            print(f"{clave}: {valor}")
    else:
        puertos = modos(modo)
        if not puertos:
            print("modo invalido! o no digitaste puertos!")
            return
        portScan(objetivo, puertos)
        
