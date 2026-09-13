from task_manager.validation import (
    validate_due_date,
    validate_task_description,
    validate_task_title,
)


def add_task(tasks, title, description, due_date):
    """Validates input fields and appends a new task dictionary to the tasks list."""
    if not (
        validate_task_title(title)
        and validate_task_description(description)
        and validate_due_date(due_date)
    ):
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    print(f"Task '{title.strip()}' added successfully!")
    return True


def mark_task_as_complete(tasks, task_index):
    """Marks a task as complete using its index in the list."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['title']}' marked as complete!")
        return True
    print("Error: Invalid task index.")
    return False


def view_pending_tasks(tasks):
    """Displays and returns all incomplete tasks."""
    pending_tasks = [task for task in tasks if not task["completed"]]

    if not pending_tasks:
        print("No pending tasks available.")
        return []

    print("\n--- Pending Tasks ---")
    for index, task in enumerate(tasks):
        if not task["completed"]:
            print(
                f"[{index}] {task['title']} - Due: {task['due_date']} - {task['description']}"
            )
    return pending_tasks


def calculate_progress(tasks):
    """Calculates and displays task completion percentage."""
    if not tasks:
        print("No working tasks currently available to calculate progress.")
        return 0.0

    completed_count = sum(1 for task in tasks if task["completed"])
    total_tasks = len(tasks)
    percentage = (completed_count / total_tasks) * 100

    print(
        f"\nProgress: {completed_count}/{total_tasks} tasks completed ({percentage:.1f}%)"
    )
    return percentage