from fastapi import FastAPI, HTTPException
from database import student_db, teacher_db, assignments_db  # Import all mock data

app = FastAPI()

# --------------------------
# Student Endpoints
# --------------------------
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in student_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_db[student_id]

# --------------------------
# Assignment Endpoints  
# --------------------------
@app.get("/assignments/{assignment_id}")
def get_assignment(assignment_id: int):
    if assignment_id not in assignments_db:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignments_db[assignment_id]
