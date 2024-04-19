#book_transactions.py
import json
from datetime import datetime, timedelta

def read_members():
    try:
        with open("members.json", "r") as file:
            members = json.load(file)
            return members
    except FileNotFoundError:
        return []

def read_books():
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def list_books():
    books = read_books()
    total_books = len(books)
    print("List of Books:")
    for index, book in enumerate(books, start=1):
        print(
            f"{index}. Barcode: {book['Barcode']}, Book Name: {book['Book_Name']}, Publishing House: {book['Publishing_House']}, Author: {book['Author']}")
    print(f"Total number of books: {total_books}")

def update_book():
    barcode = input("Enter the barcode of the book you want to update: ")
    books = read_books()
    for book in books:
        if book["Barcode"] == barcode:
            print("Book updated successfully.")
            save_books(books)
            return
    print("Book not found.")

def search_books():
    search_term = input("Enter the search term (Barcode, Book Name, Publishing House, Author): ").lower()
    books = read_books()
    found_books = []
    for book in books:
        if (search_term in book["Barcode"].lower() or
                search_term in book["Book_Name"].lower() or
                search_term in book["Publishing_House"].lower() or
                search_term in book["Author"].lower()):
            found_books.append(book)
    if found_books:
        print("Found Books:")
        for index, book in enumerate(found_books, start=1):
            print(
                f"{index}. Barcode: {book['Barcode']}, Book Name: {book['Book_Name']}, Publishing House: {book['Publishing_House']}, Author: {book['Author']}")
    else:
        print("No books found.")

def track_books(book_name):
    books = read_books()
    for book in books:
        if book["Book_Name"].lower() == book_name.lower():
            if book["status"] == "available":
                print(f"The book '{book_name}' is available for borrowing.")
            else:
                borrowed_info = book.get("borrowed_info")
                if borrowed_info:
                    print(f"The book '{book_name}' is currently borrowed.")
                    print("Date taken:", borrowed_info["date_taken"])
                    print("Return date:", borrowed_info["return_date"])
                else:
                    print(f"The book '{book_name}' is currently borrowed.")
            return
    print(f"The book '{book_name}' is not found in the library.")


