from app.models.movie import Movie
from app.core.database import SessionLocal

def clear_movies_table():
  session = SessionLocal()
  try:
    session.query(Movie).delete()
    session.commit()
  finally:
    session.close()