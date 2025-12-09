import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [task.strip() for task in file.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter task name: ")
    tasks.append(task)
    print("Task added successfully.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        print("Task deleted successfully.\n")
    except:
        print("Invalid input.\n")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        tasks[index] += " ✔"
        print("Task marked as complete.\n")
    except:
        print("Invalid input.\n")

def main():
    print("=== TO-DO LIST / TASK MANAGER ===")
    tasks = load_tasks()

    while True:
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Complete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
