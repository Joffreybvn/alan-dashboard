
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config import config
from src.database import Database

database = Database(config.DB_HOST, config.DB_PASSWORD)
app = FastAPI()

origins = [
    "http://turingbot.ml",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def status():
    """Return the status message of the server."""

    return {
        "status": True,
        "message": "The server is up and running"
    }


class Site(BaseModel):
    token: str


@app.post("/site/")
def access_dashboard(request: Site):

    # Return the access token if found
    if result := database.get_account_settings(request.token):

        return {
            "status": True,
            "access_token": result[0],
            "settings": {
                "becode_token": result[1],
                "send_notification": result[2]
            }
        }

    # Otherwise, return an error message
    return {
        "status": False,
        "message": "Your URL has timed-oud. Ask Alan another link with !settings"
    }


class UserUpdate(BaseModel):
    access_token: str
    becode_token: str
    send_notification: bool


@app.post("/settings/")
def update_settings(request: UserUpdate):
    print(request)


if __name__ == "__main__":
    uvicorn.run("main:app", port=config.PORT, host="0.0.0.0", reload=True, access_log=False)
