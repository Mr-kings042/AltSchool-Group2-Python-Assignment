from fastapi import FastAPI,status,HTTPException, UploadFile, Form
from uuid import UUID
from typing import Annotated
from models import Student, Teacher, Assignment
from database import student_db, teacher_db, assignment_db

app = FastAPI()

@app.post("/assignments/{assignment_id}/comment")
def add_comment(assignment_id: int, 
                teacher_name: Annotated[str, Form()],
                comment: Annotated[str, Form()]):
    assignment = assignment_db.get(str(assignment_id))
    if not assignment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Assignment not found")
    Comment = f"{teacher_name}:{comment}"
    assignment.comments.append(Comment)
    return {"message": "Comment added successfully"}
