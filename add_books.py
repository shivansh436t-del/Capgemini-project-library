from utilities import print_header, input_prompt, print_success, print_error, library_data


def add_book():
    print_header("ADD A NEW BOOK")

    book_id = input_prompt("Enter Book ID: ")
    if book_id in library_data:
        existing_book = library_data[book_id]

        while True:
            try:
                qty = int(input_prompt("Book already exists. Enter quantity to add: "))
                if qty <= 0:
                    print_error("Quantity to add must be greater than zero!")
                    continue
                break
            except ValueError:
                print_error("Please enter a valid number!")

        existing_book["quantity"] += qty
        print_success(
            f"Added {qty} more copies of '{existing_book['title']}'. "
            f"Total copies: {existing_book['quantity']}"
        )
        return

    title = input_prompt("Enter Book Title: ")
    author = input_prompt("Enter Author Name: ")

    # Loop to ensure the user enters a valid number for quantity
    while True:
        try:
            qty = int(input_prompt("Enter Quantity: "))
            if qty < 0:
                print_error("Quantity cannot be negative!")
                continue
            break
        except ValueError:
            print_error("Please enter a valid number!")

    # Save the quantity instead of boolean
    library_data[book_id] = {
        "title": title,
        "author": author,
        "quantity": qty
    }

    print_success(f"Book '{title}' by {author} added to the catalog with {qty} copies!")
