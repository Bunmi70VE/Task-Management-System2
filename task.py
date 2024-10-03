from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from .models import Task, TaskCategory, User
from .auth import get_current_user
from .database import tasks_db
from .utils import get_task_owner

router = APIRouter()

# Global counter for task IDs (for simplicity)
next_task_id = 1


# Create a task
@router.post("/tasks/", response_model=Task)
async def create_task(task: Task, current_user: User = Depends(get_current_user)):
    global next_task_id
    task.id = next_task_id
    next_task_id += 1
    task.assigned_to = current_user.username
    tasks_db[task.id] = task
    return task


# Get tasks (filter by category or deadline)
@router.get("/tasks/", response_model=List[Task])
async def get_tasks(
        category: Optional[TaskCategory] = Query(None),
        deadline_before: Optional[datetime] = Query(None),
        current_user: User = Depends(get_current_user),
):
    user_tasks = [task for task in tasks_db.values() if task.assigned_to == current_user.username]

    if category:
        user_tasks = [task for task in user_tasks if task.category == category]
    if deadline_before:
        user_tasks = [task for task in user_tasks if task.due_date and task.due_date <= deadline_before]

    return user_tasks


# Update a task (only for the task owner)
@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(
        task_id: int, updated_task: Task, current_user: User = Depends(get_current_user)
):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")

    get_task_owner(tasks_db, task_id, current_user)

    tasks_db[task_id].title = updated_task.title
    tasks_db[task_id].description = updated_task.description
    tasks_db[task_id].status = updated_task.status
    tasks_db[task_id].due_date = updated_task.due_date
    tasks_db[task_id].category = updated_task.category

    return tasks_db[task_id]


# Delete a task (only for the task owner)
@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")

    get_task_owner(tasks_db, task_id, current_user)

    del tasks_db[task_id]
    return {"message": "Task deleted successfully"}
