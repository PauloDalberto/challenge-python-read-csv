from pydantic import BaseModel
from typing import List

class IntervalItem(BaseModel):
  producer: str
  interval: int
  previousWin: int
  followingWin: int

class IntervalResponse(BaseModel):
  min: List[IntervalItem]
  max: List[IntervalItem]