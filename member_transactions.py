import json
import os
import book_transactions
import time_s

def load_members():
    """
    Loads member data from member.json file.
    """
    if os.path.exists("member.json"):
        with open("member.json", "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []

def save_members(members):
    """
    Saves member data to member.json file.
    """
    with open("member.json", "w", encoding="utf-8") as file:
        json.dump(members, file, indent=4)

def load_track():
    """
    Loads track data from track.json file.
    """
    if os.path.exists("track.json"):
        with open("track.json", "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []

def save_track(track):
    """
    Saves track data to track.json file.
    """
    with open("track.json", "w", encoding="utf-8") as file:
        json.dump(track, file, indent=4)

def list_members():
    """
    Lists all members.
    """
    members = load_members()
    print("\nMembers:")
    for member in members:
        print("ID:", member['ID'])
        print("Name:", member['Name'])
        print("Telephone Number:", member['Telephone Number'])
        print("Address:", member['Address'])
        print()

def add_member(member_name, telefon_number, adres):
    """
    Adds a new member.
    """
    members = load_members()
    if members:
        last_id = int(members[-1]['ID'])
        new_id = str(last_id + 1).zfill(3)
    else:
        new_id = "001"
    members.append({"ID": new_id, "Name": member_name, "Telephone Number": telefon_number, "Address": adres})
    save_members(members)
    print("Member added successfully!")

def delete_member(member_name):
    """
    Deletes a member.
    """
    members = load_members()
    for member in members:
        if member['Name'] == member_name:
            members.remove(member)
            save_members(members)
            print("Member deleted successfully!")
            return
    print("Member not found.")

def search_member(member_name):
    """
    Searches for a member by name.
    """
    members = load_members()
    for member in members:
        if member['Name'] == member_name:
            print("Member found:")
            print("ID:", member['ID'])
            print("Name:", member['Name'])
            print("Telephone Number:", member['Telephone Number'])
            print("Address:", member['Address'])
            return
    print("Member not found.")

def lend_book(member_name, book_title):
    """
    Lends a book to a member.
    """
    members = load_members()
    books = book_transactions.load_books()
    track = load_track()

    # Find member
    member = None
    for m in members:
        if m['Name'] == member_name:
            member = m
            break

    if not member:
        print("Member not found.")
        return

    # Find book
    book = None
    for b in books:
        if b['Book Title'] == book_title:
            book = b
            break

    if not book:
        print("Book not found.")
        return

    # Update track.json
    track.append({
        "Member ID": member['ID'],
        "Member Name": member['Name'],
        "Book Barcode": book['Barcode'],
        "Book Title": book['Book Title'],
        "Publisher" : book['Publisher'],
        "Author": book['Author'],
        "Lending Time": time_s.get_current_time(),
        "Due Date": time_s.get_due_date()
    })
    save_track(track)

    # Remove the book from books.json
    books.remove(book)
    book_transactions.save_books(books)
 
    print("Book lent successfully!")

def return_book(member_name, book_title):
    """
    Returns a book from a member.
    """
    books = book_transactions.load_books()
    track = load_track()


    for t in track:
        if member_name == t["Member Name"] and book_title == t["Book Title"]:
            # Add the book back to books.json
            barcode = t["Book Barcode"]
            title = t["Book Title"]
            publisher = t["Publisher"]
            author = t["Author"]
            book_transactions.add_book(barcode, title, publisher, author)

            # Save track
            track.remove(t)
            save_track(track)
            print("Book returned successfully!")
            return

    else: 
        print("Member or book not found in the tack!")

def track_book(book_title):
    """
    Tracks a book.
    """
    track = load_track()
    for t in track:
        if t['Book Title'] == book_title:
            print("\nBook found:")
            print("Member ID:", t['Member ID'])
            print("Member Name:", t['Member Name'])
            print("Book Barcode:", t['Book Barcode'])
            print("Book Title:", t['Book Title'])
            print("Lending Time:", t['Lending Time'])
            print("Due Date:", t['Due Date'])
            return
    print("Book not found in the track.")

def member_menu():
    """
    Main menu for member transactions.
    """
    while True:
        print(
            "------------------------------------------------------------------------" +
            "\n-                 MEMBER TRANSACTION                                   -" +
            "\n-                                                                      -" +
            "\n-     MEMBERS         1              LEND BOOK     5                   -" +
            "\n-     ADD MEMBER      2              RETURN BOOK   6                   -" +
            "\n-     DELETE MEMBER   3              TRACK BOOK    7                   -" +
            "\n-     SEARCH MEMBER   4              MAIN MENU     0                   -" +
            "\n------------------------------------------------------------------------"
        )
        choice = input("Enter your choice: ")

        if choice == '1':
            list_members()
        elif choice == '2':
            member_name = input("Enter the name of the member: ")
            telefon_number = input("Enter the telephone number of the member: ")
            adres = input("Enter the address of the member: ")
            add_member(member_name, telefon_number, adres)
        elif choice == '3':
            member_name = input("Enter the name of the member to delete: ")
            delete_member(member_name)
        elif choice == '4':
            member_name = input("Enter the name of the member to search: ")
            search_member(member_name)
        elif choice == '5':
            member_name = input("Enter the name of the member: ")
            book_title = input("Enter the title of the book to lend: ")
            lend_book(member_name, book_title)
        elif choice == '6':
            member_name = input("Enter the name of the member: ")
            book_title = input("Enter the title of the book to return: ")
            return_book(member_name, book_title)
        elif choice == '7':
            book_title = input("Enter the title of the book to track: ")
            track_book(book_title)
        elif choice == '0':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
