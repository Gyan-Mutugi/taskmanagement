from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    tasks = []
    
    while True:
        print("\n=== TASK MANAGEMENT SYSTEM ===")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. Calculate Progress")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, description, due_date)
            
        elif choice == "2":
            pending = view_pending_tasks(tasks)
            if pending:
                idx = input("Enter the index of the task to mark complete: ")
                mark_task_as_complete(tasks, idx)
                
        elif choice == "3":
            view_pending_tasks(tasks)
            
        elif choice == "4":
            calculate_progress(tasks)
            
        elif choice == "5":
            print("Exiting Task Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()