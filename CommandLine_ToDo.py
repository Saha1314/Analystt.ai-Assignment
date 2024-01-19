import os
import json

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    print("\nTasks:")
    if not tasks:
        print("No tasks.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = " (Completed)" if task["completed"] else ""
            print(f"{index}. {task['description']}{status}")

def add_task(description, tasks):
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f'Task "{description}" added successfully.')

def delete_task(index, tasks):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f'Task "{deleted_task["description"]}" deleted successfully.')
    else:
        print("Invalid task index.")

def mark_completed(index, tasks):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f'Task "{tasks[index - 1]["description"]}" marked as completed.')
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            add_task(description, tasks)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter the task index to delete: "))
            delete_task(index, tasks)
        elif choice == "4":
            display_tasks(tasks)
            index = int(input("Enter the task index to mark as completed: "))
            mark_completed(index, tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
