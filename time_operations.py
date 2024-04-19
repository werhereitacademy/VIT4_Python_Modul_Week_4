# time_operations.py
import json
from datetime import datetime, timedelta

def calculate_dates():
    borrow_date = datetime.now()
    return_date = borrow_date + timedelta(days=14)
    formatted_date = borrow_date.strftime("%Y-%m-%d %H:%M:%S")
    return return_date, formatted_date, borrow_date

def track_book_status(member_id):
    try:
        with open("takip.json", "r") as file:
            track_data = json.load(file)
    except FileNotFoundError:
        track_data = []

    for entry in track_data:
        if entry["member_id"] == member_id:
            track_return(member_id)
            return {
                "member_id": entry.get("member_id", None),
                "phone": entry.get("phone", None),
                "address": entry.get("address", None),
                "Barcode": entry.get("Barcode", None),
                "Book_Name": entry.get("Book_Name", None),
                "Publishing_House": entry.get("Publishing_House", None),
                "Author": entry.get("Author", None),
                "Language": entry.get("Language", None),
                "Price": entry.get("Price", None),
                "Return_Date": entry.get("Return_Date", None),
                "Return_Date_Actual": entry.get("Return_Date_Actual", None)
            }
    return {}

def track_return(member_id):
    try:
        with open("takip.json", "r") as file:
            track_data = json.load(file)
    except FileNotFoundError:
        track_data = []

    for entry in track_data:
        if entry["member_id"] == member_id:
            entry["Return_Date_Actual"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break

    with open("takip.json", "w") as file:
        json.dump(track_data, file, indent=4)

    print("Return tracking data updated successfully.")
