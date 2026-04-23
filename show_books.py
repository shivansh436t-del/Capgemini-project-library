from utilities import print_header, Fore, BOLD, WIDTH, library_data


def show_books():
    print_header("LIBRARY CATALOG")

    if not library_data:
        padding = (WIDTH - 45) // 2
        print(Fore.RED + BOLD + " " * padding + "!!! The library is currently empty !!!")
        return

    print(Fore.BLUE + BOLD + "  " + "_" * 66)
    # Changed 'Status' to 'Qty'
    print(
        Fore.BLUE + BOLD + " | " + Fore.WHITE + f"{'ID':<6} | {'Title':<25} | {'Author':<15} | {'Qty':<10}" + Fore.BLUE + " |")
    print(Fore.BLUE + BOLD + " |" + "=" * 66 + "|")

    for b_id, details in library_data.items():
        qty = details["quantity"]

        # Color coding: Green if in stock, Red if 0
        if qty > 0:
            qty_display = Fore.GREEN + f"{str(qty):<10}" + Fore.BLUE
        else:
            qty_display = Fore.RED + f"{str(qty):<10}" + Fore.BLUE

        title = details['title'][:22] + "..." if len(details['title']) > 25 else details['title']
        author = details['author'][:12] + "..." if len(details['author']) > 15 else details['author']

        print(Fore.BLUE + BOLD + " | " + Fore.WHITE + f"{b_id:<6} | {title:<25} | {author:<15} | {qty_display} |")

    print(Fore.BLUE + BOLD + " |" + "_" * 66 + "|")
    print("\n")