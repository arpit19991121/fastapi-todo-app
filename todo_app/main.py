from fastapi import FastAPI, HTTPException
from todo_app.models import TodoItem
from todo_app import crud

app = FastAPI()

@app.get("/todos")
def read_all():
    return crud.get_all_todos()

@app.get("/todos/{item_id}")
def read_one(item_id: int):
    item = crud.get_todo_by_id(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/todos", status_code=201)
def create(item: TodoItem):
    return crud.create_todo(item)

@app.put("/todos/{item_id}")
def update(item_id: int, new_item: TodoItem):
    updated = crud.update_todo(item_id, new_item)
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/todos/{item_id}", status_code=204)
def delete(item_id: int):
    deleted = crud.delete_todo(item_id)
    if deleted:
        return
    raise HTTPException(status_code=404, detail="Item not found")
