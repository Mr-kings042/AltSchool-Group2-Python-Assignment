from fastapi import FastAPI,status,HTTPException, UploadFile, Form
from uuid import UUID
from models import Student, Teacher, Assignment
from database import student_db, teacher_db

app = FastAPI()