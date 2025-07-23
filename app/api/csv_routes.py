from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from app.utils.csv_loader import load_csv_to_db
from app.utils.csv_clear import clear_movies_table

router = APIRouter()

CSV_FOLDER = "csv"

class CSVSelectionRequest(BaseModel):
  filename: str


@router.get("/csv-files")
async def list_csv_files():

  try:
    if not os.path.exists(CSV_FOLDER):
      return {"Error": "The folder 'csv' not exists"}
    
    files = []
    for f in os.listdir(CSV_FOLDER):
      file_path = os.path.join(CSV_FOLDER, f)
      if os.path.isfile(file_path) and f.endswith(".csv"):
        files.append(f)

    if not files: 
      return {"message": "No csv files found in the folder."}
    
    return {"files": files}
  
  except Exception as e:
    return {"Error": f"Error listing files: {str(e)}"}


@router.post("/select-csv")
async def select_csv(request: CSVSelectionRequest):
  csv_path = os.path.join(CSV_FOLDER, request.filename)

  if not os.path.isfile(csv_path):
    raise HTTPException(status_code=404, detail="CSV file not found")

  try:
    clear_movies_table() 
    load_csv_to_db(csv_path)

    return {"message": f"CSV '{request.filename}' loaded successfully"}

  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error loading CSV: {str(e)}")
