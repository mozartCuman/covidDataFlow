from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return {"status": "online", "versao": "1.1"}
