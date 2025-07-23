from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import router as api_router
from app.api.csv_routes import router as api_csv_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)
app.include_router(api_csv_router)