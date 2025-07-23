from app.core.database import SessionLocal
from app.repositories.movie_repository import get_winner_movies

def load_winner_movies_from_db():
  session = SessionLocal()
  try:
    movies = get_winner_movies(session)
    result = []
    for m in movies:
      result.append({
        "year": m.year,
        "title": m.title,
        "studios": m.studios,
        "producers": m.producers,
        "winner": m.winner,
      })
    return result
  finally:
    session.close()
