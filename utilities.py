import os
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# ANSI Codes to replace colorama.Style
BOLD = '\033[1m'
RESET = '\033[0m'

# Total terminal width for centering
WIDTH = 200

# ==========================================
#       GLOBAL DATA STRUCTURES
# ==========================================
# Changed "available": True to "quantity": <number>
library_data = {
    "101": {"title": "Python Crash Course", "author": "Eric Matthes", "quantity": 5},
    "102": {"title": "Clean Code", "author": "Robert C. Martin", "quantity": 2}
}

student_data = {}


# ==========================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    box_width = 50
    padding = (WIDTH - box_width) // 2

    print(Fore.CYAN + " " * padding + "__________________________________________________")
    print(Fore.CYAN + " " * padding + "==================================================")

    title_padding = (WIDTH - len(title) - 6) // 2
    print(Fore.MAGENTA + BOLD + " " * title_padding + f"--- {title} ---")

    print(Fore.CYAN + " " * padding + "--------------------------------------------------")
    print(Fore.CYAN + " " * padding + "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n")


def input_prompt(msg):
    return input(Fore.YELLOW + BOLD + f"  ===> {msg}" + RESET)


def print_success(msg):
    print(Fore.GREEN + BOLD + f"\n  [+] SUCCESS: {msg}")


def print_error(msg):
    print(Fore.RED + BOLD + f"\n  [-] ERROR: {msg}")