#main.py
import membership_transactions
import book_transactions

def main_menu():
    while True:
        print("\nWELCOME TO OUR PUBLIC LIBRARY")
        print("1- MEMBERSHIP TRANSACTIONS")
        print("2- BOOK TRANSACTIONS")
        print("3- EXIT")
        choice = input("Please enter the code of the selection : ")

        if choice == "1":
            membership_transactions.member_menu()
        elif choice == "2":
            book_transactions.book_transactions_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()