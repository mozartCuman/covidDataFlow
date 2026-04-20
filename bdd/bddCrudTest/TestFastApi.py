from fastapi import FastAPI
from sqlalchemy import create_engine, text
DB_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/covid_data"

engine = create_engine(DB_URL)
app = FastAPI()


@app.get("/api/testdb")
def test_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT current_database();")).fetchone()
            return {"status": "200 ok", "database": result[0]}
    except Exception as e:
        return {"status": "error", "details": str(e)}

@app.get("/test")
def home():
    return {"message": "FastAPI está rodando com sucesso!"}

@app.get("/api/testdb/paises")
def get_all_paises():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT nome FROM paises")).fetchall()
        paises = [row[0] for row in result]
        return {"paises": paises}
    
@app.get("/api/testdb/continentes")
def get_all_continents():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT nome FROM continentes")).fetchall()
        continentes = [row[0] for row in result]
        return {"continentes": continentes}

@app.get("/api/testdb/dados_covid")
def get_all_covid_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM dados_covid")).fetchall()
        dados = []
        for row in result:
            dados.append({
                "id": row[0],
                "pais_id": row[1],
                "casos": row[2],
                "mortes": row[3],
                "recuperados": row[4],
                "data": row[5]
            })
        return {"dados_covid": dados}

    
@app.get("/api/testedb/continentes_paises")
def get_continentes_paises():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT c.nome AS continente, p.nome AS pais
            FROM continentes c
            LEFT JOIN paises p ON p.continente_id = c.id
            ORDER BY c.nome, p.nome
        """)).fetchall()

        continentes_dict = {}
        for row in result:
            continente = row[0]
            pais = row[1]
            if continente not in continentes_dict:
                continentes_dict[continente] = []
            if pais:  
                continentes_dict[continente].append(pais)

        return {"continentes": continentes_dict}

@app.get("/api/testdb/dados_covid_paises")
def get_dados_covid_paises():
    with create_engine(DB_URL).connect() as conn:
        result = conn.execute(text("""SELECT p.nome, d.casos, d.mortes, d.recuperados
                                   FROM dados_covid d JOIN paises p ON d.pais_id = p.id""")).fetchall()
        dados = []
        for row in result:
            if row[0] is not None:
                dados.append(f"País: {row[0]}, Casos: {row[1]}, Mortes: {row[2]}, Recuperados: {row[3]}")
            else:
                dados.append(f"País: Desconecido, Casos: {row[1]}, Mortes: {row[2]}, Recuperados: {row[3]}")   
        
        return {"dados_covid": dados} 


@app.get("/api/testdb/pais/{pais}")
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

        dados = []
        for row in result:
            dados.append({
                "pais": row[0],
                "continente": row[1],
                "casos": row[2],
                "mortes": row[3],
                "recuperados": row[4],
                "data_atualizacao": row[5]
            })
        
        if not dados:
            return {"message": f"Dados para o país '{pais}' não encontrados."}

        return {"dados_covid": dados}
