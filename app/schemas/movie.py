from pydantic import BaseModel

class MovieSchema(BaseModel):
  year: int
  title: str
  studios: str
  producers: str
  winner: bool
