from fastapi import FastAPI,status,HTTPException, UploadFile, Form
from uuid import UUID
from typing import Annotated
from models import Student, Teacher, Assignment
from database import student_db, teacher_db,assignment_db


app = FastAPI()

#Implement Registration endpoint
@app.post("/register-student")
def register_student(student: Student):
    #Check if a student is already registered
    if student.email in student_db:
        raise HTTPException(status_code=400, detail="Student is already registered")

    student_db[student.email] = {
        "name": student.name,
        "email": student.email,
    }
    return {"msg": "Student registered successfully"}

