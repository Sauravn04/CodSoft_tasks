import tkinter as tk
from tkinter import messagebox
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
    task = entry_task.get()
    if task:
        todos = load_todos()
        todos.append({"task": task, "completed": False})
        save_todos(todos)
        list_todos()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def list_todos():
    todos = load_todos()
    listbox_tasks.delete(0, tk.END)
    for todo in todos:
        status = "✓" if todo["completed"] else "✗"
        listbox_tasks.insert(tk.END, f"[{status}] {todo['task']}")


def complete_todo():
    try:
        index = listbox_tasks.curselection()[0]
        todos = load_todos()
        todos[index]["completed"] = True
        save_todos(todos)
        list_todos()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")


def delete_todo():
    try:
        index = listbox_tasks.curselection()[0]
        todos = load_todos()
        todos.pop(index)
        save_todos(todos)
        list_todos()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")


root = tk.Tk()
root.title("To-Do List App")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add task", width=48, command=add_todo)
button_add_task.pack()

button_complete_task = tk.Button(
    root, text="Complete task", width=48, command=complete_todo
)
button_complete_task.pack()

button_delete_task = tk.Button(root, text="Delete task", width=48, command=delete_todo)
button_delete_task.pack()

list_todos()

root.mainloop()
