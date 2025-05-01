# **Assignment Submission System**

_A FastAPI backend for students and teachers to manage assignments._

## **Features**

- Student registration
- Assignment submission with file uploads
- Teacher commenting system
- View assignments by student
- Teacher registration and management

## **Quick Start**

### Prerequisites

- Python 3.12
- Git

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/Mr-kings042/AltSchool-Group2-Python-Assignment.git
   ```

   ```bash
   cd AltSchool-Group2-Python-Assignment
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:

   ```bash
   uvicorn main:app --reload
   ```

4. Access interactive API docs at:
   ```bash
   http://localhost:8000/docs
   ```

## **API Endpoints**

| Endpoint                               | Method | Parameters                                                                         | Description                              |
| -------------------------------------- | ------ | ---------------------------------------------------------------------------------- | ---------------------------------------- |
| `/students/`                           | POST   | -                                                                                  | Register new student                     |
| `/teachers/`                           | POST   | -                                                                                  | Register a new teacher                   |
| `/assignments/`                        | POST   | `student_name` (Form)<br>`subject` (Form)<br>`description` (Form)<br>`file` (File) | Submit a new assignment with file upload |
| `/students/{name}/assignments/`        | GET    | `name` (Path)                                                                      | View assignments for a specific student  |
| `/assignments/{assignment_id}/comment` | POST   | `teacher_name` (Form)<br>`comment` (Form)                                          | Add teacher comment to assignment        |

## **Example Responses**

### Successful Teacher Registration (201)

```json
{
  "message": "Teacher registered successfully",
  "data": {
    "name": "Dr. Smith",
    "email": "smith@example.com"
  }
}
```

### Error: Duplicate Email (409)

```json
{
  "detail": {
    "message": "Email already exists"
  }
}
```

### Assignment Submission (200)

```json
{
  "message": "Assignment submitted successfully",
  "assignment": {
    "id": 1,
    "student_name": "Alice",
    "subject": "Math",
    "description": "Chapter 1 Exercises",
    "filename": "homework.pdf",
    "comments": []
  }
}
```

## **Development Roadmap**

### Core Features

- [ ] Student authentication system
- [ ] Assignment grading functionality
- [ ] File type validation for uploads

### Improvements

- [ ] Add pagination for large lists
- [ ] Implement response caching
- [ ] Enhanced error documentation

## **Team**

| Name            | ID               | Role                            |
| --------------- | ---------------- | ------------------------------- |
| Mercy Anih      | ALT/SOE/024/5525 | Create student API              |
| Alaka Jubril    | ALT/SOE/024/2748 | Teachers registration           |
| Israel Imonitie | ALT/SOE/024/2718 |                                 |
| Anataku Aaliyah | ALT/SOE/024/4624 | Create comments on assignments  |
| Johnson Kayode  | ALT/SOE/024/5396 | Create student API              |
| Chibueze Okoh   | ALT/SOE/024/4890 | Create comments on assignments  |
| Paul Mbah       | ALT/SOE/024/5826 | Assignment submission           |
| Harry Ngere     | ALT/SOE/024/5279 | Get student assignments by name |
| Fatimah Olaitan | ALT/SOE/024/2903 | Documentation                   |
| Dorothy Ibia    | ALT/SOE/024/5047 | Student registration            |
