from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

# Connect to Postgres using env variables
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

class Todo(BaseModel):
    title: str
    completed: bool = False

@app.get("/todos")
def get_todos():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos")
    return cursor.fetchall()

@app.post("/todos")
def create_todo(todo: Todo):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (title, completed) VALUES (%s, %s)",
        (todo.title, todo.completed)
    )
    conn.commit()
    return {"message": "created"}

@app.put("/todos/{id}")
def complete_todo(id: int):
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET completed = true WHERE id = %s", (id,))
    conn.commit()
    return {"message": "updated"}

@app.delete("/todos/{id}")
def delete_todo(id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = %s", (id,))
    conn.commit()
    return {"message": "deleted"}
