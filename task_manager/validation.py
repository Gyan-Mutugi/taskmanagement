from datetime import datetime


def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Task title cannot be empty")

    return True


def validate_task_description(description):
    if len(description) == 0:
        raise ValueError("Task description cannot be empty")

    if len(description) > 500:
        raise ValueError("Task description cannot exceed 500 characters")

    return True


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid due date. Use YYYY-MM-DD")

    return True