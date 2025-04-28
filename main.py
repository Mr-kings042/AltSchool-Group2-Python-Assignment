from fastapi import FastAPI,status,HTTPException, UploadFile, Form
from uuid import UUID
from typing import Annotated
from models import Student, Teacher, Assignment
from database import student_db, teacher_db,assignment_db

app = FastAPI()

@app.get("/")
def Home():
    return {"message": "Welcome to the Assignment API"}
