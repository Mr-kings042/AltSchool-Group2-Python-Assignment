from pydantic import BaseModel
from typing import Optional, List, Annotated


class Student(BaseModel):
    name: str
    email: str

class Teacher(BaseModel):
    name: str
    email: str

class Assignment (BaseModel):
    id: int
    student_name: str
    subject: str
    description: str
    filename: str
    comments: List[str] = []