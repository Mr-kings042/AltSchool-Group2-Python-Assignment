from pydantic import BaseModel
from typing import Optional, List, Annotated


class Student(BaseModel):
    name: str
    email: str

class Teacher(BaseModel):
    name: str
    email: str
    subject: Optional[str] = None # this accounts for the subject each teacher teaches and also allows cases where a teacher is a form/class teacher and probably teaches multiple subjects

class Assignment (BaseModel):
    id: int
    student_name: str
    subject: str
    description: str
    filename: str
    comments: List[str] = []