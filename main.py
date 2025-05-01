from fastapi import FastAPI, status, HTTPException, UploadFile, Form
from uuid import UUID
from typing import Annotated, List
from models import Student, Teacher, Assignment
from database import student_db, teacher_db, assignment_db

app = FastAPI()
# assignments_comments = {}
assignment_counter = 1


@app.get("/")
def home():
    return {"message": "Welcome to the Assignment API"}


# @app.post("/assignments/{assignment_id}/comment", status_code=status.HTTP_201_CREATED)
# def add_comment(
#     assignment_id: int,
#     teacher_name: str = Form(...),
#     comment: str = Form(...)
#  ):
#     if assignment_id not in assignments_comments:
#        assignments_comments[assignment_id] = []

      assignments_comments[assignment_id].append({
         "teacher_name": teacher_name,
         "comment" : comment
      }) 
      return{
         "message": "Comment added successfully"
      }
   
@app.post("/teachers", status_code = 201)
def register_teacher(body: Teacher):
    email = body.email
    name = body.name
    print(name,email)
    if email in teacher_db:
       raise HTTPException(status_code=409, detail={"message": "email already exist"})
    teacher = {"name": name, "email": email}
    teacher_db[email] = teacher
    print(teacher)
    return {"message": "Teacher registered successful", "data": teacher}


@app.get("/teachers")
def get_teachers():
    teachers = list(teacher_db.values())
    print(teachers)
    return {"message": "Teachers retrieved successful", "data": teachers}


# Submit an assignment
@app.post("/assignments/")
async def submit_assignment(
    student_name: Annotated[str, Form()],
    subject: Annotated[str, Form()],
    description: Annotated[str, Form()],
    file: UploadFile = None
):
    if student_name not in student_db:
        raise HTTPException(status_code=404, detail="Student not found")
    global assignment_counter
    assignment = Assignment(
        id=assignment_counter,
        student_name=student_name,
        subject=subject,
        description=description,
        filename=file.filename if file else "",
        comments=[]
    )
    assignment_db[assignment_counter] = assignment
    assignment_counter += 1
    return {"message": "Assignment submitted successfully", "assignment": assignment.dict()}


# get specific student assignment by student name
@app.get(
    "/students/{name}/assignments/",
    response_model= List[Assignment]
    )
async def StudentAssignment(student_name:str):
    if student_name not in student_db:
        raise HTTPException(status_code=404. detail="Student not found.")
    
    student_assignment = [
        assignment for assignment in assignment_db.values()
        if assignment["student_name"] == student_name 
    ]
    
    return student_assignment
