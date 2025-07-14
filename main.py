from fastapi import FastAPI
from app.controllers.user_controller import router as user_router
from app.config.settings import create_db_and_tables

app = FastAPI(title="API de Usuários")

create_db_and_tables()

app.include_router(user_router, prefix="/users")

@app.get("/")
def home():
    return {"message": "API de Usuários funcionando"}
