from fastapi import FastAPI
from app.db.database import engine, Base

from app.routers import formulario

from fastapi.security import OAuth2PasswordBearer

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API_Processo Seletivo",
    description="Documentação da API para as candidaturas do Microsoft Forms",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True}
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(formulario.router)

@app.get("/")
def root():
    return {"message": "API funcionando"}