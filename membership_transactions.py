# membership_transactions.py
import json
import book_transactions
from datetime import datetime
from time_operations import track_book_status

def read_members():
    try:
        with open("members.json", "r") as file:
            members = json.load(file)
            return members
    except FileNotFoundError:
        return []

def save_members(members):
    with open("members.json", "w") as file:
        json.dump(members, file, indent=4)

def generate_id():
    members = read_members()
    if members:
        return max(member["id"] for member in members) + 1
    else:
        return 1

def add_member(name, phone, address):
    members = read_members()
    new_member = {
        "id": generate_id(),
        "name": name,
        "phone": phone,
        "address": address
    }
    members.append(new_member)
    save_members(members)
    print("Member added successfully.")

def delete_member(member_id):
    members = read_members()
    for member in members:
        if member["id"] == member_id:
            members.remove(member)
            save_members(members)
            print("Member deleted successfully.")
            return
    print("Member not found.")

def search_member(search_term):
    members = read_members()
    found_members = []
    for member in members:
        if str(member["id"]) == search_term or member["name"].lower() == search_term.lower():
            found_members.append(member)
    if found_members:
        print("Found Members:")
        for member in found_members:
            print(member)
    else:
        print("No members found.")

# def borrow_book(member_id, book_name):
#     print("Helaas")

# def return_book(book_name):
#     print("Pindakaas")

def list_members():
    members = read_members()
    print("List of Members:")
    for member in members:
        print(f"ID: {member['id']}, Name: {member['name']}, Phone: {member['phone']}, Address: {member['address']}")

def update_member(member_id):
    members = read_members()
    for member in members:
        if member["id"] == member_id:
            print("Current Member Information:")
            print(f"Name: {member['name']}")
            print(f"Phone: {member['phone']}")
            print(f"Address: {member['address']}")
            print("\nEnter new information (leave blank to keep current):")
            new_name = input("New name: ").strip() or member["name"]
            new_phone = input("New phone: ").strip() or member["phone"]
            new_address = input("New address: ").strip() or member["address"]
            member["name"] = new_name
            member["phone"] = new_phone
            member["address"] = new_address
            save_members(members)
            print("Member information updated successfully.")
            return
    print("Member not found.")

def member_menu():
    while True:
        print("\nMEMBERSHIP TRANSACTIONS")
        print("1- LIST ALL MEMBERS")
        print("2- ADD MEMBER")
        print("3- DELETE MEMBER")
        print("4- SEARCH MEMBER")
        print("5- UPDATE MEMBER")
        print("0- EXIT")
        choice = input("Select action: ")

        if choice == "1":
            list_members()
        elif choice == "2":
            name = input("Enter name of the member: ")
            phone = input("Enter phone number of the member: ")
            address = input("Enter address of the member: ")
            add_member(name, phone, address)
        elif choice == "3":
            member_id = int(input("Enter ID of member to delete: "))
            delete_member(member_id)
        elif choice == "4":
            search_term = input("Enter search term (name or ID): ")
            search_member(search_term)
        elif choice == "5":
            while True:
                try:
                    member_id = int(input("Enter ID of member to update: "))
                    update_member(member_id)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid member ID (a number).")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")