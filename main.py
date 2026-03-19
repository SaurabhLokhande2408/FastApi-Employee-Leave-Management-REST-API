from database import engine, SessionLocal
from database_models import  Leave_request
from models import  Employee_leave_request_pydantic, Employee_leave_respone_pydantic
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
import database_models

app = FastAPI(title="Kaizen's Synergy Employee Data")

database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/greet")
def greet():
    return {"message": "Hi welcome to my first built from scratch API i am Kaizen", "docs": "/docs"}


@app.get('/leaves_all', response_model=list[Employee_leave_respone_pydantic])
def get_all_data_about_leave(db: Session = Depends(get_db)):
    return db.query(database_models.Leave_request).all()  


@app.post('/to_request_leave', response_model=Employee_leave_request_pydantic)
def request_leave(request: Employee_leave_request_pydantic, db: Session = Depends(get_db)):
    req = database_models.Leave_request(**request.model_dump())
    db.add(req)
    db.commit()
    db.refresh(req)
    return req

@app.delete("/deleting_request/{id}")  # ✅ removed response_model
def delete_req(id: int, db: Session = Depends(get_db)):
    select = db.query(database_models.Leave_request).filter(database_models.Leave_request.id == id ).first()

    if not select:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Leave request with id={id} not found"
        )

    db.delete(select)
    db.commit()
    return {"message": f"Leave request id={id} deleted successfully"}

@app.put("/update_request/{id}", response_model=Employee_leave_request_pydantic)
def update(request: Employee_leave_request_pydantic, id: int, db: Session = Depends(get_db)):
    select = db.query(database_models.Leave_request).filter(
        database_models.Leave_request.id == id
    ).first()

    if not select:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Leave request with id={id} not found"
        )

    select.name         = request.name          #  request not Leave_request(its a class)
    select.department   = request.department
    select.reason       = request.reason
    select.total_leaves = request.total_leaves

    db.commit()
    db.refresh(select)
    return select                              