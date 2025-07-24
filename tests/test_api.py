from fastapi.testclient import TestClient
from collections import defaultdict
import re
from tests.utils import load_winner_movies_from_db
from main import app
from unittest.mock import patch

client = TestClient(app)

def test_root_route_returns_winner_movies():
  expected = load_winner_movies_from_db()
  response = client.get("/winners")

  assert response.status_code == 200
  data = response.json()

  assert len(data) == len(expected)

  expected_titles = {m["title"] for m in expected}
  api_titles = {m["title"] for m in data}
  assert expected_titles == api_titles

  if expected:
    assert data["year"] == expected["year"]
    assert data["studios"] == expected["studios"]
    assert data["producers"] == expected["producers"]
    assert data["winner"] is True



def test_producers_intervals_route():
  winner_movies = load_winner_movies_from_db()

  producer_wins = defaultdict(list)
  for movie in winner_movies:
    for producer in re.split(r",| and ", movie["producers"]):
      producer_wins[producer.strip()].append(movie["year"])
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
  if intervals:
    min_interval = min(i["interval"] for i in intervals)
    max_interval = max(i["interval"] for i in intervals)
    expected_min = [i for i in intervals if i["interval"] == min_interval]
    expected_max = [i for i in intervals if i["interval"] == max_interval]
  else:
    expected_min = []
    expected_max = []
  response = client.get("/producers/intervals")
  assert response.status_code == 200
  data = response.json()

  assert len(data["min"]) == len(expected_min)
  assert len(data["max"]) == len(expected_max)

  for item in expected_min:
    assert any(
      i["producer"] == item["producer"] and
      i["interval"] == item["interval"] and
      i["previousWin"] == item["previousWin"] and
      i["followingWin"] == item["followingWin"]
      for i in data["min"]
    )

  for item in expected_max:
    assert any(
      i["producer"] == item["producer"] and
      i["interval"] == item["interval"] and
      i["previousWin"] == item["previousWin"] and
      i["followingWin"] == item["followingWin"]
      for i in data["max"]
    )

def test_root_route_empty_database():
  with patch('app.repositories.movie_repository.get_winner_movies', return_value=[]):
    response = client.get("/winners")
    assert response.status_code == 200
    assert response.json() == [], "The route should return an empty list when there are no winning movies"

def test_producers_intervals_empty_database():
  with patch('app.repositories.movie_repository.get_winner_movies', return_value=[]):
    response = client.get("/producers/intervals")
    assert response.status_code == 200
    assert response.json() == {"min": [], "max": []}, "The route should return empty min and max when there are no winning movies"

