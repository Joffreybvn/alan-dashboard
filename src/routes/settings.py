
from fastapi import APIRouter, HTTPException
from config import config
from src.database import Database
from src.sanitizers import SettingsLoginRequest, SettingsUpdateRequest

database = Database(config.DB_HOST, config.DB_PASSWORD)
router = APIRouter(prefix="/settings")


@router.post("/login/")
async def login_settings(request: SettingsLoginRequest):

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
    return HTTPException(
        status_code=400,
        detail="Your URL has timed-oud. Ask Alan another link with !settings"
    )


@router.post("/update/")
async def update_settings(request: SettingsUpdateRequest):

    database.upsert_user(
        request.access_token,
        becode_token=request.get_becode_token(),
        send_notification=request.send_notification
    )

    return HTTPException(status_code=200)
