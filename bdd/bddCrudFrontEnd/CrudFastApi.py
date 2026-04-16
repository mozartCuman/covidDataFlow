from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DB_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/covid_data"
engine = create_engine(DB_URL)

@app.get("/status")
def status():
    return {"status": "online", "versao": "1.0"}


@app.get("/api/continentes")
def get_continentes():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT c.nome AS continente, p.nome AS pais
            FROM continentes c
            LEFT JOIN paises p ON p.continente_id = c.id
            ORDER BY c.nome, p.nome
        """)).fetchall()

        continentes = {}
        for row in result:
            continente, pais = row
            if continente not in continentes:
                continentes[continente] = []
            if pais:
                continentes[continente].append(pais)

        return {"continentes": continentes}
    
@app.get("/api/covid/{pais}")
def get_covid_by_pais(pais: str):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT p.nome AS pais, c.nome AS continente,
                   d.casos, d.mortes, d.recuperados, d.data_atualizacao
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            JOIN continentes c ON p.continente_id = c.id
            WHERE p.nome = :pais
            ORDER BY d.data_atualizacao
        """), {"pais": pais}).fetchall()

        dados = [
            {
                "pais": row[0],
                "continente": row[1],
                "casos": row[2],
                "mortes": row[3],
                "recuperados": row[4],
                "data_atualizacao": row[5]
            }
            for row in result
        ]

        if not dados:
            return {"message": f"Dados para o país '{pais}' não encontrados."}

        return {"dados_covid": dados}
    
@app.get("/api/covid/continente/{nome}")
def get_covid_by_continente(nome: str):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT c.nome AS continente, p.nome AS pais,
                   d.casos, d.mortes, d.recuperados, d.data_atualizacao
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            JOIN continentes c ON p.continente_id = c.id
            WHERE c.nome = :nome
            ORDER BY p.nome, d.data_atualizacao
        """), {"nome": nome}).fetchall()

        dados = {}
        for row in result:
            continente, pais, casos, mortes, recuperados, data = row
            if pais not in dados:
                dados[pais] = []
            dados[pais].append({
                "casos": casos,
                "mortes": mortes,
                "recuperados": recuperados,
                "data_atualizacao": data
            })

        if not dados:
            return {"message": f"Dados para o continente '{nome}' não encontrados."}

        return {"continente": nome, "dados_covid": dados}

@app.get("/api/covid/top/{n}")
def get_top_paises(n: int):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT p.nome AS pais, c.nome AS continente,
                   SUM(d.casos) AS total_casos,
                   SUM(d.mortes) AS total_mortes,
                   SUM(d.recuperados) AS total_recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            JOIN continentes c ON p.continente_id = c.id
            GROUP BY p.nome, c.nome
            ORDER BY total_casos DESC
            LIMIT :n
        """), {"n": n}).fetchall()

        return {"top_paises": [
            {"pais": row[0], "continente": row[1],
             "casos": row[2], "mortes": row[3], "recuperados": row[4]}
            for row in result
        ]}

@app.get("/api/covid/resumo_global")
def get_resumo_global():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT SUM(casos), SUM(mortes), SUM(recuperados)
            FROM dados_covid
        """)).fetchone()

        return {
            "casos_totais": result[0],
            "mortes_totais": result[1],
            "recuperados_totais": result[2]
        }

@app.get("/api/covid/evolucao/{pais}")
def get_evolucao_pais(pais: str):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT d.data_atualizacao, d.casos, d.mortes, d.recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            WHERE p.nome = :pais
            ORDER BY d.data_atualizacao
        """), {"pais": pais}).fetchall()

        return {"evolucao": [
            {"data": row[0], "casos": row[1], "mortes": row[2], "recuperados": row[3]}
            for row in result
        ]}

@app.get("/api/covid/ranking/{continente}")
def get_ranking_continente(continente: str):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT p.nome AS pais,
                   SUM(d.casos) AS total_casos,
                   SUM(d.mortes) AS total_mortes,
                   SUM(d.recuperados) AS total_recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            JOIN continentes c ON p.continente_id = c.id
            WHERE c.nome = :continente
            GROUP BY p.nome
            ORDER BY total_casos DESC
        """), {"continente": continente}).fetchall()

        return {"ranking": [
            {"pais": row[0], "casos": row[1], "mortes": row[2], "recuperados": row[3]}
            for row in result
        ]}

@app.get("/api/covid/resumo/{pais}")
def get_resumo_pais(pais: str):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT p.nome, c.nome AS continente,
                   SUM(d.casos) AS total_casos,
                   SUM(d.mortes) AS total_mortes,
                   SUM(d.recuperados) AS total_recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            JOIN continentes c ON p.continente_id = c.id
            WHERE p.nome = :pais
            GROUP BY p.nome, c.nome
        """), {"pais": pais}).fetchone()

        if not result:
            return {"message": f"Resumo para o país '{pais}' não encontrado."}

        return {
            "pais": result[0],
            "continente": result[1],
            "casos_totais": result[2],
            "mortes_totais": result[3],
            "recuperados_totais": result[4]
        }

@app.get("/api/covid/resumo_continente/{nome}")
def get_resumo_continente(nome: str):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT c.nome AS continente,
                   SUM(d.casos) AS total_casos,
                   SUM(d.mortes) AS total_mortes,
                   SUM(d.recuperados) AS total_recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            JOIN continentes c ON p.continente_id = c.id
            WHERE c.nome = :nome
            GROUP BY c.nome
        """), {"nome": nome}).fetchone()

        if not result:
            return {"message": f"Resumo para o continente '{nome}' não encontrado."}

        return {
            "continente": result[0],
            "casos_totais": result[1],
            "mortes_totais": result[2],
            "recuperados_totais": result[3]
        }
@app.get("/api/covid/ultima/{pais}")
def get_ultima_atualizacao(pais: str):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT d.data_atualizacao, d.casos, d.mortes, d.recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            WHERE p.nome = :pais
            ORDER BY d.data_atualizacao DESC
            LIMIT 1
        """), {"pais": pais}).fetchone()

        if not result:
            return {"message": f"Nenhum dado encontrado para o país '{pais}'."}

        return {
            "data_atualizacao": result[0],
            "casos": result[1],
            "mortes": result[2],
            "recuperados": result[3]
        }

@app.get("/api/covid/comparar/{pais1}/{pais2}")
def comparar_paises(pais1: str, pais2: str):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT p.nome,
                   SUM(d.casos) AS total_casos,
                   SUM(d.mortes) AS total_mortes,
                   SUM(d.recuperados) AS total_recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            WHERE p.nome IN (:pais1, :pais2)
            GROUP BY p.nome
        """), {"pais1": pais1, "pais2": pais2}).fetchall()

        return {"comparacao": [
            {"pais": row[0], "casos": row[1], "mortes": row[2], "recuperados": row[3]}
            for row in result
        ]}
