
from typing import Union
from pydantic import BaseModel


class SettingsUpdateRequest(BaseModel):
    access_token: str
    becode_token: str
    send_notification: bool

    def get_becode_token(self) -> Union[str, None]:
        """Return a sanitized version of the BeCode token."""

        # Set the token to False if the string is not valid
        if len(self.becode_token) < 200:
            return None

        return self.becode_token
