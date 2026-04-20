from fastapi import APIRouter
from ..Crud import (
    get_covid_by_pais, get_covid_by_continente, get_top_paises,
    get_resumo_global, get_evolucao_pais, get_ranking_continente,
    get_resumo_pais, get_resumo_continente, get_ultima_atualizacao,
    comparar_paises
)

router = APIRouter()

@router.get("/api/covid/{pais}")
def covid_pais(pais: str):
    result = get_covid_by_pais(pais)
    if not result:
        return {"message": f"Dados para o país '{pais}' não encontrados."}
    return {"dados_covid": [
        {"pais": row[0], "continente": row[1], "casos": row[2],
         "mortes": row[3], "recuperados": row[4], "data_atualizacao": row[5]}
        for row in result
    ]}

@router.get("/api/covid/continente/{nome}")
def covid_continente(nome: str):
    result = get_covid_by_continente(nome)
    if not result:
        return {"message": f"Dados para o continente '{nome}' não encontrados."}
    dados = {}
    for row in result:
        continente, pais, casos, mortes, recuperados, data = row
        if pais not in dados:
            dados[pais] = []
        dados[pais].append({
            "casos": casos, "mortes": mortes,
            "recuperados": recuperados, "data_atualizacao": data
        })
    return {"continente": nome, "dados_covid": dados}

@router.get("/api/covid/top/{n}")
def top_paises(n: int):
    result = get_top_paises(n)
    return {"top_paises": [
        {"pais": row[0], "continente": row[1],
         "casos": row[2], "mortes": row[3], "recuperados": row[4]}
        for row in result
    ]}

@router.get("/api/covid/resumo_global")
def resumo_global():
    result = get_resumo_global()
    return {"casos_totais": result[0], "mortes_totais": result[1], "recuperados_totais": result[2]}

@router.get("/api/covid/evolucao/{pais}")
def evolucao_pais(pais: str):
    result = get_evolucao_pais(pais)
    return {"evolucao": [
        {"data": row[0], "casos": row[1], "mortes": row[2], "recuperados": row[3]}
        for row in result
    ]}

@router.get("/api/covid/ranking/{continente}")
def ranking_continente(continente: str):
    result = get_ranking_continente(continente)
    return {"ranking": [
        {"pais": row[0], "casos": row[1], "mortes": row[2], "recuperados": row[3]}
        for row in result
    ]}

@router.get("/api/covid/resumo/{pais}")
def resumo_pais(pais: str):
    result = get_resumo_pais(pais)
    if not result:
        return {"message": f"Resumo para o país '{pais}' não encontrado."}
    return {"pais": result[0], "continente": result[1],
            "casos_totais": result[2], "mortes_totais": result[3], "recuperados_totais": result[4]}

@router.get("/api/covid/resumo_continente/{nome}")
def resumo_continente(nome: str):
    result = get_resumo_continente(nome)
    if not result:
        return {"message": f"Resumo para o continente '{nome}' não encontrado."}
    return {"continente": result[0], "casos_totais": result[1],
            "mortes_totais": result[2], "recuperados_totais": result[3]}

@router.get("/api/covid/ultima/{pais}")
def ultima_atualizacao(pais: str):
    result = get_ultima_atualizacao(pais)
    if not result:
        return {"message": f"Nenhum dado encontrado para o país '{pais}'."}
    return {"data_atualizacao": result[0], "casos": result[1],
            "mortes": result[2], "recuperados": result[3]}

@router.get("/api/covid/comparar/{pais1}/{pais2}")
def comparar(pais1: str, pais2: str):
    result = comparar_paises(pais1, pais2)
    return {"comparacao": [
        {"pais": row[0], "casos": row[1], "mortes": row[2], "recuperados": row[3]}
        for row in result
    ]}
