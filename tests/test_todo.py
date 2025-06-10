import os
import sys

# Adiciona a pasta pai (onde está o todo.py) no sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import todo

TEST_FILE = "test_todo.json"

def setup_module(module):
    if os.path.exists(todo.TODO_FILE):
        os.rename(todo.TODO_FILE, todo.TODO_FILE + ".bak")
    todo.TODO_FILE = TEST_FILE

def teardown_module(module):
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    if os.path.exists(todo.TODO_FILE + ".bak"):
        os.rename(todo.TODO_FILE + ".bak", todo.TODO_FILE)

def test_add_task():
    todo.add_task("Task 1")
    tasks = todo.load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Task 1"
    assert not tasks[0]["done"]

def test_mark_done():
    todo.add_task("Task 2")
    todo.mark_done(1)
    tasks = todo.load_tasks()
    assert tasks[0]["done"]

def test_remove_task():
    todo.add_task("Task 3")
    todo.remove_task(1)
    tasks = todo.load_tasks()
    assert len(tasks) == 0
