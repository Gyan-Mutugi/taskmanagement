from datetime import datetime

def validate_task_title(title):
    if not title or len(str(title).strip()) == 0:
        print("Task title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    if not description or len(str(description).strip()) == 0:
        print("Task description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(str(due_date).strip(), "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return False