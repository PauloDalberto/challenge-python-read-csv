import csv
from app.models.movie import Movie
from app.core.database import SessionLocal

def load_csv_to_db(csv_path: str):
    session = SessionLocal()

    try:
        with open(csv_path, encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                winner = row["winner"].strip().lower() == "yes"
                movie = Movie(
                    year=int(row["year"]),
                    title=row["title"],
                    studios=row["studios"],
                    producers=row["producers"],
                    winner=winner,
                )
                session.add(movie)
            session.commit()
    except FileNotFoundError:
        print(f"Erro: Arquivo {csv_path} não encontrado.")
        raise
    except Exception as e:
        print(f"Erro ao carregar dados do CSV: {e}")
        raise
    finally:
        session.close()

