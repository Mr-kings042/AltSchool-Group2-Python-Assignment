from fastapi import FastAPI, status, HTTPException, UploadFile, Form

from typing import Annotated
from models import Student, Teacher, Assignment
from database import student_db, teacher_db, assignment_db, assignment_counter

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the Assignment Submission System API"}

#Implement Student Registration endpoint
@app.post("/student",status_code = status.HTTP_201_CREATED )
def register_student(student: Student):
    #Check if a student is already registered
    if student.email in student_db:
        raise HTTPException(status_code=400, detail="Student is already registered")

    student_db[student.email] = student
    return {"message": "Student registered successfully", "detail": student}

#Implement Teachers Registration endpoint
@app.post("/teachers", status_code=status.HTTP_201_CREATED)
def register_teacher(body: Teacher):
    email = body.email
    name = body.name
    print(name,email)
    if email in teacher_db:
       raise HTTPException(status_code=409, detail={"message": "email already exist"})
    teacher = {"name": name, "email": email}
    teacher_db[email] = body
    print(teacher)
    return {"message": "Teacher registered successful", "data": teacher}

# submit assignment
@app.post("/assignments/", status_code=status.HTTP_201_CREATED)
def submit_assignment(
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

# list all teachers
@app.get("/teachers", status_code=status.HTTP_200_OK)
def get_teachers():
    teachers = list(teacher_db.values())
    print(teachers)
    return teachers


# list all assignment
@app.get("/assignments/", status_code=status.HTTP_200_OK)
def list_assignments():
    assignment = list(assignment_db.values())
    print(assignment)
    return assignment



# View assignments by student name
@app.get("/students/{name}/assignments/", status_code=status.HTTP_200_OK)
def student_assignments(name: str):
    if name not in student_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    
    student_assignments = [
    assignment for assignment in assignment_db.values() 
        if assignment.student_name == name
    ]
    if not student_assignments:
          return {"message": "No assignments found for this student"}
    return student_assignments





@app.post("/assignments/{assignment_id}/comment", status_code=status.HTTP_201_CREATED)
def add_comment(assignment_id: int, 
                teacher_name: Annotated[str, Form()],
                comment: Annotated[str, Form()]):
    if teacher_name not in teacher_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not registered")
     
    assignment = assignment_db.get(assignment_id)

    if not assignment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Assignment not found")
    Comment = f"Teacher_name:{teacher_name},:{comment}"
    assignment_db[assignment_id].comments.append(Comment)
    return {"message": "Comment added successfully", "details": Comment}








