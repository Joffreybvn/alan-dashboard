
from os import environ


class Config:

    def __init__(self):

        self.PORT = int(environ.get('PORT'))

        # MongoDB authentication
        self.DB_HOST = environ.get('DB_HOST')
        self.DB_PASSWORD = environ.get('DB_PASSWORD')

        # Website URL
        self.MY_BECODE_URL = "https://my.becode.org"
        self.TURINGBOT_URL = "https://turingbot.ml"


config = Config()
