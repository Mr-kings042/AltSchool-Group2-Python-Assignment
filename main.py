from fastapi import FastAPI,status,HTTPException, UploadFile, Form
from uuid import UUID
from typing import Annotated
from models import Student, Teacher, Assignment
from database import student_db, teacher_db, assignment_db

app = FastAPI()
# assignments_comments = {}

@app.get("/")
def Home():
    return {"message": "Welcome to the Assignment API"}



# @app.post("/assignments/{assignment_id}/comment", status_code=status.HTTP_201_CREATED)
# def add_comment(
#     assignment_id: int, 
#     teacher_name: str = Form(...), 
#     comment: str = Form(...)
#  ):
#    if assignment_id not in assignments_comments: 
#       assignments_comments[assignment_id] = []

#       assignments_comments[assignment_id].append({
#          "teacher_name": teacher_name,
#          "comment" : comment
#       }) 
#       return{
#          "message": "Comment added successfully"
#       }
@app.post("/assignments/{assignment_id}/comment", status_code=status.HTTP_201_CREATED)
def add_comment(assignment_id: int, 
                teacher_name: Annotated[str, Form()],
                comment: Annotated[str, Form()]):
    assignment = assignment_db.get(assignment_id)
    if not assignment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Assignment not found")
    Comment = f"{teacher_name}:{comment}"
    assignment["comments"].append(Comment)
    return {"message": "Comment added successfully"}
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



   

   
     
