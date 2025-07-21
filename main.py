from fastapi import FastAPI
from app.core.database import Base, engine, SessionLocal
from app.models.movie import Movie
from app.csv_loader import load_csv_to_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

load_csv_to_db("movies.csv")

@app.get("/")
def root():
    session = SessionLocal()
    try:
        winners = session.query(Movie).filter(Movie.winner == True).all()
        return [
            {
                "year": movie.year,
                "title": movie.title,
                "studios": movie.studios,
                "producers": movie.producers,
                "winner": movie.winner,
            }
            for movie in winners
        ]
    finally:
        session.close()