def return_book(barcode):
    track_data = read_track()
    books_data = read_books()
    book_found = False
    for entry in track_data:
        if entry["Barcode"] == barcode:
            book_found = True
            if "Actual_Return_Date" not in entry:
                entry["Actual_Return_Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_track(track_data)
                for book_entry in books_data:
                    if book_entry["Barcode"] == barcode:
                        book_entry["status"] = "available"
                        save_books(books_data)
                print("Book returned successfully.")
                return
            else:
                print("Book already returned.")
                return
    if not book_found:
        print("Book not found.")
    else:
        print("Book not borrowed or already returned.")

def track_return(member_id):
    track_data = read_track()
    for entry in track_data:
        if entry["member_id"] == member_id and "Return_Date" not in entry:
            entry["Return_Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_track(track_data)

def read_track():
    try:
        with open("takip.json", "r") as file:
            track_data = json.load(file)
            return track_data
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []

def save_track(track_data):
    with open("takip.json", "w") as file:
        json.dump(track_data, file, indent=4)

def borrow_book(member_id, barcode):
    books = read_books()
    members = read_members()
    
    # Üye adını bul
    member_name = None
    for member in members:
        if str(member["id"]) == member_id:
            member_name = member["name"]
            break
    
    if not member_name:
        print("Member not found.")
        return False
    
    for book in books:
        if book["Barcode"] == barcode and book["status"] == "available":
            book["status"] = "borrowed"
            save_books(books)

            # Takip verilerine üye adını ekle
            track_data = read_track()
            track_data.append({
                "member_id": member_id,
                "member_name": member_name,  # Üye adı eklendi
                "phone": member.get("phone", None),
                "address": member.get("address", None),
                "Barcode": barcode,
                "Book_Name": book.get("Book_Name", None),
                "Publishing_House": book.get("Publishing_House", None),
                "Author": book.get("Author", None),
                "Language": book.get("Language", None),
                "Price": book.get("Price", None),
                "Borrow_Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Return_Date": (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
            })
            save_track(track_data)
            print("Book borrowed successfully.")
            return True
    print("Book not available or already borrowed.")
    return False

def add_book(barcode, book_name, publishing_house, author, language, price):
    books = read_books()
    books.append({
        "Barcode": barcode,
        "Book_Name": book_name,
        "Publishing_House": publishing_house,
        "Author": author,
        "Language": language,
        "Price": price,
        "status": "available"
    })
    save_books(books)
    print("Book added successfully.")

def delete_book(book_name):
    books = read_books()
    for book in books:
        if book["Book_Name"].lower() == book_name.lower():
            books.remove(book)
            save_books(books)
            print("Book deleted successfully.")
            return
    print("Book not found.")
    
def add_borrowed_book(member_id, book_name):
    with open("takip.json", "r") as file:
        track_data = json.load(file)
    new_record = {
        "Member_ID": member_id,
        "Book_Name": book_name,
        "Borrow_Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    track_data.append(new_record)
    with open("takip.json", "w") as file:
        json.dump(track_data, file, indent=4)

def update_return_date(book_name):
    with open("takip.json", "r") as file:
        track_data = json.load(file)
    for record in track_data:
        if record["Book_Name"].lower() == book_name.lower() and "Return_Date" not in record:
            record["Return_Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("takip.json", "w") as file:
        json.dump(track_data, file, indent=4)

def search_book(search_term):
    books = read_books()
    found_books = []
    for book in books:
        if search_term.lower() in book["Book_Name"].lower():
            found_books.append(book)
    if found_books:
        print("Found Books:")
        for book in found_books:
            print(book)
    else:
        print("No books found.")

def book_transactions_menu():
    while True:
        print("\nBOOK TRANSACTIONS")
        print("1- ADD BOOK")
        print("2- DELETE BOOK")
        print("3- SEARCH BOOK")
        print("4- BORROW A BOOK")
        print("5- RETURN A BOOK")
        print("6- LIST BORROWED BOOKS")
        print("7- LIST BOOKS")
        # print("8- UPDATE BOOK")
        print("0- RETURN TO MAIN MENU")
        choice = input("Select action: ")

        if choice == "1":
            barcode = input("Enter Barcode: ")
            book_name = input("Enter Book Name: ")
            publishing_house = input("Enter Publishing House: ")
            author = input("Enter Author: ")
            language = input("Enter Language: ")
            price = input("Enter Price: ")
            add_book(barcode, book_name, publishing_house, author, language, price)
        elif choice == "2":
            book_name = input("Enter book name to delete: ")
            delete_book(book_name)
        elif choice == "3":
            search_term = input("Enter search term: ")
            search_book(search_term)
        elif choice == "4":
            member_id = input("Enter ID of member: ")
            barcode = input("Enter barcode of the book to borrow: ")
            borrow_book(member_id, barcode)

        elif choice == "5":
            barcode = input("Enter barcode of the book to return: ")
            return_book(barcode)
        elif choice == "6":
            track_data = read_track()
            borrowed_books = [entry for entry in track_data if "Actual_Return_Date" not in entry]
            if borrowed_books:
                print("List of Borrowed Books:")
                for index, book in enumerate(borrowed_books, start=1):
                    print(
                        f"{index}. Book Name: {book['Book_Name']}, Member ID: {book['member_id']}, Borrow Date: {book['Borrow_Date']}, Return Date: {book.get('Return_Date', 'Not Returned Yet')}, Actual Return Date: {book.get('Actual_Return_Date', 'Not Returned Yet')}"
                    )
            else:
                print("No borrowed books found.")
        elif choice == "7":
            list_books()
        # elif choice == "8":
        #     update_book()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    book_transactions_menu()
