from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.repositories.movie_repository import get_winner_movies
from app.services.producer_service import calculate_producer_intervals
from app.schemas.producer import IntervalResponse
from app.schemas.movie import MovieSchema
from typing import List

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/winners", response_model=List[MovieSchema])
def root(db: Session = Depends(get_db)):
  return get_winner_movies(db)

@router.get("/producers/intervals", response_model=IntervalResponse)
def get_producer_intervals(db: Session = Depends(get_db)):
  winners = get_winner_movies(db)
  return calculate_producer_intervals(winners)
