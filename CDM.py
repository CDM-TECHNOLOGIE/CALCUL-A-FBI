# ==============================
#   A-FBI 404 CDM CALCULATOR v3.0
#   MODE SÉCURISÉ 🔒
# ==============================

import os

# ===== CONFIG =====
MOT_DE_PASSE = "a-fbi123"   # <-- Change ici

# Couleurs ANSI
VERT = "\033[92m"
ROUGE = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ===== AUTH =====
def login():
    tentatives = 3

    while tentatives > 0:
        mdp = input(VERT + "Mot de passe ANTI-FBI : " + RESET)

        if mdp == MOT_DE_PASSE:
            print(VERT + "\n[ ACCÈS AUTORISÉ ]\n" + RESET)
            return True
        else:
            tentatives -= 1
            print(ROUGE + f"Incorrect ! Tentatives restantes : {tentatives}" + RESET)

    print(ROUGE + "\n[ ACCÈS REFUSÉ - SYSTÈME BLOQUÉ ]" + RESET)
    return False

# ===== MENU =====
def menu():
    print(VERT + "\n[ ANTI-FBI SYSTEM ]" + RESET)
    print(CYAN + "[1] Addition")
    print("[2] Soustraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[0] Quitter" + RESET)

# ===== CALCULATRICE =====
def calculatrice():
    while True:
        menu()
        choix = input(VERT + "\nChoix : " + RESET)

        if choix == "0":
            print(ROUGE + "\n[ A-FBI-TECH OFFLINE ]" + RESET)
            break

        if choix not in ["1", "2", "3", "4"]:
            print(ROUGE + "Choix invalide !" + RESET)
            continue

        try:
            a = float(input(CYAN + "Nombre 1 : " + RESET))
            b = float(input(CYAN + "Nombre 2 : " + RESET))

            if choix == "1":
                print(VERT + f"Résultat : {a + b}" + RESET)

            elif choix == "2":
                print(VERT + f"Résultat : {a - b}" + RESET)

            elif choix == "3":
                print(VERT + f"Résultat : {a * b}" + RESET)

            elif choix == "4":
                if b == 0:
                    print(ROUGE + "Erreur : division par 0 !" + RESET)
                else:
                    print(VERT + f"Résultat : {a / b}" + RESET)

        except:
            print(ROUGE + "Erreur de saisie !" + RESET)

        input(CYAN + "\nEntrée pour continuer..." + RESET)
        clear()

# ===== LANCEMENT =====
clear()

if login():
    calculatrice()
