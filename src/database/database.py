
from datetime import datetime
from typing import Union

from pymongo import MongoClient
from mongoframes.queries import Q

from . import User


class Database:

    def __init__(self, db_host: str, db_password: str):
        self.client = MongoClient(f"mongodb+srv://dbUser:{db_password}@{db_host}")
        db_name = "discord"

        # Link frames to the database
        User._client = self.client
        User._db = db_name

    @staticmethod
    def remove_site_token(user_id: str):
        """Remove the site token and its timeout from the database."""

        user = User(
            _id=user_id,
            site_token=None,
            site_token_timeout=None
        )

        user.upsert()

    def get_account_settings(self, site_token: str) -> Union[tuple, bool]:
        """
        Return the account settings for the user with the given site token.
        If returned, remove the site token and its timeout.
        """

        # Check if a user with this token exists
        user = User.one(Q.site_token == site_token, projection={
            "site_token_timeout": True,
            "access_token": True,
            "becode_token": True,
            "send_notification": True
        })

        if user:
            document = user.__dict__['_document']

            # Check if the user has a token and a token timeout
            access_token = document.get("access_token", None)
            timeout_time = document.get("site_token_timeout", None)
            if access_token and timeout_time:

                # Check if the timeout time has not passed yet
                if timeout_time < datetime.now():
                    return False

                # Remove the site token and token timeout
                self.remove_site_token(user._id)

                # Return the acces token and settings
                becode_token = document.get("becode_token", "")
                send_notification = document.get("send_notification", False)
                return access_token, becode_token, send_notification

        return False

    @staticmethod
    def upsert_user(access_token: str, **kwargs):
        """
        Update or Insert a user to the database.

        :param access_token: The access token of the user
        :param kwargs:
            - send_notification (bool)
            - becode_token (str)
        """

        # Create a User object with the given arguments
        user = User.one(Q.access_token == access_token, projection={
            "access_token_timeout": True,
        })

        if user:
            document = user.__dict__['_document']

            # Check the token timeout
            if access_token_timeout := document.get("access_token_timeout", False):

                # Check if the timeout time has not passed yet
                if access_token_timeout.date() < datetime.now().date():
                    return False

                # Upsert the user
                kwargs['_id'] = user._id
                updated_user = User(**kwargs)
                updated_user.upsert()
