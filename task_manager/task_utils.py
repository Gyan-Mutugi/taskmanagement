from validation import validate_task_title, validate_task_description, validate_due_date

def add_task(tasks, title, description, due_date):
    if not (validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date)):
        return False
    
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    return True

def mark_task_as_complete(tasks, task_index):
    try:
        task_index = int(task_index)
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Invalid task index.")
            return False
    except (ValueError, TypeError):
        print("Invalid task index.")
        return False

def view_pending_tasks(tasks):
    pending_tasks = [task for task in tasks if not task.get("completed", False)]
    if not pending_tasks:
        print("No pending tasks available.")
        return []
    
    for index, task in enumerate(tasks):
        if not task.get("completed", False):
            print(f"[{index}] {task['title']} - Due: {task['due_date']} - {task['description']}")
    return pending_tasks

def calculate_progress(tasks):
    if not tasks:
        print("No working tasks currently available to calculate progress.")
        return 0.0
    
    completed_count = sum(1 for task in tasks if task.get("completed", False))
    total_tasks = len(tasks)
    percentage = (completed_count / total_tasks) * 100
    print(f"Progress: {completed_count}/{total_tasks} tasks completed ({percentage:.1f}%)")
    return percentage