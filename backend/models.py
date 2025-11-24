# backend/models.py
from sqlalchemy import Column, Integer, String, Text
from database import Base

class Rule(Base):
    __tablename__ = "rules"
    id = Column(Integer, primary_key=True, index=True)
    # comma-separated keywords, e.g. "hello,hi,hey"
    keywords = Column(String(512), nullable=False)
    # the bot message to return
    response = Column(Text, nullable=False)
    # higher runs first
    priority = Column(Integer, default=0)
