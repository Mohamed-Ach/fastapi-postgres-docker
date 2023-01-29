from .routes import controller
from fastapi import FastAPI
from typing import Optional

app = FastAPI()
app.include_router(controller.router)
