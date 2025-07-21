from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Movie(Base):
  __tablename__ = "movies"

  id = Column(Integer, primary_key=True, index=True)
  year = Column(Integer)
  title = Column(String)
  studios = Column(String)
  producers = Column(String)
  winner = Column(Boolean)