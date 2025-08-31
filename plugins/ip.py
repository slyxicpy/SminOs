import requests
import re
import json
from rich.console import Console
console = Console()

def run(args):
    output = []
    def print_to_output(message):
        output.append(str(message))
        console.print(message)
    #print_to_output(f"[cyan]recibido: {args}[/cyan]")
    ip = None
    if len(args) >= 1:
        for arg in args:
            if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", arg):
                ip = arg
                break
    if not ip:
        print_to_output("[red][X] Proporciona una IP![/red]")
        print_to_output("[cyan]Uso: ip <ip>[/cyan]")
        print_to_output("[cyan]Ejemplo: ip 192.175.11.165[/cyan]")
        return {"status": "error", "message": "Proporciona una IP válida", "output": output}
    print_to_output(f"[magenta]Análisis para IP: {ip}[/magenta]")
    results = {}
    services = [
        ("ip-api", f"http://ip-api.com/json/{ip}?fields=status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,mobile,proxy,hosting,query"),
        ("ipinfo", f"https://ipinfo.io/{ip}/json"),
        ("freegeoip", f"https://freegeoip.app/json/{ip}"),
        ("ipwhois", f"https://ipwhois.app/json/{ip}"),
        ("ip2location", f"https://api.ip2location.io/?ip={ip}"),
        ("ipstack", f"http://api.ipstack.com/{ip}?access_key=free"),
        ("ipdata", f"https://api.ipdata.co/{ip}?api-key=free"),
        ("abstractapi", f"https://ipgeolocation.abstractapi.com/v1/?api_key=free&ip_address={ip}"),
        ("keycdn", f"https://tools.keycdn.com/geo.json?host={ip}"),
        ("extreme-ip", f"https://extreme-ip-lookup.com/json/{ip}"),
        ("geojs", f"https://get.geojs.io/v1/ip/geo/{ip}.json"),
        ("ipfind", f"https://ipfind.co/me?ip={ip}"),
        ("db-ip", f"https://api.db-ip.com/v2/free/{ip}"),
        ("ipregistry", f"https://api.ipregistry.co/{ip}?key=free"),
        ("iplocation", f"https://www.iplocation.net/api/iplocation/v1/ip/{ip}"),
        ("ipapi", f"https://ipapi.co/{ip}/json/"),
        ("ipgeolocationapi", f"https://ipgeolocationapi.com/api/ip/{ip}"),
        ("iplocate", f"https://www.iplocate.io/api/lookup/{ip}"),
        ("ipapi-com", f"https://api.ipapi.com/api/{ip}?access_key=free"),
        ("ip-api-io", f"https://ip-api.io/json/{ip}")
    ]

    for name, url in services:
        try:
            r = requests.get(url, timeout=20)
            r.raise_for_status()
            data = r.json()
            results[name] = data
            print_to_output(f"[blue][{name}] Datos obtenidos:[/blue]")
            for key, value in data.items():
                print_to_output(f"  {key}: {value}")
        except Exception as e:
            results[name] = {"error": str(e)}
            print_to_output(f"[red][{name}] Error: {str(e)}[/red]")

    return {"status": "success", "message": "completado exitosamente", "output": output, "data": results}

if __name__ == "__main__":
    import sys
    result = run(sys.argv)
    for message in result.get("output", []):
        print(message)
    print(result["message"])
