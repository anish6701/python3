from fastapi import FastAPI
from routers import bank
from bank_information.database import  Base,engine
from bank_information import models

app=FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(bank.router)