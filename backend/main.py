import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

script_dir = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.abspath(os.path.join(script_dir, "..", "data.json"))

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])  # OJOO

@app.get("/")
def saludo():
    return "PRUEBA"

@app.get("/data")
def get_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


