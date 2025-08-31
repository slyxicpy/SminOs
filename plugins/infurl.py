import socket
import ssl
import subprocess
import requests
import json
import sys, os, re
import argparse
from urllib.parse import urlparse
from datetime import datetime

#---helper pa url >;v----

def norm_url(u):
    if not u:
        return None
    if not u.startswith("http://") and not u.startswith("https://"):
        u = "http://" + u
    return u

def resolve_host(host):
    result = {"A": [], "AAAA": []}
    try:
        infos = socket.getaddrinfo(host, None)
        for info in infos:
            addr = info[4][0]
            if ":" in addr:
                if addr not in result["AAAA"]:
                    result["AAAA"].append(addr)
            else:
                if addr not in result["A"]:
                    result["A"].append(addr)
    except Exception as e:
        result["error"] = str(e)
    return result

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return None

def http_fetch(url, timeout=10, headers=None):
    try:
        r = requests.get(url, timeout=timeout, headers=headers, allow_redirects=True, verify=False)
        return r
    except Exception as e:
        return e

def tls_info(host, port=443, timeout=10):
    info = {}
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                proto = ssock.version()
                info["cipher"] = cipher
                info["protocol"] = proto
                info["cert"] = cert
                notBefore = cert.get("notBefore")
                notAfter = cert.get("notAfter")
                info["notBefore"] = notBefore
                info["notAfter"] = notAfter
    except Exception as e:
        info["error"] = str(e)
    return info

