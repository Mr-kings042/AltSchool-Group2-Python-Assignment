# ** Assignment Submission System**

_A FastAPI backend for students and teachers to manage assignments._

## ** Features**

- Student registration
- Assignment submission with file uploads
- Teacher commenting system
- View assignments by student

## ** Quick Start**

### Prerequisites

- Python 3.12
- Git

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/Mr-kings042/AltSchool-Group2-Python-Assignment.git
   ```

   cd AltSchool-Group2-Python-Assignment

2. Install dependencies
   pip install -r requirements.txt

3. Run the server
   uvicorn main:app --reload

## API Endpoints

| Endpoint                    | Method | Parameters                | Description                    |
| --------------------------- | ------ | ------------------------- | ------------------------------ |
| `/assignments/{id}/comment` | POST   | `teacher_name`, `comment` | Add a comment to an assignment |

## ** Team **

| Name            | ID               | Role                 |
| --------------- | ---------------- | -------------------- |
| Mercy Anih      | ALT/SOE/024/5525 |                      |
| Alaka Jubril    | ALT/SOE/024/2748 |                      |
| Israel Imonitie | ALT/SOE/024/2718 |                      |
| Anataku Aaliyah | ALT/SOE/024/4624 |                      |
| Johnson Kayode  | ALT/SOE/024/5396 |                      |
| Chibueze Okoh   | ALT/SOE/024/4890 |                      |
| Paul Mbah       | ALT/SOE/024/5826 |                      |
| Harry Ngere     | ALT/SOE/024/5279 |                      |
| Fatimah Olaitan | ALT/SOE/024/2903 | Documentation        |
| Dorothy Ibia    | ALT/SOE/024/5047 | Student registration |
