import re
import pyfiglet
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear_screen()
    # Big bold hacker-style banner
    ascii_banner = pyfiglet.figlet_format("PassGuard", font="slant")
    print(Fore.CYAN + ascii_banner)
    print(Fore.YELLOW + "🔒 Password Strength Analyzer")
    print(Fore.RED + "[+] Coded by: Vansh Dhawan")
    print(Fore.MAGENTA + "--------------------------------------\n")

def check_password_strength(password):
    reasons = []
    strength = Fore.RED + "Weak ❌"

    if len(password) < 8:
        reasons.append("Password too short (<8)")
    else:
        reasons.append("Length OK")

    if not re.search(r"[A-Z]", password):
        reasons.append("Missing uppercase letter")
    if not re.search(r"[a-z]", password):
        reasons.append("Missing lowercase letter")
    if not re.search(r"[0-9]", password):
        reasons.append("Missing number")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        reasons.append("Missing special character")

    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        strength = Fore.GREEN + "Strong ✅"
    elif len(password) >= 6:
        strength = Fore.YELLOW + "Medium ⚠️"

    return strength, reasons

def main():
    banner()
    while True:
        pwd = input(Fore.CYAN + "Enter password (or 'q' to quit): " + Style.RESET_ALL)
        if pwd.lower() == "q":
            print(Fore.YELLOW + "\nExiting PassGuard...\n")
            break
        result, details = check_password_strength(pwd)
        print("\nStrength:", result)
        print(Fore.BLUE + "Reasons: " + ", ".join(details))
        print(Fore.MAGENTA + "-" * 40 + "\n")

if __name__ == "__main__":
    main()
