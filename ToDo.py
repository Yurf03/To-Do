def welcome_users():
    print()
    print("Welcome to the To-Do List Application!")
    
def add(tasks):
    print()
    print("Add Task:")
    print()
    task = input("Enter your task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("No task entered.")
        
def view(tasks):
    print()
    print("Your tasks:")
    print()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")    
        
def delete(tasks):
    print()
    print("Delete Task")
    print()
    
    if not tasks:
        print("No tasks to delete.")
        print()
        return
    
    print("Your tasks:")
    print()
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
def select_task():
    try:
        choice = int(input("Input task number: ").strip())
        return choice
    except ValueError:
        return None
    
def menu():
    print()
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    print()

def main():
    tasks = []
    welcome_users()
    
    while True:
        menu()
        choice = select_task()
        
        if choice == 1:
            add(tasks)
        elif choice == 2:
            view(tasks)
        elif choice == 3:
            delete(tasks)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid input")
        
        input("Press Enter to continue...")
            
if __name__ == "__main__":
    main()