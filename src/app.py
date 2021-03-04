
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import status, settings


class Dashboard:

    def __init__(self):
        self.app = FastAPI()

        # Allow CORS
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Register all routes
        self.app.include_router(status)
        self.app.include_router(settings)

    def get_app(self):
        return self.app
