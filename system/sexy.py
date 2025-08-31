import os, random

def run(args):
    sexy = "system/ascii"
    files = [f for f in os.listdir(sexy) if f.endswith(".txt")]
    if not files:
        print("[!!!!] NO HAY ARTSSSS")
        return
    choice = random.choice(files)
    with open(os.path.join(sexy, choice), "r", encoding="utf-8") as f:
        print(f.read())
