from sqlalchemy.orm import Session
from app.models.movie import Movie

def get_winner_movies(db: Session):
    return db.query(Movie).filter(Movie.winner == True).all()
