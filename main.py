from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .database import SessionLocal, engine, Base
from .crud import save_prompt, get_user_history
from .prompts import casual_prompt, formal_prompt
from .config import settings
import openai

Base.metadata.create_all(bind=engine)

app = FastAPI()
openai.api_key = settings.OPENAI_API_KEY

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class QueryInput(BaseModel):
    user_id: str
    query: str

@app.post("/generate")
def generate_response(input: QueryInput, db: Session = Depends(get_db)):
    try:
        casual_prompt_text = casual_prompt(input.query)
        formal_prompt_text = formal_prompt(input.query)

        casual_resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": casual_prompt_text}]
        )["choices"][0]["message"]["content"]

        formal_resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": formal_prompt_text}]
        )["choices"][0]["message"]["content"]

        save_prompt(db, input.user_id, input.query, casual_resp, formal_resp)

        return {"casual_response": casual_resp, "formal_response": formal_resp}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
def history(user_id: str, db: Session = Depends(get_db)):
    records = get_user_history(db, user_id)
    return [
        {
            "query": r.query,
            "casual_response": r.casual_response,
            "formal_response": r.formal_response,
            "created_at": r.created_at
        } for r in records
    ]