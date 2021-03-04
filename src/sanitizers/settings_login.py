
from pydantic import BaseModel


class SettingsLoginRequest(BaseModel):
    token: str
