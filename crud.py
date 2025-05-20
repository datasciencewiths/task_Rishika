from sqlalchemy.orm import Session
from .models import Prompt
import uuid

def save_prompt(db: Session, user_id: str, query: str, casual: str, formal: str):
    prompt = Prompt(
        user_id=user_id,
        query=query,
        casual_response=casual,
        formal_response=formal,
    )
    db.add(prompt)
    db.commit()
    db.refresh(prompt)
    return prompt

def get_user_history(db: Session, user_id: str):
    return db.query(Prompt).filter(Prompt.user_id == user_id).order_by(Prompt.created_at.desc()).all()
