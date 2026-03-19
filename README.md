# 🏢 Saurabh's Synergy — Employee Leave Management API

A REST API built from scratch using **FastAPI** and **PostgreSQL** to manage employee leave requests. Supports full CRUD operations with a clean, auto-documented interface.

---

## 🛠️ Tech Stack

- **FastAPI** — Web framework
- **SQLAlchemy** — ORM for database interaction
- **PostgreSQL** — Relational database
- **Pydantic** — Data validation and serialization
- **Uvicorn** — ASGI server

---

## 📁 Project Structure

```
├── main.py              # FastAPI app and all route definitions
├── database.py          # Database engine and session setup
├── database_models.py   # SQLAlchemy table models
├── models.py            # Pydantic schemas for request/response
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

### 4. Configure your database

Open `database.py` and update the connection URL with your PostgreSQL credentials:

```python
db_url = "postgresql://your_username:your_password@localhost:5432/your_db_name"
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

The API will be live at: `http://127.0.0.1:8000`  
Interactive docs (Swagger UI): `http://127.0.0.1:8000/docs`

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/greet` | Welcome message |
| `GET` | `/leaves_all` | Fetch all leave requests |
| `POST` | `/to_request_leave` | Submit a new leave request |
| `PUT` | `/update_request/{id}` | Update an existing leave request |
| `DELETE` | `/deleting_request/{id}` | Delete a leave request by ID |

---

## 📦 Request Body Example (POST / PUT)

```json
{
  "name": "Saurabh",
  "department": "Engineering",
  "reason": "Family vacation",
  "total_leaves": 5
}
```

---

## 🙋 Author

**Saurabh** — Built this project from scratch to learn FastAPI and PostgreSQL integration.  
Open for suggestion 
🔗 [Connect with me on LinkedIn](https://www.linkedin.com/in/saurabh-lokhande-111459376)