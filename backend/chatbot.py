# backend/chatbot.py
from typing import Optional
from sqlalchemy.orm import Session
from models import Rule

DEFAULT_FALLBACK = (
    "Sorry"
    ", I’m not sure about that. I can help with PCOD topics like symptoms, "
    "causes, diagnosis, treatment, diet, and lifestyle."
)

def _normalize(text: str) -> str:
    return (text or "").strip().lower()

def find_rule_reply(db: Session, user_input: str) -> Optional[str]:
    """
    Very simple rule lookup:
    - For each rule, we store comma-separated keywords like 'diet,food,nutrition'
    - We match if ANY keyword is a substring of the user_input
    - Then pick the highest-priority rule
    """
    q = _normalize(user_input)

    # Pull all rules once; small table is fine. For a big set, do SQL filtering.
    rules = db.query(Rule).order_by(Rule.priority.desc()).all()

    for r in rules:
        # split and strip keywords
        kws = [k.strip().lower() for k in r.keywords.split(",") if k.strip()]
        if any(k in q for k in kws):
            return r.response
    return None

def get_response(db: Session, user_input: str) -> str:
    q = _normalize(user_input)

    # Some super-basic hardwired greeters/fallbacks can live here if you want:
    if not q:
        return "Hi! Ask me anything about PCOD—symptoms, causes, diagnosis, treatment, diet, or lifestyle."

    db_reply = find_rule_reply(db, q)
    if db_reply:
        return db_reply

    return DEFAULT_FALLBACK
