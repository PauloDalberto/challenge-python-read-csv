from collections import defaultdict
import re
from typing import List, Dict

from app.models.movie import Movie

def calculate_producer_intervals(movies: List[Movie]):
  producer_wins: Dict[str, List[int]] = defaultdict(list)

  for movie in movies:
    for producer in re.split(r",| and ", movie.producers):
      producer_wins[producer.strip()].append(movie.year)

  intervals = []

  for producer, years in producer_wins.items():
    if len(years) < 2:
      continue
    years.sort()
    for i in range(1, len(years)):
      interval = years[i] - years[i - 1]
      intervals.append({
        "producer": producer,
        "interval": interval,
        "previousWin": years[i - 1],
        "followingWin": years[i]
      })

  if not intervals:
    return {"min": [], "max": []}

  min_interval = min(i["interval"] for i in intervals)
  max_interval = max(i["interval"] for i in intervals)

  return {
    "min": [i for i in intervals if i["interval"] == min_interval],
    "max": [i for i in intervals if i["interval"] == max_interval]
  }
