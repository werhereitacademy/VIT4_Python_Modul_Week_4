import json
import os

def load_books():
    """
    Loads book data from books.json file.
    """
    if os.path.exists("books.json"):
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []

def save_books(books):
    """
    Saves book data to books.json file.
    """
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)

def add_book(barcode, title, publisher, author):
    """
    Adds a new book.
    """
    books = load_books()
    books.append({"Barcode": barcode, "Book Title": title, "Publisher": publisher, "Author": author})
    save_books(books)
    print("Book added successfully!")

def delete_book():
    """
    Deletes a book.
    """
    books = load_books()
    title = input("Enter the title of the book to delete: ")
    for book in books:
        if book['Book Title'] == title:
            books.remove(book)
            save_books(books)
            print("Book deleted successfully!")
            return
    print("Book not found.")

def search_book():
    """
    Searches for a book by title.
    """
    books = load_books()
    title = input("Enter the title of the book to search: ")
    for book in books:
        if book['Book Title'] == title:
            print("The book is available!")
            print("Barcode:", book['Barcode'])
            print("Title:", book['Book Title'])
            print("Publisher:", book['Publisher'])
            print("Author:", book['Author'])
            return
    print("Book not found.")

def book_menu():
    """
    Main menu for book transactions.
    """
    while True:
        print("\nBook Transactions:")
        print(
            "------------------------------------------------------------------------" +
            "\n-                 WELCOME TO THE LIBRARY!                              -" +
            "\n-                                                                      -" +
            "\n-      ADD BOOK         1                                              -" +
            "\n-      DELETE BOOK      2                                              -" +
            "\n-      SEARCH BOOK      3                                              -" +
            "\n-      MAIN MENU        0                                              -" +
            "\n-                                                                      -" +
            "\n------------------------------------------------------------------------"
        )
        choice = input("Enter your choice: ")

        if choice == '1':
            barcode = input("Enter the barcode of the book: ")
            title = input("Enter the title of the book: ")
            publisher = input("Enter the publisher of the book: ")
            author = input("Enter the author of the book: ")           
            add_book(barcode, title, publisher, author)
        elif choice == '2':
            delete_book()
        elif choice == '3':
            search_book()
        elif choice == '0':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
