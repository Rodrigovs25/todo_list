import json
import sys
import os

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for idx, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{idx}. {status} {task['description']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index-1]["done"] = True
        save_tasks(tasks)

def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks.pop(index-1)
        save_tasks(tasks)

def main():
    if len(sys.argv) < 2:
        print("Usage: todo.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        list_tasks()
    elif command == "done":
        index = int(sys.argv[2])
        mark_done(index)
    elif command == "remove":
        index = int(sys.argv[2])
        remove_task(index)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
