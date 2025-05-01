from fastapi import FastAPI, status, HTTPException, UploadFile, Form
from uuid import UUID
from typing import Annotated
from models import Student, Teacher, Assignment
from database import student_db, teacher_db, assignment_db

app = FastAPI()
# assignments_comments = {}
assignment_counter = 1


@app.get("/")
def home():
    return {"message": "Welcome to the Assignment API"}

#Implement Student Registration endpoint
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


# @app.post("/assignments/{assignment_id}/comment", status_code=status.HTTP_201_CREATED)
# def add_comment(
#     assignment_id: int,
#     teacher_name: str = Form(...),
#     comment: str = Form(...)
#  ):
#     if assignment_id not in assignments_comments:
#        assignments_comments[assignment_id] = []

    #   assignments_comments[assignment_id].append({
    #      "teacher_name": teacher_name,
    #      "comment" : comment
    #   }) 
    #   return{
    #      "message": "Comment added successfully"
    #   }
   
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
