import json
import os

TODO_FILE = "todo_list.json"


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []


def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file, indent=4)


def add_todo():
    task = input("Enter a new task: ")
    todos = load_todos()
    todos.append({"task": task, "completed": False})
    save_todos(todos)
    print("Task added.")


def list_todos():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
        return
    for i, todo in enumerate(todos):
        status = "✓" if todo["completed"] else "✗"
        print(f"{i + 1}. [{status}] {todo['task']}")


def complete_todo():
    list_todos()
    todos = load_todos()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(todos):
            todos[task_number - 1]["completed"] = True
            save_todos(todos)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_todo():
    list_todos()
    todos = load_todos()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(todos):
            todos.pop(task_number - 1)
            save_todos(todos)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\nTo-Do List App")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Complete a task")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_todo()
        elif choice == "2":
            list_todos()
        elif choice == "3":
            complete_todo()
        elif choice == "4":
            delete_todo()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
