from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Railway!"}
@app.get("/me", summary="Get developer profile", tags=["Profile"])

def get_profile():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "Cats are mysterious creatures.")
    except Exception as e:
        print(f"Error fetching cat fact: {e}")
        cat_fact = "Could not fetch a cat fact at this time."

    return JSONResponse(
        content={
            "status": "success",
            "user": {
                "name": os.getenv("MY_NAME"),
                "email": os.getenv("MY_EMAIL"),
                "stack": os.getenv("MY_STACK")
            },
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "fact": cat_fact
        }
    )
