# backend/main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from seed_data import ensure_seed
from chatbot import get_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.on_event("startup")
def on_startup():
    # create tables & seed if empty
    ensure_seed()

@app.post("/chat")
async def chat(req: ChatRequest, db: Session = Depends(get_db)):
    reply = get_response(db, req.message)
    return {"reply": reply}

