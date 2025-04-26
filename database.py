from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Dict

# --- Database Configuration ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./assignments.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Please replace with real DB queries when ready
# --- Temporary Mock Data ---
student_db: Dict[int, dict] = {
    1: {"id": 1, "name": "Alex Johnson", "email": "alex@school.com"},
    2: {"id": 2, "name": "Sam Lee", "email": "sam@school.com"}
}

teacher_db: Dict[int, dict] = {
    1: {"id": 1, "name": "Dr. Smith", "department": "Mathematics"}
}

assignments_db: Dict[int, dict] = {
    1: {
        "id": 1,
        "student_id": 1,
        "subject": "Math",
        "filename": "hw1.pdf",
        "comments": []
    }
}