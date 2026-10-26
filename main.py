from fastapi import FastAPI
from . import models, database
from .routes import aircrafts

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(aircrafts.router)
