from fastapi import APIRouter
from ..Crud import get_continente, get_paises_by_continente

router = APIRouter()

@router.get("/api/continentes")
def continentes():
    result = get_continente()
    continentes = [row[1] for row in result]  # extrai só o nome
    return {"continentes": continentes}

@router.get("/api/continentes/{nome}/paises")
def paises_por_continente(nome: str):
    result = get_paises_by_continente(nome)
    paises = [row[0] for row in result if row[0]]  # extrai só o nome dos países, ignorando nulos
    return {"continente": nome, "paises": paises}