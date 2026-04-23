import sys
from colorama import Fore, Style
from utilities import clear_screen, print_header, input_prompt, WIDTH
from add_books import add_book
from show_books import show_books
from issue_books import issue_book
from return_books import return_book


def main():
    while True:
        clear_screen()

        padding = (WIDTH - 40) // 2

        print("\n")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "+--------------------------------------+")
        print(
            Fore.BLUE + Style.BRIGHT + " " * padding + "| " + Fore.CYAN + "      LIBRARY MANAGEMENT SYSTEM     " + Fore.BLUE + " |")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "+======================================+")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "|                                      |")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "|   " + Fore.WHITE + " [ 1 ] Add a New Book             " + Fore.BLUE + " |")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "|   " + Fore.WHITE + " [ 2 ] Show All Books             " + Fore.BLUE + " |")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "|   " + Fore.WHITE + " [ 3 ] Issue a Book               " + Fore.BLUE + " |")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "|   " + Fore.WHITE + " [ 4 ] Return a Book              " + Fore.BLUE + " |")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "|   " + Fore.WHITE + " [ 5 ] Exit                       " + Fore.BLUE + " |")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "|                                      |")
        print(Fore.BLUE + Style.BRIGHT + " " * padding + "+--------------------------------------+\n")

        choice = input_prompt("Enter your choice (1-5): ")

        clear_screen()

        # Function calls are now much simpler!
        if choice == '1':
            add_book()
        elif choice == '2':
            show_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print_header("SYSTEM SHUTDOWN")
            sys.exit()
        else:
            print(Fore.RED + Style.BRIGHT + "\n  [-] ERROR: Invalid choice! Please try again.")

        input(Fore.MAGENTA + f"\n  ... Press [ENTER] to return to the main menu ...")


if __name__ == "__main__":
    main()