def whois_lookup(host):
    try:
        p = subprocess.run(["whois", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=8)
        if p.returncode == 0:
            return p.stdout
        else:
            return p.stdout + p.stderr
    except Exception as e:
        return str(e)

def run_cmd(cmd):
    try:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
        return p.stdout.strip()
    except Exception as e:
        return ""

def query_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            try:
                data = r.json()
                subs = set()
                for item in data:
                    name = item.get("name_value", "")
                    for n in name.split("\n"):
                        n = n.strip().lower()
                        if n and "*" not in n:
                            subs.add(n)
                return sorted(subs)
            except Exception:
                txt = r.text
                domains = set(re.findall(r'"name_value":"([^"]+)"', txt))
                cleaned = set()
                for name in domains:
                    for n in name.split("\n"):
                        n = n.strip().lower()
                        if n and "*" not in n:
                            cleaned.add(n)
                return sorted(cleaned)
    except Exception:
        pass
    return []

def geo_ip(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return {}

def detect_technologies(headers, body_text):
    tech = set()
    if not headers:
        return tech
    server = headers.get("Server", "").lower()
    powered = headers.get("X-Powered-By", "").lower()
    if "nginx" in server: tech.add("Nginx")
    if "apache" in server: tech.add("Apache")
    if "cloudflare" in server: tech.add("Cloudflare")
    if "gws" in server: tech.add("GWS")
    if "php" in powered or "php" in body_text.lower(): tech.add("PHP")
    if "wp-" in body_text.lower() or "wordpress" in body_text.lower(): tech.add("WordPress")
    if "joomla" in body_text.lower(): tech.add("Joomla")
    if "drupal" in body_text.lower(): tech.add("Drupal")
    if "express" in powered or "express" in body_text.lower(): tech.add("Node.js (Express)")
    if "asp.net" in powered or "asp.net" in body_text.lower(): tech.add("ASP.NET")
    if "jsecurity" in body_text.lower(): tech.add("Java")
    return sorted(tech)
   
COMMON_PATHS = [
    "/robots.txt","/sitemap.xml","/wp-login.php","/wp-admin/","/admin/","/login/","/.env",
    "/.git/","/phpmyadmin/","/server-status","/manager/html","/xmlrpc.php","/api","/config.json"
]
COMMON_SUBS = ["www","admin","mail","dev","test","staging","api","cdn","m","portal","blog","shop","smtp"]

def run(args):
    parser = argparse.ArgumentParser(prog="scanurl", add_help=False)
    parser.add_argument("target", nargs='?', default=None)
    parser.add_argument("--subs", action="store_true", help="Buscar subdominios en crt.sh")
    parser.add_argument("--enum", action="store_true", help="Enumerar subdominios con lista pequeña")
    parser.add_argument("--paths", action="store_true", help="Comprobar paths comunes")
    parser.add_argument("--tls", action="store_true", help="Obtener info TLS/Cert")
    parser.add_argument("--whois", action="store_true", help="Hacer whois (si disponible)")
    parser.add_argument("--geo", action="store_true", help="Geolocalizar IP")
    parser.add_argument("--timeout", type=int, default=8)
    try:
        ns = parser.parse_args(args)
    except SystemExit:
        print("""typea: infurl <url> --modo
Modos: [--subs] [--enum] [--paths] [--tls] [--whois] [--geo]
        """)
        return
    target = ns.target
    if not target:
        print("typea: infurl <url> [--subs] [--enum] [--paths] [--tls] [--whois] [--geo]")
        return
    url = norm_url(target)
    parsed = urlparse(url)
    host = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    print(f"\n\033[36m[!+!] Escaneando: {url}\033[0m")
    print(f"[*]Host {host}  Puerto: {port}")
    print("\n\033[33m[!+!]DNS | IPs:\033[0m")
    dns_info = resolve_host(host)
    for t, addrs in dns_info.items():
        if addrs:
            print(f"  {t}:")
            for a in addrs:
                rd = reverse_dns(a) or "-"
                print(f"    - {a} (reverse: {rd})")
    if dns_info.get("error"):
        print("error DNS:", dns_info["error"])
    print("\n\033[33m[!+!]HTTP fch:\033[0m")
    headers = {}
    body_text = ""
    r = http_fetch(url, timeout=ns.timeout, headers={"User-Agent":"Mozilla/5.0 (compatible; scanurl/1.0)"})
    if isinstance(r, Exception):
        print("error en url! shit:")
    else:
        print(f"stado: {r.status_code}")
        if r.history:
            print("redirects:")
            for h in r.history:
                print(f"{h.status_code} -> {h.url}")
        headers = r.headers
        body_text = r.text[:400000] #byxStyx Bitch Shit
        print("Content-Type:", headers.get("Content-Type"))
        print("Server:", headers.get("Server"))
        print("X-Powered-By:", headers.get("X-Powered-By"))
    if ns.tls:
        print("\n\033[33m[!+!] TLS?/CertInfo:\033[0m")
        tinfo = tls_info(host, port=443, timeout=ns.timeout)
        if "error" in tinfo:
            print("error tls:", tinfo["error"])
        else:
            cert = tinfo.get("cert", {})
            print("Protocol:", tinfo.get("protocol"))
            print("Cipher:", tinfo.get("cipher"))
            subj = cert.get("subject", ())
            issuer = cert.get("issuer", ())
            subj_cn = ""
            for tup in subj:
                for k,v in tup:
                    if k == "commonName":
                        subj_cn = v
            issuer_cn = ""
            for tup in issuer:
                for k,v in tup:
                    if k == "commonName":
                        issuer_cn = v
            print("Subject CN:", subj_cn)
            print("Issuer:", issuer_cn)
            print("Valid from:", tinfo.get("notBefore"))
            print("Valid until:", tinfo.get("notAfter"))

    if ns.geo:
        print("\n\033[33m[!+!]Geo:\033[0m")
        ip = (dns_info.get("A") or [None])[0]
        if ip:
            geo = geo_ip(ip)
            for k,v in geo.items():
                print(f"  {k}: {v}")
        else:
            print("no ip para geo!")
    print("\n\033[33m[!+!] Tecnologias:\033[0m")
    tech = detect_technologies(headers, body_text)
    if tech:
        print("  " + ", ".join(tech))
    else:
        print("no detectadas!")
    if ns.paths:
        print("\n\033[33m[!+!] Paths:\033[0m")
        for p in COMMON_PATHS:
            full = parsed.scheme + "://" + host + p
            try:
                rr = requests.head(full, timeout=ns.timeout, allow_redirects=True, verify=False)
                status = rr.status_code
            except Exception:
                try:
                    rr = requests.get(full, timeout=ns.timeout, allow_redirects=True, verify=False)
                    status = rr.status_code
                except Exception:
                    status = None
            print(f"  {p} -> {status}")
    subs = []
    if ns.subs:
        print("\n\033[33m[!+!] Subdominios:\033[0m")
        try:
            crt = query_crtsh(host)
            if crt:
                print(f"Encontrados {len(crt)} subdominios (crt.sh):")
                for s in crt[:200]:
                    print("  -", s)
                subs.extend(crt)
            else:
                print("no resultados!")
        except Exception:
            print("error:{e}")
    if ns.enum:
        print("\n\033[33m[!+!]Subdominios-WRL:\033[0m")
        found = []
        for label in COMMON_SUBS:
            candidate = f"{label}.{host}"
            try:
                ai = socket.gethostbyname(candidate)
                found.append((candidate, ai))
                print(f"  + {candidate} -> {ai}")
            except Exception:
                pass
        if not found:
            print("no encontre subdominios con wordlist!")
        else:
            subs.extend([s[0] for s in found])

    if ns.whois:
        print("\n\033[33m[!+!] WHOIS:\033[0m")
        w = whois_lookup(host)
        print(w[:4000] + ("\n... (truncated)" if len(w) > 4000 else ""))
    print("\n\033[36m[+] Rsx:\033[0m")
    print("  Objetivo:", host)
    print("  IPs A:", ", ".join(dns_info.get("A", []) or ["-"]))
    print("  IPs AAAA:", ", ".join(dns_info.get("AAAA", []) or ["-"]))
    print("  Subdominios (sample):", ", ".join(subs[:20]) or "-")
    print("  Techs:", ", ".join(tech) or "-")
    print("  Paths:", len(COMMON_PATHS) if ns.paths else 0)
    print("\n[!x+x!] Scan finished!.\n")
                
