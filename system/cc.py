import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "cc"))

# from binchk import chkbin
from passchk import run as passchk_run
from passgen import run as passgen_run
from fakerus import run as faker_run
from parsegmail import run as parsegmail_run
from extrapolate import extrapolationstyx
from checker import run as run_checker
from genc import run as gen_luhn

def run(args):
    while True:
        print("""
1 > Genera cc
2 > Checker
3 > Extrapolate cc
4 > Parse Gmail
5 > Password Gen
6 > Password Check
7 > FakerUsser
0 > Salir
              """)
        opcion = input('digite su eleccion: ')
        if opcion == "1":
            gen_luhn([])
        elif opcion == "2":
            run_checker([])
        elif opcion == "3":
            cc_input = input("digite la tarjeta: ").strip()
            extrapolationstyx(cc_input)
        elif opcion == "4":
            parsegmail_run()
        elif opcion == "5":
            passgen_run()
        elif opcion == "6":
            passchk_run()
        elif opcion == "7":
            faker_run()
        elif opcion == "0":
            break
        else:
            print("opcion no dispo!")

if __name__ == "__main__":
    run(sys.argv)
