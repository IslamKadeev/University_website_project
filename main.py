from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from crud import *
from models import *

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/db_restaurant"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_page/")
def create_page_endpoint(title: str, content: str, db: Session = Depends(get_db)):
    return create_page(db, title=title, content=content)

@app.get("/get_page/{page_id}")
def get_page_endpoint(page_id: int, db: Session = Depends(get_db)):
    return get_page(db, page_id=page_id)

@app.get("/get_pages/")
def get_pages_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_pages(db, skip=skip, limit=limit)

@app.delete("/delete_page/{page_id}")
def delete_page_endpoind(page_id: int, db: Session = Depends(get_db)):
    return delete_page(db, page_id=page_id)