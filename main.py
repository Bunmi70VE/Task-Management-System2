from fastapi import FastAPI
from .auth import router as auth_router
from .tasks import router as tasks_router

app = FastAPI()

# Register authentication and task routes
app.include_router(auth_router)
app.include_router(tasks_router)

# Health check route
@app.get("/")
async def root():
    return {"message": "Task Management System is running"}
