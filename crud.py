from sqlalchemy.orm import Session
from models import *


# Подсистема управления контентом (CMS)
def create_page(db: Session, title: str, content: str):
    db_page = Page(title=title, content=content)
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page

def get_page(db: Session, page_id: int):
    return db.query(Page).filter(Page.id == page_id).first()

def get_pages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Page).offset(skip).limit(limit).all()

def delete_page(db: Session, page_id: int):
    return db.query(Page).delete(Page.id==page_id)
