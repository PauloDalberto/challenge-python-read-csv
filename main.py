from fastapi import FastAPI
from app.core.database import Base, engine
from app.csv_loader import load_csv_to_db
from app.api.routes import router as api_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

load_csv_to_db("movies.csv")

app.include_router(api_router)
