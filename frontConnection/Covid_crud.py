from sqlalchemy import text
from .database import engine

def get_covid_by_pais(pais: str):
    with engine.connect() as conn:
        return conn.execute(text("""
            SELECT p.nome AS pais, c.nome AS continente,
                   d.casos, d.mortes, d.recuperados, d.data_atualizacao
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            JOIN continentes c ON p.continente_id = c.id
            WHERE p.nome = :pais
            ORDER BY d.data_atualizacao
        """), {"pais": pais}).fetchall()

def get_covid_by_continente(nome: str):
    with engine.connect() as conn:
        return conn.execute(text("""
            SELECT c.nome AS continente, p.nome AS pais,
                   d.casos, d.mortes, d.recuperados, d.data_atualizacao
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            JOIN continentes c ON p.continente_id = c.id
            WHERE c.nome = :nome
            ORDER BY p.nome, d.data_atualizacao
        """), {"nome": nome}).fetchall()

def get_top_paises(n: int):
    with engine.connect() as conn:
        return conn.execute(text("""
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

def get_resumo_global():
    with engine.connect() as conn:
        return conn.execute(text("""
            SELECT SUM(casos), SUM(mortes), SUM(recuperados)
            FROM dados_covid
        """)).fetchone()

def get_evolucao_pais(pais: str):
    with engine.connect() as conn:
        return conn.execute(text("""
            SELECT d.data_atualizacao, d.casos, d.mortes, d.recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            WHERE p.nome = :pais
            ORDER BY d.data_atualizacao
        """), {"pais": pais}).fetchall()

def get_ranking_continente(continente: str):
    with engine.connect() as conn:
        return conn.execute(text("""
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

def get_resumo_pais(pais: str):
    with engine.connect() as conn:
        return conn.execute(text("""
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

def get_resumo_continente(nome: str):
    with engine.connect() as conn:
        return conn.execute(text("""
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

def get_ultima_atualizacao(pais: str):
    with engine.connect() as conn:
        return conn.execute(text("""
            SELECT d.data_atualizacao, d.casos, d.mortes, d.recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            WHERE p.nome = :pais
            ORDER BY d.data_atualizacao DESC
            LIMIT 1
        """), {"pais": pais}).fetchone()

def comparar_paises(pais1: str, pais2: str):
    with engine.connect() as conn:
        return conn.execute(text("""
            SELECT p.nome,
                   SUM(d.casos) AS total_casos,
                   SUM(d.mortes) AS total_mortes,
                   SUM(d.recuperados) AS total_recuperados
            FROM dados_covid d
            JOIN paises p ON d.pais_id = p.id
            WHERE p.nome IN (:pais1, :pais2)
            GROUP BY p.nome
        """), {"pais1": pais1, "pais2": pais2}).fetchall()
