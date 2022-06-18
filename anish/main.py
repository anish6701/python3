from fastapi import FastAPI
import models
from database import engine
from routers import kyc, merchant, authentication, bank, personal, store

app=FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(merchant.router)
app.include_router(kyc.router)
app.include_router(bank.router)
app.include_router(personal.router)
app.include_router(store.router)