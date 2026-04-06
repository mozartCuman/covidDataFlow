from sqlalchemy import create_engine, text
import pandas as pd
from transformation import Transformation

# Criar DataFrame a partir do dicionário
df = pd.DataFrame(Transformation.dic.items(), columns=["nome", "valor"])
print(df)

# Conexão com o banco
DB_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/covid_data"
engine = create_engine(DB_URL)

# Testar conexão corretamente com SQLAlchemy 2.0
with engine.connect() as conn:
    result = conn.execute(text("SELECT current_database();"))
    print("Conectado ao banco:", result.scalar())

# Inserir dados
df.to_sql("dados_covid", engine, if_exists="append", index=False)
print("Delícia! Dados inseridos com sucesso no banco de dados!")