from utilities import print_header, input_prompt, print_success, print_error, Fore, library_data, student_data


def return_book():
    print_header("RETURN A BOOK")

    roll_no = input_prompt("Enter Student Roll No: ")

    if roll_no not in student_data or len(student_data[roll_no]) == 0:
        print_error(f"No books are currently issued to Roll No: {roll_no}")
        return

    print(Fore.CYAN + f"\n  >>> Books currently issued to {roll_no}: {', '.join(student_data[roll_no])}\n")
    book_id = input_prompt("Enter Book ID to return: ")

    if book_id in student_data[roll_no]:
        student_data[roll_no].remove(book_id)

        if not student_data[roll_no]:
            del student_data[roll_no]

        if book_id in library_data:
            # Add 1 back to the quantity
            library_data[book_id]["quantity"] += 1
            title = library_data[book_id]['title']
            print_success(f"Book '{title}' returned successfully!")
        else:
            print_error("Book returned, but it was deleted from the main catalog.")
    else:
        print_error(f"Book ID {book_id} was not issued to this student.")