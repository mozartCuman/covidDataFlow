from sqlalchemy import create_engine, text
#import pandas as pd
from transformation import Transformation

dados_paises = Transformation.dados_paises

# Conexão com o banco
DB_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/covid_data"
engine = create_engine(DB_URL)

with engine.begin() as conn:
    for pais in dados_paises:
        nome_cont = pais.get('continent', 'Desconhecido')
        nome_pais = pais['country']
        casos = pais['cases']
        mortes = pais['deaths']
        recuperados = pais['recovered']

        
        conn.execute(text("""
            INSERT INTO continentes (nome)
            VALUES (:nome)
            ON CONFLICT (nome) DO NOTHING
        """), {"nome": nome_cont})

        
        conn.execute(text("""
            INSERT INTO paises (nome, continente_id)
            VALUES (:nome_pais, (SELECT id FROM continentes WHERE nome=:nome_cont))
            ON CONFLICT (nome) DO NOTHING
        """), {"nome_pais": nome_pais, "nome_cont": nome_cont})

        
        conn.execute(text("""
            INSERT INTO dados_covid (pais_id, casos, mortes, recuperados)
            VALUES (
                (SELECT id FROM paises WHERE nome=:nome_pais),
                :casos, :mortes, :recuperados
            )
        """), {"nome_pais": nome_pais, "casos": casos, "mortes": mortes, "recuperados": recuperados})

print("Delícia! Dados inseridos com sucesso no banco de dados!")