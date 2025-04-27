from fastapi import FastAPI,status,HTTPException, UploadFile, Form
from uuid import UUID
from typing import Annotated
from models import Student, Teacher, Assignment
from database import student_db, teacher_db, assignment_db

app = FastAPI()
assignments_comments = {}

@app.get("/")
def Home():
    return {"message": "Welcome to the Assignment API"}



@app.post("/assignments/{assignment_id}/comment")
def add_comment(
    assignment_id: int, 
    teacher_name: str = Form(...), 
    comment: str = Form(...)
 ):
   if assignment_id not in assignments_comments: 
      assignments_comments[assignment_id] = []

      assignments_comments[assignment_id].append({
         "teacher_name": teacher_name,
         "comment" : comment
      }) 
      return{
         "message": "Comment added successfully"
      }


   

   
     
