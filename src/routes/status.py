
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def status():
    """Return a status message of the server."""

    return {
        "status": True,
        "message": "The server is up and running"
    }
