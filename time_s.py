from datetime import datetime, timedelta

def get_current_time():
    """
    Returns the current date and time in the appropriate format.
    """
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

def get_due_date():
    """
    Returns the due date, which is two weeks from the current date, in the appropriate format.
    """
    current_time = datetime.now()
    due_date = current_time + timedelta(weeks=2)
    return due_date.strftime("%Y-%m-%d")

