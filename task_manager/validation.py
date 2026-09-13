from datetime import datetime


def validate_task_title(title):
    """Checks that the title is a non-empty string."""
    if not isinstance(title, str) or len(title.strip()) == 0:
        print("Error: Task title cannot be empty.")
        return False
    return True


def validate_task_description(description):
    """Checks that the description is a non-empty string."""
    if not isinstance(description, str) or len(description.strip()) == 0:
        print("Error: Task description cannot be empty.")
        return False
    return True


def validate_due_date(due_date):
    """Validates that the date follows the YYYY-MM-DD format."""
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return False