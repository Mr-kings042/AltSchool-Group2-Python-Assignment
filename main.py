from fastapi import FastAPI,status,HTTPException, UploadFile, Form
from uuid import UUID
from models import Student, Teacher, Assignment
from database import student_db, teacher_db, assignment_db

app = FastAPI()

# ✅ GET /assignments/
# List all submitted assignments

# Create ann endpoint that gets all the assignments submitted by a student,
# To do this, i should be able to grab all students Id, and check if all student has submitted an assignment
# If a student is present and has no assignment submitted, there should be an http response with a 404 status code
# But if a student is present and has submitted an assignment, the response should be a 200 status code
# and return all the assignments, I think the assignments should return with a namee, So it coould be:
# Name: Johndoe
# Assignemt: 'The assignment payload' (If there is an assignment submitted)
# And if there is no assignment submitted, it should return:
# Name: Johndoe
# No assignment submitted

# I can also try to see if all details can be pushed into a list, and reeturn the list after it is done checking for the assignments and names or student id


# @app.get("/assignments/")
# async def assignments(id):
#     Assignment_list = Assignment
#     for id in Assignment_list:
#         Assignment_storage = {
#             'StudentId': id,
#             'StudentName' : Assignment_list.student_name,
#             'StudentAssignment' : Assignment_list.filename,
#         }
#         if not id:
#             return HTTPException(status_code=400, detail="No students found")
#         else:
#             Assignment_storage['StudentId'] = id
#             if Assignment_list.student_name or Assignment_list.filename:
#                 Assignment_storage['StudentName'] = Assignment_list.student_name
#                 Assignment_storage['StudentAssignment'] = Assignment_list.filename
#             return Assignment_storage
#     return Assignment_storage



@app.get("/assignments/")
async def get_assignments():
    assignments = []
    for student_id, student in student_db.items():
        if student_id in assignment_db:
            assignment = assignment_db[student_id]
            assignments.append({
                "student_id": student_id,
                "student_name": student.name,
                "assignment": assignment
            })
        else:
            assignments.append({
                "student_id": student_id,
                "student_name": student.name,
                "assignment": None
            })
    return assignments