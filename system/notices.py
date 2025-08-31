import requests
import random
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def run(args):
    urls = [
        "https://thehackernews.com/",
        "https://www.darkreading.com/",
        "https://www.securityweek.com/",
        "https://cybersecuritynews.es/",
        "https://es.wired.com/tag/ciberseguridad"
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }
    pintura = ["\033[94m", "\033[96m", "\033[34m", "\033[36m"]
    reset = "\033[0m"

    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=40)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find_all(['h2', 'h3'], limit=10)
            print(f"\n{url}")
            for headline in headlines:
                tittle = headline.get_text(strip=True)
                parent_link = headline.find_parent('a')
                if parent_link and "href" in parent_link.attrs:
                    link = parent_link['href']
                    link = urljoin(url, link)
                else:
                    link = "No links disponible de captar en js ;c"
                color = random.choice(pintura)
                for char in tittle:
                    print(color + char, end="", flush=True)
                    time.sleep(0.01)
                print(reset)
                print(f"{link}\n")
        except requests.RequestException as e:
            print(f"error al acceder a {url}: {e}")
