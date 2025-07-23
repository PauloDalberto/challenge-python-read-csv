import csv

def load_winner_movies_from_csv():
  with open("movies.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    return [
      {
        "year": int(row["year"]),
        "title": row["title"],
        "studios": row["studios"],
        "producers": row["producers"],
        "winner": row["winner"].strip().lower() == "yes"
      }
      for row in reader if row["winner"].strip().lower() == "yes"
    ]
