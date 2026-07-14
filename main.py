from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Import our database setup and our table blueprints
from database import engine, get_db, Base
from models import TaskModel

# Tell SQLAlchemy to automatically create the database file and table
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic Schema (for validating user input)
class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False
    priority: int = 1

# GET Route: Fetch all tasks permanently saved in SQLite
@app.get("/tasks/")
def get_all_tasks(db: Session = Depends(get_db)):
    # Run a query to select all tasks
    tasks = db.query(TaskModel).all()
    return tasks

# POST Route: Receive actual input, translate it, and save it permanently!
@app.post("/tasks/")
def create_task(task_input: TaskCreate, db: Session = Depends(get_db)):
    # 1. Translate the Pydantic input data into an ORM Database Object
    new_task = TaskModel(
        title=task_input.title,
        description=task_input.description,
        is_completed=task_input.is_completed,
        priority=task_input.priority
    )
    
    # 2. Add and commit to the database file
    db.add(new_task)
    db.commit()
    db.refresh(new_task)  # Get the newly generated 'id' from the database
    
    return {
        "message": "Task permanently saved to database!",
        "saved_task": new_task
    }
    # DELETE Route: Remove a specific task from the database using its unique ID number
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    # 1. Search the database for a task that matches the incoming 'task_id'
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    
    # 2. If the task doesn't exist, stop and return a 404 error
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
        
    # 3. If found, remove it from the database session and commit the change
    db.delete(task)
    db.commit()
    
    # 4. Return a success message back to the client
    return {"message": f"Task with ID {task_id} has been successfully deleted!"}