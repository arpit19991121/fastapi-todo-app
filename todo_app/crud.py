from typing import List
from todo_app.models import TodoItem

# Fake in-memory database
fake_db: List[TodoItem] = []

def get_all_todos():
    return fake_db

def get_todo_by_id(item_id: int):
    for item in fake_db:
        if item.id == item_id:
            return item
    return None

def create_todo(item: TodoItem):
    fake_db.append(item)
    return item

def update_todo(item_id: int, new_item: TodoItem):
    for i, item in enumerate(fake_db):
        if item.id == item_id:
            fake_db[i] = new_item
            return new_item
    return None

def delete_todo(item_id: int):
    for i, item in enumerate(fake_db):
        if item.id == item_id:
            return fake_db.pop(i)
    return None
