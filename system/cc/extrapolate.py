import random

def lh_digit(number: str) -> str:
    digits = [int(d) for d in number if d.isdigit()]
    checksum = 0
    is_even = True
    for d in reversed(digits):
        if is_even:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d
        is_even = not is_even
    return str((10 - (checksum % 10)) % 10)

def mt1(cc: str) -> str:
    return cc[:6] + 'x'*(len(cc)-10) + cc[-4:]

def mt2(cc: str) -> str:
    blocks = [cc[i:i+4] for i in range(0, len(cc), 4)]
    if len(blocks) >= 3:
        blocks[1] = 'x'*4
    return ''.join(blocks)

def mt3(cc: str) -> str:
    pattern = ''
    for i, d in enumerate(cc):
        if 6 <= i < len(cc)-4 and i%2==1:
            pattern += 'x'
        else:
            pattern += d
    return pattern

def mt4(cc: str) -> str:
    return cc[:6] + 'x'*(len(cc)-8) + cc[-2:]

def mt5(cc: str) -> str:
    pattern = ''
    for i, d in enumerate(cc):
        if i < 6 or i >= len(cc)-2:
            pattern += d
        elif (i - 6) % 2 == 0:
            pattern += 'x'
        else:
            pattern += d
    return pattern

def extrapolationstyx(cc: str):
    print(f"extrapolando... {cc}\n")
    methods = [mt1, mt2, mt3, mt4, mt5]
    results = []
    for i, m in enumerate(methods, 1):
        combo = m(cc)
        if combo[-1] == 'x':
            combo = combo[:-1] + lh_digit(combo[:-1] + '0')
        results.append(combo)
        print(f"[Mt] {i}: {combo}")
    return results
    


if __name__ == "__main__":
    cc_input = input("ingrese la cc: ").strip()
    extrapolationstyx(cc_input)
