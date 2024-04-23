import book_transactions
import member_transactions

def main():
    """
    Main function to run the library management system.
    """
    while True:
        print(
            "------------------------------------------------------------------------" +
            "\n-                 WELCOME TO THE LIBRARY!                              -" +
            "\n-                                                                      -" +
            "\n-      MEMBER OPERATIONS    1                                          -" +
            "\n-      BOOK OPERATIONS      2                                          -" +
            "\n-      EXIT                 0                                          -" +
            "\n-                                                                      -" +
            "\n------------------------------------------------------------------------"
        )
        choice = input("Enter your choice: ")

        if choice == '1':
            member_transactions.member_menu()
        elif choice == '2':
            book_transactions.book_menu()
        elif choice == '0':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
