from fastapi import FastAPI
from backend.routes import Status, Continentes, Covid #, Comparacao
from fastapi.middleware.cors import CORSMiddleware

# Criação da aplicação FastAPI
app = FastAPI(
    title="COVID DataFlow API",
    description="API para consulta de dados de COVID por país e continente",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Registro dos routers
app.include_router(Status.router)
app.include_router(Continentes.router)
app.include_router(Covid.router)


