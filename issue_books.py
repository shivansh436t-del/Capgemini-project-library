from utilities import print_header, input_prompt, print_success, print_error, library_data, student_data


def issue_book():
    print_header("ISSUE A BOOK")

    roll_no = input_prompt("Enter Student Roll No: ")
    book_id = input_prompt("Enter Book ID to issue: ")

    if book_id not in library_data:
        print_error("Book ID not found in library.")
        return

    # Check if quantity is greater than 0
    if library_data[book_id]["quantity"] <= 0:
        print_error("Sorry, all copies of this book are currently issued out.")
        return

    # Subtract 1 from the quantity
    library_data[book_id]["quantity"] -= 1

    if roll_no not in student_data:
        student_data[roll_no] = []
    student_data[roll_no].append(book_id)

    title = library_data[book_id]['title']
    print_success(f"Book '{title}' successfully issued to Roll No: {roll_no}")